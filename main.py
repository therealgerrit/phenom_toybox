import numpy as np
from phenom.spectrum import linear_SASE_spectrum


if __name__ == '__main__':
    t = np.linspace(-25e-15, 25e-15, 1500)
    spectrum = linear_SASE_spectrum(t, pulse_duration=5e-15, photon_energy=9500, bandwidth=1e-12, plot=True)

