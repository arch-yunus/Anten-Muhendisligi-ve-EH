# Vektör Potansiyelleri ve Dalga Denklemleri (Level 01) 📐

Elektromanyetik alanların doğrudan çözümü zor olduğunda, $\mathbf{A}$ (Manyetik Vektör Potansiyeli) ve $\mathbf{F}$ (Elektrik Vektör Potansiyeli) yardımcı fonksiyonları kullanılır.

## 1. Manyetik Vektör Potansiyeli ($\mathbf{A}$)

Kayıpsız bir ortamda, $\nabla \cdot \mathbf{B} = 0$ olduğu için $\mathbf{B}$'yi bir vektörün rotasyoneli olarak tanımlayabiliriz:
$$\mathbf{B} = \mu \mathbf{H} = \nabla \times \mathbf{A}$$

Maxwell denklemlerini kullanarak homojen olmayan dalga denklemini elde ederiz:
$$\nabla^2 \mathbf{A} + k^2 \mathbf{A} = -\mu \mathbf{J}$$
Burada $k = \omega \sqrt{\mu \epsilon}$ dalga numarasıdır. Bu denklemin çözümü, akım yoğunluğu $\mathbf{J}$ üzerinden alınan integral ile bulunur:
$$\mathbf{A} = \frac{\mu}{4\pi} \iiint_V \mathbf{J} \frac{e^{-jkR}}{R} dV'$$

## 2. Zamanla Değişen Alanlar ve Pozitif Fazörler

Anten analizlerinde genellikle sinüzoidal (harmonik) değişimler incelenir. Bu durumda zaman domainindeki $\mathcal{E}(x,y,z,t)$ alanı, fazör domainindeki $\mathbf{E}(x,y,z)$ ile temsil edilir:
$$\mathcal{E}(x,y,z,t) = \text{Re}\{ \mathbf{E}(x,y,z) e^{j\omega t} \}$$
---

## 🤖 Post-AI Perspektifi: Potansiyelleri Veriden Öğrenmek

Geleneksel olarak $\mathbf{A}$ potansiyelini bulmak için akım yoğunluğu ($\mathbf{J}$) üzerinden üç katlı integral çözülür.

**Post-AI yaklaşımında;**
- **Diferansiyellenebilir Işıma Integralleri:** Işıma integrali bir "sinir ağı katmanı" gibi modellenerek, uzak alan (far-field) verisinden kaynak akım dağılımı ($\mathbf{J}$) otonom olarak kestirilebilir (**Inverse Source Problem**).
- **Green Fonksiyonu Yakınsaması:** Karmaşık ortamlarda Green fonksiyonunu analitik olarak bulmak imkansızdır. AI, bu fonksiyonu bir vekil model (surrogate) olarak öğrenip potansiyel hesaplamalarını gerçek zamanlı hale getirir.
