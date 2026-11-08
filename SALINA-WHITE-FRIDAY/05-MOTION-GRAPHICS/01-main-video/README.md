# الفيديو الرئيسي: ملفات المصدر وطريقة التعديل

| الملف | وظيفته |
|---|---|
| `main-video.html` | الحركة كلها: رسومات SVG وكلام HTML، وكل إطار بيتحسب من الوقت بالدالة `renderAt(t)` |
| `audio.py` | المؤثرات الصوتية (numpy)، وبيطلّع `soundtrack.wav`. الموسيقى مقفولة (`MUSIC = False`) |
| `soundtrack.wav` | الصوت الجاهز اللي بيتركّب على الفيديو |
| `../../07-SOURCE-FILES/render-video.js` | بيطلّع الإطارات من الصفحة ويحوّلها لفيديو بـ ffmpeg |
| `../../06-STORYBOARDS/01-main-video/` | الـ Storyboard وصور الإطارات |
| `../../08-EXPORTS/video/salina-wf-main-video-1080x1920.mp4` | الفيديو النهائي |

## المعاينة في المتصفح
افتحي `main-video.html#play` في Chrome، والفيديو هيشتغل لوحده ويعيد من الأول.

## التعديل
- **الكلام:** النص مكتوب في عناصر `#s1a … #s4d` جوه ملف HTML، تدوّري عليه وتغيّريه.
- **التوقيت:** كل حركة ليها وقت بداية ونهاية بالثواني جوه `renderAt`، مثلًا `P(t, 10.3, 10.75)` معناها إن «استثمري» بتدخل من الثانية 10.3 لـ 10.75. لو حرّكتي حركة، حرّكي المؤثر الصوتي بتاعها بنفس الوقت في `audio.py`.
- **الألوان:** متحددة في `:root` أول الملف (`--pu`, `--gd`, …).
- **العناصر:** مكان وحجم وميل كل حاجة مكتوبين في الجداول `BAGS` و`ITEMS` و`LEARN` و`SB`.

## التصدير
الأوامر دي بتتشغّل من فولدر `SALINA-WHITE-FRIDAY`:
```bash
python3 05-MOTION-GRAPHICS/01-main-video/audio.py 05-MOTION-GRAPHICS/01-main-video/soundtrack.wav
```
```bash
node 07-SOURCE-FILES/render-video.js 05-MOTION-GRAPHICS/01-main-video/main-video.html /tmp/main-silent.mp4
```
```bash
ffmpeg -y -i /tmp/main-silent.mp4 -i 05-MOTION-GRAPHICS/01-main-video/soundtrack.wav -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-15:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k -shortest -movflags +faststart 08-EXPORTS/video/salina-wf-main-video-1080x1920.mp4
```
