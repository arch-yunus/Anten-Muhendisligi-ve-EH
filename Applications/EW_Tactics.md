# Elektronik Harp Taktik Entegrasyonu (Level 06) 🛡️⚡

Antenlerin harp sahasındaki en kritik kullanımı, düşman sistemlerini tespit etmek ve etkisiz hale getirmektir.

## 1. Radar Kesit Alanı (RCS) Analizi

RCS, bir hedefin radar sinyallerini ne kadar geri yansıttığının bir ölçüsüdür ($ \sigma $). Anten mühendisi için hedef, kendi anteninin RCS'sini minimize ederek (LPI) görünmezlik sağlamaktır.
$$ \sigma = \lim_{r \to \infty} 4\pi r^2 \frac{|E_s|^2}{|E_i|^2} $$

## 2. Karıştırma (Jamming) Denklemleri

Bir karıştırıcının (Jammer), bir radarı etkisiz hale getirebilmesi için gerekli olan J/S (Jamming-to-Signal) oranı:
$$ \frac{J}{S} = \frac{P_{j} G_{j} \sigma}{P_{t} G_{t} 4\pi R^{2}} \dots $$
Burada $G_j$ karıştırıcının anten kazancı olup, enerjiyi düşmanın radar lóbuna odaklamalıdır.

## 3. LPI (Low Probability of Intercept) Tasarımı

Düşman ELINT sistemleri tarafından fark edilmemek için kullanılan teknikler:
- Çok düşük yan lob seviyeleri (SLL < -30 dB).
- Geniş bantlı spektrum yayılımı.
- Hüzmeleme ile sadece hedefe odaklanma, etrafa enerji kaçırmama.

---
*İpucu: Sayısal hüzmeleme (Beamforming) kullanarak aynı anda birden fazla hedefi karıştırırken, kendi dost sistemlerimize 'null' (sıfır noktası) oluşturabiliriz.*
