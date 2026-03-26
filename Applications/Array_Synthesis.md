# Dizi Sentezi ve Hüzmeleme (Level 05) 📡📡📡

Dizi antenler (Array Antennas), birden fazla anten elemanının belirli bir geometride dizilerek, toplam ışıma örüntüsünün (radiation pattern) kontrol edilmesini sağlar.

## 1. Dizi Faktörü (Array Factor)
Toplam alan, tek bir elemanın alanı ile **Dizi Faktörü**'nün çarpımıdır:
$$E_{total} = E_{element} \times AF$$

Doğrusal bir dizi (ULA) için dizi faktörü:
$$AF = \sum_{n=1}^N I_n e^{j(n-1)(kd \cos \theta + \beta)}$$
Burada $\beta$ faz kaymasıdır ve hüzmenin (beam) yönünü belirler.

## 2. Yan Lob (Sidelobe) Kontrolü
Klasik yöntemler (Binom, Dolph-Tschebyscheff, Taylor), dizi katsayılarını ($I_n$) ağırlıklandırarak yan lob seviyesini düşürür. Bu, EH sahasında tespit edilebilirliği (LPI) azaltmak için kritiktir.

---

## 🤖 Post-AI Perspektifi: Bilişsel Dizi Sentezi

Geleneksel ağırlıklandırma yöntemleri statiktir ve sadece belirli paternler üretir.

- **Neural Beamforming:** Derin öğrenme modelleri, ortamdaki gürültü ve karıştırma sinyallerini anlık olarak analiz ederek, dizi katsayılarını milisaniyeler içinde optimize eder. Bu sayede, aynı anda birden fazla hedef takip edilebilir (Multi-beamforming).
- **Arıza Telafisi (Failure Compensation):** Dizi içindeki bir eleman bozulduğunda, AI geri kalan elemanların faz ve genliklerini yeniden hesaplayarak paternin bozulmasını engeller.
- **Null-Steering AI:** Düşman karıştırıcısının yönüne "sıfır" noktası (null) koyma işlemi, artık klasik matris tersi almak yerine, hiyerarşik takviyeli öğrenme (RL) ile çok daha hızlı yapılmaktadır.
