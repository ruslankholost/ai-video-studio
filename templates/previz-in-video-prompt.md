# Previz in the video prompt

How the Blender previz montage (stage 05, `docs/stages/05-previz-camera.md`) is attached to the video generation (stage 06) and what the prompt says about it. The previz is a moving blueprint: grey or coloured figures and boxes that show where the camera goes and where everyone stands and walks, with no faces, no hands and no textures. The video model copies what the prompt tells it to copy. If the prompt does not say what the blueprint is for, the model copies too much (flat shapes, blank bodies) or too little.

## Attach it

On Higgsfield pass the previz in `video_references`. It becomes `@Video1` (the first video; images and audio are numbered separately). See `templates/video-prompt-seedance.md` for the full call.

- Seedance 2.5: `seedance_2_5`, previz in `video_references`, drafts at 480p.
- Kling 4.0: `kling4_0`, mode reference-to-video, previz in `video_references`. Each side of the previz must be at least 700 px (a 640x480 render is rejected; render 960x720 or upscale with `ffmpeg -vf scale=960:720:flags=lanczos`). Each video is 3 to 30 s, all videos together at most 30 s, up to 5 videos, 300 MB, mp4 or mov. Kling has a separate video-edit mode that changes the video itself and starts with "Edit @Video1". Previz is a reference, not an edit.
- Render the previz at the same aspect ratio as the final video.

## The role line

The reference block must give `@Video1` a role, and the role is movement only.

Seedance, in the `参考素材分工` field:

```
"@Video1": "只提供镜头运动、人物位置、路线和时间，不提供人物外貌、表情和手部动作。"
```

English meaning: `@Video1` gives only camera movement, character positions, paths and timing; not looks, faces, expressions or hands.

Pair it with acting in every shot. The figures have no faces and no hands. If the acting field is empty the model repeats the blueprint literally: a motionless body and an empty face. The look comes from the character cards, the performance from `表演`.

## Name every figure

When the previz has several figures, say what each one becomes, with its card. Otherwise the model does not know which figure is whom.

Kling, in the active-references block (English):

```
@Video1 is a colored white-model blocking animation of this exact shot, with no sound.
It is a moving blueprint and controls only the motion: the camera's path, height,
framing and lens changes, the timing and speed changes, and the positions and paths of
the people and objects. Follow it frame by frame. Its pink figure becomes the heroine
from @Image4, its light-blue figure becomes the driver from @Image5, its black box
becomes the car from @Image3, its room becomes the hall from @Image1. Do not take its
flat untextured shapes, primitive geometry, colors or lighting.
```

For Seedance use the same idea in Chinese, one line per figure inside `参考素材分工`, for example `"@Video1": "只提供镜头运动、人物位置、路线和时间。粉色人形是 @Image4 的女主角，蓝色人形是 @Image5 的司机，黑色方块是 @Image3 的车。不提供人物外貌、表情和手部动作。"`.

## Other rules

- Orientation of anything that moves is fixed in words, in the object lock field (Seedance) or the location map (Kling): "both cars drive nose first from frame-left to frame-right. This never changes."
- The timecodes of the prompt must match the previz: cuts and key moments in the text sit on the same seconds as in the montage.
- Name every person in every shot, or a figure from the previz can go missing (a car once drove four seconds with no driver because the shot did not name him).
- A short clean previz is copied better than a long one. Trim it to the part the batch needs.
- The previz is only a guide. Check the generated draft against it for camera jumps, drifting positions and wrong order, and fix the prompt, not the previz, when the model drifts.
- Never write process words about the previz inside the prompt body beyond the role line ("this is a previz", "for the lesson").
