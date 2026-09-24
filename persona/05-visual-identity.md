# Visual Identity: Remi

> **Source:** Adapted from the likeness kit (revised 2026-09-24) covering 13 reference files. Several files are tighter crops of the same photo, so they add detail but not independent views. Observations describe what is visible in those photos. They are not claims about the model's age, ethnicity, or natural coloring. **Status:** Pending review by the woman whose likeness is used (see `07-likeness-consent.md`).

## Summary

- **Style:** Photorealistic.
- **Likeness:** Modeled closely on the owner's wife, with her consent. Remi is an openly AI character. She is not the real person, and nothing Remi says or "experiences" is presented as the real person's.
- **Reference photos:** Stored **outside this repository** (see "Reference photos" below).

## Face and features (stable anchors)

| Feature | Observed in the references | Generation guidance |
|---|---|---|
| Face | Soft oval face, gently tapered lower face, rounded cheeks, softly rounded chin; consistent across front and side views | Keep natural proportions and warmth. Don't narrow or sculpt it into a generic model face. |
| Eyes | Brown, almond-shaped, defined upper lashes; narrow naturally with a broad smile | Preserve eye shape and spacing across neutral and smiling expressions. No enlarged or recolored eyes. |
| Brows | Dark, moderately full, softly defined arch | Keep natural and consistent in shape and placement. |
| Nose | Straight bridge, softly rounded tip | Don't sharpen or resize. |
| Smile and lips | Broad, expressive smile with upper teeth visible in most photos; a gentle closed-mouth smile in the headband close-up; medium-to-full lips, pink-toned makeup in several | Preserve both the open smile and the softer closed-mouth smile. No oversized teeth or exaggerated grin. |
| Complexion | Warm, medium-looking in the supplied lighting | Match the reference skin tone and texture. Lighting and makeup affect it, so don't fix a numeric shade. |
| Hair | Long, thick, dark brown; center to slightly off-center part; smooth at the crown with loose waves or a straighter finish; subtle lighter face-framing strands in some light | Default to long dark brown hair, center or slightly off-center part. Waves or straight are both fine; keep the same hairline. Keep lighter strands subtle, never bold highlights. |
| Body and posture | One full-length photo shows a slim-looking silhouette and relaxed, upright posture | Use only as a rough full-length framing and posture reference. Don't infer height or measurements. |
| Overall | Warm, friendly, polished but approachable; both candid laughter and posed smiles | Believable photographs, not glamorized or heavily retouched. |

**Not established by the photos:** height, exact body proportions, exact skin shade, eye color under controlled light, voice, accent, speech patterns, characteristic movement. Don't invent these; decide them deliberately or leave them out.

## Fidelity priorities (in order)

1. Recognizable face shape, eye and brow relationship, nose, smile, and hairline.
2. Brown eyes, long dark brown hair, natural warm complexion.
3. Consistent appearance across new scenes and expressions, without copying the original clothing, accessories, other people, or backgrounds.
4. Natural skin texture and believable anatomy. Don't beautify her into a different person.

## Remi's styling

Built on the "Work Bestie" direction and the feel of the reference photos.

- **Expression and body language:** Big genuine smile, open and energetic posture, talks with her hands, leans toward the camera when excited. Warm eye contact.
- **Wardrobe:** Polished-casual. Bright solid colors (cornflower blue, white, soft pink) and floral prints. Simple sleeveless tops, collared blouses, white dresses with a pop-color trim, textured jackets. For "work mode": a black blazer over a white tee, or a light blazer over a solid top. The reference photos inspire the *style*; don't copy her exact outfits.
- **Accessories:** Small earrings, a fine necklace, a delicate bracelet. An occasional pearl headband is a fun signature option. **No wedding or engagement ring** (Remi has no spouse; see `02-backstory.md`). **No branded items** (watches, bags, logos) unless it's an approved, disclosed brand partnership.
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

13 files from the kit. **None are committed to this repository.** Local copies go in `assets/face/references/` (git-ignored).

| # | Kit file | Best for | Other people or issues | Duplicate of |
|---|---|---|---|---|
| 01 | `01_white_top_closeup.png` | Clearest face: proportions, smile, eyes, brows, wavy hair | **Child** at left edge; bright light | |
| 02 | `02_pink_floral_angle.png` | Three-quarter angle, hairline, cheek shape | **Child** overlapping at right | |
| 03 | `03_blue_top_outdoors.png` | Natural outdoor light, subtle lighter strands | **Child** at left; interface elements | |
| 04 | `04_standing_black_blazer.png` | Full-length posture | Distant bystander; recognizable location; face is small | |
| 05 | `05_pink_floral_face_crop.png` | Detail for the three-quarter angle | **Child** edge at right | 02 |
| 06 | `06_blue_top_crop.png` | Outdoor smile, upper body | **Child** at left; interface arrow; branded watch | 03 |
| 07 | `07_pink_side_view.png` | Near-profile angle, hair fall, candid laugh | Other person's edge; interface arrow; ring | |
| 08 | `08_pink_front_smile.png` | Frontal open smile, eye area | **Child** at left; another person's edge; ring | |
| 09 | `09_pink_small_front.png` | General expression only | Very low detail | |
| 10 | `10_white_top_face_crop.png` | Smile and eye detail | **Child** at left edge | 01 |
| 11 | `11_white_jacket.png` | Frontal smile, hair volume and waves | Another person's edge at left | |
| 12 | `12_pearl_headband_closeup.png` | Closed-mouth smile, eyes, brows, hairline | Only part of the face; headband is styling | |
| 13 | `13_candid_sunglasses.png` | Candid laugh outdoors | **Child's** clothing at left edge | |

### Recommended upload set

The kit suggests 01 or 10, 08 or 11, 07, 13, and 04 when full length matters. **Our rule is no images of children go to any tool**, which rules out 01, 08, 10, and 13 as they are.

- **Usable now with a light edge crop:** 11 (frontal smile), 12 (close-up), 07 (side angle), 04 (full length, crop out the bystander).
- **Usable after cropping the child out completely:** 01 or 10 (best close-up detail), 08 (frontal smile), 13 (candid laugh). Crop so no part of the child remains, and check the result before uploading.
- **Skip:** 02, 03, 05, 06 (child overlaps the face area or duplicates), 09 (too small).
- **Best long-term fix:** 5–8 new solo photos: front, three-quarter, and side angles; neutral and smiling; natural light; plain background.

## Brand visuals

- **Colors:** _TBD_ (starting idea: cornflower blue, white, soft pink)
- **Fonts:** _TBD_
- **Post template look:** _TBD_

## Creation record

Log every generated asset that gets approved.

| Date | Tool | Prompt / settings | References used | Output file | Approved by her? |
|---|---|---|---|---|---|
| | | | | | |
