# فيديو عرض ورشة Personal Branding: وده قالب فيديوهات العروض

كل الكلام جاي من جزء واحد اسمه **`OFFER`** في أول الـ script جوه `video.html`:
- **السؤال اللي بيبدأ بيه الفيديو:** `hook`.
- **اسم البرنامج ونوعه والجملة اللي تحته:** `name` و`kind` و`sub`.
- **التفاصيل:** `facts`، وكل تفصيلة ليها أيقونة: `online` أو `cal` أو `clock` أو `rec` أو `cert`.
- **مناسب لمين:** `who`.
- **محاور الأيام:** `days`.
- **الخصم:** `discTop` و`discBig` و`offerOn` و`offerJoke`.
- **نسخة الحجز من كارت النهاية:** `cta`.

## عشان تعملي فيديو لكورس تاني
1. انسخي الفولدر ده بالكامل باسم جديد، مثلًا `06-offer-content-writing`.
2. غيّري `OFFER` ببيانات الكورس الجديد.
3. لو حبيتي المشهد الأول (الوشوش) يتغير لمشهد يناسب الكورس، ده الجزء الوحيد اللي محتاج رسم.
4. صدّري بنفس الأوامر اللي تحت.

أوقات المشاهد متحددة في `T`، وبنفس الأوقات في `audio.py`.

## التصدير
الأوامر دي بتتشغّل من فولدر `SALINA-WHITE-FRIDAY`:
```bash
python3 05-MOTION-GRAPHICS/05-offer-personal-branding/audio.py 05-MOTION-GRAPHICS/05-offer-personal-branding/soundtrack.wav
```
```bash
node 07-SOURCE-FILES/render-video.js 05-MOTION-GRAPHICS/05-offer-personal-branding/video.html /tmp/v5-silent.mp4
```
```bash
ffmpeg -y -i /tmp/v5-silent.mp4 -i 05-MOTION-GRAPHICS/05-offer-personal-branding/soundtrack.wav -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k -shortest -movflags +faststart 08-EXPORTS/video/salina-wf-offer-personal-branding-1080x1920.mp4
```
