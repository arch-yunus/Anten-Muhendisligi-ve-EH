# DRFM ve Dijital Aldatma Teknikleri (Level 07) 🎭⚔️

**Digital Radio Frequency Memory (DRFM)**, bir EH sisteminin, düşman radarı tarafından yayılan sinyali anlık olarak kaydedip, üzerinde manipülasyon yaparak geri yansıtma kabiliyetidir.

## 1. DRFM Çalışma Mekanizması
1. **Analiz:** Gelen RF sinyali örneklenir ve dijital belleğe alınır.
2. **Manipülasyon:** Kaydedilen sinyale gecikme (Range Delay), faz kayması (Doppler Shift) veya genlik değişikliği eklenir.
3. **Tekrar Yayın:** Manipüle edilmiş sinyal, gerçek hedeften gelen yansımadan daha güçlü bir şekilde geri gönderilir.

## 2. Yaygın Aldatma (Deception) Teknikleri
- **RGPO (Range Gate Pull-Off):** Hedefin mesafesini yanlış göstererek radar takibini kaydırır.
- **VGPO (Velocity Gate Pull-Off):** Doppler kayması ekleyerek hız bilgisini manipüle eder.
- **Sahte Hedef Üretimi (Multiple False Targets):** Radarın ekranını onlarca "sahte uçak" ile doldurarak gerçek hedefi gizler.

---

## 🤖 Post-AI Perspektifi: Bilişsel Aldatıcı (Cognitive Deceiver)

- **DRFM Optimization via RL:** Takviyeli öğrenme (RL) ajanı, düşman radarının algoritmasını anlık olarak analiz eder ve hangi "pull-off" hızının veya mesafesinin radar kilidini (track-lock) en hızlı bozduğunu deneyerek bulur.
- **AI-Managed Signal Fidelity:** DRFM ile üretilen sahte sinyaller, AI tarafından optimize edilerek gerçek uçak yansımasına (RCS) %100 benzer hale getirilir; böylece düşmanın "saldırı mı yoksa gerçek mi" ayrımı yapması imkansızlaşır.
