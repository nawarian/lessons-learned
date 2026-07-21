# Session Handoff — Next Agent

## Session Context

The user is learning about **diffusion-based language models** for text generation. They are an experienced software engineer with some AI familiarity, who has trained small models but doesn't design architectures. They want to understand whether they can build and train diffusion LMs themselves.

### Hardware Constraints
- **Local**: 8 GB VRAM GPU
- **Cloud**: 1× L40S (48 GB VRAM), 64 GB RAM, 8 vCPUs, ~100 GB SSD (expandable)
- **Potential cluster**: nodes with 2× L40S each

### What's Been Built
- `MISSION.md` — Mission document (buildable on single GPU, Portuguese angle)
- `RESOURCES.md` — Curated resources (MDLM, SEDD, D3PM, Diffusion-LM, LLaDA, DiffuMamba, etc.)
- `GLOSSARY.md` — Core terminology
- `NOTES.md` — User preferences
- `LESSON-PLAN.md` — 7-lesson plan (v2)
- `assets/lesson.css` — Shared stylesheet (Tufte-inspired, light/dark mode)
- `reference/cost-and-hardware.html` — Cost/specs reference table
- `reference/training-costs-deep-dive.html` — Cluster training feasibility analysis
- **Lesson 0001** (`lessons/0001-feasibility-check.html`) — Economics & hardware reality
- **Lesson 0002** (`lessons/0002-why-not-autoregressive.html`) — The AR sequential bottleneck, interactive simulation
- **Bridge note 0002b** (`lessons/0002b-context-prompting-output-length.html`) — Context window, prompting, output length constraints
- **Lesson 0003** (`lessons/0003-core-mechanics.html`) — Forward/reverse diffusion, why text is hard, three solution families (continuous, discrete, masked), interactive 2D visualization
- **Bridge note 0003b** (`lessons/0003b-context-length-management.html`) — Context length scaling, VRAM analysis, four levers for long-context MDLMs (sliding window, SSM, block-AR, brute-force), DiffuMamba's strategic importance for 200K
- `learning-records/0001` through `0006` — Session progression

### Key Findings So Far
1. **16× compute gap**: Masked diffusion needs 16× more training FLOPs than AR for same loss (per SMDM paper)
2. **Output length**: Must be fixed upfront in pure diffusion; block-autoregressive (DiffusionGemma) is the main workaround
3. **Length router idea** (user's own architectural intuition): a lightweight classifier (like MoE router) that predicts ideal output length from prompt → feed to diffusion LM as conditioning. Marked as **future experiment**, not part of lesson plan
4. **Portuguese angle**: Vocabulary reduction + domain-specific data makes training more accessible. User interested in this direction
5. **DiffuMamba**: SSM backbone critical for long-context diffusion; code not yet publicly released
6. **Context length wall**: Pure transformer MDLMs at 200K won't fit on L40S (activations alone exceed 48 GB). SSM backbone or block-AR required for long-context coding tasks
7. **User interest in coding at 200K tokens** — confirmed this is a target use case. Pure MDLM with transformer backbone is suboptimal here vs AR + KV-cache. DiffuMamba SSM approach is the architecture to watch

### Next Lesson (0004): Masked Diffusion Deep-Dive
Not yet built. Should cover:
- The MDLM algorithm in detail
- The [MASK] schedule: how many tokens to mask at each timestep
- The loss function: cross-entropy on masked vs unmasked predictions
- Relationship to BERT and why it's NOT the same as masked LM
- Why MDLM is simpler than D3PM and more reliable than continuous approaches
- Interactive simulation: watch tokens get masked/unmasked over timesteps

### Subsequent Lessons (planned)
- **0005**: Hands-On — train a tiny masked diffusion LM (on 8 GB GPU, 256-token context)
- **0006**: At Scale — DiffusionGemma & DiffuMamba architectures
- **0007**: Scaling Laws & Build Decision — synthesis for L40S

### Teaching Preferences (from NOTES.md)
- Hands-on > pure theory; always accompany explanation with code or visual
- Theoretical intuition needed to read papers, not derive proofs
- Concise, focused lessons (one tangible win per session)
- Hardware-conscious: every technique discussed should include cost note

### Files to Open
When starting a new session and the user asks to continue, open:
1. `MISSION.md` — to reorient
2. `NOTES.md` — to recall preferences
3. The next unbuilt lesson in sequence
