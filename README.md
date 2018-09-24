# ADS8718: Python class for the ADS7818 AD-converter

This is a very short and simple class. It uses the SPI bus for the interface. That
ensures that the tight timing requirements of the ADS7818 are met.

## Constructor

### adc = ADS7818(spi, \*, baudrate = 1000000, vref = 2.5, inverted = False)

- spi is an SPI object which has to be created by the caller. Just the Pins have to be assigned by the caller.
The init method of the class sets baud rate, phase, polarity and word size.
- baudrate defines the baud rate of the SPI. the default is 1000000.
The valid range is 200kHz through 4 MHz. These boundaries are silently enforced by the class.
- vref is the reference voltage, used to calculate the voltage value. If the internal Vref is used, this allows small
corrections. If an external Vref is applied, it can be assigned here. Vref is only used for the calculation
of the equivalent voltage.
- inverted set True is an inverted is added between the MOSI output and CONV input
in order to get an high CONV level during quiet times.

## Methods

### value = adc.value()

Retrieves the adc raw value using the setting of the constructor. The returned
value is in the range of 0 - 4095

### volt = adc.voltage()

Reads the adc value and return the equivalent voltage. This is based on the vref
value set in the constructor. The formula is:   
    voltage = 2 * vref * value / 4096

## Interface

The ADS7818 is connected to the SPI bus signals. There is no CS needed. The
connection consist of:

|Micro|ADS7818|
|:---|:---|
|MOSI|CONV (5)|
|MISO|DATA (6)|
|CLK|CLK (7)|

The ADS7818 needs a Vcc of 5V. For connecting to a 3.3V device, insert a resistor
of about 4.7 kOhm between MISO and DATA.
Device like those of Pycom have low MOSI level. This does not nicely match the
interface description of the ADS7818. In that is a problem, an inverter can be
placed between MOSI and CONV, and the flag inverted has to be set True when calling
the constructor.

## Example

```
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
```
