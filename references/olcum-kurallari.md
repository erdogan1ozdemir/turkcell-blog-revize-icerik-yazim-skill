# Ölçüm Kuralları

## Gövde ayıklama

Ölçümler **yalnız yazı gövdesinden** yapılır. Sıra:

1. `<article>` etiketi; içeriği 1.500 karakterden kısaysa bir sonrakine geçilir
2. `blog-detail | article-content | content-detail | post-content | blog-content` sınıflı kapsayıcı
3. `<main>`
4. Hiçbiri yoksa tüm sayfa (bu durumda ölçüm "yaklaşık" olarak işaretlenir)

Ardından `İlgili Yazılar` başlığından itibaren kalan kısım atılır. Menü, altbilgi, form ve yazar
kutusu sayıma girmez.

## Sık yapılan sayım hataları

| Hata | Sonucu | Doğrusu |
|---|---|---|
| Görselleri `h.count('<img')` ile tüm sayfadan saymak | Bir yazıda 15 görsel bulundu, gerçekte gövdede **0** vardı | Gövdeye daraltıp logo ve `.svg` ikonları elemek |
| Bağlantıları sayfa genelinden saymak | 38 iç link göründü, gövdede yalnız yazar bağlantısı vardı | `İlgili Yazılar` öncesi kesitten saymak |
| Hedef kelimeyi tam öbek aramak | "nfc ne demek" gövdede 0 çıkar | Niyet ekini ayırıp **ana terim** üzerinden saymak |
| Ayrık/bitişik yazımı tek biçim saymak | "wifi 6" varken "wi-fi 6" sayılmaz | Normalizasyonda wi fi→wifi, e posta→eposta, type c→typec |

## Yoğunluk okuması

- Ana terim yoğunluğu = ana terim geçişi / gövde kelime sayısı
- Rakip bandı ile karşılaştırılır; **bandın içindeyse artırma önerilmez**
- Hedef geçiş sayısı, rakibin yoğunluğunun kendi gövde uzunluğumuza uyarlanmasıyla bulunur ve
  %2.0 yoğunlukla sınırlanır, taban 4 geçiştir

## Rakip seçimi

Karşılaştırma **aynı türde sayfayla** yapılır: rakibin blog ya da bilgilendirici yazısı. Sorgulama
aracı, hizmet sayfası, ürün listesi ve sözlük sitesi karşılaştırmaya alınmaz; alınırsa sapma yaratır.

## Teknik kontroller

- Görünmez karakter: `​` (ZWSP), `﻿` (BOM), `­` (SHY). Bu karakterler CMS'e yapıştırma
  sırasında giriyor ve **kaynak docx'te görünmüyor**; canlı sayfadan kontrol edilmelidir. Turkcell
  blogunda birden çok yazıda ilk H2'nin başında bulundu.
- Şema: BlogPosting ve BreadcrumbList standart; FAQPage sorusu olan yazılarda eksikse not edilir
- Canonical, datePublished, dateModified
- Gövde içi iç link sayısı ve anchor metinleri
