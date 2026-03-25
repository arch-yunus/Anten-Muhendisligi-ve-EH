import numpy as np

def calculate_dipole_length(frequency_mhz):
    """
    Hesaplama: Yarım dalga dipol anten boyu (l = 143 / f)
    """
    length = 143.0 / frequency_mhz
    return length

def calculate_friis_link_budget(pt, gt, gr, freq_mhz, distance_km):
    """
    Friis İletim Denklemi (Link Bütçesi)
    L_free = 32.4 + 20log10(d) + 20log10(f)
    Pr = Pt + Gt + Gr - L_free
    """
    free_space_loss = 32.44 + 20 * np.log10(distance_km) + 20 * np.log10(freq_mhz)
    received_power = pt + gt + gr - free_space_loss
    return received_power, free_space_loss

def vswr_to_reflection_coeff(vswr):
    """
    VSWR'dan Yansıma Katsayısı (Gamma) hesaplama
    """
    gamma = (vswr - 1) / (vswr + 1)
    return gamma

if __name__ == "__main__":
    print("--- Anten Mühendisliği Hesaplama Aracı ---")
    
    # Örnek 1: 2.4 GHz için Dipol Boyu
    freq = 2400
    L = calculate_dipole_length(freq)
    print(f"[+] {freq} MHz için Yarım Dalga Dipol Boyu: {L*100:.2f} cm")
    
    # Örnek 2: Link Bütçesi
    pt, gt, gr = 20, 5, 2 # dBm, dBi, dBi
    dist = 10 # km
    pr, loss = calculate_friis_link_budget(pt, gt, gr, freq, dist)
    print(f"[+] 10 km Mesafede Alınan Güç: {pr:.2f} dBm (Kayıp: {loss:.2f} dB)")
    
    # Örnek 3: VSWR Analizi
    vswr_val = 1.5
    gamma_val = vswr_to_reflection_coeff(vswr_val)
    return_loss = -20 * np.log10(gamma_val)
    print(f"[+] VSWR {vswr_val} için Geri Dönüş Kaybı (Return Loss): {return_loss:.2f} dB")
