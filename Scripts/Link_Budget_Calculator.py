import numpy as np

"""
Post-AI Anten Mühendisliği: Profesyonel Link Bütçesi Hesaplayıcı 📡🛰️
-----------------------------------------------------------------
Friis İletim Denklemi baz alınarak, bir haberleşme veya EH linkinin 
uçtan uca performansını (SNR) hesaplar.
"""

def calculate_link_budget(freq_ghz, distance_km, pt_dbm, gt_dbi, gr_dbi, l_cable_db=2, nf_db=3):
    print(f"🚀 Link Bütçesi Analizi Başlatıldı ({freq_ghz} GHz, {distance_km} km)")
    
    # 1. Serbest Uzay Yayılım Kaybı (FSPL) - Path Loss
    # FSPL (dB) = 20log10(d) + 20log10(f) + 92.45
    fspl = 20 * np.log10(distance_km) + 20 * np.log10(freq_ghz) + 92.45
    
    # 2. EIRP (Equivalent Isotropic Radiated Power)
    eirp = pt_dbm + gt_dbi - l_cable_db
    
    # 3. Alınan Güç (Pr)
    pr_dbm = eirp - fspl + gr_dbi
    
    # 4. Gürültü Tabanı (Noise Floor) - Oda sıcaklığında 1 MHz bant genişliği için
    # Pn = -174 dBm/Hz + 10log10(BW) + NF
    bw_mhz = 10 # 10 MHz bandwidth example
    noise_floor = -174 + 10 * np.log10(bw_mhz * 1e6) + nf_db
    
    # 5. SNR (Signal-to-Noise Ratio)
    snr = pr_dbm - noise_floor
    
    print("-" * 30)
    print(f"📡 EIRP: {eirp:.2f} dBm")
    print(f"📉 Path Loss (FSPL): {fspl:.2f} dB")
    print(f"📥 Received Power: {pr_dbm:.2f} dBm")
    print(f"🔊 Noise Floor: {noise_floor:.2f} dBm")
    print(f"✅ Sinyal Gürültü Oranı (SNR): {snr:.2f} dB")
    print("-" * 30)
    
    if snr > 15:
        print("💡 Durum: Link kalitesi mükemmel!")
    elif snr > 5:
        print("⚠️ Durum: Link kalitesi sınırda.")
    else:
        print("❌ Durum: Link başarısız (Sinyal gürültü altında).")
        
    return snr

if __name__ == "__main__":
    # Örnek Operasyonel Senaryo: 10 GHz Radar, 50 km Mesafe
    calculate_link_budget(
        freq_ghz=10.0, 
        distance_km=50, 
        pt_dbm=60,  # 1 kW transmitter
        gt_dbi=35,  # High gain radar antenna
        gr_dbi=10,  # Target ES receiver antenna
        nf_db=4
    )
