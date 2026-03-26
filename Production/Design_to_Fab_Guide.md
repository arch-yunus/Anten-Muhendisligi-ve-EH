# Tasarımdan Üretim Bandına: Fabrikasyon Rehberi Factory 🛠️⚙️

Anten tasarımınız simülasyonlarda başarılı olduktan sonra, fiziksel dünyaya geçiş süreci başlar.

## 1. Çıkış Formatları (Export)
- **Gerber Files:** Standart PCB üretim formatı. Bakır katmanları, delikler (drill) ve maskeler için ayrı dosyalar içerir.
- **GDSII:** Özellikle MMIC (Monolithic Microwave Integrated Circuit) ve çip seviyesi tasarımlar için kullanılan vektörel format.
- **DXF:** Mekanik CNC kesim veya lazer kazıma için CAD formatı.

## 2. Üretim Parametreleri (D-Fab)
Üreticiye (Örn: Eurocircuits, JLCPCB, Rogers Fab) gönderilecek teknik notlar:
- **Copper Thickness:** Genellikle $35\mu m$ (1 oz) kullanılır.
- **Solder Mask:** Anten bölgesinde **maske kullanılmaması** önerilir; maskenin dielektrik sabiti rezonansı kaydırabilir.
- **Surface Finish:** ENIG (Gold) kaplama, yüksek frekanslarda iletkenliği korumak için HASL (Kurşun) kaplamadan daha iyidir.

## 3. Post-Fab Kontrol Listesi
1. **Dimension Check:** Kumpas ile yama boyutlarının doğrulanması.
2. **VSWR Test:** VNA (Vector Network Analyzer) ile giriş empedansının ölçülmesi.
3. **Patern Test:** Yankısız oda (Anechoic Chamber) ortamında ışıma karakteristiğinin ölçülmesi.

---
✅ *Tasarım bitmez; üretimle mühürlenir.*
