# Anten Açıklığı ve Verimlilik (Level 03) 🎯

Aperture (açıklık) antenler (horn, reflektör) için tasarımdaki en kritik parametrelerden biridir.

## 1. Etkin Açıklık ($A_e$)

Bir antenin gelen elektromanyetik dalgadan ne kadar güç 'yakalayabildiğinin' bir ölçüsüdür. Maksimum kazanç ($G_{max}$) ile direkt ilişkilidir:
$$A_e = \frac{\lambda^2}{4\pi} G_{max}$$
Bu denklem, frekans arttıkça ($\lambda$ azaldıkça) aynı kazancı elde etmek için daha geniş fiziksel alanlara ihtiyaç duyulduğunu gösterir.

## 2. Açıklık Verimliliği ($\epsilon_{ap}$)

Antenin fiziksel alanı ($A_p$) ile etkin alanı ($A_e$) arasındaki orandır:
$$\epsilon_{ap} = \frac{A_e}{A_p}$$
Verimliliği etkileyen alt faktörler:
-   **İlümünasyon Verimliliği:** Anten yüzeyindeki alan dağılımının homojenliği.
-   **Spillover (Taşma) Verimliliği:** Feed anteninden gelen enerjinin ana reflektörü kaçırması.
-   **Faz Verimliliği:** Yansıma sonrası dalga fazlarının odak noktasındaki uyumu.

## 3. Friis Gürültü Denklemi ve $G/T$

Sistem hassasiyeti (sensitivity), alınan sinyalin gürültüden ne kadar üstün olduğuyla belirlenir.
$$T_{sys} = T_{ant} + T_1 + \frac{T_2}{G_1} + \frac{T_3}{G_1 G_2} \dots$$
Burada $T_{ant}$ antenin gökyüzünden veya yerden topladığı gürültü sıcaklığıdır. Alıcı zincirindeki ilk yükseltecin (LNA) kazandığı $G_1$, sonraki katların gürültüsünü baskılamak için hayati önem taşır.
