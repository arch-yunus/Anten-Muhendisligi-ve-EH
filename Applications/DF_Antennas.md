# Elektronik Harp ve Yön Bulma (DF) Antenleri 🛸

Elektronik Harp'te en kritik görevlerden biri, tehdit sinyalinin konumunu belirlemektir.

## Temel DF Anten Yapıları

-   **Spiral Antenler:** Geniş açılı ve dairesel polarizasyona sahip oldukları için sinyal yakalama (ES) görevlerinde sıklıkla tercih edilirler.
-   **Log-Periodic Antenler:** Çok geniş frekans bantlarında (Örn: 2-18 GHz) sabit kazanç sağladıkları için spektrum izlemede vazgeçilmezdir.
-   **İnterferometrik Diziler:** Gelen dalganın iki veya daha fazla anten arasındaki faz farkını ölçerek son derece hassas yön kestirimi yaparlar.

## 🤖 Post-AI Perspektifi: Akıllı Yön Kestirimi (DoA)

- **AI-Driven DoA Estimation:** Kaynak tespiti için kullanılan klasik MUSIC veya ESPRIT algoritmaları, düşük sinyal-gürültü oranlarında (SNR) başarısız olabilir. Derin öğrenme tabanlı yön kestiriciler, gürültülü ortamlarda bile sinyal kaynağını derecenin onda biri hassasiyetle bulabilir.
- **Spiral Antenlerde Patern Düzeltme:** Spiral antenlerin frekansa bağlı faz kaymaları, AI tarafından "kalibrasyon haritası" olarak öğrenilir ve ölçüm hataları yazılımsal olarak otonom düzeltilir.
