# Visual Identity: Remi

> **Source:** Adapted from the likeness kit prepared 2026-09-24 from three reference photos. Observations describe what is visible in those photos. They are not claims about the model's age, ethnicity, or natural coloring. **Status:** Pending review by the woman whose likeness is used (see `07-likeness-consent.md`).

## Summary

- **Style:** Photorealistic.
- **Likeness:** Modeled closely on the owner's wife, with her consent. Remi is an openly AI character. She is not the real person, and nothing Remi says or "experiences" is presented as the real person's.
- **Reference photos:** Stored **outside this repository** (see "Reference photos" below).

## Face and features (stable anchors)

| Feature | Observed in the references | Generation guidance |
|---|---|---|
| Face | Soft oval face, gently tapered lower face, full cheeks, rounded chin | Keep natural proportions and warmth. Don't narrow or sculpt it into a generic model face. |
| Eyes | Brown, almond-shaped, defined upper lashes | Preserve eye shape and spacing. No enlarged or recolored eyes. |
| Brows | Dark, moderately full, softly defined arch | Keep natural and consistent in shape and placement. |
| Nose | Straight bridge, softly rounded tip | Don't sharpen or resize. |
| Smile and lips | Broad, expressive smile; upper teeth visible; naturally full lips with pink-toned makeup | Preserve smile shape and natural teeth. No oversized teeth or exaggerated grin. |
| Complexion | Warm, medium-looking in the supplied lighting | Match the reference skin tone and texture. Lighting and makeup affect it, so don't fix a numeric shade. |
| Hair | Long, thick, dark brown; center to slightly off-center part; soft waves or straighter finish; a few lighter face-framing strands outdoors | Default to long dark brown hair, center or slightly off-center part. Waves or straight are both fine; keep the same hairline. |
| Overall | Warm, friendly, polished but approachable | Believable photographs, not glamorized or heavily retouched. |

**Not established by the photos:** height, full-body proportions, exact skin shade, eye color under controlled light, voice, accent, gestures. Don't invent these; decide them deliberately or leave them out.

## Fidelity priorities (in order)

1. Recognizable face shape, eye and brow relationship, nose, smile, and hairline.
2. Brown eyes, long dark brown hair, natural warm complexion.
3. Consistent appearance across new scenes, without copying the original clothing or backgrounds.
4. Natural skin texture and believable anatomy. Don't beautify her into a different person.

## Remi's styling

Built on the "Work Bestie" direction and the feel of the reference photos.

- **Expression and body language:** Big genuine smile, open and energetic posture, talks with her hands, leans toward the camera when excited. Warm eye contact.
- **Wardrobe:** Polished-casual. Bright solid colors (cornflower blue, white, soft pink) and floral prints. Simple sleeveless tops, blouses with collars, light blazers for "work mode." Delicate jewelry, such as a fine necklace.
- **Signature color idea:** Cornflower blue, as seen in one reference. Use it often so she's recognizable at a glance. *(Suggestion; confirm.)*
- **Settings:** Bright home office or desk with laptop and notebook; café table; clean white or soft-colored backdrop for talking-head videos. Natural daylight.
- **Always excluded:** Children, other real people, the original photo backgrounds, social media interface elements, watermarks.

## Consistency plan

1. **Pick one "anchor" reference** (the clearest close-up) for face fidelity, and use all adult-only references together when a tool supports multiple images.
2. **Use the master identity prompt** in `06-generation-prompts.md` every time, then add the scene.
3. **Save approved outputs.** Once a generated image is approved, save it with its exact prompt and use it as a future reference.
4. **If the likeness drifts,** change one thing at a time: use a clearer reference, reduce stylization, simplify the scene, frame closer, or pick a different take.
5. **Don't assume a tool "remembers" her.** Only treat a saved character or avatar as persistent if the platform says it is, and only after she approves building one (see `07-likeness-consent.md`).

## Reference photos

| Kit file name | Best for | Caution |
|---|---|---|
| `01_white_top_closeup.png` | Clearest face: proportions, smile, eyes, brows, wavy hair | Bright studio-like light affects apparent skin tone. **Child at left edge.** |
| `02_pink_floral_angle.png` | Three-quarter angle, hairline, cheek shape | **Child at right edge, overlapping.** |
| `03_blue_top_outdoors.png` | Natural outdoor light, lighter hair strands, upper body | **Child at left.** Screenshot crop with interface elements; don't reproduce them. |

**Storage rule:** These photos are not committed to this repository, because they show a real person and a child. `assets/face/references/` is ignored by git for local working copies. **Recommended:** replace these with a set of **solo, adult-only** photos of her (several angles, neutral and smiling, natural light), so no tool ever receives an image of a child.

## Brand visuals

- **Colors:** _TBD_ (starting idea: cornflower blue, white, soft pink)
- **Fonts:** _TBD_
- **Post template look:** _TBD_

## Creation record

Log every generated asset that gets approved.

| Date | Tool | Prompt / settings | References used | Output file | Approved by her? |
|---|---|---|---|---|---|
| | | | | | |
