# Işıma Teorisi ve Kaynaklar (Level 02) 🕯️

Antenlerin nasıl enerji yaydığını anlamak için Maxwell denklemlerinden ışıma integrallerine geçiş yapmamız gerekir.

## 1. Vektör Potansiyelleri ($\mathbf{A}$ ve $\mathbf{F}$)

Doğrudan $\mathbf{E}$ ve $\mathbf{H}$ alanlarını çözmek yerine yardımcı vektör potansiyellerini kullanmak matematiksel olarak daha verimlidir:
- **Manyetik Vektör Potansiyeli ($\mathbf{A}$):** Elektrik akım kaynakları ($\mathbf{J}$) tarafından oluşturulur.
- **Elektrik Vektör Potansiyeli ($\mathbf{F}$):** Manyetik akım kaynakları ($\mathbf{M}$) (Magnetik dipoller veya yarık antenler) tarafından oluşturulur.

## 2. Hertzian Dipol (Sonsuz Küçük Dipol)

Fiziksel uzunluğu dalga boyundan çok küçük olan ($l \ll \lambda$) bir dipolün Far-field (Uzak Alan) ışıması şu bileşenleri içerir:

$$E_\theta = j\eta \frac{k I_0 l e^{-jkr}}{4\pi r} \sin \theta$$
$$H_\phi = j \frac{k I_0 l e^{-jkr}}{4\pi r} \sin \theta$$

Bu denklemler bize ışımanın $\sin \theta$ ile orantılı olduğunu, yani dipolün ekseni yönünde hiç ışıma yapmadığını gösterir.

## 3. Huygens-Fresnel İlkesi

Bir antenin önündeki sanal bir yüzeydeki alan dağılımı biliniyorsa, bu yüzey her biri birer küresel dalga kaynağı olan sonsuz küçük kaynakların toplamı olarak düşünülebilir. Bu ilke, horn ve reflektör antenlerin analizinde temel teşkil eder.
