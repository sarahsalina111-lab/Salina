# فيديو ٣ «إيه اللي نفسك تتعلميه؟»: ملفات المصدر

| الملف | وظيفته |
|---|---|
| `video.html` | الحركة كلها، وكل إطار بيتحسب من الوقت بالدالة `renderAt(t)`. افتحيه بـ `#play` عشان تشوفيه شغال |
| `audio.py` | المؤثرات الصوتية، وبيستخدم `../lib/sfx.py` |
| `soundtrack.wav` | الصوت الجاهز |
| `../../08-EXPORTS/video/salina-wf-what-to-learn-1080x1920.mp4` | الفيديو النهائي |

## التعديل
- **أسماء البرامج ونوعها:** كل كارت عنصر `<div class="card" id="c0..c3">` جوه الملف، واسمه ونوعه («كورس» أو «ورشة») مكتوبين جواه.
- **الترتيب والتوقيت:** `CARD0` وقت أول كارت، و`CARD` مدة كل كارت (3 ثواني)، و`SUM` وقت الملخص. لو غيّرتي توقيت، غيّري نفس الأوقات في `audio.py`.
- **لو زاد كورس:** انسخي كارت كامل وغيّري رقمه (`c4`)، وضيفي أيقونة صغيرة `m4` ومكانها في `SLOTS`. وبعدين زوّدي `DURATION` و`SUM` 3 ثواني.

## التصدير
الأوامر دي بتتشغّل من فولدر `SALINA-WHITE-FRIDAY`:
```bash
python3 05-MOTION-GRAPHICS/03-what-to-learn/audio.py 05-MOTION-GRAPHICS/03-what-to-learn/soundtrack.wav
```
```bash
node 07-SOURCE-FILES/render-video.js 05-MOTION-GRAPHICS/03-what-to-learn/video.html /tmp/v3-silent.mp4
```
```bash
ffmpeg -y -i /tmp/v3-silent.mp4 -i 05-MOTION-GRAPHICS/03-what-to-learn/soundtrack.wav -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k -shortest -movflags +faststart 08-EXPORTS/video/salina-wf-what-to-learn-1080x1920.mp4
```
