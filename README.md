# USB-Lora-inteface
Circuitpython based LoRa USB stick, which allows browser based (GUI) serial communication via WebUSB to LoRa and back
![image](https://user-images.githubusercontent.com/26468273/211173999-1578e1f9-d74e-44f0-9335-6285dec42d40.png)


## Purpose
Communication adapter to any remote LoRa satellite device, e.g. remote sensing over distances of several kilometers. The device can be used for collecting sensor data from widely distributed devices with a time resolution of seconds.

## Usage
 * Plug device in, opens up as USB stick (circuitpython)
 * Open .html file in Web Serial API compatible browser (Chrome, Edge, Opera; see https://developer.mozilla.org/en-US/docs/Web/API/Serial)
 * Use browser as GUI, connect to device and send/receive commands to/from device via serial interface
 * commands will be forwarded via LoRa RFM98W radio chip to remote device
 
 ## Content
 - PCB:             EAGLE Cad PCB files, list of components
 - Housing:         3D CAD files for 3D printing
 - Circuit Python:  Bootloader .bin for ATSAMD51, Circuitpython .uf2, device code
 - GUI:             .html code with .js elements
 
 ## Manual
 - Make PCB, solder components
 - flash bootloader using .bin file, e.g. via JLink, see https://learn.adafruit.com/how-to-program-samd-bootloaders
 - mount device via usb, put into bootloader mode, upload circuitpython .uf2 file
 - upload .html file to device, adjust accordingly
 enjoy!
 
[Grn.Solar](https://www.grn.solar)
 
 Big shoutouts to [Adafruit](https://www.adafruit.com "Adafruit rocks"), all was based on their work.
