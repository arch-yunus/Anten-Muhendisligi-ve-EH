# Maxwell Denklemleri ve Elektromanyetik Dalgalar 🧪
---

## 🤖 Post-AI Perspektifi: Maxwell Analitiği

Geleneksel olarak Maxwell denklemlerini çözmek için sınır şartlarını (boundary conditions) belirleyip karmaşık integral veya diferansiyel denklemlerle uğraşırız. 

**Post-AI döneminde;**
- **Physics-Informed Neural Networks (PINN):** Yapay sinir ağları, sadece veriyi değil, Maxwell denklemlerinin kendisini bir "kayıp fonksiyonu" (loss function) olarak kullanarak fiziksel kurallara %100 uyan çözümler üretir.
- **Diferansiyellenebilir Programlama:** Anten geometrisindeki küçük bir değişimin uzak alan ışımasına etkisi, gradyan tabanlı AI algoritmalarıyla anlık olarak hesaplanabilir.
Anten mühendisliğinin temeli olan Maxwell denklemleri, elektrik ve manyetik alanların birbiriyle ve maddeyle nasıl etkileşime girdiğini açıklar.

## Serbest Uzayda Maxwell Denklemleri

1.  **Gauss Yasası (Elektrik):** $\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$
2.  **Gauss Yasası (Manyetik):** $\nabla \cdot \mathbf{B} = 0$
3.  **Faraday Yasası:** $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$
4.  **Ampere-Maxwell Yasası:** $\nabla \times \mathbf{B} = \mu_0 \left( \mathbf{J} + \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} \right)$

## Dalga Yayılımı

Homojen ve kayıpsız bir ortamda, bu denklemler ikinci dereceden bir diferansiyel denklem olan **Dalga Denklemi**'ne dönüşür:

$$\nabla^2 \mathbf{E} - \mu \epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0$$

Bu denklem, elektromanyetik enerjinin boşlukta ışık hızıyla ($c \approx 3 \times 10^8$ m/s) yayıldığını kanıtlar. Antenler, bu dalgaları kontrollü bir şekilde oluşturmak veya yakalamak için tasarlanmış geçiş yapılarıdır.
