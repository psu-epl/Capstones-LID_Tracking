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






### BOM:
| Qty | Value | Device     | Package                         | Parts              | Description                                        | Digikey                 | Mouser               |
|-----|-------|------------|---------------------------------|--------------------|----------------------------------------------------|-------------------------|----------------------|
| 1   |       | ESP12ESMD  | ESP12E-SMD                      | U1                 | ESP12E Module                                      | 1528-1438-ND            | 485-2491             |
| 1   | 3.3V  | D1      | SOT23                          | D1                 | TVS Diode            | MMBZ5V6ALT1GOSCT-ND      | 863-MMBZ5V6ALT1G      |
| 2   |       | DTSM-3     | DTSM-3                          | S1,S2              | flash and reset button                             | 450-2146-1-ND           | FSM2JMTR             |
| 1   | 3.3V  | REG1117    | SOT223                          | IC1                | 800mA and 1A Low Dropout (LDO) Positive Regulator  | AZ1117CH-3.3TRG1DICT-ND | 621-AZ1117CH-3.3TRG1 |
| 2   |       | 4050B      | 16-SOIC                         | U$1, U$2           | 6ch Buffer                                         | MC14050BDR2GOSCT-ND     | 863-MC14050BDR2G     |
| 2   | 1x5   |            | FEM 1x5POS .1"                  | SPI_Header         | SPI header breakout(optional)                      | S6103-ND                |                      |
| 1   | 1x9   |            | Term block 9-pos .1" screw term | APD / RFID Header  | Screw Terminal for APD and RFID scanner (Optional) | 277-1280-ND             | 651-1725724          |
| 1   | 1x4   |            | Term block 4-pos .1"            |                    | Screw terminal for Power (Optional)                | ED10563-ND              | 651-1725672          |
| 1   | 1x2   |            | Term block 2-pos .1"            |                    | Screw terminal for stop button   (Optional)        | ED10561-ND              | 571-282834-2         |
| 3   | 100n  | C0805K     | 0805                            | C1, C4, C5         | bypass cap                                         |                         |                      |
| 1   | 100u  | C0805K     | 0805                            | C2                 | 3.3v reg output cap                                |                         |                      |
| 1   | 10u   | C0805K     | 0805                            | C3                 | 3.3v reg input cap                                 |                         |                      |
| 5   | 10k   | R-US_R0805 | 0805                            | R1, R2, R3, R4, R5 | RESISTOR                                           |                         |                      |
| 1   | 33k   | R-US_R0805 | 0805                            | R6                 | RESISTOR                                           |                         |                      |
