## Station Module

### Hardware:
#### ESP8266 - 12E 
<a href="https://espressif.com/en/products/hardware/esp8266ex/overview">EXPRESSIF</a>



This module was chosen for it's cost/size/power consumption, and prior experience the team had using them.<br>
Also the following:
- Features:
  - 802.11 b/g/n
  - Integrated TCP/IP protocol stack
  - 32-bit MCU running at 80MHz
  - 4M Flash memory
  - Integrated 10-bit ADC
  - SDIO 2.0, (H) SPI, UART, I2C, I2S, IRDA, PWM, GPIO

### RFID things
The PSUID card functions at 125kHz.

#### Decoding the signal

<p align="center">

<img src="supporting%20docs/PSUID.jpg" width="200">
<br>
PSU ID card modulating a 125kHz signal
<br><br>
<img src="supporting%20docs/FSK%20modulation.png" width="400">
<br>
From: <a href="http://ww1.microchip.com/downloads/en/DeviceDoc/51115F.pdf">Microchip 125kHz design guide AN680</a>
</p>

### USB Bridge (HID)
May be able to populate (or not) this part of the SM.

Software: Use an ATTiny and some HID library.

Or hardware: Would be nice to use a bridge that supports I2C or SPI like: 
<a href="http://ww1.microchip.com/downloads/en/DeviceDoc/22288A.pdf">MCP2210</a>
