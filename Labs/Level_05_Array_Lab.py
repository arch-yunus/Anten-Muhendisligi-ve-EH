import numpy as np
import matplotlib.pyplot as plt

"""
Post-AI Anten Mühendisliği: Seviye 05 Dizi Anten Laboratuvarı 🧪📡
---------------------------------------------------------------
Bu laboratuvar, bir Phased Array antenin hüzme yönlendirme (beamsteering) 
ve yan lob (sidelobe) seviyelerini interaktif olarak analiz eder.
"""

def analyze_phased_array(elements=16, d_lambda=0.5, scan_angle=25):
    print(f"📡 {elements} Elemanlı Dizi Analiz Ediliyor...")
    
    theta = np.deg2rad(np.linspace(-90, 90, 1000))
    k = 2 * np.pi
    
    # Phase shift for scanning
    phi = -k * d_lambda * np.sin(np.deg2rad(scan_angle))
    
    # Array Factor calculation
    AF = np.zeros_like(theta, dtype=complex)
    for n in range(elements):
        AF += np.exp(1j * n * (k * d_lambda * np.sin(theta) + phi))
        
    AF_norm = 20 * np.log10(np.abs(AF) / elements)
    
    # Visualization
    plt.figure(figsize=(10, 5))
    plt.plot(np.rad2deg(theta), AF_norm, color='#00ffcc', linewidth=2)
    plt.fill_between(np.rad2deg(theta), AF_norm, -40, color='#00ffcc', alpha=0.2)
    
    plt.title(f"Phased Array: {elements} Eleman | Yön: {scan_angle}°", color='white')
    plt.xlabel("Açı (Derece)", color='white')
    plt.ylabel("Normalize Kazanç (dB)", color='white')
    plt.grid(True, alpha=0.2)
    plt.ylim([-40, 0])
    
    plt.gcf().set_facecolor('#1a1a1a')
    plt.gca().set_facecolor('#1a1a1a')
    plt.gca().tick_params(colors='white')
    
    plt.tight_layout()
    plt.savefig('Labs/array_lab_steering.png')
    print("✅ Analiz tamamlandı: Labs/array_lab_steering.png")

if __name__ == "__main__":
    analyze_phased_array(elements=24, scan_angle=-15)
