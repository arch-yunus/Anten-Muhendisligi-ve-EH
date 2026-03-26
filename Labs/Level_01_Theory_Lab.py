import numpy as np
import matplotlib.pyplot as plt

"""
Post-AI Anten Mühendisliği: Seviye 01 Teori Laboratuvarı 🧪📡
-----------------------------------------------------------
Bu laboratuvar, boşlukta yayılan bir elektromanyetik dalganın 
elektrik (E) ve manyetik (H) alan bileşenlerini simüle eder.
"""

def simulate_em_wave(frequency_hz=1e9, duration_ns=5):
    print(f"🌊 EM Dalga Yayılımı Simüle Ediliyor ({frequency_hz/1e9} GHz)...")
    
    c = 3e8 # Speed of light
    lam = c / frequency_hz # Wavelength
    k = 2 * np.pi / lam # Wave number
    
    z = np.linspace(0, 3 * lam, 500) # 3 wavelengths distance
    t = 0 # Snapshot at t=0
    
    # E and H fields (Linearly polarized in x and y)
    E_x = np.cos(k * z)
    H_y = np.cos(k * z) # In phase for plane wave
    
    # Plotting
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # E-field (Blue)
    ax.plot(z, np.zeros_like(z), E_x, label='Elektrik Alan (E)', color='cyan', linewidth=2)
    # H-field (Red)
    ax.plot(z, H_y, np.zeros_like(z), label='Manyetik Alan (H)', color='magenta', linewidth=2)
    
    # Propagation Axis
    ax.plot(z, np.zeros_like(z), np.zeros_like(z), color='white', linestyle='--', alpha=0.5)
    
    ax.set_xlabel('Yayılım Ekseni (z)', color='white')
    ax.set_ylabel('Manyetik Eksen (y)', color='white')
    ax.set_zlabel('Elektrik Eksen (x)', color='white')
    ax.set_title('Sinüsoidal Düzlem Dalga Yayılımı', color='white', pad=20)
    
    # Styling
    fig.set_facecolor('#121212')
    ax.set_facecolor('#121212')
    ax.tick_params(colors='white')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('Labs/em_wave_lab.png')
    print("✅ Simülasyon tamamlandı: Labs/em_wave_lab.png")

if __name__ == "__main__":
    # Ensure Labs directory exists (handled by tool)
    simulate_em_wave()
