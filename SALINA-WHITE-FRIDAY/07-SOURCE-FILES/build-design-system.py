# Builds 00-BRIEF/design-system.html from design-system.src.html by inlining the logo and key visual as data URIs.
import base64, io, pathlib
from PIL import Image
root = pathlib.Path(__file__).resolve().parent.parent
def uri(img, fmt, **kw):
    b = io.BytesIO(); img.save(b, fmt, **kw)
    return f"data:image/{fmt.lower()};base64," + base64.b64encode(b.getvalue()).decode()
logo = Image.open(root/'01-BRAND-ASSETS/salina-logo-transparent.png'); logo = logo.resize((480, round(480*logo.height/logo.width)), Image.LANCZOS)
kv = Image.open(root/'08-EXPORTS/salina-wf-key-visual-1080x1350.png').convert('RGB').resize((720, 900), Image.LANCZOS)
src = (root/'00-BRIEF/design-system.src.html').read_text(encoding='utf-8')
out = src.replace('__LOGO__', uri(logo, 'PNG', optimize=True)).replace('__KV__', uri(kv, 'JPEG', quality=86))
(root/'00-BRIEF/design-system.html').write_text(out, encoding='utf-8')
print('built', len(out)//1024, 'KB')
