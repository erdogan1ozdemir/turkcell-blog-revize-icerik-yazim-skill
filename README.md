# Turkcell Blog · Tek Yazı Revize Skill'i

Bir blog yazısını tek başına SEO ve GEO açısından inceleyip revize eden Claude Code skill'i.
İki çıktı üretir: ClickUp'a yapıştırılabilir bulgu metni ve her değişikliği dosya içinde
yorumla gerekçelendiren revize docx.

## Kurulum

```bash
git clone https://github.com/erdogan1ozdemir/turkcell-blog-revize-icerik-yazim-skill.git \
  ~/.claude/skills/turkcell-blog-revize
```

## Kullanım

Claude Code oturumunda yazının adresini ya da docx dosyasını verip revize istenir:

```
https://www.turkcell.com.tr/blog/<yazi-slug> bu yazıyı inceleyip revize eder misin?
```

## İçerik

| Dosya | Ne işe yarıyor |
|---|---|
| `SKILL.md` | Akış, üç temel kural, çıktı yapısı |
| `references/olcum-kurallari.md` | Gövde ayıklama, sayım tuzakları, yoğunluk okuması, rakip seçimi |
| `references/yazim-dili.md` | Turkcell blog yazım dili profili; cümle, kip ve bölüm kalıpları |
| `references/revize-kurallari.md` | Neye dokunulur, yorum yazımı, skill'in yapamadıkları |
| `references/rapor-formati.md` | ClickUp yanıtının bölümleri ve beklenti hesabı |
| `scripts/olcum.py` | Gövde ayıklama ve kelime geçişi ölçümü |
| `scripts/revize_sablon.py` | Yorumlu docx revizesi için çalışan örnek (bitrate yazısı) |

## Dayandığı ölçümler

Yazım dili profili, yayındaki dört Turkcell yazısının gövde ölçümünden çıkarıldı: ortalama 13.5
kelime/cümle, baskın "-yor" kipi, seyrek "siz" hitabı, 9-14 ara başlık.

Ölçüm kuralları, fiilen yapılmış hatalardan yazıldı; en pahalısı görsel sayımının sayfa genelinden
yapılmasıydı: bir yazıda 15 görsel görünürken gövdede sıfır görsel vardı.
