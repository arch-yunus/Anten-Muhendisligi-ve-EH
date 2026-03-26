# Mikroşerit Yama (Patch) Anten Tasarımı (Level 04) 🛰️

Mikroşerit antenler; hafiflikleri, düşük profilleri ve PCB üzerine kolayca basılabilmeleri nedeniyle modern iletişim ve EH sistemlerinde yaygın kullanılır.

## 1. Dikdörtgen Yama Tasarım Formülleri

Belirli bir rezonans frekansı ($f_r$) ve dielektrik sabit ($ \epsilon_r $) için genişlik ($W$) ve uzunluk ($L$) hesaplanır.

### Genişlik ($W$)
Düşük yan lob seviyesi ve uygun ışıma için:
$$W = \frac{c}{2 f_r} \sqrt{\frac{2}{\epsilon_r + 1}}$$

### Etkin Dielektrik Sabiti ($\epsilon_{reff}$)
Hava ve substrat arasındaki alan paylaşımı nedeniyle:
$$\epsilon_{reff} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} [1 + 12h/W]^{-1/2}$$

### Fringing (Kenar) Etkileri ve $\Delta L$
Elektrik alan çizgileri yamanın kenarlarından dışarı taşar (fringing fields). Bu durum, antenin elektriksel olarak fiziksel boyutundan daha büyük görünmesine neden olur:
$$\Delta L = 0.412h \frac{(\epsilon_{reff} + 0.3)(W/h + 0.264)}{(\epsilon_{reff} - 0.258)(W/h + 0.8)}$$
Gerçek rezonans uzunluğu: $L = \frac{c}{2 f_r \sqrt{\epsilon_{reff}}} - 2 \Delta L$

## 2. Avantajlar ve Dezavantajlar

-   **Artılar:** Seri üretim kolaylığı, konformal (yüzeye uyumlu) yapı, dizi antenlere (array) uygunluk.
-   **Eksiler:** Dar bant genişliği (genellikle %1-5), düşük verimlilik, düşük güç taşıma kapasitesi.

## 🤖 Post-AI Perspektifi: Yama Antenlerde Tersiz Tasarım (Inverse Design)

Geleneksel tasarım süreci (Analiz), boyutları verip performansı görmektir. Post-AI süreci ise (Sentez), istenen performansı verip boyutları bulmaktır.

- **Otomatik Geometri Üretimi:** Genetik algoritmalar ve GAN'lar, klasik dikdörtgen formun ötesine geçerek, ultra geniş bant sağlayan "fraktal" veya "serbest form" (free-form) yama şekilleri üretebilir.
- **Substrat Optimizasyonu:** AI, farklı dielektrik sabitli malzemelerin hibrit kullanımını optimize ederek antenin hem boyutunu küçültür hem de verimliliğini artırır.

---
*İpucu: Bant genişliğini artırmak için substrat kalınlığı ($h$) artırılabilir veya parazitik yamalar kullanılabilir.*
