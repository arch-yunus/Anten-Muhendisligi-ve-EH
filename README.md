# Anten Mühendisliği ve Elektronik Harp (EH) Araştırma Arşivi 📡⚡

![Banner](assets/banner.png)

> **"Elektromanyetik spektrumda üstünlük, modern harp sahasının anahtarıdır."**

Bu depo; elektromanyetik teori, anten tasarımı ve bu teknolojilerin **Elektronik Harp (Electronic Warfare - EW)** sahasındaki stratejik kullanım senaryolarını kapsayan, akademik düzeyde yapılandırılmış profesyonel bir teknik kütüphanedir. 

### 🚀 [Eğitim Yol Haritası (Roadmap)](Roadmap.md)
*Temellerden Elektronik Harp taktiklerine uzanan 7 seviyeli kapsamlı müfredat.*

---

## 🏛️ Mimari Yapı ve Müfredat

Proje, bir Elektronik Harp sisteminin yaşam döngüsüne ve anten mühendisliğinin temel direklerine uygun olarak 4 ana modüle ayrılmıştır:

### 1. 📖 [Elektromanyetik Teori ve Işıma Esasları](Theory/)
Antenin fiziksel katmanını ve dalganın boşluktaki davranışını anlamak, etkili bir EH stratejisinin temelidir.
- **Maxwell Denklemleri:** Kaynaktan uzaklaşan dalgaların matematiksel modeli.
- **Işıma Mekanizması:** Akım yoğunluğu ve yük ivmelenmesinin ışıma ile ilişkisi.
- **Yakın Alan (Near-Field) vs Uzak Alan (Far-Field):** Ölçüm ve analiz sınırlarının belirlenmesi.
- **Friis İletim Denklemi:** Sinyal gücünün mesafe ve kazançla değişimi (Link Bütçesi).

### 2. 🎯 [Kritik Anten Parametreleri (EH Perspektifi)](Parameters/)
Bir EH anteni, standart haberleşme antenlerinden çok daha zorlu kriterlere sahip olmalıdır:
- **Geniş Bantlılık (Wideband):** 0.5 GHz - 18 GHz gibi geniş spektrumları tek bir antenle kapsama.
- **Düşük Yan Lob Seviyesi (SLL):** Tespit edilebilirliği (LPI) minimize etme.
- **Polarizasyon Çevikliği:** Düşman yayınlarına anında uyum sağlama veya çapraz polarizasyon ile karıştırma.
- **VSWR ve Verimlilik:** Yüksek güçlü karıştırma (High Power Microwave) sinyallerini yönetebilme.

### 3. 🚀 [Stratejik Anten Türleri ve Uygulamalar](Applications/)
EH operasyonlarında kritik rol oynayan anten yapıları:
- **Yön Bulma (DF) Antenleri:** Spiral, Log-Periodic ve İnterferometrik diziler.
- **Phased Array (Dizi Antenler):** Milisaniyeler içinde hüzme (beam) yönlendirme ve hedef takibi.
- **Digital Beamforming:** Eş zamanlı çoklu hedef takibi ve *null-steering* teknikleri.
- **Geniş Bantlı Horn Antenler:** Yüksek kazançlı karıştırma (Jamming) operasyonları.

### 4. 💻 [Simülasyon, Analiz ve SDR](Simulation/)
- **Elektromanyetik Çözücüler:** CST Studio Suite, HFSS ve FEKO metodolojileri.
- **Hesaplamalı EH:** MATLAB/Python ile Radar Kesit Alanı (RCS) ve karıştırma etkinliği analizleri.
- **Spektrum Analizi & SDR:** RTL-SDR, HackRF ve USRP cihazları ile sinyal kestirimi ve GNSS karıştırma.

---

## 🛠️ Elektronik Harp Operasyonel Kabiliyetleri

Repo içerisinde aşağıdaki üç ana fonksiyonel alan için teknik notlar ve algoritmalar yer almaktadır:

1.  **ES (Elektronik Destek):** Sinyal tespiti, parametre kestirimi ve AoA (Angle of Arrival) algoritmaları (MUSIC, ESPRIT).
2.  **EA (Elektronik Taarruz):** Gürültü ve aldatma karıştırması techniques (DRFM temelli karıştırma).
3.  **EP (Elektronik Koruma):** Kendi radar ve haberleşme sistemlerimizi düşman karıştırmasından koruma yöntemleri.

---

## 📜 Lisans ve Katkı
Bu proje **MIT Lisansı** ile korunmaktadır. Akademik veya profesyonel katkı sağlamak isteyen araştırmacılar [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyebilirler.

---
**Yazar:** [Bahattin Yunus Çetin](https://github.com/arch-yunus)  
*IT Architect & RF Systems Researcher*
