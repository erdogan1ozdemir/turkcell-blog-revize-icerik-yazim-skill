# -*- coding: utf-8 -*-
"""Bitrate yazısının SEO ve GEO revizesi · her değişiklik dosya içinde yorumla gerekçelendirilir."""
import docx, re, copy
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

KAYNAK="orijinal.docx"; HEDEF="Turkcell - Blog - Bitrate Nedir (SEO revize).docx"
YAZAR="Inbound SEO"; BAS="SEO"
d=docx.Document(KAYNAK)
P=d.paragraphs
LOG=[]

def yorum(p, metin):
    """Paragrafa gerekçe yorumu ekler; run yoksa oluşturur."""
    runs=p.runs or [p.add_run("")]
    d.add_comment(runs, text=metin, author=YAZAR, initials=BAS)

def bul(desen, bas=0):
    for i,p in enumerate(P[bas:],bas):
        if re.search(desen,p.text): return i
    return None

def stil_kopya(kaynak_p):
    return kaynak_p.style

from docx.text.paragraph import Paragraph
def ekle_sonra(ref, metin, stil=None):
    """Verilen paragrafın ardına yeni paragraf ekler ve nesnesini döndürür."""
    ref_p = ref._p if hasattr(ref,'_p') else P[ref]._p
    ref_o = ref if hasattr(ref,'_p') else P[ref]
    yeni=copy.deepcopy(ref_p)
    ref_p.addnext(yeni)
    np=Paragraph(yeni, ref_o._parent)
    for r in list(np.runs): r._r.getparent().remove(r._r)
    np.add_run(metin)
    np.style = stil if stil else ref_o.style
    return np

# ------------------------------------------------------------------ 1 · görünmez karakter
temiz=0
for p in d.paragraphs:
    for r in p.runs:
        if "​" in r.text or "﻿" in r.text:
            r.text=r.text.replace("​","").replace("﻿",""); temiz+=1
LOG.append(f"Görünmez karakter temizliği: {temiz} run")

# ------------------------------------------------------------------ 2 · giriş: tanım ilk cümleye
i=bul(r'^Aynı film dosyası')
if i is not None:
    p=P[i]
    for r in list(p.runs): r._r.getparent().remove(r._r)
    p.add_run("Bitrate, bir ses ya da görüntü içeriğinin saniyede taşıdığı veri miktarını ifade ediyor; "
              "Türkçede bit hızı, İngilizce kaynaklarda ise bit rate olarak geçiyor. Saniyede taşınan bit "
              "sayısı arttıkça görüntüdeki ayrıntı ve sesteki netlik yükseliyor, dosya da büyüyor. Aynı film "
              "bir ekranda kristal netliğinde açılırken diğerinde donuk görünüyorsa, aradaki fark çoğu zaman "
              "çözünürlük değil bitrate.")
    yorum(p, "Giriş paragrafı yeniden yazıldı. Önceki hâlinde tanım üçüncü cümlede başlıyordu; "
             "arama sonuçlarının üstündeki AI Overview ve öne çıkan snippet, başlığın hemen altındaki "
             "bağlamdan bağımsız okunabilen ilk cümleyi alıntılıyor. Tanım ilk cümleye alındı, benzetme "
             "arkasına bırakıldı. Aynı cümlede 'bit hızı' (aylık 210 arama) ve 'bit rate' (aylık 480 arama) "
             "karşılıkları da geçiriliyor; ayrık yazım gövdede hiç bulunmuyordu.")
    LOG.append("Giriş paragrafı yeniden yazıldı, tanım ilk cümleye alındı")

# ------------------------------------------------------------------ 3 · yeni bölüm: bit rate / bit hızı
i=bul(r'^Bitrate Ölçü Birimleri')
if i is not None:
    govde_stil=P[i+1].style
    h=ekle_sonra(P[i-1], "Bit Rate ile Bit Hızı Aynı Şey mi?", stil=P[i].style)
    g1=ekle_sonra(h,
        "Bit rate, bitrate ve bit hızı aynı kavramı anlatıyor. İngilizce kaynaklarda terim iki kelime "
        "hâlinde 'bit rate' biçiminde yazılırken Türkçede bitişik kullanımı yaygınlaşmış durumda; "
        "Türkçe karşılığı ise bit hızı.", stil=govde_stil)
    g2=ekle_sonra(g1,
        "Üçü de saniyede aktarılan bit sayısını ifade ediyor ve aralarında teknik bir fark bulunmuyor. "
        "Ölçü birimi her üç kullanımda da bps ve katları oluyor.", stil=govde_stil)
    yorum(h, "Yeni bölüm eklendi (mevcutta yok). 'bit rate nedir' aylık 480, 'bit hızı nedir' aylık 210 "
             "arama alıyor ve ikisi de gövdede karşılanmıyordu. Sonuç sayfasındaki soru bloğunda da terim "
             "'Bit rate kaç olmalı?' biçiminde ayrık geçiyor. Bölüm hem bu yazımları karşılıyor hem "
             "okuyucunun kafasındaki 'ikisi farklı mı' sorusunu kapatıyor.")
    LOG.append("Yeni bölüm: Bit Rate ile Bit Hızı Aynı Şey mi?")
d.save(HEDEF)
print("\n".join(LOG))
print("kaydedildi:",HEDEF)

# ------------------------------------------------------------------ 4 · SSS bölümü
P=d.paragraphs
son=len(P)-1
while son>0 and not P[son].text.strip(): son-=1
h2_stil=next(p.style for p in P if p.style.name=="Heading 2")
govde_stil=next(p.style for p in P if p.style.name=="normal" and len(p.text)>80)
sss=[("Bit rate kaç olmalı?",
      "Bit rate, içeriğin türüne ve izleneceği ortama göre değişiyor. 1080p video için 8 Mbps, 4K video için "
      "35-45 Mbps, 1080p60 canlı yayın için 6.000 kbps, yüksek kaliteli müzik için 320 kbps çoğu durumda "
      "dengeli bir başlangıç değeri oluyor."),
     ("Bit hızı yüksek olursa ne olur?",
      "Bit hızı yükseldikçe görüntü ve seste daha fazla ayrıntı korunuyor, buna karşılık dosya boyutu ve "
      "gereken bağlantı hızı da artıyor. Kaynak içeriğin kalitesi bir tavan oluşturduğu için, bu tavanın "
      "ötesine geçen değerler kaliteyi artırmıyor; yalnız dosyayı büyütüyor."),
     ("4K yayın için kaç bitrate gerekir?",
      "4K yayında 24-30 FPS için 35-45 Mbps, 48-60 FPS için 53-68 Mbps bandı öneriliyor. Canlı yayında bu "
      "değerin kesintisiz taşınabilmesi için yükleme hızının seçilen bitrate'in en az iki katı olması gerekiyor."),
     ("Bitrate nasıl hesaplanır?",
      "Dosyanın bit cinsinden boyutu, saniye cinsinden süresine bölünüyor. 90 megabyte'lık 60 saniyelik bir "
      "video için önce boyut 8 ile çarpılıp 720 megabite çevriliyor, ardından 60'a bölünüyor ve ortalama "
      "12 Mbps sonucu çıkıyor.")]
ref=P[son]
basH=ekle_sonra(ref,"Bitrate Hakkında Sık Sorulan Sorular",stil=h2_stil)
yorum(basH,"Sık sorulan sorular bölümü eklendi (mevcutta yok). Dört soru, arama sonucundaki soru bloğunda "
           "görünen sorularla birebir eşleşiyor: bit rate kaç olmalı, bit hızı yüksek olursa ne olur, "
           "4K yayın için kaç bitrate gerekir, bitrate nasıl hesaplanır. Yanıtlar yazının gövdesindeki "
           "değerlerle tutarlı ve tek başına alıntılanabilecek uzunlukta tutuldu. Bu bölüm ayrıca FAQPage "
           "işaretlemesinin dayanağını oluşturuyor.")
ref=basH
# Sorular ara başlık düzeyinde olmalı: belgede Heading 3 kullanılmadığı için stil sözlüğünden alınır
try: h3_stil=d.styles["Heading 3"]
except KeyError: h3_stil=h2_stil
for s,c in sss:
    hs=ekle_sonra(ref,s,stil=h3_stil); ref=ekle_sonra(hs,c,stil=govde_stil)
LOG.append("Sık sorulan sorular bölümü eklendi (4 soru)")
d.save(HEDEF)
print("SSS eklendi")

# ------------------------------------------------------------------ 5 · iç link yerleşimleri
P=d.paragraphs
LINK=[
 (r'İnternet ihtiyacı: İçeriğin bitrate',
  "İç link (mevcutta yok): 'gereken minimum bağlantı hızı' ifadesi mbps nedir yazısına bağlanabilir · "
  "https://www.turkcell.com.tr/blog/mbps-nedir · Anchor: Mbps nedir. Gövde içinden verilen bağlantı, "
  "ilgili yazılar bloğundaki bağlantının yerini tutmuyor; yazının şu an gövdesinde tek bir iç link bile bulunmuyor."),
 (r'^Yayıncı tarafı \(Yükleme\)',
  "İç link (mevcutta yok): 'yükleme hızı' ifadesi upload yazısına bağlanabilir · "
  "https://www.turkcell.com.tr/blog/upload-nedir-downloaddan-farki-ve-ideal-hiz-degerleri · Anchor: upload hızı."),
 (r'^Rekabetçi oyun',
  "İç link (mevcutta yok): 'düşük gecikme' ifadesi ping yazısına bağlanabilir · "
  "https://www.turkcell.com.tr/blog/5g-ve-ping-5g-ile-oyunlarda-ping-dusurme-yollari-ve-cozumler · Anchor: ping."),
 (r'Önerilen bitrate çözünürlük ve kare hızıyla',
  "İç link (mevcutta yok): 'kare hızı' ifadesi FPS yazısına bağlanabilir · "
  "https://www.turkcell.com.tr/blog/fps-nedir · Anchor: FPS nedir."),
]
n=0
for desen,not_ in LINK:
    i=bul(desen)
    if i is not None: yorum(P[i],not_); n+=1
LOG.append(f"İç link önerisi: {n} nokta")

# ------------------------------------------------------------------ 6 · görsel yerleşimleri
GORSEL=[
 (r'^Bitrate, saniyedeki bit sayısına göre bps',
  "Görsel (mevcutta yok): bps, kbps, Mbps ve Gbps basamaklarını gösteren bir ölçek görseli eklenebilir. "
  "Yazının gövdesinde şu an tek bir açıklayıcı görsel bulunmuyor; arama sonucunda ilk sıradaki üç sayfanın "
  "satırında görsel küçük resmi görünüyor. Dosya adı bitrate-olcu-birimleri.jpg, alt metni 'bitrate ölçü "
  "birimleri bps kbps Mbps Gbps' olabilir."),
 (r'^Sabit bitrate \(CBR\)',
  "Görsel (mevcutta yok): CBR ve VBR'nin veri hızını zaman içinde nasıl dağıttığını gösteren iki çizgili "
  "basit bir grafik, bu bölümü tek bakışta anlaşılır hâle getiriyor. Alt metin: 'CBR ve VBR bitrate farkı'."),
 (r'^Canlı yayın için bitrate ayarları platforma göre',
  "Görsel (mevcutta yok): platform bazlı önerilen değerleri özetleyen bir görsel eklenebilir. "
  "Alt metin: 'canlı yayın bitrate ayarları YouTube Twitch Instagram'."),
]
m=0
for desen,not_ in GORSEL:
    i=bul(desen)
    if i is not None: yorum(P[i],not_); m+=1
LOG.append(f"Görsel önerisi: {m} nokta")
d.save(HEDEF); print(f"iç link {n} · görsel {m}")

# ------------------------------------------------------------------ 7 · başlık altı özet ve kelime karşılığı
P=d.paragraphs
i=bul(r'^Bitrate Görüntü ve Ses Kalitesini')
if i is not None and i+1<len(P):
    p=P[i+1]
    if not p.text.startswith("Bit hızı arttıkça"):
        pass
    yorum(p,"Bu bölümde 'bit hızı' karşılığı zaten kullanılıyor; korunmasında yarar var. Terimin yazı "
            "boyunca yalnız dört kez geçtiği düşünülürse, aynı kullanımın ölçü birimleri ve hesaplama "
            "bölümlerinde de tekrarlanması kelime karşılığını güçlendiriyor.")
i=bul(r'^Bitrate Seçiminde Doğru Denge')
if i is not None:
    yorum(P[i],"Kapanış bölümü olduğu gibi korundu. Yazının kapsamı, arama sonucundaki rakiplerin üç katı "
               "uzunlukta ve tablo bakımından tek başına önde; içerik tarafında ekleme gerekmiyor. "
               "Revizyon, tanım kurgusu ve kelime karşılığı üzerine yoğunlaştı.")
i=bul(r'^Aşağıdaki tablo, YouTube')
if i is not None:
    yorum(P[i],"Tablolar korundu. Arama sonucundaki dört rakip sayfanın hiçbirinde tablo bulunmuyor; "
               "yapılandırılmış veri hem okuyucu hem AI yanıtları için bu yazının en güçlü tarafı.")
# başlık: hedef kelimenin ilk H2'de tam öbek geçmesi
i=bul(r'^Bitrate Ne Anlama Gelir')
if i is not None:
    p=P[i]
    for r in list(p.runs): r._r.getparent().remove(r._r)
    p.add_run("Bitrate Ne Demek, Ne Anlama Geliyor?")
    yorum(p,"Ara başlık 'Bitrate Ne Demek' kalıbını da kapsayacak biçimde güncellendi (aylık 70 arama). "
            "Yazıda bu kalıp yalnız gövde içinde bir kez geçiyordu, ara başlıkta karşılığı yoktu.")
    LOG.append("Ara başlık güncellendi: Bitrate Ne Demek, Ne Anlama Geliyor?")
d.save(HEDEF)
print("\n".join(LOG))

# ------------------------------------------------------------------ 8 · giriş tekrarının giderilmesi
P=d.paragraphs
i=bul(r'^Bitrate, dijital ses ve görüntü içeriklerinin birim zamanda')
if i is not None:
    p=P[i]
    for r in list(p.runs): r._r.getparent().remove(r._r)
    p.add_run("Bu değer, video izlemekten canlı yayına, görüntülü görüşmeden bulut oyuna kadar dijital "
              "deneyimin her aşamasında karşımıza çıkıyor. Büyük platformlar da bitrate'i tesadüfe "
              "bırakmıyor: YouTube çözünürlüğe göre önerilen bantları yayımlıyor, Twitch yayıncılar için "
              "üst sınır koyuyor, müzik servisleri ise akış kalitesini bu değere göre kademelendiriyor.")
    yorum(p,"İkinci paragraf yeniden yazıldı. Önceki hâlinde bitrate tanımı ilk paragraftaki tanımı "
            "neredeyse birebir tekrarlıyordu ('saniyede taşıdığı veri miktarını ifade ediyor' / 'birim "
            "zamanda taşıdığı veri miktarını ifade eden temel bir teknik ölçüttür'). Tanım ilk paragrafta "
            "kaldı, bu paragraf konunun nerede karşımıza çıktığıyla devam ediyor. Ayrıca 'Günümüzde' "
            "kalıbı ve '-dır' kipi, blogun geri kalanındaki '-yor' anlatımına uyacak biçimde değiştirildi.")
    LOG.append("İkinci paragraftaki tanım tekrarı giderildi")

# ------------------------------------------------------------------ 9 · SSS: önce cevap, sonra açıklama
i=bul(r'^Bit rate, içeriğin türüne ve izleneceği ortama göre değişiyor')
if i is not None:
    p=P[i]
    for r in list(p.runs): r._r.getparent().remove(r._r)
    p.add_run("1080p video için 8 Mbps, 4K video için 35-45 Mbps, 1080p60 canlı yayın için 6.000 kbps, "
              "yüksek kaliteli müzik için 320 kbps çoğu durumda dengeli bir değer oluyor. Bit rate "
              "içeriğin türüne ve izleneceği ortama göre değiştiği için tek bir doğru sayı bulunmuyor; "
              "yukarıdaki değerler başlangıç noktası olarak alınabiliyor.")
    yorum(p,"Yanıt sırası değiştirildi. Önceki hâlinde cevap 'içeriğin türüne göre değişiyor' cümlesiyle "
            "erteleniyordu; sorunun karşılığı olan değerler ikinci cümlede kalıyordu. Sorunun yanıtı ilk "
            "cümleye alındı, koşul açıklaması arkasına bırakıldı. Diğer üç soru zaten doğrudan yanıtla "
            "başlıyor, onlara dokunulmadı.")
    LOG.append("SSS ilk yanıtı doğrudan cevapla başlayacak biçimde düzenlendi")
d.save(HEDEF); print("\n".join(LOG[-2:]))

# ------------------------------------------------------------------ 10 · gövde içi iç linkler
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT

def link_yap(p, anchor, url):
    """Paragraf metnindeki anchor ifadesini gerçek bağlantıya çevirir."""
    metin=p.text
    k=metin.find(anchor)
    if k<0: return False
    once, sonra = metin[:k], metin[k+len(anchor):]
    for r in list(p.runs): r._r.getparent().remove(r._r)
    if once: p.add_run(once)
    rid=p.part.relate_to(url, RT.HYPERLINK, is_external=True)
    h=OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid)
    r=OxmlElement('w:r'); rPr=OxmlElement('w:rPr')
    st=OxmlElement('w:rStyle'); st.set(qn('w:val'),'Hyperlink'); rPr.append(st)
    c=OxmlElement('w:color'); c.set(qn('w:val'),'1D5AFF'); rPr.append(c)
    u=OxmlElement('w:u'); u.set(qn('w:val'),'single'); rPr.append(u)
    r.append(rPr)
    t=OxmlElement('w:t'); t.text=anchor; t.set(qn('xml:space'),'preserve'); r.append(t)
    h.append(r); p._p.append(h)
    if sonra: p.add_run(sonra)
    return True

LINKLER=[
 (r'İnternet ihtiyacı: İçeriğin bitrate','minimum bağlantı hızını',
  'https://www.turkcell.com.tr/blog/mbps-nedir',
  "İç link eklendi: 'minimum bağlantı hızını' ifadesi Mbps yazısına bağlandı. Bitrate ile bağlantı hızı "
  "arasındaki ilişki okuyucunun ilk takıldığı yer oluyor ve blogun bu konudaki sayfası aramada 2.5 "
  "ortalama sırada. Bağlantı gövde içinden veriliyor; ilgili yazılar bloğu bu yerleşimin yerini tutmuyor."),
 (r'^Yayıncı tarafı \(Yükleme\)','yükleme hızı',
  'https://www.turkcell.com.tr/blog/upload-nedir-downloaddan-farki-ve-ideal-hiz-degerleri',
  "İç link eklendi: 'yükleme hızı' ifadesi upload yazısına bağlandı. Canlı yayın bölümünde yükleme hızı "
  "belirleyici kavram ve blogda bu konuyu karşılayan ayrı bir yazı bulunuyor."),
 (r'^Rekabetçi oyun','düşük gecikme',
  'https://www.turkcell.com.tr/blog/5g-ve-ping-5g-ile-oyunlarda-ping-dusurme-yollari-ve-cozumler',
  "İç link eklendi: 'düşük gecikme' ifadesi ping yazısına bağlandı. Oyun bölümünde belirleyici olanın "
  "bitrate değil gecikme olduğu anlatılıyor; okuyucunun bir sonraki sorusu doğrudan bu yazıya gidiyor."),
 (r'^Önerilen bitrate çözünürlük ve kare hızıyla','kare hızıyla',
  'https://www.turkcell.com.tr/blog/fps-nedir',
  "İç link eklendi: 'kare hızıyla' ifadesi FPS yazısına bağlandı. Tablodaki 24-30 FPS ve 48-60 FPS "
  "sütunları bu kavramı gerektiriyor."),
]
P=d.paragraphs; ek=0
for desen,anchor,url,not_ in LINKLER:
    i=bul(desen)
    if i is None: continue
    if link_yap(P[i],anchor,url):
        yorum(P[i],not_); ek+=1
LOG.append(f"Gövde içi iç link: {ek} bağlantı eklendi")
d.save(HEDEF); print(f"iç link eklendi: {ek}")

# ------------------------------------------------------------------ 11 · anchor metni hedefin kelimesi olur
def paragraf_kur(p, parcalar):
    """Paragrafı sıfırdan kurar. parcalar: (metin, url|None) çiftleri."""
    for h in p._p.findall(f'.//{{{p._p.nsmap["w"]}}}hyperlink'): p._p.remove(h)
    for r in list(p.runs): r._r.getparent().remove(r._r)
    for metin,url in parcalar:
        if not url: p.add_run(metin); continue
        rid=p.part.relate_to(url, RT.HYPERLINK, is_external=True)
        h=OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid)
        r=OxmlElement('w:r'); rPr=OxmlElement('w:rPr')
        st=OxmlElement('w:rStyle'); st.set(qn('w:val'),'Hyperlink'); rPr.append(st)
        c=OxmlElement('w:color'); c.set(qn('w:val'),'1D5AFF'); rPr.append(c)
        u=OxmlElement('w:u'); u.set(qn('w:val'),'single'); rPr.append(u)
        r.append(rPr)
        t=OxmlElement('w:t'); t.text=metin; t.set(qn('xml:space'),'preserve'); r.append(t)
        h.append(r); p._p.append(h)

MBPS='https://www.turkcell.com.tr/blog/mbps-nedir'
UPLOAD='https://www.turkcell.com.tr/blog/upload-nedir-downloaddan-farki-ve-ideal-hiz-degerleri'
PING='https://www.turkcell.com.tr/blog/5g-ve-ping-5g-ile-oyunlarda-ping-dusurme-yollari-ve-cozumler'
FPS='https://www.turkcell.com.tr/blog/fps-nedir'
ANCHOR=[
 (r'^İnternet ihtiyacı: İçeriğin bitrate',
  [("İnternet ihtiyacı: İçeriğin bitrate'i, onu kesintisiz izlemek için gereken minimum bağlantı hızını "
    "doğrudan belirliyor; bu hız ",None),("Mbps",MBPS),(" cinsinden ölçülüyor.",None)],
  "Anchor metni hedef sayfanın kelimesine çevrildi: 'minimum bağlantı hızını' yerine 'Mbps'. "
  "Bağlantı verilen yazının hedef kelimesi 'mbps nedir' ve terim bu yazıda zaten 22 kez geçiyor; "
  "cümlenin sonuna terimi doğal biçimde taşıyan bir bölüm eklendi."),
 (r'^Yayıncı tarafı \(Yükleme\)',
  [("Yayıncı tarafı (Yükleme): Canlı yayında belirleyici olan ",None),("upload hızı",UPLOAD),
   (" oluyor ve çoğu ev bağlantısında bu değer indirmenin belirgin altında kalıyor.",None)],
  "Anchor 'yükleme hızı' yerine 'upload hızı' yapıldı ve terim yazıya eklendi. Bağlantı verilen yazının "
  "hedef kelimesi 'upload'; terim bu yazıda hiç geçmiyordu, yalnız Türkçe karşılığı kullanılıyordu."),
 (r'^Rekabetçi oyun',
  [("Rekabetçi oyun: Oyun trafiği saniyede birkaç yüz kbps ile çalışıyor. Belirleyici olan bitrate değil, ",None),
   ("ping",PING),(" olarak ölçülen düşük gecikme ve düzenli veri akışı oluyor.",None)],
  "Anchor 'düşük gecikme' yerine 'ping' yapıldı ve terim yazıya eklendi. Bağlantı verilen yazının hedef "
  "kelimesi 'ping'; terim bu yazıda hiç geçmiyordu."),
 (r'^Önerilen bitrate çözünürlük ve kare hızıyla',
  [("Önerilen bitrate çözünürlük ve kare hızıyla, yani ",None),("FPS",FPS),
   (" değeriyle birlikte artıyor. 720p için 5 Mbps civarı yeterliyken 1080p 8 Mbps, 4K ise 35-45 Mbps "
    "bandına çıkıyor.",None)],
  "Anchor 'kare hızıyla' yerine 'FPS' yapıldı. Bağlantı verilen yazının hedef kelimesi 'fps' ve terim "
  "tablo başlıklarında zaten kullanılıyor; gövdede de karşılığı verildi."),
]
P=d.paragraphs; n=0
for desen,parca,not_ in ANCHOR:
    i=bul(desen)
    if i is None: continue
    paragraf_kur(P[i],parca); yorum(P[i],not_); n+=1
LOG.append(f"Anchor metni hedef kelimeye çevrildi: {n} bağlantı")

# dış kaynak bağlantılarının anchor'ı da kaynağı adlandırır
DIS=[(r'^Aşağıdaki tablo, YouTube',
  [("Aşağıdaki tablo, ",None),("YouTube'un resmi olarak önerdiği yükleme değerlerini",
    "https://support.google.com/youtube/answer/1722171"),
   (" standart dinamik aralık (SDR) içerik için Mart 2026 itibarıyla özetliyor:",None)],
  "Dış kaynak bağlantısının anchor metni 'özetliyor' idi; kaynağı adlandıran bir ifadeye çevrildi. "
  "Anlam taşımayan anchor, bağlantının neye gittiğini okuyucuya da arama motoruna da anlatmıyor."),
 (r"^Not: Twitch'in resmi yayın kılavuzuna",
  [("Not: ",None),("Twitch'in resmi yayın kılavuzuna","https://help.twitch.tv/s/article/broadcasting-guidelines"),
   (" göre, transkodlama garantisi olmayan yayıncılar için 720p60 çözünürlükte 4.500 kbps, izleyici "
    "erişilebilirliği açısından daha güvenli bir tercih oluyor.",None)],
  "Dış kaynak bağlantısının anchor metni 'oluyor' idi; kaynağı adlandıran ifadeye çevrildi.")]
for desen,parca,not_ in DIS:
    i=bul(desen)
    if i is None: continue
    paragraf_kur(P[i],parca); yorum(P[i],not_); n+=1
LOG.append("Dış kaynak anchor metinleri kaynağı adlandıracak biçimde düzeltildi")
d.save(HEDEF); print(f"anchor düzeltildi: {n}")
