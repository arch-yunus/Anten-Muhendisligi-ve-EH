# SDR Entegrasyon Rehberi: Yazılımdan Sahaya 📡📻

Post-AI Anten Mühendisliği, sadece simülasyonlarda kalmaz; donanım ile gerçek dünyaya bağlanır. Bu rehber, Python projelerinizi popüler SDR (Software Defined Radio) cihazlarıyla nasıl entegre edeceğinizi açıklar.

## 1. Donanım Gereksinimleri
- **RTL-SDR (V3/V4):** Giriş seviyesi sinyal dinleme ve spektrum izleme (24 MHz - 1.7 GHz).
- **Adalm-Pluto:** Hem verici (TX) hem alıcı (RX) kabiliyetli, hobi ve akademik kullanım için ideal.
- **Ettus USRP (B210/N210):** Profesyonel ve askeri sınıf EH çalışmaları (70 MHz - 6 GHz).

## 2. Python Kütüphaneleri
Donanımla haberleşmek için şu kütüphaneleri kullanacağız:
```bash
pip install pyrtlsdr      # RTL-SDR için
pip install pyadi-iio     # Adalm-Pluto ve IIO cihazları için
```

## 3. Örnek: Canlı Spektrum Okuma (RTL-SDR)
```python
from rtlsdr import RtlSdr

sdr = RtlSdr()
sdr.sample_rate = 2.048e6
sdr.center_freq = 100e6 # 100 MHz (FM Radyo)
sdr.gain = 'auto'

samples = sdr.read_samples(256*1024)
sdr.close()

# 'samples' verisi artık AI modellerine (Örn: Modülasyon Sınıflandırıcı) giriş olarak verilebilir.
```

## 4. Post-AI Uygulaması: Otonom Karıştırıcı Tespiti
1. SDR üzerinden spektral veri alınır.
2. `AI_and_ML/Cognitive_Beamforming.md` içindeki modeller bu veriyi analiz eder.
3. Tespit edilen bir EH tehdidi varsa, anten dizisi o yöne otonom olarak "null" (sıfır noktası) koyar.
