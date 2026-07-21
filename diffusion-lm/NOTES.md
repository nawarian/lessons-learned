# Diffusion Language Models — Notes

## User Preferences
- Hands-on > pure theory. Always accompany an explanation with code or a visual.
- Theoretical intuition needed to read papers, not to derive proofs.
- Prefers concise, focused lessons (one tangible win per session).
- Hardware-conscious: every architecture/technique discussed should include a "what does this cost" note.

## Teaching Approach
- Start with "why NOT autoregressive" to motivate the mission.
- Use image diffusion as an analogy wall, then show what breaks for text.
- Tiny experiments (character-level diffusion) before discussing billion-parameter papers.
- Each lesson ends with a pointer to the next, so the user sees the arc.

## Viability Assessment Notes (to fill as we go)
- DiffusionGemma: based on Gemma 2B/7B backbones. Training from scratch on L40S likely infeasible (billions of tokens). Fine-tuning or distillation might be possible.
- DiffuMamba: S4/SSM backbone. More efficient per-token, possibly more accessible.
- Tiny own experiments: definitely feasible on 8 GB with small vocab and short sequences.
