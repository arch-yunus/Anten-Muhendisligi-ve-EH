import os
import subprocess

class NECWrapper:
    """
    NEC2 (Numerical Electromagnetics Code) için Python sarmalayıcı (wrapper).
    Bu sınıf, .nec dosyalarını otonom olarak üretmek ve çalıştırmak için tasarlanmıştır.
    """
    def __init__(self, filename="simulation.nec"):
        self.filename = filename
        self.content = []

    def add_wire(self, tag, segments, x1, y1, z1, x2, y2, z2, radius):
        """Tel (wire) geometrisi ekler."""
        line = f"GW {tag} {segments} {x1} {y1} {z1} {x2} {y2} {z2} {radius}"
        self.content.append(line)

    def set_frequency(self, freq_mhz):
        """Çalışma frekansını ayarlar."""
        self.content.append(f"FR 0 1 0 0 {freq_mhz} 0")

    def add_excitation(self, tag, segment=1):
        """Besleme noktası (excitation) tanımlar."""
        self.content.append(f"EX 0 {tag} {segment} 0 1 0")

    def generate_file(self):
        """NEC dosyasını diske yazar."""
        header = ["CE - Python-Generated Antenna Simulation"]
        footer = ["GE 0", "GN -1", "RP 0 37 73 1001 0 0 5 5", "EN"]
        full_content = header + self.content + footer
        with open(self.filename, "w") as f:
            f.write("\n".join(full_content))
        print(f"[*] Simulation file generated: {self.filename}")

    def run_simulation(self):
        """
        Yerel sistemde nec2++ veya necc yürütülebilir dosyası varsa çalıştırır.
        Not: Bu bir şablondur, sistemde NEC motorunun kurulu olması gerekir.
        """
        print("[!] Pro-Tip: To run, you need 'nec2++' installed on your system.")
        # subprocess.run(["nec2++", "-i", self.filename])

if __name__ == "__main__":
    # Örnek: Yarım dalga dipol simülasyonu (300 MHz)
    sim = NECWrapper("dipole_test.nec")
    sim.add_wire(1, 11, 0, 0, -0.25, 0, 0, 0.25, 0.001)
    sim.set_frequency(300)
    sim.add_excitation(1, 6)
    sim.generate_file()
    sim.run_simulation()
