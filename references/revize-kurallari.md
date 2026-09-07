# Revize Kuralları

## Neye dokunulur, neye dokunulmaz

**Değiştirilir**
- Giriş paragrafı: tanım ilk cümleye alınır, benzetme ve bağlam arkasına bırakılır
- Ara başlıklar: hedef kelimenin karşılanmayan kalıbı varsa başlığa taşınır
- Eksik yazım varyantı: ayrık/bitişik yazım ve Türkçe karşılık gövdeye ve bir ara başlığa eklenir
- Sık sorulan sorular bölümü: sonuç sayfasındaki soru bloğuyla **birebir** eşleşen sorular

**Korunur**
- Yazının kapsamı, bölüm sırası ve tabloları. Kapsam rakiplerin önündeyse ekleme yapılmaz
- Yazarın ses tonu, örnekleri ve benzetmeleri. Revizyon metni yeniden yazmak değildir
- Kaynak satırları ve `Not:` blokları

## Yeni bölüm eklerken

- Yeni bölüm yalnız **karşılanmayan bir arama** varsa açılır; hacmi yorumda yazılır
- Bölüm iki-üç cümleyi geçmez; yazının ritmini bozmaz
- Soru başlıkları H3, konu başlıkları H2 düzeyinde eklenir. Belgede Heading 3 kullanılmamışsa
  stil sözlüğünden (`d.styles["Heading 3"]`) alınır; H2'ye düşürülmez

## Sık sorulan sorular bölümü

- Sorular sonuç sayfasındaki blokta göründüğü **yazımla** alınır ("Bit rate kaç olmalı?")
- Yanıt 2-3 cümle; gövdedeki değerlerle çelişmez, tek başına alıntılanabilir
- Bölüm, FAQPage işaretlemesinin dayanağıdır; şemanın kendisi geliştirici tarafına yazılır

## Yorum yazımı

Her değişiklik dosya içinde yorumlanır. Yorum üç parçadan oluşur:

1. **Ne yapıldı** · "Giriş paragrafı yeniden yazıldı, tanım ilk cümleye alındı."
2. **Neden** · "AI Overview ve öne çıkan snippet, başlığın hemen altındaki bağlamdan bağımsız
   okunabilen ilk cümleyi alıntılıyor."
3. **Veri** · "'bit rate' aylık 480 arama alıyor ve gövdede hiç geçmiyordu."

Eklenen ama belgede karşılığı olmayan öneriler `(mevcutta yok)` ibaresiyle işaretlenir. İç link ve
görsel önerileri metne yazılmaz, ilgili paragrafa yorum olarak bırakılır: anchor metni, hedef adres
ve gerekçe birlikte verilir.

## Skill'in yapamadıkları

Bunlar her teslimde `yapilamayanlar.md` dosyasında listelenir ve kullanıcıya iletilir:

- FAQPage ve diğer şema işaretlemeleri (CMS ya da geliştirici tarafı)
- Görsellerin üretimi; skill yalnız yerleşim, dosya adı ve alt metin önerir
- Gerçek hyperlink yerleşimi; docx yorumunda adres verilir, bağlantı CMS'te kurulur
- Yayın ve güncelleme tarihi ayarları
- Görünmez karakterin kaynağı: kaynak docx temiz olabilir, karakter yayın sırasında giriyor
