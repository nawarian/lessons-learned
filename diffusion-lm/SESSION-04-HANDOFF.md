# Session Handoff — Next Agent

## Session Context (2025-07-20)

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
- **Bridge note** (`lessons/0002b-context-prompting-output-length.html`) — Context window, prompting, output length constraints
- `learning-records/0001` through `0004` — Session progression

### Key Findings So Far (for Lesson 0003+)
1. **16× compute gap**: Masked diffusion needs 16× more training FLOPs than AR for same loss (per SMDM paper)
2. **Output length**: Must be fixed upfront in pure diffusion; block-autoregressive (DiffusionGemma) is the main workaround
3. **Length router idea** (user's own architectural intuition): a lightweight classifier (like MoE router) that predicts ideal output length from prompt → feed to diffusion LM as conditioning. Marked as **future experiment**, not part of lesson plan
4. **Portuguese angle**: Vocabulary reduction + domain-specific data makes training more accessible. User interested in this direction
5. **DiffuMamba**: SSM backbone critical for long-context diffusion; code not yet publicly released

### Next Lesson (0003): Core Mechanics
Not yet built. Should cover:
- Forward diffusion process (adding noise/masking over timesteps)
- Reverse diffusion process (denoising)
- Why text is hard (discrete tokens vs continuous diffusion)
- Three solution families: continuous embedding space (Diffusion-LM), discrete transitions (D3PM), masked diffusion (MDLM)
- Interactive visualization of forward/reverse pass

### Subsequent Lessons (planned)
- **0004**: Masked Diffusion deep-dive (MDLM algorithm)
- **0005**: Hands-On — train a tiny masked diffusion LM (on 8 GB GPU)
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
