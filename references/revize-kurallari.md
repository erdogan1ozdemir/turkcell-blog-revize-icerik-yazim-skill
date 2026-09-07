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

## Öneri vermeden önce bölüm envanteri

Hiçbir ekleme önerisi, o bölümde zaten ne olduğu ölçülmeden verilmez. Ölçüm **bölüm bazındadır**;
belgenin tamamında altı tablo bulunması, önerinin verildiği bölümde tablo olduğu anlamına gelmiyor.

Her ara başlık için şunlar sayılır: tablo, madde listesi, görsel, kaynak satırı.

```python
def bolum_envanteri(d):
    env={}; son=None
    for el in list(d.element.body):
        if el.tag.endswith('}p'):
            p=Paragraph(el,d)
            if p.style.name.startswith('Heading'):
                son=p.text.strip(); env.setdefault(son,{"tablo":0,"madde":0})
            elif son and p.text.strip().startswith(("•","-")): env[son]["madde"]+=1
        elif el.tag.endswith('}tbl') and son: env[son]["tablo"]+=1
    return env
```

Envanterin çıktısına göre:

- **Tablosu olan bölüme "tablo hâline getirilsin" önerilmez.** Bu hata bir kez yapıldı: canlı yayın
  bölümü için "değerler tablo hâline getirilir: platform, çözünürlük, önerilen bitrate" önerildi;
  bölümde zaten "Platform / 1080p60 için Tipik Bitrate / Ek Not" tablosu duruyordu ve önerilen
  sütunlar mevcut tablonun sütunlarıydı.
- **Tablosu olan bölüme görsel önerilecekse gerekçe ayrışır.** "Tek bakışta anlaşılır hâle getirir"
  gerekçesi tabloyu yok sayar. Görsel ancak tablodan farklı bir işi yapıyorsa önerilir: tablo değer
  karşılaştırır, grafik davranışı ya da zaman içindeki dağılımı gösterir. Bu ayrım yorumda yazılır.
- **Görsel önerileri önce tablosuz bölümlere verilir.** Anlatımı tamamen metne dayanan bölümler
  görselden en çok yararlanan yerlerdir.

Aynı disiplin madde listesi, kaynak satırı ve `Not:` bloğu önerileri için de geçerlidir.

## Giriş paragrafları

Tanım bir kez verilir. Giriş paragrafını tanımla açtıktan sonra ikinci paragrafın aynı tanımı
başka kelimelerle tekrarlamadığı **karşılaştırarak** denetlenir; iki paragrafın ilk 160 karakteri
arasındaki karakter benzerliği 0.45'i aşıyorsa tekrar vardır.

- İlk paragraf: tanım, kısa mekanizma, konuya bağlayan bir cümle
- İkinci paragraf: tanımı tekrarlamaz; konunun nerede karşımıza çıktığı, kimin işine yaradığı ya da
  somut bir örnekle devam eder
- Kaynak metinde "Günümüzde", "teknolojinin gelişmesiyle birlikte" gibi açılışlar ve "-dır" kipi
  varsa blogun "-yor" anlatımına çevrilir

Bir örnek: bir yazının girişi "Bitrate, bir ses ya da görüntü içeriğinin saniyede taşıdığı veri
miktarını ifade ediyor" ile açılırken ikinci paragraf "Bitrate, dijital ses ve görüntü içeriklerinin
birim zamanda taşıdığı veri miktarını ifade eden temel bir teknik ölçüttür" diye devam ediyordu.
İkinci paragraf, konunun kullanım alanlarıyla yeniden yazıldı.

## Sık sorulan sorular: önce cevap

Her yanıt **sorunun karşılığıyla** başlar; koşul ve açıklama arkaya bırakılır. "Değişir", "duruma
göre farklılık gösterir", "birçok etkene bağlıdır" ile açılan yanıt cevabı erteliyor demektir.

| Kaçınılacak açılış | Tercih edilen açılış |
|---|---|
| "Bit rate, içeriğin türüne göre değişiyor. 1080p için 8 Mbps…" | "1080p video için 8 Mbps, 4K için 35-45 Mbps… Değer içeriğin türüne göre değişiyor." |
| "Bu sorunun tek bir cevabı yok." | Somut değer ya da tanım, ardından koşul |

Yanıt 2-3 cümleyi geçmez ve sayı içeren sorularda değer ilk cümlede bulunur. Bu yapı hem öne çıkan
snippet hem AI Overview alıntısı için gerekli.

## İç link yerleşimi

Bağlantılar **gerçek hyperlink olarak metne yerleştirilir**, yorum olarak bırakılmaz. Yorumda yalnız
gerekçe kalır. Anchor, cümlenin doğal bir parçası olan ifadedir; "buraya tıklayın" ya da çıplak adres
kullanılmaz.

### Anchor metni hedefin kelimesini taşır

Anchor, bağlantı verilen yazının **hedef kelimesini içerir**. Birebir aynı olması gerekmez, kelime
anchor içinde geçerse yeter: "upload hızı" anchor'ı `upload` hedefini karşılar, "minimum bağlantı
hızını" karşılamaz.

| Hedef yazı | Hedef kelime | Zayıf anchor | Doğru anchor |
|---|---|---|---|
| mbps nedir | mbps | minimum bağlantı hızını | **Mbps** |
| upload nedir | upload | yükleme hızı | **upload hızı** |
| 5G ve ping | ping | düşük gecikme | **ping** |
| fps nedir | fps | kare hızıyla | **FPS** |

**Terim yazıda geçmiyorsa metin güncellenir.** Anchor uydurulmaz, cümle terimi doğal biçimde
taşıyacak hâle getirilir:

- "Belirleyici olan bitrate değil, düşük gecikme ve düzenli veri akışı" →
  "Belirleyici olan bitrate değil, **ping** olarak ölçülen düşük gecikme ve düzenli veri akışı"
- "Canlı yayında belirleyici olan yükleme hızı oluyor" →
  "Canlı yayında belirleyici olan **upload hızı** oluyor"
- "çözünürlük ve kare hızıyla birlikte artıyor" → "çözünürlük ve kare hızıyla, yani **FPS**
  değeriyle birlikte artıyor"

Bağlantı kurulmadan önce hedef kelimenin gövdede kaç kez geçtiği ölçülür; sıfırsa terimin eklendiği
cümle yorumda belirtilir. Terim yazının konusuyla ilgisizse bağlantı hiç kurulmaz, zorlanmaz.

### Dış kaynak bağlantıları

Dış bağlantıların anchor'ı da kaynağı adlandırır. "özetliyor", "oluyor", "buradan" gibi anlam
taşımayan anchor'lar bağlantının nereye gittiğini ne okuyucuya ne arama motoruna anlatıyor:
"YouTube'un resmi olarak önerdiği yükleme değerlerini", "Twitch'in resmi yayın kılavuzuna".

### Yerleşim

- Bağlantı gövde içinden verilir; ilgili yazılar bloğu bu yerleşimin yerini tutmaz
- Bir yazıda 3-4 iç link yeterli; her biri okuyucunun o noktada soracağı sorunun karşılığıdır
- python-docx'te hyperlink `w:hyperlink` öğesiyle eklenir (`scripts/revize_sablon.py` içindeki
  `link_yap` işlevi), stil olarak `Hyperlink` ve altı çizili mavi kullanılır

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
