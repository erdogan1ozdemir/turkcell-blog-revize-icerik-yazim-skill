# -*- coding: utf-8 -*-
"""Yazı gövdesinden kelime sayısı, başlık yapısı ve hedef kelime geçiş sayısı."""
import re,html as _h
def _temiz(hml):
    s=re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>',' ',hml)
    return s
def govde(hml):
    """Blog yazısının ana gövdesini ayıklar; bulunamazsa tüm metni döndürür."""
    s=_temiz(hml)
    for des in (r'(?is)<article[^>]*>(.*?)</article>',
                r'(?is)<div[^>]*class="[^"]*(?:blog-detail|article-content|content-detail|post-content|blog-content)[^"]*"[^>]*>(.*)',
                r'(?is)<main[^>]*>(.*?)</main>'):
        m=re.search(des,s)
        # gövde adayı anlamlı uzunlukta değilse bir sonrakine geçilir
        if m and len(re.sub(r'<[^>]+>',' ',m.group(1)))>1500: return m.group(1)
    return s
def basliklar(hml):
    s=govde(hml); out=[]
    for lv in (2,3):
        for m in re.finditer(rf'(?is)<h{lv}[^>]*>(.*?)</h{lv}>',s):
            t=_h.unescape(re.sub(r'<[^>]+>','',m.group(1))).strip()
            if t: out.append((lv,re.sub(r'\s+',' ',t)))
    return out
def metin(hml):
    s=govde(hml)
    s=re.sub(r'(?is)<(nav|header|footer|form|aside)[^>]*>.*?</\1>',' ',s)
    t=_h.unescape(re.sub(r'<[^>]+>',' ',s))
    return re.sub(r'\s+',' ',t).strip()
def nrm(s):
    s=s.lower().replace('ı','i').replace('İ','i').replace('ş','s').replace('ğ','g').replace('ü','u').replace('ö','o').replace('ç','c')
    s=re.sub(r'\s+',' ',re.sub(r'[^a-z0-9ğüşıöç ]',' ',s)).strip()
    # ayrık/bitişik yazım varyantları tek biçime indirgenir
    for a,b in (('wi fi','wifi'),('e posta','eposta'),('e mail','email'),('e sim','esim'),
                ('type c','typec'),('usb c','usbc'),('e imza','eimza'),('e devlet','edevlet')):
        s=re.sub(r'\b'+a+r'\b',b,s)
    return s
def gecis(t,kw):
    """Kelimenin metinde tam öbek olarak kaç kez geçtiği (ek toleranslı)."""
    a=nrm(t); k=nrm(kw)
    if not k: return 0
    desen=r'\b'+r'\W+'.join(re.escape(w) for w in k.split())+r'\w{0,6}\b'
    return len(re.findall(desen,a))
def kelime_sayisi(t): return len([w for w in nrm(t).split() if w])
def yogunluk(t,kw):
    n=kelime_sayisi(t)
    return round(gecis(t,kw)/max(1,n)*100,2)
