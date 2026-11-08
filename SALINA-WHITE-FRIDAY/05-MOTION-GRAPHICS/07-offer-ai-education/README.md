# فيديو عرض كورس الذكاء الاصطناعي في التعليم

الملف ده نسخة من قالب العروض، ومتعدّل فيه حاجتين:
- **المشهد الأول:** تحضير الدرس بالليل (ورق، وساعة، وقهوة)، وبعدين لابتوب AI بيرتّب كل حاجة.
- **المحتوى:** تسع نقاط مترقمة. في `OFFER.steps`، لو الأيقونة `null` بيظهر الرقم بس.

كل الكلام في `OFFER` جوه `video.html`، وأوقات المشاهد في `T`، وبنفس الأوقات في `audio.py`.

## التصدير
الأوامر دي بتتشغّل من فولدر `SALINA-WHITE-FRIDAY`:
```bash
python3 05-MOTION-GRAPHICS/07-offer-ai-education/audio.py 05-MOTION-GRAPHICS/07-offer-ai-education/soundtrack.wav
```
```bash
node 07-SOURCE-FILES/render-video.js 05-MOTION-GRAPHICS/07-offer-ai-education/video.html /tmp/v7-silent.mp4
```
```bash
ffmpeg -y -i /tmp/v7-silent.mp4 -i 05-MOTION-GRAPHICS/07-offer-ai-education/soundtrack.wav -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k -shortest -movflags +faststart 08-EXPORTS/video/salina-wf-offer-ai-education-1080x1920.mp4
```
