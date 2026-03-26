# Malzeme Bilimi ve Üretim Toleransları 💎⚙️

Bir antenin teorik başarısı, üzerine basıldığı (veya üretildiği) malzemenin fiziksel kararlılığına bağlıdır.

## 1. Substrat Seçimi (FR4 vs Rogers)
- **FR4 (Flame Retardant 4):** Ucuz, her yerde bulunabilen epoksi reçine. Ancak 1-2 GHz üzerinde yüksek dielektrik kaybı ($\tan\delta$) ve frekansla değişen dielektrik sabiti ($\epsilon_r$) nedeniyle hassas tasarımlar için uygun değildir.
- **Rogers (PTFE/Teflon tabanlı):** Çok düşük kayıplı, yüksek frekans kararlılığına sahip substratlar. Milimetre dalga (mmWave) projelerinin vazgeçilmezidir.

## 2. Kritik Malzeme Parametreleri
- **$\epsilon_r$ (Dielektrik Sabiti):** Anten boyutlarını küçültür ama bant genişliğini de daraltabilir.
- **$\tan\delta$ (Loss Tangent):** Isıya dönüşen enerji kaybı.
- **Bakır Pürüzlülüğü (Copper Roughness):** Cilt etkisi (Skin Effect) nedeniyle yüksek frekanslarda iletkenlik kaybına yol açar.

## 3. Üretim Toleransları (Manufacturing)
- **Aşındırma (Etching) Toleransı:** Planlanan $1 \text{ mm}$ hattın $0.95 \text{ mm}$ üretilmesi frekansı kaydırır.
- **Via Hassasiyeti:** Çok katmanlı (layered) yapılarda via hizalaması (misalignment) rezonansı bozar.

---

## 🤖 Post-AI Perspektifi: Malzeme Telafisi (AI-Compensation)

AI-modelleri, belirli bir PCB üreticisinin "hata karakteristiğini" öğrenerek tasarımı önceden "deforme" eder:
- **Pre-distortion:** Üretimde meydana gelecek aşındırma kaybını önceden hesaba katarak geometride revizyon yapılması.
- **Substrat Tanıma:** AI, gelen ham S-parametre verisinden malzemenin o anki gerçek $\epsilon_r$ değerini kestirerek simülasyonu günceller.
