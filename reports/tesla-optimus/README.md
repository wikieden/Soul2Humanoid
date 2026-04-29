# Tesla Optimus Deep Dive: Task Planning, Long-Horizon Execution & Embodied Brain

> Research Date: 2026-04-26 | Scope: Task Planning, Long-Horizon Execution, Embodied Brain
> Core Methodology: End-to-End Neural Networks + FSD Tech Stack Transfer + Massive Data Flywheel

---

## 1. Overview

Tesla Optimus is not a traditional robot built from modular perception-planning-control layers. Its core technical bet is: **directly porting the FSD (Full Self-Driving) end-to-end neural network architecture to humanoid robotics**, replacing explicit hierarchical planners, behavior trees, and state machines with a single neural network.

> "All the above points not just solve for vehicle autonomy, but also seamlessly transfer to Optimus."
> — Ashok Elluswamy, VP of AI Software, Tesla (ICCV 2025)

---

## 2. Task Planning

### 2.1 End-to-End Unified Architecture Philosophy

Tesla explicitly rejects traditional Hierarchical Task Networks (HTN), temporal logic planners, and behavior trees. Instead, it employs a **single end-to-end neural network** derived from FSD.

**Overall Architecture:**

```
+-----------------------------------------------------------------------------+
|           Unified End-to-End Architecture (Optimus & FSD)                   |
+-----------------------------------------------------------------------------+
|                                                                             |
|   [8 Autopilot Cameras] + [IMU] + [Force/Torque Sensors] + [Proprioception] |
|         |                                                                   |
|         v                                                                   |
|   +-------------------------------------+                                   |
|   |  Vision Foundation Model (Shared w/ FSD)                                |
|   |  - Occupancy Networks                                                   |
|   |  - 3D Voxel Reconstruction                                              |
|   |  - Depth Estimation                                                     |
|   +------------------+------------------+                                   |
|                      |                                                      |
|   +------------------v------------------+                                   |
|   |  Single End-to-End Neural Network     |                                 |
|   |  - Latent Space Task Decomposition    |                                 |
|   |  - Grok Language Understanding        |                                 |
|   +------------------+------------------+                                   |
|                      |                                                      |
|   +------------------v------------------+                                   |
|   |  Guardian Network + Force Limiters    |                                 |
|   +------------------+------------------+                                   |
|                      |                                                      |
|   +------------------v------------------+                                   |
|   |  28 Body Actuators + 22-DoF Hand Control                              |
|   +-------------------------------------+                                   |
+-----------------------------------------------------------------------------+
```

![Tesla Optimus End-to-End Architecture](../../assets/tesla-end-to-end-architecture.svg)

**图**：Tesla Optimus 端到端神经网络架构 — 传感器输入经共享 FSD 视觉基础模型处理后，由单一端到端神经网络直接输出动作， guardian 网络提供安全兜底。

**Advantages of Tesla's End-to-End Approach:**

| Advantage | Explanation |
|-----------|-------------|
| **Value Alignment** | "Codifying human values is incredibly difficult. It is easier to learn them from data." |
| **Interface Elimination** | "Gradients flow all the way from controls to sensor inputs, optimizing the entire network holistically." |
| **Long-tail Scalability** | Easily scalable to handle the fat and long tail of real-world robotics. |
| **Deterministic Latency** | Homogenous compute with predictable latency for real-time control. |

### 2.2 Implicit vs Explicit Task Decomposition

**Traditional Approach (HTN):**

```
  High-Level Task          Sub-task A          Perception Module
       |                         |                       |
       v                         v                       v
  Task Decomposer  --->  Sub-task B  --->   Planning Module  --->  Actuators
       |                         |                       |            ^
       v                         v                       |            |
  (Manual Rules)           Sub-task C  --->  Control Module  --------+
```

**Tesla End-to-End Approach:**

```
  Natural Language    +    Camera Input
       |                       |
       v                       v
   Grok LLM  +  Vision Foundation Model
              |
              v
      Single Neural Network
              |
              v
      Latent Space (Implicit Task Decomposition)
              |
              v
        Motor Commands
```

**Key Difference:**
- **Traditional**: Engineers manually define sub-task boundaries, state transitions, and failure recovery logic.
- **Tesla**: Task decomposition happens automatically in the neural network's latent space. The network implicitly learns "when to grasp, when to move, when to place" from massive human demonstration data.

### 2.3 Role of LLM/VLM in Task Planning

As of early 2026, Tesla has confirmed integrating xAI's **Grok LLM** into Optimus:

```
+-------------------+      +---------------------+      +-------------------+
|  User Interaction |      |   Language Layer    |      | Physical Execution|
+-------------------+      +---------------------+      +-------------------+
| Voice Command     |----->| Grok 3 LLM          |----->| VLA Network       |
| Text Command      |----->| Task Embedding      |----->| Vision Encoder    |
+-------------------+      +---------------------+      | Action Decoder    |
                                                        +---------+---------+
                                                                  |
                    +---------------------+                       |
                    | Action Primitives   |<----------------------+
                    | (3000+ Tasks)       |
                    | Grasp/Lift/Rotate/  |
                    | Place/Push          |
                    +---------------------+
```

| Capability | Status | Description |
|-----------|--------|-------------|
| Natural Language Understanding | Confirmed (2026.02) | Users can give spoken instructions |
| Text-Physical Unified Network | Partially Confirmed | Grok handles language, FSD network handles physical execution |
| Complex Reasoning & Planning | Early Stage | Sept 2025 demo still required multiple voice prompts for simple fetch tasks |

Elluswamy demonstrated at ICCV that Tesla's network supports:

> "Reasoning can be done in natural language along with video grounding. A small version of this reasoning model is already running in the FSD v14.x release."

This means LLM/VLM capabilities are gradually融入ing Tesla's unified architecture as "reasoning as a service," but the primary task planning body remains the end-to-end neural network, not an independent LLM planning module.

### 2.4 Learning Tasks from Human Videos

In May 2025, Tesla demonstrated Optimus learning household tasks by watching human videos:

```
   Data Sources              Training                 Model            Deployment
  +-----------+         +----------------+      +------------+      +-------------+
  | Human     |         | Cortex         |      | Unified    |      | OTA Update  |
  | Video     |-------->| Supercomputer  |----->| VLA        |----->| Global Fleet|
  | (POV)     |         |                |      | Network    |      +-------------+
  +-----------+         | Neural World   |      +------------+
  | Teleop    |-------->| Simulator      |
  | Data      |         |                |
  +-----------+         | Digital Dreams |
  | Factory   |-------->| (Synthetic)    |
  | Fleet     |         +----------------+
  | Data      |
  +-----------+
```

> "All these tasks are done by a single neural net and were learned directly from human videos... We recently had a significant breakthrough... and can now transfer a big chunk of the learning directly from human videos to the bots (1st person views for now)."
> — Milan Kovac (Former Optimus VP & Head of Engineering)

Tesla AI team member Ashish Kumar further confirmed:

> "All tasks are from the same neural net that understands text instructions! The technical breakthrough is in directly learning from first person videos of humans doing tasks!"

**Three Task Acquisition Methods:**

| Method | Data Source | Scalability |
|--------|-------------|-------------|
| Imitation Learning | Human videos (YouTube, POV videos) | Extremely High: theoretically unlimited data |
| Sim RL | Neural World Simulator | High: 10,000+ variants per real sample |
| Fleet Learning | Factory robot operational data | Medium: limited by physical deployment count |

### 2.5 Multi-Step Task Planning in Factory Scenarios

Current confirmed autonomous factory tasks at Fremont and Giga Texas:

```
  +------------------------+      +------------------------+
  | Confirmed Autonomous   |      | Execution Method       |
  | Tasks                  |      |                        |
  +------------------------+      +------------------------+
  | Battery Cell Sorting   |      | Single Neural Network  |
  | (4680 batteries)       |      | End-to-End             |
  | Parts Handling         |      | Force Feedback Loop    |
  | Kitting                |      | Tactile Sensing        |
  | Visual Quality Inspect |      |                        |
  | Pick and Place         |      |                        |
  | Auto-Charging Nav      |      |                        |
  +------------------------+      +------------------------+
```

**Multi-step Task Execution Sequence:**

```
User -> Grok LLM -> VLA Network -> Actuators -> Environment
                ^                                    |
                |________ Force Feedback ____________|
```

### 2.6 Transfer of FSD Scene Understanding to Robotics

This is Tesla's core technical advantage. Elluswamy demonstrated the **seamless transfer** from FSD to Optimus:

```
  FSD Tech Stack              Transfer Layer              Optimus Application
  +----------------+         +--------------------+      +-------------------+
  | 8 Camera       |         | Neural World       |      | Workspace         |
  | Perception     |-------->| Simulator          |----->| Understanding     |
  +----------------+         |                    |      +-------------------+
  | Occupancy      |         | Shared Vision      |      | Object            |
  | Network        |-------->| Foundation Model   |----->| Manipulation      |
  +----------------+         |                    |      +-------------------+
  | End-to-End     |         | Unified Training   |      | Navigation &      |
  | Path Planning  |-------->| Pipeline           |----->| Avoidance         |
  +----------------+         +--------------------+      +-------------------+
  | Fleet Learning |                                    | Multi-Robot       |
  |                |----------------------------------->| Data Sharing      |
  +----------------+                                    +-------------------+
```

| FSD Technology | Optimus Application |
|----------------|---------------------|
| 8-Camera Pure Vision | Robot environment perception |
| Occupancy Network / 3D Reconstruction | Workspace understanding |
| End-to-End Path Planning | Navigation & avoidance |
| Neural World Simulator | Robot action simulation & RL |
| Fleet Learning | Multi-robot data sharing |


---

## 3. Long-Horizon Task Execution

### 3.1 Current Capability Boundary

```
  SOLVED                      DEMO LEVEL                 UNSOLVED
  +----------------+          +----------------+         +----------------+
  | Single-step    |          | Trash Throwing |         | Complete Meal  |
  | Tasks          |          |                |         | Preparation    |
  |                |          | Desktop Clean  |         |                |
  | Low-coupling   |          |                |         | Find Item in   |
  | Tasks          |          | Part Recognize |         | Cluttered Room |
  |                |          |                |         |                |
  | Factory        |          | Basic Assembly |         | Load           |
  | Repetitive Work|          |                |         | Dishwasher     |
  +----------------+          +----------------+         +----------------+
```

Per Optimusk.blog analysis (April 2026):

> "Complex Multi-Step Tasks — Making a full meal, loading a dishwasher from scratch, navigating a cluttered room to find a specific item — these require chaining many sub-tasks together with error recovery. Demos show individual sub-tasks, not full chains in realistic conditions."

### 3.2 VLA Model: Vision-Language-Action Unified Network

The core of Optimus task execution is the **Vision-Language-Action (VLA) unified neural network**:

| Component | Function | Source |
|-----------|----------|--------|
| **Vision** | 8 autopilot-grade cameras, pure vision (no LiDAR) | Tesla AI Day |
| **Language** | Grok LLM understands natural language commands | NotATeslaApp, July 2025 |
| **Action** | Directly outputs force/position commands for 78 actuators | Optimusk.blog |

**VLA Data Flow:**

```
  Vision Input              Language Input             Action Output
  +----------------+        +----------------+        +----------------+
  | 8 Cameras      |        | Grok 3 LLM     |        | 78 Actuators   |
  | Pure Vision    |   +    | Voice/Text     |   ->   | 28 Body + 50   |
  | Occupancy Net  |        | Understanding  |        | Hand Control   |
  | 3D Voxel Maps  |        |                |        | Force/Position |
  +----------------+        +----------------+        +----------------+
           |                         |                        |
           v                         v                        v
  +-----------------------------------------------------------------------+
  |              Unified VLA Neural Network (Single Network)              |
  |     Visual perception + Language grounding + Motor control learned    |
  |     jointly, not modularly                                            |
  +-----------------------------------------------------------------------+
                                    |
                                    v
                          +-------------------+
                          | Real-time Control |
                          |     (< 5ms)       |
                          +-------------------+
```

### 3.3 Task Interruption and Recovery Mechanisms

**Frankly, Tesla has disclosed almost no explicit failure recovery / replanning algorithm architecture.** Existing information is mainly inferred from side evidence.

#### (1) Neural World Simulator Adversarial Testing

Tesla's core validation tool is the **Neural World Simulator**, detailed by Elluswamy at ICCV 2025:

> "This system is trained on the same 'Niagara Falls of data' from its vehicle fleet and learns to synthesize new, high-fidelity video of the world in response to the AI's actions."

**Implication for failure recovery**: Tesla's failure recovery is likely **implicit** — the end-to-end network learns to handle anomalies "naturally" from massive training data (including failure cases), rather than through explicit state-machine replanning.

#### (2) Human Supervision in Factory Deployments

Per Musk's Q4 2025 earnings call:

> "Optimus units are primarily for learning and data collection rather than performing productive tasks."

This means current factory failure recovery largely relies on **human supervisors**.

#### (3) Miami Fall Incident: Teleoperation as Implicit Safety Net

At the December 2025 Miami "Future of Autonomy" event, Optimus fell backward while handing water. Teslarati reported remote operator error caused the collapse, indicating teleoperation remains an **implicit backup mechanism**.

#### Inferred Three-Level Recovery Strategy

```
  Level 1: Implicit Recovery (Network-Level)
  +--------------------------------------------------+
  | End-to-end network has seen millions of failure    |
  | cases during training; directly outputs corrective |
  | actions without explicit replanning.               |
  +--------------------------------------------------+
              | (if insufficient)
              v
  Level 2: World Model Prediction
  +--------------------------------------------------+
  | Neural World Simulator predicts future outcomes    |
  | of different actions; selects optimal path before  |
  | executing.                                         |
  +--------------------------------------------------+
              | (if still uncertain)
              v
  Level 3: Human Intervention
  +--------------------------------------------------+
  | Factory supervisor or remote operator takes over.  |
  | (Current primary safety net in actual deployment)  |
  +--------------------------------------------------+
```

### 3.4 Memory Mechanisms

#### (1) Environmental Mapping & Spatial Memory

Brian D. Colwell's review explicitly states:

> "Environmental mapping and memory systems allow Optimus to remember familiar locations and optimize its behavior accordingly."

#### (2) Fleet Learning as Collective Memory

Tesla's **Fleet Flywheel** mechanism is essentially a **distributed collective memory**:

```
   Robot A                Robot B                Robot C
      |                      |                      |
      | Sensor Data          | Sensor Data          | Sensor Data
      v                      v                      v
  +----------------------------------------------------------+
  |                     Data Pipeline                         |
  +----------------------------------------------------------+
                              |
                              v
  +----------------------------------------------------------+
  |  Cortex Supercomputer (67,000+ H100 GPUs)                 |
  |  1. Data aggregation    2. Model training   3. Validation |
  +----------------------------------------------------------+
                              |
                              v
  +----------------------------------------------------------+
  |  OTA Update                                               |
  |  "Robot learns in Texas factory -> London home robot      |
  |   gets same skill the next morning"                       |
  +----------------------------------------------------------+
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
           Robot A         Robot B         Robot C
           (updated)       (updated)       (updated)
```

#### (3) Neural World Simulator as Generative Memory

Neural World Simulator can be understood as a **generative world memory**: instead of storing discrete memory fragments, it learns a dynamic world model that can "imagine" future states. This conceptually resembles the "predictive processing" theory in neuroscience.

#### Memory Types Disclosure Status

| Memory Type | Status | Analysis |
|-------------|--------|----------|
| **Episodic Memory** | Not explicitly disclosed | No evidence Optimus can "recall" specific past event timelines |
| **Working Memory** | Not explicitly disclosed | VLA model's implicit state may partially serve WM function |
| **Semantic Memory** | Inferred | Grok LLM provides common-sense knowledge; vision network provides object semantics |
| **Procedural Memory** | Disclosed | End-to-end network stores motor skills (walking, grasping) |
| **Spatial Memory** | Disclosed | Environmental mapping and navigation capabilities confirmed |

### 3.5 Continual Learning and Online Adaptation

#### Fleet Flywheel: Cloud-Centric Continual Learning

Tesla's continual learning is primarily **centralized**, not real-time edge adaptation:

```
  [Robot A collects data] ---
  [Robot B collects data] ---> [Cortex Training] -> [New Model] -> [OTA Push] -> [All robots updated]
  [Robot C collects data] ---
```

Trade-offs:

| Advantages | Disadvantages |
|------------|---------------|
| Leverage massive compute for deep training | Adaptation latency: hours/days from data collection to model update |
| All robots sync to latest capabilities | Cannot handle real-time, robot-specific environmental changes |
| Data quality and safety validated in cloud | Requires network connectivity |

#### On-Device Adaptation Hardware Foundation

**AI5 chip** (expected end of 2026) is described as 40x faster than AI4, potentially enabling **on-device online adaptation**:

> "AI5 chip (end 2026) will enable on-device training refinement vs. current cloud-dependent model."

If realized, robots could perform small-scale local gradient updates (e.g., adapting to specific factory lighting, specific worker collaboration habits) without waiting for cloud training cycles.

#### RL's Role in Continual Learning

RL is mainly used for **exploratory learning in simulation**:

| Application | RL Role | BC Limitation |
|-------------|---------|---------------|
| **Gait Optimization** | Explore millions of gaits in sim to find energy-optimal solutions | Human demos cannot cover all terrains |
| **Force Control** | Discover optimal force curve for grasping eggs via trial-and-error | Human demo force signals hard to capture precisely |
| **Dynamic Motion** | Learn high-dynamic motions like Kung fu, running, dancing | Human demonstrators cannot safely show dangerous moves |
| **Fall Recovery** | Learn recovery strategies after countless virtual falls | Real robot falls too costly |

> "Sim2real RL is the key to getting next level agile, dynamic motions. It's also the key to precision and robustness."
> — Murtaza Dalal, Tesla AI

### 3.6 Three Stages of Learning from Demonstration

Tesla's imitation learning strategy has evolved through three distinct stages:

```
  Stage 1 (2022-2024)         Stage 2 (2025 Mid)         Stage 3 (2025+)
  +----------------+         +----------------+         +----------------+
  | Teleoperation  |         | Camera Rig POV |         | Internet Video |
  |                |         |                |         |                |
  | Motion Capture |         | 5 Built-in     |         | YouTube, etc.  |
  | Suit + VR      |         | Cameras        |         |                |
  | Headset        |         |                |         | 3rd-person     |
  |                |         | Scale: Medium  |         | random video   |
  | Scale: Very    |         | (no robot HW   |         |                |
  | Low            |         | needed)        |         | Scale: Infinite|
  +----------------+         +----------------+         | (theoretical)  |
       ^                           ^                   +----------------+
       |                           |
       |         EVOLUTION: Increasing Scalability      |
       |                  of Data Collection             |
```

Milan Kovac's May 2025 statement marked the Stage 2/3 transition:

> "Tesla can now teach Optimus directly from videos of people — even footage captured from a first-person perspective. This dramatically accelerates learning and enables the robot to generalize across a variety of real-world scenarios."

Musk on CNBC went further:

> "If Optimus can watch YouTube videos and learn to do that thing... you really have task extensibility that is dramatic."

### 3.7 Synthetic Data Amplification: Digital Dreams

Tesla solved imitation learning's fundamental bottleneck — data scale — through **generative video AI synthetic training data** (internally called "Digital Dreams"):

```
  Step 1: Real Demo        Step 2: Synthesize       Step 3: Train
  +----------------+       +----------------+       +----------------+
  | Human folds    |       | Video Gen AI   |       | Recover Pseudo-|
  | shirt once     |------>| (Sora-like)    |------>| Actions from   |
  |                |       |                |       | Synthetic Video|
  +----------------+       | Generates      |       +----------------+
                           | 10,000+        |
                           | variants       |
                           +----------------+
```

**NVIDIA DreamGen research insight (same approach):**

> "By starting with just a single real-world task, their humanoid robot was able to learn 22 new behaviors without a single demonstration... from 0% success to over 40% success on novel tasks in unseen environments."

### 3.8 Behavior Cloning vs Reinforcement Learning

**BC is the Primary Paradigm:**

Tesla's end-to-end neural network is essentially **large-scale behavior cloning**:
- **Input**: Visual video stream + natural language instruction
- **Output**: Motor torque/position commands
- **Training objective**: Imitate human operator (or human video) action distribution

FSD v12's historic transition is the best proof of this paradigm:

> "In 2023, Tesla replaced 300,000 lines of explicit C++ driving code with a single end-to-end neural network (FSD v12)."

**RL plays a supplementary role:**

| Application | RL's Role |
|-------------|-----------|
| Gait optimization | Explore millions of gaits in simulation, migrate to real robot |
| Force control | Discover optimal force curves via trial-and-error |
| Dynamic motion | Learn Kung fu, running, dancing in simulation |
| Fall recovery | Learn recovery strategies after countless virtual falls |

> "The routine was entirely trained in simulation with reinforcement learning."
> — Milan Kovac, on dance demonstration (May 2025)


---

## 4. Embodied Brain

### 4.1 Brain Hardware Architecture

Optimus's onboard computing core shares the same technology stack as Tesla vehicles' FSD computers, using a vertically integrated hardware strategy:

| Chip Generation | Compute | Application | Optimus Relation |
|-----------------|---------|-------------|------------------|
| HW3 / AI3 | ~144 TOPS | Early FSD | Not used in Optimus |
| HW4 / AI4 | Dual-redundant SoC | Current vehicle FSD | Used in Optimus Gen 2 |
| **AI5 (HW 5.0)** | **~2,500 TOPS** | Late 2026 production | **Optimus Gen 3 core brain** |
| AI6 | Planned, sub-3nm | Next generation | Future multi-modal models |

**Key Technical Details:**
- **AI5 chip tape-out completed April 2026** — design finalized and sent to TSMC/Samsung for fabrication
- Musk explicitly stated: **AI4 is sufficient for FSD; AI5's core target is accelerating Optimus robots and Dojo supercomputing clusters**
- AI5 uses **3nm process**, significantly improving power efficiency — critical for robots where "every watt spent thinking is stolen from movement"
- Optimus Gen 3 adopts **dual-redundant AI5 architecture** — if one chip fails, the other takes over in <5ms, bringing the robot to a safe state
- **48V electrical architecture**: shared with Cybertruck, enabling thinner wiring and faster brain-to-actuator data transmission

### 4.2 Cloud Training Infrastructure: Dojo & Cortex

Tesla has built a two-tier training infrastructure:

**Dojo Supercomputer**
- Based on Tesla's self-developed **D1 chip** custom training clusters
- Optimized for video/sensor data AI training, distinct from general-purpose GPU clusters
- **Rebooted Dojo 3 project in January 2026** after team reorganization pause
- Target: Provide exaflop-level training compute for FSD and Optimus, reducing Nvidia dependency

**Cortex Cluster (Current Mainstay)**
- **Cortex v1**: ~50,000 Nvidia H100 equivalents
- **Cortex expansion**: 67,000+ H100 equivalent GPUs (confirmed March 2026)
- **Cortex 2**: Under construction at Giga Texas
- Each full neural network training cycle requires ~**70,000 GPU hours**

**Optimus-Training Facility Connection:**
- Every hour of Optimus factory operation generates training data
- Data trained through Dojo/Cortex, then pushed to global robots via **OTA**
- Forms a flywheel effect: "One robot learns smooth-ground walking in Texas -> London home robot gets the same skill the next morning"

### 4.3 End-to-End Neural Network: Shared FSD & Optimus Architecture

Tesla AI VP **Ashok Elluswamy** delivered a speech at ICCV 2025 titled "Building Foundational Models for Robotics at Tesla," core confirmation:

> "All the above points not just solve for vehicle autonomy, but also **seamlessly transfer to Optimus**."

**Architecture Evolution:**
- **FSD v11 and earlier**: Modular system, 300,000 lines of C++ code, split into perception, planning, control modules
- **FSD v12+**: **Single end-to-end neural network**, raw video input -> neural network -> direct control output
- **Optimus**: Uses FSD v12's single neural network architecture, but replaces the "driving action head" with a "humanoid action head"

**FSD vs Optimus Technical Comparison:**

| Dimension | FSD (Vehicle) | Optimus (Robot) |
|-----------|---------------|-----------------|
| **Core Network** | Same Vision Foundation Model | Same Vision Foundation Model |
| **Action Head** | Steering, acceleration, braking | 28+ joint motors + 22-DoF hand control |
| **Sensors** | 8-9 cameras, pure vision | 8 cameras + torque sensors + IMU + tactile sensors |
| **DoF** | Low (~4 control dimensions) | High (50+ body DoF, 22 hand DoF) |
| **Environment** | Structured roads | Unstructured human spaces |
| **Training Data** | 8.2 billion miles driving data | Driving data + teleop + synthetic + factory footage |

**Key Difference**: Optimus's neural network requires higher TOPS to handle bipedal balance and finger fine-control complex physics. But both share underlying visual representations, meaning improvements in driving scene object recognition directly boost robot manipulation of the same objects.

### 4.4 Perception-Action Loop Architecture

By 2026, Tesla has migrated to the **VLA (Vision-Language-Action) model** architecture:

```
[8 camera inputs: 576+ MP/s visual data]
           |
           v
    [Vision Foundation Model]
    (Occupancy Networks + 3D voxel maps)
           |
           v
    [Grok Language Layer] <- User voice command
           |
           v
    [Single End-to-End Neural Network]
           |
           v
    [Kinematics Network + Safety Network]
           |
           v
    [78 actuator outputs]
```

**Perception Layer: Pure Vision + Occupancy Networks**
- **Rejects LiDAR**: Optimus continues Tesla Vision's pure vision approach, building real-time 3D environment maps through 8 high-resolution cameras
- **Occupancy Networks**: Convert 2D photos to 3D voxel maps, enabling robots to recognize "transparent glass tables" as solid obstacles not to collide with
- **Depth perception**: Uses multi-camera parallax to precisely measure distances for grasping delicate cups without collision

**Cognition Layer: Neural Network "Dark Knowledge"**
- Tesla emphasizes end-to-end networks learn human "soft intent":
  - Waiting for chicks to cross the road vs. going around geese "just hanging out"
  - Such value judgments cannot be implemented through if-then code, only implicitly learned from human behavior data

**Action Layer: Real-time Closed-Loop Control**
- **Local inference**: All decisions completed on AI5 chip, no cloud connection needed for safe operation
- **Force feedback loop**: Brain monitors each motor's current consumption, detecting unexpected resistance (e.g., child's hand) and stopping in <5ms
- **Vision-Touch loop**: Gen 3 fingers integrate tactile sensors; after touching objects, AI5 chip adjusts motor power in real-time for "not crushing strawberries" fine control

### 4.5 World Model: Neural World Simulator

This is one of Tesla's most ambitious technical disclosures. Ashok Elluswamy explicitly demonstrated the **unified world simulator** serving both FSD and Optimus at ICCV 2025:

> "The great thing about all the above points is that they not just solve for vehicle autonomy, but also seamlessly transfer to Optimus."

**Technical Characteristics:**
- System trained on Tesla fleet's "Niagara Falls of data"
- Capable of **simultaneously synthesizing 8-camera full synthetic video streams** in response to AI action inputs
- When used for Optimus, generates realistic video of robots walking and turning in factories

**Core Functions:**
1. **Closed-loop simulation**: Run closed-loop tests of new AI models, not open-loop prediction
2. **Historical playback validation**: Let AI "diverge" in historical scenarios, showing what different actions it could have taken
3. **Adversarial scenario generation**: Inject rare events (suddenly rushing pedestrians or falling objects)
4. **Large-scale reinforcement learning**: Achieve superhuman performance in simulation before migrating to real robots

**Essential Difference from Traditional Simulation:**

| Feature | Traditional Sim (e.g., NVIDIA Isaac Sim) | Tesla Neural World Simulator |
|---------|------------------------------------------|------------------------------|
| Physics fidelity | Hand-coded, prone to missing complex physics like deformable objects | Learned from real video, automatically inherits all real-world physics |
| Environment creation | Engineers manually model | Generated from data |
| Sim-to-Real gap | Significant performance drop | Minimized — AI already knows the real world |
| Scalability | Limited by engineering time | Scales with data volume |

**Key Conclusion**: Tesla publicly confirmed its world model is used not just for cars but **directly migrated to Optimus robots**. Elluswamy's demo video explicitly showed Optimus training footage in the Neural World Simulator.

### 4.6 Generalization: Digital Dreams + Fleet Learning

Tesla's core method for solving generalization is **large-scale synthetic data generation**:

**Bottleneck Problem:**
- Human teleoperation was called the "fossil fuel" of robotics by Nvidia robotics director Jim Fan — effective but not scalable
- Cannot physically demonstrate every object, every environment, every task

**Tesla's Solution:**
- Use video generation AI (similar to Sora) as a "neural physics engine"
- One real demo -> generate 10,000 synthetic variants (different shirts, folding methods, lighting, angles)
- Train thousands of iterations in "Digital Dreams" without moving physical servo motors

**Cross-Task Representation Sharing:**
- Single neural network architecture enables generalization:
  - Perception improvements for "battery sorting" automatically boost "quality inspection" accuracy
  - Force control learned from grasping eggs migrates to handling precision electronic components

**Fleet Learning Flywheel:**
- **8.2 billion miles** real-world visual data (vehicles)
- Every additional Optimus factory hour improves the global model
- Competitors can deploy more robots, but **cannot retroactively obtain 8.2 billion miles of pre-training data**

### 4.7 Multimodal Fusion

Optimus Gen 3's perception system integrates multiple modalities:

| Modality | Sensor Type | Function |
|----------|-------------|----------|
| **Vision** | 8 autopilot-grade cameras | Environment mapping, object recognition, depth estimation |
| **Tactile** | Fingertip skin-like pressure sensors (Gen 3 new) | Detect contact force, enable "Vision-Touch" closed loop |
| **Force** | 6-axis force/torque sensors (wrist, foot) | Balance control, contact force adjustment |
| **Proprioception** | Full-joint torque sensors + IMU | Joint position perception, posture estimation |
| **Temperature/Current** | Motor current monitoring | Abnormal resistance detection (safety) |

**Multimodal Fusion Mechanism:**
- **Tactile enters FSD pipeline**: Gen 3's biggest innovation is feeding tactile data directly into the previously vision-dominant FSD neural network
- When robot touches objects, AI5 chip immediately adjusts motor power for fine grasping
- **Bipedal balance**: Fuses foot force/torque sensing + IMU + vision for stable walking on uneven ground

**Modality Differences from FSD:**
- FSD mainly relies on vision (pure vision strategy)
- Optimus must fuse more modalities: manipulation tasks need tactile feedback for closed-loop grasp control; bipedal walking needs proprioception and force sensing for balance
- But **underlying vision network is shared**, visual representations directly migrated from FSD

### 4.8 Physical AI Definition & Tech Stack

Tesla explicitly repositioned itself as a **"Physical AI Company"** in 2025-2026:

> "We are no longer primarily an automotive company. We are a Physical AI company." — Elon Musk, 2026

**Physical AI Definition (based on public information):**
- Applying neural networks to **hardware that interacts with the physical world**
- Unlike digital AI living in servers, Physical AI requires massive real-world data from millions of physical devices
- Tesla's patent portfolio is now **40% AI-related**

**Four-Layer Tech Stack:**

| Layer | Component | Function |
|-------|-----------|----------|
| **Layer 1: Data Infrastructure** | Tesla fleet (millions of sensors) + X platform (human behavior data) + Dojo/Cortex | Source of training data and compute |
| **Layer 2: Inference Intelligence** | Grok (xAI large language model) | Data processing, decision generation, intent interpretation |
| **Layer 3: Edge Execution** | AI5 chip (FSD-derived network) | Real-time perception, planning, control |
| **Layer 4: Physical Hardware** | Optimus robot + Tesla vehicles | Physical interaction with the world |

### 4.9 Grok-Optimus Integration

**Division of Labor: Cloud Large Model (Grok) + Edge Embodied Intelligence (AI5/FSD Network)**

| Capability | Processing Location | Requirement |
|------------|---------------------|-------------|
| Real-time motor control | AI5 chip (local) | <5ms latency, no network needed |
| Visual perception & obstacle avoidance | AI5 chip (local) | Continuous operation, safety-critical |
| Natural language understanding | Grok (cloud) | Requires network connection |
| Complex reasoning & planning | Grok (cloud) | High compute, not latency-sensitive |
| Grok-level conversation | Grok (cloud) | Requires network connection |

**Local Autonomy vs Cloud Dialogue:**
- **Local autonomy**: Optimus v3 with AI5 chip can perform useful work even after losing WiFi/cellular, similar to FSD's local operation mode
- **Cloud dialogue**: For Grok-level AI conversations, network connection to Grok-level AI is needed
- This分层 architecture ensures safety and availability while leveraging the latest large model capabilities


---

## 5. Key Conclusions & Outlook

### 5.1 Cross-Domain Synthesis

| Direction | Core Finding | Key Uncertainty |
|-----------|--------------|-----------------|
| **Task Planning** | No explicit hierarchical planner; task decomposition occurs implicitly in neural network latent space. Grok provides natural language interface but physical execution remains FSD-derived end-to-end network. | Whether LLM will take on more planning responsibility, or remain a "task selector" |
| **Long-Horizon Execution** | Current capability limited to single-step/low-coupling tasks. Complex multi-step task chains (cooking, loading dishwasher) remain unsolved. Failure recovery primarily implicit + human supervision. | When true autonomous multi-step task chains will emerge |
| **Embodied Brain** | Unified end-to-end architecture with FSD, sharing visual foundation model. AI5 chip provides local compute. Neural World Simulator enables closed-loop training. | Whether Sim2Real gap can be closed for complex manipulation tasks |

### 5.2 Technical Route Judgment

Tesla's Optimus follows a clear **"End-to-End + Massive Data + Vertical Integration"** route:

1. **End-to-End**: Single neural network replaces modular perception-planning-control, eliminating ill-defined interfaces between modules
2. **Massive Data**: Three-stage data flywheel (human video -> synthetic amplification -> fleet learning) solves robotics' data bottleneck
3. **Vertical Integration**: Self-developed chips (AI5), self-built training clusters (Dojo/Cortex), self-manufactured actuators, forming a complete closed loop

### 5.3 Risks & Uncertainties

| Risk | Severity | Description |
|------|----------|-------------|
| **Timeline Risk** | High | Tesla has a history of overpromising timelines; Optimus v3 summer 2026 production target faces Fremont factory conversion challenges |
| **Autonomy Transparency** | High | Multiple public demos relied on teleoperation; lack of transparency damages credibility |
| **Actuator Manufacturing** | Medium | Planetary roller screws mass production at consumer-grade prices remains unproven |
| **Sim2Real Gap** | Medium | Complex manipulation tasks may not transfer smoothly from Neural World Simulator to physical world |
| **Safety & Regulation** | Medium | Humanoid robots in human spaces face undefined regulatory frameworks |

### 5.4 Future Outlook

**Near-term (2026-2027):**
- Optimus v3 release and production start is the biggest milestone
- Large-scale deployment validation in internal scenarios (Tesla factories)
- AI5 chip deployment, enhancing on-device autonomy

**Mid-term (2027-2030):**
- Texas production line reaches scale, costs expected to drop significantly
- Expansion from factory scenarios to more B2B scenarios (logistics, retail, care)
- FSD and Optimus AI capabilities mutually reinforce, forming a data flywheel

**Long-term Strategic Significance:**
- Musk repeatedly emphasized Optimus will be **"Tesla's biggest product ever, possibly the biggest product in human history"**
- Tesla is repositioning itself as an **"AI + Robotics + Autonomous Driving"** company, not just an automaker
- If humanoid robot costs truly drop to ~$20,000 with practical autonomy, it will trigger structural transformation in the labor market

---

## 6. References

### Task Planning
- Ashok Elluswamy, ICCV 2025 Keynote: "Building Foundational Models for Robotics at Tesla"
- https://x.com/aelluswamy/status/1981644831790379245
- https://www.humanoidsdaily.com/news/tesla-ai-chief-details-unified-world-simulator-for-fsd-and-optimus
- https://botinfo.ai/articles/tesla-optimus
- https://optimusk.blog/blog/tesla-optimus-skills-packages/
- https://briandcolwell.com/a-complete-review-of-teslas-optimus-robot/

### Long-Horizon Execution
- Milan Kovac X post (May 2025): https://x.com/_milankovac_/status/1925047791954612605
- https://www.humanoidsdaily.com/feed/teslas-optimus-learns-new-tricks-autonomously-performing-chores-by-watching-humans
- https://optimusk.blog/blog/tesla-optimus-capabilities/
- https://optimusk.blog/blog/ai-training-for-tesla-optimus/
- https://www.notateslaapp.com/news/2998/an-in-depth-look-at-how-teslas-optimus-learns-digital-dreams-and-ai-simulation
- https://www.notateslaapp.com/news/2732/tesla-engineers-reveal-how-optimus-learns-and-show-off-its-dance-moves-video
- https://www.teslarati.com/tesla-optimus-dramatically-collapses-after-teleoperator-mishap/

### Embodied Brain
- https://ilovetesla.com/teslas-ai5-chip-hits-tape-out-revolutionizing-optimus-and-dojo-while-ai4-powers-safer-than-human-fsd/
- https://www.getrobothub.com/2026/02/28/the-tech-behind-the-bot-how-teslas-fsd-brain-powers-the-optimus-gen-3/
- https://applyingai.com/2025/08/tesla-refocuses-ai-chip-strategy-from-dojo-to-ai5-and-ai6-inference-engines/
- https://tahaabbasi.com/blog/taha-abbasi-tesla-dojo-ai-training-supercomputer-2026
- https://www.techspot.com/news/111005-tesla-restarts-dojo-ai-project-after-shutdown-pivots.html
- https://www.nextbigfuture.com/2025/10/tesla-vp-ashok-describes-technology-of-fsd.html
- https://en.wikipedia.org/wiki/Optimus_(robot)
- https://en.wikipedia.org/wiki/Tesla_Dojo

### Earnings & Official Statements
- Tesla Q1 2026 Earnings Call Transcript (April 22, 2026)
- https://eu.usatoday.com/story/cars/news/2026/04/22/elon-musk-tesla-optimus-robot-earnings-call/89741046007/
- https://assets-ir.tesla.com/tesla-contents/IR/TSLA-Q1-2026-Update.pdf

---

*Disclaimer: Tesla maintains high confidentiality around Optimus's core AI architecture (especially task planning layer specifics). This analysis is based on synthesis of public speeches, social media, video demos, and third-party technical analysis. As of April 2026, Optimus remains in early R&D stage; many technical details may continue to evolve.*

*Report generated: 2026-04-26*
