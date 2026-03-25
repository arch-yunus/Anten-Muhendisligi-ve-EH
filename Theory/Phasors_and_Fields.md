# Fazörler ve Zamanla Değişen Alanlar (Level 01) ⏳⚡

Maxwell denklemlerinin zaman domaininde çözümü karmaşık diferansiyel denklemler gerektirir. Harmonik (sinüzoidal) sinyaller için **Fazör** kullanımı bu süreci cebirsel işlemlere indirger.

## 1. Zaman Harmonik Alanlar

Bir manyetik alan $\mathbf{H}$'nin zamanla değişimi $\cos(\omega t)$ ise:
$$\mathbf{H}(x,y,z,t) = \mathbf{H}_0(x,y,z) \cos(\omega t + \phi)$$
Bunu karmaşık fazör formunda şöyle yazarız:
$$\mathbf{H}(x,y,z,t) = \text{Re}\{ \mathbf{H}_s(x,y,z) e^{j\omega t} \}$$

## 2. Maxwell Denklemlerinin Fazör Formu

Zaman türevleri ($ \partial / \partial t $) yerine $j\omega$ operatorü gelir:
-   $\nabla \times \mathbf{E} = -j\omega\mu \mathbf{H}$
-   $\nabla \times \mathbf{H} = \mathbf{J} + j\omega\epsilon \mathbf{E}$

## 3. Poynting Vektörü ve Güç Akışı

Elektromanyetik enerjinin birim alandan geçen miktarını (güç yoğunluğu) temsil eder. Fazör domaininde ortalama güç yoğunluğu ($\mathbf{W}_{av}$):
$$\mathbf{W}_{av} = \frac{1}{2} \text{Re}\{ \mathbf{E} \times \mathbf{H}^* \}$$
Antenlerde ışıma direnci ve kazanç hesaplamaları, bu vektörün anteni çevreleyen sanal bir yüzey üzerinden entegre edilmesiyle bulunur.
 health
