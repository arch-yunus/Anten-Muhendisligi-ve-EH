# Genetik Algoritmalar ve Otonom Optimizasyon 🧬🤖

Anten tasarımında parametre uzayı çok boyutlu ve karmaşıktır. Bir geniş bantlı antenin onlarca değişkeni olduğunda, her kombinasyonu elle test etmek imkansızdır. **Stokastik Optimizasyon Algoritmaları**, en iyi çözümü bulmak için doğadaki mekanizmalardan esinlenir.

## 🧬 1. Genetik Algoritmalar (Genetic Algorithms - GA)
Biyolojik evrim prensiplerini taklit eder:
- **Popülasyon:** Rastgele tasarlanmış yüzlerce anten.
- **Fitness (Uygunluk):** Antenin performansı (örn: VSWR < 2 ve Kazanç > 5 dBi).
- **Çaprazlama (Crossover):** İki iyi antenin özelliklerinin birleştirilmesiyle yeni bir "çocuk" anten üretilmesi.
- **Mutasyon:** Tasarımda rastgele küçük değişiklikler yaparak "lokal optimum" tuzaklarından kaçınma.

## 🐝 2. Parçacık Sürü Optimizasyonu (Particle Swarm Optimization - PSO)
Kuş sürülerinin veya balık okullarının hareketini taklit eder:
- Her "parçacık" bir anten tasarımıdır.
- Parçacıklar, hem kendi en iyi deneyimlerine hem de sürünün bulduğu en iyi noktaya doğru tasarım uzayında hareket ederler.
- Mikroşerit antenlerin boyut optimizasyonu için son derece etkilidir.

## 🧠 3. Reinforcement Learning (RL) ile Otonom Tasarım
Yapay zekanın bir "ajan" gibi davranarak anten tasarım kurallarını öğrenmesi:
- **Ödül (Reward):** Verilen parametreler hedefe yaklaştıkça ajana (+) puan verilmesi.
- **Ceza:** SWR arttıkça veya verimlilik düştükçe (-) puan verilmesi.
- RL ajanları, insan mühendislerin aklına gelmeyecek "fraktal" benzeri, son derece karmaşık ama verimli geometriler üretebilir.

---

### 💡 Post-AI İpucu: Çok Amacıyla Optimizasyon (Multi-Objective)
Gerçek hayatta "hem en küçük hem de en yüksek kazançlı" anteni istersiniz. AI destekli **Pareto Optimizasyonu** ile bu iki zıt uç arasındaki en iyi denge noktalarını (Pareto Front) kolayca belirleyebilirsiniz.
