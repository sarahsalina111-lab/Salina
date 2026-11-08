# فيديو ٢ «Shopping vs. Learning»: ملفات المصدر

| الملف | وظيفته |
|---|---|
| `video.html` | الحركة كلها، وكل إطار بيتحسب من الوقت بالدالة `renderAt(t)`. افتحيه بـ `#play` عشان تشوفيه شغال |
| `audio.py` | المؤثرات الصوتية (من غير موسيقى)، وبيستخدم `../lib/sfx.py` |
| `soundtrack.wav` | الصوت الجاهز |
| `../../08-EXPORTS/video/salina-wf-shopping-vs-learning-1080x1920.mp4` | الفيديو النهائي |

## التعديل
- **الجمل اللي تحت كل نص:** في `CAPS_R` و`CAPS_L`، ولكل جملة وقت ظهورها.
- **مستويات العدادين:** في `meter('mRf', …)` و`meter('mLf', …)`، وكل مستوى مكتوب كـ [الوقت، القيمة من 0 لـ 1].
- **أوقات المراحل:** في `DAY` و`MONTH` و`YEAR` و`OUT`. لو غيّرتي وقت، غيّري المؤثر بتاعه في `audio.py` بنفس الوقت.

## التصدير
الأوامر دي بتتشغّل من فولدر `SALINA-WHITE-FRIDAY`:
```bash
python3 05-MOTION-GRAPHICS/02-shopping-vs-learning/audio.py 05-MOTION-GRAPHICS/02-shopping-vs-learning/soundtrack.wav
```
```bash
node 07-SOURCE-FILES/render-video.js 05-MOTION-GRAPHICS/02-shopping-vs-learning/video.html /tmp/v2-silent.mp4
```
```bash
ffmpeg -y -i /tmp/v2-silent.mp4 -i 05-MOTION-GRAPHICS/02-shopping-vs-learning/soundtrack.wav -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k -shortest -movflags +faststart 08-EXPORTS/video/salina-wf-shopping-vs-learning-1080x1920.mp4
```
