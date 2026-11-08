# فيديو عرض ورشة تصميم الفيديوهات بالذكاء الاصطناعي

الملف ده نسخة من قالب العروض (`../05-offer-personal-branding/README.md`)، ومتعدّل فيه حاجتين:
- **المشهد الأول:** الباب بيتخبط عليه «طق طق» وبعدين يتفتح. ده بدل مشهد الوشوش.
- **خط الإنتاج:** ست خطوات مترقمة بدل كارتين الأيام، ومتعرّفة في `OFFER.steps` (الأيقونة والكلام). الأيقونات المتاحة: `idea` و`script` و`image` و`play` و`wave` و`cut`.

لو `OFFER.who` فاضية، سطر «مناسبة لـ» مابيظهرش.

## التصدير
الأوامر دي بتتشغّل من فولدر `SALINA-WHITE-FRIDAY`:
```bash
python3 05-MOTION-GRAPHICS/06-offer-ai-video/audio.py 05-MOTION-GRAPHICS/06-offer-ai-video/soundtrack.wav
```
```bash
node 07-SOURCE-FILES/render-video.js 05-MOTION-GRAPHICS/06-offer-ai-video/video.html /tmp/v6-silent.mp4
```
```bash
ffmpeg -y -i /tmp/v6-silent.mp4 -i 05-MOTION-GRAPHICS/06-offer-ai-video/soundtrack.wav -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k -shortest -movflags +faststart 08-EXPORTS/video/salina-wf-offer-ai-video-1080x1920.mp4
```
