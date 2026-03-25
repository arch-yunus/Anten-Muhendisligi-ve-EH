import numpy as np

def calculate_js_ratio(pj, gj, rj, pt, gt, sigma, rt, bandwidth_ratio=1.0):
    """
    Jamming-to-Signal (J/S) Oranı Hesaplayıcı
    pj: Jammer Gücü (W)
    gj: Jammer Anten Kazancı
    rj: Jammer Mesafesi (m)
    pt: Radar Gücü (W)
    gt: Radar Anten Kazancı
    sigma: Hedef RCS (m^2)
    rt: Radar Mesafesi (m)
    """
    # Jamming Power at Radar
    j_power = (pj * gj) / (4 * np.pi * rj**2)
    
    # Signal Power at Radar (Reflected from target)
    s_power = (pt * gt * sigma) / ((4 * np.pi)**2 * rt**4)
    
    js_ratio_raw = (j_power / s_power) * bandwidth_ratio
    js_ratio_db = 10 * np.log10(js_ratio_raw)
    
    return js_ratio_db

if __name__ == "__main__":
    print("--- Elektronik Harp J/S Oranı Hesaplayıcı ---")
    
    # Senaryo: Bir EH uçağı 50km ötedeki radarı karıştırıyor
    pj, gj, rj = 1000, 10, 50000 # 1kW Jammer, 10dBi gain
    pt, gt, sigma, rt = 50000, 30, 1, 50000 # 50kW Radar, 30dBi gain, 1m2 RCS
    
    js = calculate_js_ratio(pj, gj, rj, pt, gt, sigma, rt)
    
    print(f"[+] Radar Mesafesi: {rt/1000} km")
    print(f"[+] Jammer Mesafesi: {rj/1000} km")
    print(f"----------------------------------------")
    print(f"[RESULT] Jamming-to-Signal (J/S) Oranı: {js:.2f} dB")
    
    if js > 10:
        print("[STATUS] Karıştırma Başarılı (Effective Jamming)")
    else:
        print("[STATUS] Karıştırma Yetersiz (Burn-through risk)")
