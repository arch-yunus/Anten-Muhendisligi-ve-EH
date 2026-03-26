# Surrogate Modeling: EM Simülasyonlarını Hızlandırma ⚡🧠

Vekil modeller (Surrogate Models), karmaşık elektromanyetik simülasyonların "kara kutu" (black-box) olarak modellenmesidir. Amaç, giriş parametreleri (boyutlar, malzeme sabitleri) ile çıkış parametreleri (S11, kazanç, patern) arasındaki ilişkiyi öğrenmektir.

## 🛠️ Süreç Akışı (Workflow)

1.  **Örnekleme (Sampling):** Tasarım uzayının (Design Space) Latin Hypercube Sampling (LHS) gibi yöntemlerle etkili bir şekilde taranması.
2.  **Simülasyon:** Örnek noktaların elektromagnetik çözücülerde (CST/HFSS) koşturulması.
3.  **Eğitim (Training):** Veri setinin bir regresyon modeline (ML) beslenmesi.
4.  **Tahmin (Prediction):** Yeni bir tasarım denendiğinde simülatör yerine vekil modelin kullanılması.

## 🔬 Kullanılan Algoritmalar

### 1. Yapay Sinir Ağları (ANN)
Çok katmanlı perseptronlar, doğrusal olmayan karmaşık ilişkileri modellemede oldukça başarılıdır. Özellikle geniş bantlı antenlerin empedans uyumunu tahmin etmede kullanılırlar.

### 2. Gaussian Process Regression (GPR)
Veri miktarının az olduğu durumlarda bile yüksek doğruluk sağlar. Ayrıca tahminin yanına bir "güven aralığı" (Uncertainty) eklemesi büyük bir avantajdır.

### 3. Support Vector Regression (SVR)
Yüksek boyutlu parametrik uzaylarda kararlı sonuçlar verir.

## 💡 Pratik Uygulama: Simülasyon Hızlandırma Örneği

| Yöntem | Süre (1000 iterasyon) | Doğruluk |
| :--- | :--- | :--- |
| Tam Dalga (CST) | ~150 Saat | %100 (Referans) |
| **ANN Surrogate** | **~2 Saniye** | **%98-99** |

---

> [!TIP]
> Bir vekil model eğitildikten sonra, optimizasyon döngüsünde (Optimization Loop) binlerce farklı geometriyitek bir kahve molası süresince test edebilirsiniz.
