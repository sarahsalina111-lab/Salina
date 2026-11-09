# فيديو عرض كورس «يقنع»

الملف ده نسخة من قالب العروض، ومتعدّل فيه حاجتين:
- **المشهد الأول:** بوست بيتكتب ويتمسح ومحدش بيتفاعل معاه، وبعدين القلوب والكومنتات.
- **مشهد الهدية الجديد:** صندوق هدية فيه «اشتراك شهر ChatGPT مجانًا». كلامه في `OFFER.gift`، ووقته في `T.GIFT`.

اسم الكورس لو كلمة قصيرة زي «يقنع»، بيظهر كبير على التيكت لوحده.

**الكابشن المقترح:** في `CAPTION.md`.

## التصدير
الأوامر دي بتتشغّل من فولدر `SALINA-WHITE-FRIDAY`:
```bash
python3 05-MOTION-GRAPHICS/08-offer-content-writing/audio.py 05-MOTION-GRAPHICS/08-offer-content-writing/soundtrack.wav
```
```bash
node 07-SOURCE-FILES/render-video.js 05-MOTION-GRAPHICS/08-offer-content-writing/video.html /tmp/v8-silent.mp4
```
```bash
ffmpeg -y -i /tmp/v8-silent.mp4 -i 05-MOTION-GRAPHICS/08-offer-content-writing/soundtrack.wav -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k -shortest -movflags +faststart 08-EXPORTS/video/salina-wf-offer-content-writing-1080x1920.mp4
```
