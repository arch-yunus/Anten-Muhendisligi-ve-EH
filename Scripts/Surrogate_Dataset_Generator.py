import numpy as np
import pandas as pd

"""
Post-AI Anten Mühendisliği: Sentetik Veri Üreticisi 📡📊
-------------------------------------------------------
Bu script, bir AI modelini (Surrogate) eğitmek için gerekli olan 
elektromanyetik veri setini simüle eder. Gerçek dünyada bu veriler 
CST, HFSS veya gerçek ölçümlerden gelir.
"""

def generate_antenna_dataset(num_samples=1000):
    print(f"📡 {num_samples} örnekli sentetik anten veri seti üretiliyor...")
    
    # Giriş Parametreleri (Features)
    lengths = np.random.uniform(10, 30, num_samples)    # mm
    widths = np.random.uniform(5, 20, num_samples)     # mm
    eps_r = np.random.uniform(2.1, 10.2, num_samples)   # Dielektrik Sabiti
    
    # Çıkış Parametreleri (Targets) - Fiziksel kurallara benzetilmiş rastgelelik
    # Örn: Rezonans frekansı f_r ~ c / (2 * L * sqrt(eps_r))
    c = 3e8
    fr_base = c / (2 * (lengths * 1e-3) * np.sqrt(eps_r))
    fr_actual = (fr_base / 1e9) + np.random.normal(0, 0.05, num_samples) # GHz
    
    # Kazanç (Gain) ~ Yüzey Alanı (W * L) ile orantılı
    gain = 2 + (lengths * widths / 100) + np.random.normal(0, 0.2, num_samples) # dBi
    
    # Veri setini oluşturma
    df = pd.DataFrame({
        'Length_mm': lengths,
        'Width_mm': widths,
        'Dielectric_Const': eps_r,
        'Resonance_Freq_GHz': fr_actual,
        'Peak_Gain_dBi': gain
    })
    
    filename = 'antenna_design_dataset.csv'
    df.to_csv(filename, index=False)
    print(f"✅ Veri seti başarıyla oluşturuldu: {filename}")
    return df

if __name__ == "__main__":
    data = generate_antenna_dataset(1000)
    print("\n--- Veri Seti Önizleme ---")
    print(data.head())
