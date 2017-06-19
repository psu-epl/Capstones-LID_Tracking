### BOM:

The relay control output will supply a 5V signal at up to 6mA.
[Power Switch Tail 2](http://www.powerswitchtail.com/) was used successfully. It is superceded by the [IOT Relay](http://www.digital-loggers.com/iot.html), which can be found at [Adafruit](https://www.adafruit.com/product/2935)

The RFID readers that will work with this module are the [HID-PROX 125kHz readers](https://www.hidglobal.com/products/readers/hid-prox-readers)
 (HID Proxpro II, HID Proxpoint plus.. etc) that use the Wiegand protocol.



| Qty | Value | Device     | Package                         | Parts              | Description                                        | Digikey                 | Mouser               |
|-----|-------|------------|---------------------------------|--------------------|----------------------------------------------------|-------------------------|----------------------|
| 1   |       | ESP12ESMD  | ESP12E-SMD                      | U1                 | ESP12E Module                                      | 1528-1438-ND            | 485-2491             |
| 1   | 3.3V  | D1         | SOT23                           | D1                 | TVS Diode            | MMBZ5V6ALT1GOSCT-ND      | 863-MMBZ5V6ALT1G      |
| 2   |       | DTSM-3     | DTSM-3                          | S1,S2              | flash and reset button                             | 450-2146-1-ND           | FSM2JMTR             |
| 1   | 3.3V  | REG1117    | SOT223                          | IC1                | 800mA and 1A Low Dropout (LDO) Positive Regulator  | AZ1117CH-3.3TRG1DICT-ND | 621-AZ1117CH-3.3TRG1 |
| 2   |       | 4050B      | 16-SOIC                         | U1, U2             | 6ch Buffer                                         | MC14050BDR2GOSCT-ND     | 863-MC14050BDR2G     |
| 2   | 1x7   |            | FEM 1x7POS .1"                  | SPI_Header         | SPI header breakout(optional)                      |                 |                      |
| 1   | 1x6   |            | Term block 6-pos .1" screw term | APD / RFID Header  | Screw Terminal for RFID scanner | ED10565-ND             |           |
| 1   | 1x4   |            | Term block 4-pos .1"            |                    | Screw terminal for Power (Optional)                | ED10563-ND              | 651-1725672          |
| 1   | 1x2   |            | Term block 2-pos .1"            |                    | Screw terminal for stop button   (Optional)        | ED10561-ND              | 571-282834-2         |
| 3   | 100n  | C0805K     | 0805                            | C1, C4, C5         | bypass cap                                         |                         |                      |
| 2   | 10u   | C0805K     | 0805                            | C3,C3              | 3.3v reg input cap                                 |                         |                      |
| 5   | 10k   | R-US_R0805 | 0805                            | R1, R2, R3, R4, R5 | RESISTOR                                           |                         |                      |
| 1   | 33k   | R-US_R0805 | 0805                            | R6                 | RESISTOR                                           |                         |                      |
