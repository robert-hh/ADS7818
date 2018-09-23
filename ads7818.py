#
# Simple class for the ADS7818 ADC using SPI
# Connections:
# xxPy | ADS7818
# -----|-------
# CLK  |  CLK
# MOSI |  CONV
# MISO |  DATA add a series resistor of about 4.7k between DATA and P14
#
from machine import SPI

class ADS7818:
    def __init__(self, spi, *, vref=2.5, baudrate=1000000):
        self.spi = spi
        self.vref = vref
        self.buf = bytearray(2)
        self.spi.init(SPI.MASTER, baudrate=baudrate, polarity=1, phase=1, bits=16)

    def value(self):
        spi.write_readinto(b"\xe0\x00", self.buf)
        return ((self.buf[0] << 8) | self.buf[1]) & 0xfff

    def voltage(self):
        return 2.0 * self.vref * self.value() / 4096

