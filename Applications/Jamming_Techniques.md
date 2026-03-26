# Karıştırma Teknikleri ve Sinyal Analizi (Level 06) ⚔️

Elektronik Taarruz (Electronic Attack - EA) bir düşman sensörünün spektral olarak boğulması veya aldatılması üzerine kuruludur.

## 1. Karıştırma Türleri

### A. Gürültü Karıştırması (Noise Jamming)
-   **Spot Jamming:** Tüm gücü tek bir frekansa odaklayarak dar bantlı sistemleri (Örn: Telsiz) felç eder.
-   **Barrage Jamming:** Gücü geniş bir frekans bandına yayar. Birçok radarı aynı anda etkiler ancak birim frekans başına düşen güç düşer.
-   **Sweep Jamming:** Dar bantlı bir gücü bandın içinden hızla geçirerek (tarayarak) sistemi karıştırır.

### B. Aldatma Karıştırması (Deception Jamming)
DRFM (*Digital Radio Frequency Memory*) teknolojisi kullanarak düşman sinyali kaydedilir, değiştirilir (gecikme veya faz kayması eklenerek) ve geri yansıtılır. Düşman radarı gerçek hedef yerine onlarca sahte hedef görür.

## 2. Burn-Through Mesafesi

Bir radarın, karıştırma altındaki bir hedefi hala görebildiği maksimum mesafedir. Hedef yaklaştıkça yansıyan sinyal ($1/R^4$) karıştırma sinyalinden ($1/R^2$) daha hızlı artar ve bir noktada karıştırmayı aşar.
$$ R_{BT} = \sqrt{\frac{P_t G_t \sigma G_r}{P_j G_j (J/S)_{req} 4\pi \dots}} $$

## 3. ECCM (Electronic Counter-Countermeasures)

Karıştırmaya karşı koruma yöntemleri:
-   **Frequency Hopping:** Sürekli frekans değiştirerek yakalanmayı zorlaştırmak.
-   **Sidelobe Cancellation:** Karıştırma sinyalini yan loblardan değil, sadece ana hüzmeden kabul etmek.
-   **Pulse Compression:** Karmaşık sinyal modülasyonları ile gürültüden ayrışmak.

---

## 🤖 Post-AI Perspektifi: Bilişsel Elektronik Harp (Cognitive EW)

Geleneksel jamming sistemleri, önceden tanımlanmış tehdit kütüphanelerine (Threat Library) dayanır. Ancak modern LPI radarlar sürekli parametre değiştirdiği için bu kütüphaneler yetersiz kalır.

- **Otonom Tehdit Analizi:** AI, daha önce hiç karşılaşılmamış bir radar sinyalini (Zero-day threat) anlık olarak analiz eder ve onun zayıf noktasını tespit eder.
- **Akıllı Karıştırma Stratejisi:** RL ajanı, hangi jamming tekniğinin o anki radar takibini daha etkili bozduğunu milisaniyeler içinde öğrenir.
- **Düşük Enerji Tüketimi:** AI, tüm bandı boğmak yerine sadece radarın "dinlediği" pencereleri hedefleyerek enerji verimliliğini artırır.
