---
name: turkcell-blog-revize
description: Turkcell blogunda yayında olan ya da yayına hazırlanan bir yazıyı SEO ve GEO açısından inceleyip revize eder. Canlı sayfayı ve sonuç sayfasını ölçer, rakip yazılarla gövde karşılaştırması yapar, hedef kelime karşılığını denetler, docx dosyasını revize edip her değişikliği dosya içinde yorumla gerekçelendirir. Bu skill'i şu durumlarda kullan · kullanıcı bir blog yazısının adresini verip "bu yazıyı incele", "revize et", "ilk 3'e nasıl girer", "rakipler ne durumda", "hedef kelime kaç kez geçiyor" dediğinde · ClickUp ya da içerik ekibinden gelen bir yazı için SEO değerlendirmesi istendiğinde · elindeki docx içeriğin yayın öncesi denetimini istediğinde · yayınlanmış bir yazının neden sıralanmadığını sorduğunda. "Tek yazı" ve "revize" birlikte geçiyorsa tetikle.
---

# Turkcell Blog · Tek Yazı Revizesi

Bir blog yazısını tek başına ele alıp iki çıktı üretir: **chat/ClickUp yanıtı** (bulgular ve öneriler)
ve **yorumlanmış revize docx** (değişikliğin kendisi, her biri gerekçesiyle).

Yazının kapsamı çoğu zaman sorun değildir. Turkcell yazıları rakiplerin iki-üç katı uzunlukta olur;
kaybedilen yer tanım kurgusu, kelime karşılığı, gövde içi bağlantı ve işaretlemedir. Revizyon bu
dört başlıkta yoğunlaşır, metni uzatmaya çalışmaz.

## Akış

| # | Adım | Nasıl |
|---|---|---|
| 1 | Canlı sayfayı ölç | `scripts/olcum.py` · gövde kelime sayısı, ara başlık, hedef kelime geçişi, şema, iç link, görsel |
| 2 | Sonuç sayfasını çek | Ahrefs `serp-overview` · ilk 10, AI Overview kaynakları, soru bloğu |
| 3 | Rakipleri ölç | İlk üç bilgilendirici sayfayı indirip aynı ölçümü uygula |
| 4 | Hacimleri al | DataForSEO Keyword Planner · kelime kümesinin tamamı, yazım varyantları dahil |
| 5 | Kanibalizasyon | Blogun kendi sayfaları aynı kelimede sıralanıyor mu (GSC + Ahrefs) |
| 6 | Bulguları yaz | `references/rapor-formati.md` |
| 7 | Docx'i revize et | `scripts/revize_sablon.py` · her değişikliğe yorum |
| 8 | Yapılamayanları notla | Şema, görsel üretimi, CMS ayarları · listelenip kullanıcıya iletilir |

Her adımın kuralı ilgili referans dosyasındadır; adımı yapmadan önce oku.

- `references/olcum-kurallari.md` · ölçüm tuzakları ve doğru sayım yöntemi
- `references/yazim-dili.md` · Turkcell blog yazım dili, cümle ve kip kalıpları
- `references/revize-kurallari.md` · neyin değiştirileceği, neyin korunacağı, yorum yazımı
- `references/rapor-formati.md` · ClickUp yanıtının yapısı

## Üç kural

1. **Ölçüm gövdeyle sınırlıdır.** Görsel, tablo, liste ve bağlantı sayımı yazının gövdesinden yapılır;
   sayfa çerçevesi, ilgili yazılar bloğu ve menü sayıma girmez. Bu hata bir kez yapıldı: bir yazıda
   "15 görsel" bulundu, gövdeye daraltılınca **sıfır** çıktı.
2. **Kapsam sorun değilse uzatma önerilmez.** Yoğunluk rakip bandındaysa kelime tekrarı artırılmaz;
   revizyon tanım kurgusu, eksik yazım varyantı, bağlantı ve işaretleme üzerinden ilerler.
3. **Her değişiklik dosya içinde gerekçelenir.** Docx yorumu "ne yapıldı ve neden" biçiminde yazılır,
   veriyle desteklenir (hangi kelime kaç arama, sonuç sayfasında ne görünüyor).

## Çıktı

```
<yazı-adı>-revize/
  orijinal.docx
  <Marka> - Blog - <Konu> (SEO revize).docx     yorumlanmış revize
  revize.py                                      yeniden üretilebilir olması için
  bulgular.md                                    ClickUp yanıtı
  yapilamayanlar.md                              CMS ve tasarım tarafına düşen işler
```

**REQUIRED SUB-SKILL:** `icerik-dili-rehberi` · ClickUp yanıtı yazılmadan önce ilgili bölüm,
yazıldıktan sonra self-check. Revize edilen **yazı metni** bu rehbere tabi değildir; blog yazısı
kendi ses tonunu korur (bkz. `references/yazim-dili.md`).
