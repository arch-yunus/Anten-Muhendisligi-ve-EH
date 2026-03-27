# Seviye 08: Fizik Bilgili Sinir Ağları (PINNs) in EM 🧠⚡⚖️

Post-AI anten mühendisliğinin zirvesi, yapay zekanın sadece veriye (data-driven) değil, aynı zamanda fizik yasalarına (physics-driven) dayalı olarak eğitilmesidir. **Physics-Informed Neural Networks (PINNs)**, Maxwell denklemlerini doğrudan kayıp fonksiyonuna (loss function) entegre ederek, veri setine ihtiyaç duymadan (veya çok az veriyle) EM problemlerini çözen devrim niteliğinde bir mimaridir.

## 1. Geleneksel AI vs. PINN 🔬
- **Standart AI:** Sadece giriş-çıkış verilerine bakarak aradaki korelasyonu öğrenir. Fizik kurallarını bilmez, bu yüzden "fiziksel olarak imkansız" sonuçlar üretebilir (örneğin, enerjinin yoktan var olması).
- **PINN:** Sinir ağının ağırlıkları güncellenirken, sadece hataya bakılmaz; aynı zamanda ağın ürettiği çözümün Maxwell denklemlerini (veya dalga denklemini) ne kadar sağladığına bakılır.

## 2. PINN Matematiksel Formülasyonu 📐
PINN'in toplam kayıp fonksiyonu ($L_{total}$) şu şekilde tanımlanır:

$$L_{total} = L_{data} + L_{physics} + L_{boundary}$$

- **$L_{data}$:** Bilinen ölçüm veya simülasyon noktalarındaki klasik hata (MSE).
- **$L_{physics}$:** Sinir ağının çıktısının Maxwell denklemlerini ne kadar bozduğunun ölçüsü (Residual loss). Örneğin: $\nabla \times \mathbf{E} + \mu \frac{\partial \mathbf{H}}{\partial t} \approx 0$ olması zorunlu kılınır.
- **$L_{boundary}$:** Sınır şartlarının (PEC, Absorbing BC vb.) sağlanma derecesi.

## 3. EM Problemlerinde PINN Avantajları 🚀
- **Verisiz Çözüm:** Bazı durumlarda hiçbir simülasyon verisi olmadan, sadece Maxwell denklemleri ve sınır şartlarıyla problem çözülebilir.
- **Simülasyon Hızlandırma:** Eğitildikten sonra, geleneksel nümerik yöntemlerle (FEM/FDTD) saatler süren analizleri milisaniyeler içinde gerçekleştirebilir.
- **Ters Tasarım (Inverse Design):** İstenen bir radyasyon diyagramı verildiğinde, bu diyagramı sağlayacak en uygun fiziksel yapıyı bulmakta (Optimization) çok daha güçlüdür.

## 4. PINN Uygulama Alanları (Post-AI EH)
1.  **Görünmezlik (Cloaking):** Metamalzeme parametrelerini öyle optimize eder ki, dalga çarpıp geçtiğinde hiç sapma olmaz.
2.  **Kör Nokta Analizi:** Geleneksel yöntemlerin zorlandığı çok dar açıklıklarda (small aperture) EM sızıntı tahmini.
3.  **Hızlı Link Analizi:** Değişen atmosferik şartlarda sinyal yayılımının anlık (real-time) fiziksel tahmini.

---

### 🏛️ Geleceğin Vizyonu
Dost veya düşman her türlü EM sinyalinin fiziksel davranışını, AI modellerimizin içinde "yerleşik bir fizik motoru" (embedded physics engine) varmış gibi analiz etmek, Spektrum Egemenliği yolundaki en büyük silahtır.
