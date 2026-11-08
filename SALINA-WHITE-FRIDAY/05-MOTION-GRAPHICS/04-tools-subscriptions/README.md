# فيديو ٤ «اشتراكات بتطوّرك»: ملفات المصدر

| الملف | وظيفته |
|---|---|
| `video.html` | الحركة كلها، وكل إطار بيتحسب من الوقت بالدالة `renderAt(t)`. افتحيه بـ `#play` عشان تشوفيه شغال |
| `audio.py` | المؤثرات الصوتية، وبيستخدم `../lib/sfx.py` |
| `soundtrack.wav` | الصوت الجاهز |
| `../../08-EXPORTS/video/salina-wf-tools-subscriptions-1080x1920.mp4` | الفيديو النهائي |

## التعديل
- **الأدوات:** في `TOOLS` (الاسم، والنوع بالعربي، والأيقونة). كل سطر بياخد 1.42 ثانية (`ROWD`).
- **مراحل العداد:** في `STAGES`، ومكتوبة كـ [عدد الأدوات اللي اتفعّلت، والجملة].
- **لو زادت الأدوات:** زوّدي `DURATION` وأوقات الختام (`14.9…16.95`) وCTA0، وغيّري نفس الأوقات في `audio.py`.

## التصدير
الأوامر دي بتتشغّل من فولدر `SALINA-WHITE-FRIDAY`:
```bash
python3 05-MOTION-GRAPHICS/04-tools-subscriptions/audio.py 05-MOTION-GRAPHICS/04-tools-subscriptions/soundtrack.wav
```
```bash
node 07-SOURCE-FILES/render-video.js 05-MOTION-GRAPHICS/04-tools-subscriptions/video.html /tmp/v4-silent.mp4
```
```bash
ffmpeg -y -i /tmp/v4-silent.mp4 -i 05-MOTION-GRAPHICS/04-tools-subscriptions/soundtrack.wav -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k -shortest -movflags +faststart 08-EXPORTS/video/salina-wf-tools-subscriptions-1080x1920.mp4
```
