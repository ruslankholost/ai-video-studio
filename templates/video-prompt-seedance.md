# Video prompt for Seedance 2.5

The main video prompt template. Use it for stage 06 (`docs/stages/06-video.md`). The prompt is a JSON object with Chinese keys and Chinese values, in a fixed field order. Seedance is a ByteDance model, reads Chinese natively, and Chinese is about three times shorter than the same detail in English or Russian, which leaves room for camera, acting and timecodes.

Check every prompt with `python scripts/check_prompt.py prompt.json` before it is sent. The script checks the structure below, not the quality of the writing or typos in characters. Reread the Chinese yourself.

## The three rules

1. **Camera first.** In every shot the camera field comes before the picture field and is written in detail: position, height in metres or centimetres, angle to the subject, focal length, what is in focus. The model never invents a camera. Without it the camera sits flat in front of the scene and objects can turn around backwards.
2. **Acting through the body in every shot.** For every visible person: pose, action in order, emotion shown by face, hands and torso (never a bare word like "scared"), manner of speech if they talk, a gesture on a named word, and what the people in the second plan do. Without this the model produces blank dummies: stiff posture, empty face, hanging arms.
3. **Only what is seen and heard.** The prompt describes the video. Do not write rules to the model ("the camera matters most", "every character must act"), process notes ("voice added later", "this is a previz", "draft"), explanations of why, or the same fact twice. A fact true for the whole video goes once in a general field. A fact about one shot goes only in that shot.

## Output format

Give the user two versions in one reply:

1. A plain-text English version for reading, in the same field order as the JSON so the two can be compared block by block. Mark it as a draft. It is usually longer than 5000 characters, which is fine, it is not pasted.
2. The Chinese JSON for pasting, in one code block with nothing but JSON inside, and under it a line `Characters: N / 5000` with the number from `check_prompt.py`.

Dialogue stays in the language the character speaks. Never translate it.

JSON rules:
- Keys exactly as in the table below, in that order. Leave out a field you do not need, never leave an empty field. The exception is the acting field, which every shot has.
- Write Chinese as characters, not `\uXXXX` escapes. If code builds the JSON, use `json.dumps(..., ensure_ascii=False)`.
- No straight double quotes inside a string, one of them breaks the JSON. Put dialogue and gesture words in guillemets `« »`.
- Indent with 2 spaces. If that does not fit in 5000, send the compact one-line form, spaces are counted too.
- No brand or studio names ("in the style of ..."). Describe the picture instead: large-format look, clean sharp image, wide latitude, warm sun against cool shadows.
- Never put the agent's own signature or any tool name inside the prompt body. Seedance can draw text from the prompt on screen.

## Fields, in this exact order

| Field | What it holds |
|---|---|
| `概述` | Overview, one string: duration in seconds ("12秒"), orientation, genre, image quality, time of day and light. |
| `参考素材分工` | Reference block, an object. Key is one reference (`@Image1`) or a group (`@Image4、@Image5`). Value says what to take AND what not to take. |
| `角色固定` | Character lock: look and clothes of each person, and how they carry themselves through the whole video. |
| `物体固定与朝向` | Object lock and orientation: for anything that moves, which end is the front, named by anchor details. |
| `整体风格` | Overall style: picture properties, not brand names. |
| `场景` | Scene rules, a list of strings: what holds for the whole video (who is where and never swaps, who stays silent, one continuous take, slow motion limits). |
| `人声` | Voice. Only when an `@Audio1` track supplies the voice. No dialogue text here. |
| `分镜` | Storyboard, a list of shots. Each shot has the fields below. |
| `声音` | Sound: an object with `总则` (general rule, a string) and `分段` (a list of `{时间, 内容}`). |
| `负面提示` | Negative list: short list of artifacts to avoid. |

Required: `概述`, `分镜`, `负面提示`. The rest depend on the job.

Fields of each shot, in this order:

| Field | What it holds |
|---|---|
| `时间` | Time range in whole seconds, `"0s-3s"`. |
| `衔接` | Link to the previous shot, only if needed: `切到` or `硬切到` (cut), `同一镜头不剪辑` (same continuous shot). |
| `机位` | Camera: position, height, angle, focal length, focus. For a moving camera write the path, not two points. |
| `画面` | Picture: what happens and what is visible. |
| `表演` | Acting, see rule 2. A shot with nobody in it says `画面中没有人物。` so it is clear the shot was checked. |
| `台词` | Dialogue, only if someone speaks, in the speaker's language, in `« »`, with the language named: `她用英语说：«...»`. The line appears here and nowhere else, or the model hears two lines. |

## Writing acting

Write for each person in each shot:
1. Pose, specific: not "stands" but "leans a shoulder on the wall, weight on one leg, other foot crossed over it".
2. Actions of hands and body, in order.
3. Emotion by what can be seen. Face: brows (raised, drawn together, one higher), eyes (wide, narrowed, darting), mouth (open, pressed, a corner pulled up), nose, cheeks. Hands: gripping, spread fingers, covering the face. Torso and head: head pulled into shoulders, leaning back, a sharp turn.
4. Manner of speech: pace, volume, tone, where they look while speaking.
5. A gesture on a word: on the word «blender» she raises an eyebrow and nods at the camera. The word goes in guillemets inside the acting field.
6. Second plan: what people around do. If extras must not speak, say "they only shout, no words", or the model gives them lines.

When two people share a frame, give them different emotions. A panicking driver next to a bored passenger reads stronger than two scared faces.

Slow motion is allowed. Say so in the shot with its limits ("from the impact slow motion: shards hang in the air; when she finishes speaking time snaps back to normal"), and slow the acting too.

## The reference block

Every `@ImageN`, `@VideoN` and `@AudioN` in the prompt must be declared in `参考素材分工`, each with a role. Images, videos and audio are numbered separately (`@Image1`, `@Video1`, `@Audio1`). Upload in exactly the order the prompt uses.

- Say what is taken and what is not: `只提供...，不提供...` ("provides only ..., not ..."). Every object reference drags in the place it was photographed, and that background leaks into any window, doorway or reflection. Limit each one: "interior structure only, no outside environment or light; the window shows a moving highway".
- A character card gives look and clothes only: `只提供外貌和服装，不提供姿势和表情`. Pose and expression come from the acting field. Otherwise the person freezes like the neutral card.
- Group several cards for one role (three angles of one car, four cards of one location). It is more reliable than one card per role.
- When there are more than two references the block is required, or the model mixes the look of a character with the people on style and location cards. Add `避免参考之间身份混合` to the negative list.
- "Unlike": `与 @Image4 不同的是，这个世界里的车全都在天上飞。` takes a location and changes one property. Repeat the ban in the negative list.
- The previz video is described in `templates/previz-in-video-prompt.md`.
- Audio: the voice comes from the track. In `人声` write `人声只来自 @Audio1，不要重新合成人声，口型与这段音频逐字对齐。` The dialogue text still goes in the shot's `台词`, because it sets the word boundaries for lip sync. Ask for the audio length, round up to whole seconds, and size the shot to it.

## Timecodes

- Whole seconds only: `0s-2s`, `2s-5s`. Never `2.5s`, `1,5s`, `第2.5秒`, anywhere in the prompt. The shortest block is 1 second.
- Blocks are contiguous from 0 with no gaps and cover the whole duration.
- An event shorter than a second (a flash, a hit) is not its own block. Order it in words inside a whole-second block: "at the start of the block", "right after the hit".
- A line of speech takes about 2 to 2.5 words per second. Round up.
- At most 15 cuts in 30 seconds. For dense editing keep at least 2 s per shot, for drama 3 to 4 s.
- Timing is followed accurately: on a 30 s test the key moments landed on the second.

## Batches

Plan in batches of 10 to 15 seconds. One pass can reach 30 s on Seedance 2.5, but quality and control are better in short batches, and a failed batch costs less. The checker accepts up to 30 s per prompt.

- Use the last good frame of one batch as the `start_image` of the next.
- Repeat the character lock and the reference block in every batch.
- Cut a long scene at a natural seam: a hard cut, a change of place, a pause. Not in the middle of slow motion or a transformation.
- A scene with a lot of dialogue works better as two passes of 15 s than one of 30 s.

## Transformations and effects

Models cheat: they cover the change with a white flash and show the finished result.
- Forbid it in `场景`: `变形不允许用闪白遮盖，不允许直接跳到变形完成的结果。`
- Give each phase its own camera, about 2 seconds each, walking around the object: three-quarter front, macro at ground level, clean profile, three-quarter rear from above. Add: each cut must show the change further along than the last.
- Describe the physics of each phase: what the effect is made of ("a stream of ice crystals, snow and frost vapour, glowing pale blue from inside", not "ice magic"), how it touches the surroundings, and the light it throws.
- Give the object one detail that never changes (a visual anchor) and say it twice.
- Fix front and back of every moving object by named anchor details, put it in `物体固定与朝向`, show the anchors facing the lens in one shot, and ban the wrong direction in the negative list.
- Negative for effects: `避免彩色粉末云，避免颜料烟雾，避免平面彩色雾气，避免特效边缘伪影`.

## Sound

For videos over 15 s split the sound by timecodes in `声音.分段`, also in whole seconds. Say `没有背景音乐` in the general rule unless music was asked for, and repeat it in the negative list. Tricks that give scale: change the listening point (inside the car the engine is muffled, breath is close), two seconds of near silence after a bang, a build from far to near, in slow motion the sound drags and dulls.

## Negative list

Base set, the value of `负面提示`:

```
避免参考之间身份混合，避免面部漂移，避免年龄漂移，避免换装，避免多手指，避免手部变形，避免人物僵硬，避免面无表情，避免假人一样的动作，避免参考图的拍摄环境背景泄漏进画面，避免卡通感，避免字幕，避免屏幕文字，避免水印，避免背景音乐，避免边缘伪影。
```

Add `避免慢动作` only when the video must have no slow motion. Add object-specific lines (`避免车辆倒着行驶`, `避免变形中丢失视觉锚点`). Every problem you closed in the body text is repeated here once.

## Calling it on Higgsfield

Check `models_explore` for the current model list and `estimate_video_cost` for the price in credits before any paid run, and get the user's explicit "yes" on the exact list first (model, number of jobs, credits).

Call `generate_video` with:
- `model`: `seedance_2_5` (or `seedance_2_5_flash` for cheaper tests).
- `prompt`: the Chinese JSON text, exactly as checked.
- `start_image`: the first frame (an approved frame from stage 04, or the last frame of the previous batch).
- `image_references`: the character, location and object cards, in the order of `@Image1`, `@Image2`, ...
- `video_references`: the previz video as `@Video1` (see `templates/previz-in-video-prompt.md`).
- `audio_references`: a voice track as `@Audio1` if the voice is supplied.
- Resolution `480p` for drafts, aspect ratio `9:16` for vertical, duration 10 to 15 s per batch.

Upload local files first with `media_upload` and `media_confirm`. Run drafts at 480p and approve the motion before spending more. Use `jobs_wait` to follow the job.

Platform limits: 5000 characters for the whole JSON including brackets and indentation, up to 30 s per pass, up to 50 reference images, whole-second timecodes. The editing filter on already generated video is separate and can reject action-heavy clips. If one is rejected, retry, cut a shorter sensitive-free piece, or regenerate the whole clip.

## Complete example, a 12 s two-shot scene

Two people in a kitchen at dusk, a late partner. Vertical 9:16, four shots, one dialogue line each from two speakers, a previz video for the camera.

```json
{
  "概述": "12秒，竖屏9:16，剧情片，真实电影质感，傍晚，窗边暖色台灯光加冷色窗外天光",
  "参考素材分工": {
    "@Image1": "女主角参考，只提供外貌和服装，不提供姿势和表情。",
    "@Image2": "男主角参考，只提供外貌和服装，不提供姿势和表情。",
    "@Image3": "厨房场景参考，只提供空间布局、家具和光线，不提供人物。",
    "@Video1": "只提供镜头运动、人物位置、路线和时间，不提供人物外貌、表情和手部动作。"
  },
  "角色固定": "女主角（@Image1）：三十岁左右，齐肩黑发，米色毛衣，全片不变，克制、冷静。男主角（@Image2）：三十五岁左右，短发，深蓝衬衫，袖子卷到手肘，全片不变，尴尬、想缓和气氛。",
  "整体风格": "画面干净锐利，宽容度高，暖色灯光对比冷色窗光，浅景深，肤色自然。",
  "场景": [
    "全片在同一间厨房，女主角始终在灶台一侧，男主角始终从门口一侧进入，两人隔着中岛，位置不互换。",
    "只有这两人说话，每人一句，其余时间没有对白。"
  ],
  "分镜": [
    {
      "时间": "0s-3s",
      "机位": "正面平视双人中景，离中岛约三米，高度一米四，35毫米，焦点在两人之间的中岛台面。",
      "画面": "傍晚的厨房，女主角站在灶台旁，男主角从门口走到餐桌旁放下公文包。",
      "表演": "女主角：背靠灶台，双臂交叉，重心压在右脚；眉头微蹙，嘴唇抿紧，目光跟着男主角移动。男主角：脚步放慢，肩膀下沉，低头避开她的视线，手指慢慢松开公文包把手。"
    },
    {
      "时间": "3s-6s",
      "衔接": "硬切到",
      "机位": "男主角肩后过肩镜头，高度一米六，女主角在画面远端，50毫米，焦点在女主角的脸。",
      "画面": "女主角向前走一步，右手按在中岛台面上。",
      "表演": "女主角：身体前倾，指尖轻敲台面；一边眉毛挑起，嘴角下压；压低声音、语速很慢，说到«six»时目光直直盯住对方。男主角（背影）：肩膀僵住，头微微低下。",
      "台词": "她用英语说：«You said you'd be home by six.»"
    },
    {
      "时间": "6s-9s",
      "机位": "女主角面部特写，高度一米六，平视，85毫米，焦点在眼睛，背景虚化。",
      "画面": "她安静地等他回答，背景里男主角的身影模糊。",
      "表演": "女主角：下巴微抬，眼睛一眨不眨，鼻翼轻动，嘴唇微张又合上，手指停在台面上不动。背景虚化处的男主角：抬手揉后颈，肩膀缩起。"
    },
    {
      "时间": "9s-12s",
      "衔接": "硬切到",
      "机位": "回到正面平视双人中景，与0到3秒同一机位，高度一米四，35毫米，焦点在两人之间。",
      "画面": "男主角绕过中岛走向她，两人间距缩到一米。",
      "表演": "男主角：双手摊开、掌心向上，肩膀耸起，苦笑，眼睛看着她；声音低、语速慢，说到«cook»时指向灶台。女主角：双臂仍然交叉，翻了个白眼，嘴角却忍不住往上抬一点，头偏向一边。",
      "台词": "他用英语说：«I know. I'm sorry. Let me cook.»"
    }
  ],
  "声音": {
    "总则": "真实环境音，全片没有背景音乐。",
    "分段": [
      {"时间": "0s-3s", "内容": "公文包放下的闷响，冰箱低频嗡鸣，远处街道的车声。"},
      {"时间": "3s-6s", "内容": "近距离的声音，指尖敲台面，她压低的声音清晰。"},
      {"时间": "6s-9s", "内容": "几乎安静，只有呼吸声和冰箱嗡鸣。"},
      {"时间": "9s-12s", "内容": "脚步声靠近，他的声音低而温和，台词清晰。"}
    ]
  },
  "负面提示": "避免参考之间身份混合，避免面部漂移，避免换装，避免手部变形，避免人物僵硬，避免面无表情，避免假人一样的动作，避免参考图的拍摄环境背景泄漏进画面，避免两人位置互换，避免慢动作，避免卡通感，避免字幕，避免屏幕文字，避免水印，避免背景音乐，避免边缘伪影。"
}
```

English gloss, field by field:
- Overview: 12 s, vertical 9:16, drama, realistic film look, dusk, warm lamp light against cool window light.
- References: card 1 and 2 give look and clothes only, no pose or expression; card 3 gives the kitchen layout, furniture and light, no people; the previz video gives only camera movement, positions, paths and timing, not looks, expressions or hands.
- Character lock: she is about thirty, shoulder-length black hair, beige sweater, restrained and calm. He is about thirty-five, short hair, dark blue shirt with sleeves rolled to the elbow, awkward and wanting to ease the mood. Neither changes.
- Style: clean sharp picture, wide latitude, warm light against cool window light, shallow depth of field, natural skin.
- Scene: one kitchen the whole time; she stays on the stove side, he enters from the door side, they never swap; only these two speak, one line each.
- Shot 0s-3s: front-on eye-level two-shot, about 3 m from the island, 1.4 m high, 35 mm, focus on the island between them. He walks to the table and puts down a briefcase. She leans on the stove, arms crossed, weight on the right foot, brows slightly drawn, lips pressed, eyes following him; he slows his steps, shoulders drop, eyes down, fingers slowly let go of the handle.
- Shot 3s-6s: hard cut, over his shoulder, 1.6 m high, she is at the far end, 50 mm, focus on her face. She steps forward and puts her right hand on the island. She leans in, tapping a fingertip, one eyebrow up, mouth corners down, low and very slow voice, eyes locked on him on the word "six"; he is seen from behind, shoulders stiff, head dipping. Dialogue: "You said you'd be home by six."
- Shot 6s-9s: close-up of her face, 1.6 m, eye level, 85 mm, focus on the eyes, blurred background. She waits quietly. Chin slightly up, no blinking, nostrils moving, lips open and close, fingers still. In the blur he rubs his neck, shoulders hunched.
- Shot 9s-12s: hard cut back to the first two-shot position. He walks around the island to her, the gap shrinks to one metre. He spreads his hands palms up, shoulders raised, rueful smile, low slow voice, points at the stove on the word "cook". She keeps her arms crossed, rolls her eyes, a corner of her mouth lifts, head tilts. Dialogue: "I know. I'm sorry. Let me cook."
- Sound: real room sound, no music, split in four whole-second segments matching the shots.
- Negative list: the base set plus "no swapping of the two people's places" and "no slow motion", because this scene has none.

## Check before sending

1. `python scripts/check_prompt.py prompt.json` prints OK.
2. Camera is first and detailed in every shot.
3. Acting is in every shot, by body and face, not by emotion words.
4. Timecodes cover the whole duration in whole seconds.
5. Every reference has a role with "takes" and "does not take".
6. Moving objects have front and back fixed, transformations have a visual anchor.
7. Dialogue appears only in its own shot.
8. Audio length is counted and rounded up if a track is used.
9. Every fixed problem is repeated in the negative list, and slow motion is removed from it if the video has slow motion.
10. No brand names, no rules to the model, no process words, no repeated facts.
11. The Chinese was reread for wrong characters.
12. Both versions are given, and the upload order of references is stated.
