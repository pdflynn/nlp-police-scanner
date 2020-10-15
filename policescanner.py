from rtlsdr import RtlSdr
from pylab import *
import numpy as np

# Montgomery County Channels
FR1 = 453.3125e6 # Fire/Rescue 1
FRS3 = 460.45e6 # Fire/Rescue South 3
FRS5 = 460.4125e6 # Fire/Rescue South 5
FRS7 = 460.05e6 # Fire/Rescue South 7
FRS9 = 460.1625e6 #Fire/Rescue South 9
FRS11 = 453.8375e6 #Fire/Rescue South 11
LSMFR1 = 451.7875e6 #Longshop-McCoy Fire/Rescue
MED4 = 463.075e6 # EMS to Lewis Gale
MED10 = 462.975e6 # EMS to Carillion NRV Med Center
MONTDISP = 452.3e6 # Montgomery Sheriff Dispatch
MONTCOURT = 453.975e6 # Montgomery Sheriff Courts
MONTJAIL = 453.725e6 # Montgomery Sheriff Jail

# Blacksburg Town Channels
BBFIREDISP = 451.10000e6 # Fire Dispatch
BBFIRETAC = 451.27500e6 # Fire Tac
BBRESCUE = 460.02500e6 # Rescue
BBPOLDISP = 453.48750e6 # Police Dispatch
BTFR = 453.85000e6 # BT Fixed Route Buses
BTACCS = 453.85000e6 # BT Access

# Virginia Tech Channels
VTRS1 = 461.12500e6 # VT Rescue Squad 1
VTRS3 = 464.76250e6 # VT Rescue Squad 3
VTPOL1 = 453.87500e6 # VT Police 1
VTSF = 155.11500e6 # VT Safe Ride


# Configure RTL-SDR
sdr = RtlSdr()
sdr.sample_rate = 2.048e6
sdr.center_freq = VTPOL1
sdr.gain = 'auto'

# Sample from the RTL-SDR and close it
samples = sdr.read_samples(256*1024)
sdr.close()

# Algorithm...
# while loop
# sample from the RTL SDR