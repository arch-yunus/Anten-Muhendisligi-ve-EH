# Seviye 07: Hesaplamalı Elektromanyetik (Computational EM) 💻🔋

Anten mühendisliğinin en kritik aşamalarından biri, Maxwell denklemlerinin analitik olarak çözülemediği karmaşık yapılar için **Sayısal (Nümerik) Yöntemler** kullanarak çözüm üretmektir. Bu modül, modern EM çözücülerin (CST, HFSS, FEKO) kalbinde yatan algoritmaları ve bu algoritmaların EH simülasyonlarındaki etkisini inceler.

## 1. Moment Metodu (Method of Moments - MoM) 🎯
MoM, integral tabanlı bir çözüm yöntemidir ve özellikle metalik antenlerin (dipol, patch, slot) ve tel yapıların analizi için altın standarttır.

- **Çalışma Prensibi:** Maxwell integralleri, bilinmeyen yüzey akımları ($J$) cinsinden ifade edilir. Bu akımlar, "basis functions" (genellikle RWG - Rao-Wilton-Glisson) kullanılarak ayrıklaştırılır (discretize).
- **Avantajı:** Sadece metalik yüzeylerin ayrıklaştırılması yettiği için boş uzay için bellek harcamaz. Uzak alan (Far-field) ve kazanç hesaplamalarında son derece hızlıdır.
- **Kullanım Alanı:** Anten yerleşim analizleri, tel antenler, büyük metalik platformlar üzerindeki antenler.

## 2. Sonlu Elemanlar Yöntemi (Finite Element Method - FEM) 📐
FEM, diferansiyel tabanlı bir yöntemdir ve düzensiz, karmaşık ve dielektrik ağırlıklı geometrilerin analizi için en hassas yöntemdir.

- **Çalışma Prensibi:** Çözüm alanı tetrahedral (dört yüzlü) küçük hacimlere bölünür. Her hacim içinde alanlar polinomlarla ifade edilir ve enerji minimizasyonu prensibiyle global matris çözülür.
- **Avantajı:** Malzeme değişimlerine (dielektrik sabitleri, manyetik malzemeler) karşı son derece toleranslıdır.
- **Kullanım Alanı:** Filtre tasarımı, metamalzemeler, dalga kılavuzları ve kapalı rezonatörler.

## 3. Zaman Tanım Kümesinde Sonlu Farklar (FDTD) ⚡
FDTD, Maxwell denklemlerinin zaman ve uzayda doğrudan basit farklar (central difference) ile çözüldüğü bir yöntemdir.

- **Çalışma Prensibi:** "Yee Cell" adı verilen ızgaralar üzerinde elektrik ve manyetik alanlar birbirini takip eden zaman adımlarında (leap-frog) güncellenir.
- **Avantajı:** Tek bir simülasyonla çok geniş bir frekans bandında sonuç verebilir (UWB sistemler için idealdir). Lineer olmayan (non-linear) malzemeleri kolayca modelleyebilir.
- **Kullanım Alanı:** Darbe (Pulse) yayılımı, UWB antenler, insan vücudu etkileşimleri (SAR analizleri).

## 4. Sayısal Yöntemlerin EH Stratejisindeki Farkı
| Yöntem | Dominant Uygulama | EH Karşılığı |
| :--- | :--- | :--- |
| **MoM** | Radar Kesit Alanı (RCS) | Uçağın radarda ne kadar göründüğünü hesaplama |
| **FEM** | Minyatür Antenler | Küçük gövdeli İHA/SİHA anten optimizasyonu |
| **FDTD** | Ultra Geniş Bant (UWB) | Jammer sinyalinin spektral etkisini görme |

---

### 🚀 Uygulama Önerisi
Pratik bir deneyim için [Python_NEC_Wrapper.py](../Simulation/Python_NEC_Wrapper.py) aracını kullanarak basit bir dipol antenin MoM ile nasıl analiz edildiğini inceleyin.
