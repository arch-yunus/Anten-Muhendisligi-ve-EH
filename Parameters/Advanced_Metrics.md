# İleri Seviye Anten Metrikleri (Level 03) 📈

Standart kazanç ve VSWR metrics ötesinde, profesyonel sistem tasarımında karşılaşılan kritik parametreler.

## 1. Polarizasyon Kayıp Faktörü (PLF)

Verici antenin polarizasyonu ile alıcı antenin polarizasyonu arasındaki uyumsuzluktan kaynaklanan güç kaybıdır.
$$PLF = |\hat{\rho}_w \cdot \hat{\rho}_a|^2$$
Örneğin, dikey polarize bir verici ile yatay polarize bir alıcı arasındaki PLF teorik olarak $-\infty$ dB'dir (tam kayıp).

## 2. Gürültü Sıcaklığı ve G/T Oranı

Bir alıcı sisteminin hassasiyetini belirleyen en önemli faktör Anten Gürültü Sıcaklığı ($T_A$) ve Sistemin Toplam Gürültü Sıcaklığıdır ($T_{sys}$).
$$G/T = \frac{G_{max}}{T_{sys}} [dB/K]$$
Bu oran, özellikle uydu haberleşmesi ve zayıf sinyal kestirimi (ES) yapan sistemler için kilit bir başarı göstergesidir.

## 3. Poincare Küresi

Anten polarizasyon durumlarını (Doğrusal, Dairesel, Eliptik) görselleştirmek ve analiz etmek için kullanılan küresel bir representasyondur. Kürenin kutupları dairesel polarizasyonları, ekvatoru ise doğrusal polarizasyonları temsil eder.

---

## 🤖 Post-AI Perspektifi: Metriklerin "Maliyet Fonksiyonu" (Cost Function) Olarak Kullanımı

Bir AI optimizasyon döngüsünde (GA, PSO, RL), yukarıdaki her metrik birer ceza (penalty) veya ödül (reward) bileşenine dönüşür:
- **VSWR Hedefleme:** AI, S11 değerini belirli bir eşiğin altında tutmak için geometriyi büker.
- **G/T Optimizasyonu:** Özellikle düşük gürültülü (LNA) sistemlerde AI, anten kazancı ile sistem sıcaklığı arasındaki en iyi dengeyi (Pareto Front) bulur.
- **Polarizasyon Çevikliği:** AI, Poincare küresi üzerindeki herhangi bir noktaya milisaniyeler içinde uyum sağlayacak dizi katsayılarını hesaplar.
