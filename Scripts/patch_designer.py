import numpy as np

def calculate_patch_dimensions(freq_ghz, dielectric_constant, substrate_height_mm):
    """
    Dikdörtgen Mikroşerit Yama (Patch) Anten Tasarımcısı
    """
    c = 3e8 # Işık hızı (m/s)
    f_r = freq_ghz * 1e9
    er = dielectric_constant
    h = substrate_height_mm * 1e-3

    # 1. Genişlik (W)
    W = (c / (2 * f_r)) * np.sqrt(2 / (er + 1))

    # 2. Etkin Dielektrik Sabiti (er_eff)
    er_eff = ((er + 1) / 2) + ((er - 1) / 2) * (1 + 12 * h / W)**-0.5

    # 3. Uzunluk Uzantısı (delta L)
    term1 = (er_eff + 0.3) * (W / h + 0.264)
    term2 = (er_eff - 0.258) * (W / h + 0.8)
    delta_L = 0.412 * h * (term1 / term2)

    # 4. Uzunluk (L)
    L_eff = c / (2 * f_r * np.sqrt(er_eff))
    L = L_eff - 2 * delta_L

    return W, L, er_eff

if __name__ == "__main__":
    print("--- Mikroşerit Yama Anten Tasarım Aracı ---")
    
    # Standart 2.4 GHz WiFi Anteni (FR4 Substrat: er=4.4, h=1.6mm)
    freq = 2.44
    er = 4.4
    h = 1.6
    
    W, L, er_eff = calculate_patch_dimensions(freq, er, h)
    
    print(f"[+] Frekans: {freq} GHz")
    print(f"[+] Substrat: er={er}, h={h}mm")
    print(f"----------------------------------------")
    print(f"[RESULT] Yama Genişliği (W): {W*1000:.2f} mm")
    print(f"[RESULT] Yama Uzunluğu (L): {L*1000:.2f} mm")
    print(f"[RESULT] Etkin Dielektrik (er_eff): {er_eff:.3f}")
