import numpy as np
import matplotlib.pyplot as plt

def calculate_rcs_sphere(radius, wavelength):
    """
    Sovereign Edition: Simple MoM-like RCS calculation for a sphere (Mie scattering approximation).
    Used in Level 07: Computational EM Lab.
    """
    print(f"[*] Calculating RCS for Sphere (r={radius}m, lambda={wavelength}m)...")
    k = 2 * np.pi / wavelength
    size_parameter = k * radius
    
    # Simple Optical Region Approximation for RCS of a sphere: Sigma = PI * r^2
    sigma_optical = np.pi * (radius ** 2)
    
    print(f"[+] Optical RCS: {sigma_optical:.4f} m^2 ({10*np.log10(sigma_optical):.2f} dBsm)")
    return sigma_optical

def visualize_rcs_vs_frequency(radius):
    frequencies = np.linspace(0.1e9, 10e9, 100) # 100MHz to 10GHz
    c = 3e8
    rcs_values = []
    
    for f in frequencies:
        lam = c / f
        rcs_values.append(calculate_rcs_sphere(radius, lam))
        
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies / 1e9, 10 * np.log10(rcs_values), label='Sphere RCS (Optical Approx)')
    plt.title(f'RCS vs Frequency (Sphere Radius = {radius}m)')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('RCS (dBsm)')
    plt.grid(True, which="both", ls="-")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("-" * 50)
    print("   Level 07 Lab: Computational EM & RCS Analysis")
    print("-" * 50)
    visualize_rcs_vs_frequency(0.5) # 0.5m radius sphere
