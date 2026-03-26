# Bilişsel Hüzmeleme: Derin Öğrenme Tabanlı Dizi Kontrolü 📡⚡🧠

Phased Array (Dizi Antenler) sistemlerinde hüzme yönlendirme (beam steering) ve sinyal tespiti, geleneksel olarak yoğun matematiksel hesaplamalar ve sinyal işleme algoritmaları (MUSIC, ESPRIT) ile yapılır. Bilişsel Hüzmeleme (Cognitive Beamforming), bu süreci yapay zekaya emanet eder.

## 🎯 Derin Öğrenme ile Varış Açısı (DoA) Kestirimi
Geleneksel MUSIC algoritması, yüksek gürültülü (SNR) ortamlarda ve sinyaller birbirine çok yakın olduğunda hata yapabilir.
- **CNN Yaklaşımı:** Anten elemanlarından gelen sinyalleri bir "görüntü" veya "harita" gibi işleyerek, hedeflerin açısını çok daha yüksek doğrulukla ve hızlıca tahmin eder.
- **Avantaj:** Güzültüye (Noise) ve karıştırmaya (Jamming) karşı çok daha dayanıklıdır.

## 🤖 Akıllı Null-Steering (Karıştırmayı Yok Etme)
Elektronik Harp sahasında, bir yandan hedefi takip ederken diğer yandan düşman karıştırıcısının (Jammer) yönünde "kör nokta" (null) oluşturmanız gerekir.
- **Deep Reinforcement Learning:** Jammer'ın hareketlerini ve stratejisini öğrenen bir yapay zeka, anten dizi katsayılarını (weights) anlık olarak değiştirerek dost sinyali korumayı başarır.

## ⚡ Real-Time Digital Beamforming
Post-AI EH sistemleri, milisaniyeler içinde binlerce anten elemanının faz ve genlik değerlerini optimize etmek zorundadır.
- **FPGA Üzerinde AI:** Eğitilmiş sinir ağları, FPGA veya yüksek hızlı çipler üzerinde koşturularak "sıfır gecikmeli" bir hüzmeleme performansı sunar.

---

### 🏛️ Gelecek Vizyonu: Yazılım Tanımlı Akıllı Yüzeyler (RIS)
Yapay zeka sadece anteni değil, dalganın çarptığı "duvarları" veya "yüzeyleri" de kontrol ederek (Reconfigurable Intelligent Surfaces), kör noktası olmayan hibrit akıllı haberleşme ağları oluşturur.
