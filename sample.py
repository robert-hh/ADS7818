# Drive the ADS7818 ADC using SPI
# Connections:
# xxPy | ADS7818
# -----|-------
# P10  |  CLK
# P11  |  CONV
# P14  |  DATA add a series resistor of about 4.7k between DATA and P14
#
from machine import SPI
from ads7818 import ADS7818

spi = SPI(0, SPI.MASTER)
vref = 2.493 # measured at the ADS7818
ads = ADS7818(spi)

while True:
    # start a conversion and get the result back
    value = ads.value()
    volt = 2.0 * vref * value / 4096

    print(value, volt)
    res= input("Next: ")
    if res == "q":
        break

