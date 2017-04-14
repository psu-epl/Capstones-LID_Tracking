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





#### ESP Pin Functions:
| Pin     | Function                   |
|---------|----------------------------|
| GPIO 0  | Green LED status indicator |
| GPIO 1  | SPI Slave Select 1         |
| GPIO2   | Audible alarm control      |
| GPIO 3  | SPI Slave Select 2         |
| GPIO 4  | RFID-DATA1                 |
|  GPIO 5 | RFID-DATA0                 |
| GPIO 12 | SPI MOSI                   |
| GPIO 13 | SPI MISO                   |
| GPIO 14 | SPI Clock                  |
| GPIO 15 | APD Enable                 |
| ADC     | Stop / Logout              |








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
The Station module may be configured to act as a human interface device (HID) such as a keyboard for entering credentials into a computer.
The ESP-12E does not support USB natively, but a USB-to-SPI Protocol Converter may be used such as the MCP2210, and plugged into the SPI breakout.
