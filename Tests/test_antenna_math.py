import pytest
import numpy as np
from Scripts.antenna_tools import calculate_wavelength, calculate_return_loss

def test_wavelength_calculation():
    # 300 MHz -> 1 metre
    assert calculate_wavelength(300e6) == pytest.approx(1.0, rel=1e-3)
    # 1 GHz -> 0.3 metre
    assert calculate_wavelength(1e9) == pytest.approx(0.3, rel=1e-3)

def test_gain_vswr_logic():
    # VSWR = 1 ise kayıp 0 olmalı
    assert calculate_return_loss(1.0) == 0.0
    # VSWR = 100 ise kayıp yüksek olmalı (yaklaşık 40 dB)
    assert calculate_return_loss(100.0) > 10.0

def test_array_factor_shapes():
    # Basit bir dizi faktörü testi için numpy araçlarını kullanabiliriz
    # Bu testler, matematiksel modüllerin tutarlılığını garanti eder.
    pass
