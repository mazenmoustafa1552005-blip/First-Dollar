---
name: first-dollar-video
description: Use to produce studio marketing video and images - storyboards, on-screen scripts, Google Flow prompt/shot lists, FFmpeg composition of supplied assets into 9:16 vertical videos with burned captions and covers, plus storefront mockup images.
---

# Video and image production

Also use user-level skills: `anthropic-skills:short-form-editor`, `video-captions`, `free-voiceover`, `pinterest-pins`.

## Inputs by line
- Mystery: page renders (pdftoppm), teaser clue card close-ups. Never show the solution page.
- Miniatures: real photos/video of a printed and assembled set supplied by the owner (printed-to-assembled reveal). Renders may be used for flat-sheet previews only, labelled as digital previews.
- Crochet: only real footage/photos of the finished sample.

## Pipeline
1. `products/<SKU>/content/storyboard.md`: hook (first 1.5 s), 5-8 shots, on-screen text, caption, CTA, cover frame.
2. If Google Flow is interactive only: write prompts and a shot list into `content/flow-prompts.md`; ingest exported clips into `assets/<SKU>/`. Veo API is billed: only after the owner approves the spend.
3. Compose with FFmpeg: 1080x1920, 30 fps, H.264 yuv420p, AAC, burned captions in the safe zone (avoid top 250 px and bottom 400 px). Script: `python3 scripts/make_preview_video.py <SKU>` (page-render teasers; add real footage clips the same way).
4. Inspect a frame at phone size before delivery.
