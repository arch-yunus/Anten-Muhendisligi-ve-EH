# Mikroşerit Yama (Patch) Anten Tasarımı (Level 04) 🛰️

Mikroşerit antenler; hafiflikleri, düşük profilleri ve PCB üzerine kolayca basılabilmeleri nedeniyle modern iletişim ve EH sistemlerinde yaygın kullanılır.

## 1. Dikdörtgen Yama Tasarım Formülleri

Belirli bir rezonans frekansı ($f_r$) ve dielektrik sabit ($ \epsilon_r $) için genişlik ($W$) ve uzunluk ($L$) hesaplanır.

### Genişlik ($W$)
Düşük yan lob seviyesi ve uygun ışıma için:
$$W = \frac{c}{2 f_r} \sqrt{\frac{2}{\epsilon_r + 1}}$$

### Uzunluk ($L$)
Havanın ve dielektrik malzemenin etkisini birleştiren etkin dielektrik sabit ($\epsilon_{reff}$) hesaplanır, ardından saçılma (fringing) etkileri eklenerek gerçek uzunluk ($\Delta L$) düzeltmesi yapılır:
$$L = \frac{c}{2 f_r \sqrt{\epsilon_{reff}}} - 2 \Delta L$$

## 2. Avantajlar ve Dezavantajlar

-   **Artılar:** Seri üretim kolaylığı, konformal (yüzeye uyumlu) yapı, dizi antenlere (array) uygunluk.
-   **Eksiler:** Dar bant genişliği (genellikle %1-5), düşük verimlilik, düşük güç taşıma kapasitesi.

---
*İpucu: Bant genişliğini artırmak için substrat kalınlığı ($h$) artırılabilir veya parazitik yamalar kullanılabilir.*
