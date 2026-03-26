import numpy as np
import matplotlib.pyplot as plt

"""
Post-AI Anten Mühendisliği: Phased Array Beamforming Görselleştirici 📡🎨
----------------------------------------------------------------------
Bu araç, bir doğrusal dizi antenin (ULA) hüzmeleme yeteneğini ve 
faz kaydırmanın ışıma örüntüsü üzerindeki etkisini görselleştirir.
"""

def plot_beam_pattern(num_elements=8, spacing=0.5, scan_angle_deg=0):
    print(f"📡 {num_elements} elemanlı dizi için hüzmeleme hesaplanıyor...")
    print(f"🎯 Yönlendirme açısı: {scan_angle_deg}°")

    theta = np.linspace(-np.pi/2, np.pi/2, 1000) # -90 to 90 degrees
    k = 2 * np.pi # Assume normalized wavelength (lambda = 1)
    d = spacing # Spacing in terms of lambda
    
    # Faz kaydırma (Phase Shift) hesaplama - Elektronik Yönlendirme
    scan_angle_rad = np.deg2rad(scan_angle_deg)
    psi = -k * d * np.sin(scan_angle_rad)
    
    # Dizi Faktörü (Array Factor) hesaplama
    # AF = sum( exp( j * n * (kd sin(theta) + psi) ) )
    af = np.zeros_like(theta, dtype=complex)
    for n in range(num_elements):
        af += np.exp(1j * n * (k * d * np.sin(theta) + psi))
    
    # Normalizasyon
    af_db = 20 * np.log10(np.abs(af) / num_elements)
    af_db = np.maximum(af_db, -40) # Limit dynamic range to -40dB

    # Görselleştirme
    plt.figure(figsize=(10, 6))
    plt.plot(np.rad2deg(theta), af_db, linewidth=2, color='#00ff99', label=f'Scan: {scan_angle_deg}°')
    plt.axvline(scan_angle_deg, color='red', linestyle='--', alpha=0.5, label='Target direction')
    plt.title(f"Phased Array Radiation Pattern ({num_elements} Elements)", color='white', pad=20)
    plt.xlabel("Angle (Degrees)", color='white')
    plt.ylabel("Normalized AF (dB)", color='white')
    plt.grid(True, alpha=0.3, linestyle=':')
    
    # Estetik ayarlar (Dark Mode teması)
    plt.gcf().set_facecolor('#1e1e1e')
    plt.gca().set_facecolor('#1e1e1e')
    plt.gca().tick_params(colors='white')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('phased_array_pattern.png')
    print("✅ Patern görselleştirildi: phased_array_pattern.png")
    # plt.show() # Not shown in non-interactive mode

if __name__ == "__main__":
    # Örnek: 12 elemanlı, 30 dereceye yönlendirilmiş hüzme
    plot_beam_pattern(num_elements=12, spacing=0.5, scan_angle_deg=30)
