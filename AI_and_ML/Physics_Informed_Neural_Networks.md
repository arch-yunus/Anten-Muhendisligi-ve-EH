# Physics-Informed Neural Networks (PINN) ve Maxwell Çözümleri 🧠🧬

Geleneksel derin öğrenme modelleri "saf veri" odaklıdır (Data-Driven). Ancak elektromanyetik dünyasında, fizik kuralları (Maxwell denklemleri) mutlak gerçektir. **PINN mimarileri**, bu fizik kurallarını yapay sinir ağının eğitim sürecine dahil eder.

## 🏛️ PINN Çalışma Prensibi

Normal bir sinir ağı $y = f(x)$ fonksiyonunu öğrenmeye çalışırken; PINN, bu fonksiyonun aynı zamanda bir diferansiyel denklemi (PDE) sağlamasını zorunlu kılar.

Maxwell'in rotor (curl) denklemleri:
$$\nabla \times \mathbf{E} = - \frac{\partial \mathbf{B}}{\partial t}$$

PINN eğitiminde kullanılan **Kayıp Fonksiyonu (Loss Function)** şöyledir:
$$Loss = Loss_{Veri} + Loss_{Fizik} + Loss_{Sınır\_Şartları}$$

- **Loss_Veri:** Etiketli ölçüm veya simülasyon verisine uyum.
- **Loss_Fizik:** Tahmin edilen alanların Maxwell denklemlerini ne kadar sağladığı.

## 🚀 Avantajları

1.  **Daha Az Veri:** Fizik kuralları bilindiği için, modeli eğitmek için çok daha az simülasyon verisine ihtiyaç duyulur.
2.  **Genellenebilirlik:** Eğitim setinde olmayan senaryolarda bile fiziksel olarak tutarlı sonuçlar üretir.
3.  **Hız:** Eğitilmiş bir PINN, karmaşık bir antenin yakın alan (near-field) dağılımını milisaniyeler içinde hesaplayabilir.

---

> [!IMPORTANT]
> PINN'ler, "Kara Kutu" (Black Box) AI modellerini "Gri Kutu" (Grey Box) modellere dönüştürerek mühendislik güvenilirliğini artırır.
