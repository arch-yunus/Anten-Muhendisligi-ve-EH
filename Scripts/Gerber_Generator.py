import os
import datetime

class GerberGenerator:
    """
    Sovereign Edition: Basic Gerber (RS-274X) Generator for Rectangular Patch Antennas.
    Developed for the 'Anten Muhendisligi ve EH' Repository.
    """
    def __init__(self, width_mm, length_mm, filename="patch_antenna.gbr"):
        self.width = width_mm
        self.length = length_mm
        self.filename = filename

    def generate(self):
        print(f"[*] Generating Gerber file: {self.filename}")
        print(f"[*] Design Dimensions: {self.width}mm x {self.length}mm")

        # Gerber RS-274X Header & Configuration
        gerber_content = [
            "G04 Sovereign Anten Gerber Generator v1.0*",
            "G04 Creation Date: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "*",
            "%FSLAX34Y34*%",      # Format Statement: Absolute, 3.4 leading zeros omitted
            "%MOMM*%",            # Unit: Millimeters
            "%LPD*%",             # Layer Polarity: Dark
            "G04 Define Aperture: Rectangular Patch*",
            f"%ADD10R,{self.width:.4f}X{self.length:.4f}*%", # Aperture Definition D10
            "D10*",               # Select Aperture D10
            "X0Y0D03*",           # Flash aperture at origin
            "M02*"                # End of file
        ]

        with open(self.filename, "w") as f:
            f.write("\n".join(gerber_content))
        
        print(f"[+] Success: {self.filename} created at {os.path.abspath(self.filename)}")

if __name__ == "__main__":
    # Example: A typical 2.4 GHz patch might be ~30mm x 40mm depending on substrate
    print("-" * 50)
    print("   Sovereign Antenna Fabrication Tool: Gerber Gen")
    print("-" * 50)
    
    w = float(input("Enter Patch Width (mm): ") or 29.5)
    l = float(input("Enter Patch Length (mm): ") or 38.0)
    
    gen = GerberGenerator(w, l)
    gen.generate()
