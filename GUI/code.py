# Test program for Alex - sends command "CL5" every 5 sec., prints answer - enjoy!
import time
import board
import busio
import digitalio
import adafruit_rfm9x
from adafruit_ads1x15.analog_in import AnalogIn
import sys
import supervisor
import usb_cdc
#storage.remount("/", False)
RADIO_FREQ_MHZ = 433.0   # LORA frequency 433 MHz

# Define pins connected to the chip, A4 and A3, initialize SPI
CS = digitalio.DigitalInOut(board.A4)
RESET = digitalio.DigitalInOut(board.A3)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze LORA
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.tx_power = 23   #transmission power: 23dB
rfm9x.signal_bandwidth = 62500
rfm9x.coding_rate = 8
rfm9x.spreading_factor = 9
rfm9x.enable_crc = True

#startTime = time.monotonic()  #start timer

def read_serial(serial):
    available = serial.in_waiting
    text = ""
    while available:
        raw = serial.read(available)
        text = raw.decode("utf-8")
        available = serial.in_waiting
    return text

serial = usb_cdc.console
inText = ""
while True:
    inText += read_serial(serial)
    if inText.endswith("\n"):
        if (inText.find("measure") > -1):
            rfm9x.send("CL5",destination=0,node=0,identifier=0,flags=0)
            packet = rfm9x.receive(timeout=2)
            if packet is not None:
              try:
                packetText = str(packet, 'ascii')
              except:
                packetText = "<gibberish>"
              print(packetText)
        inText = ""


#      rfm9x.send("CL5",destination=0,node=0,identifier=0,flags=0)
#      packet = rfm9x.receive(timeout=2)
#      if packet is not None:
#        try:
#          packetText = str(packet, 'ascii')
#        except:
#          packetText = "<gibberish>"
#      print(packetText)



    #send out measurement signal every 5 seconds
#    if (time.monotonic() - startTime >= 5):
#      rfm9x.send("CL5",destination=0,node=0,identifier=0,flags=0)
#      print("measure command sent")
#      startTime = time.monotonic()
#    packet = rfm9x.receive(timeout=2)
#    if packet is not None:
#        try:
#          packetText = str(packet, 'ascii')
#        except:
#          packetText = "<gibberish>"
#        printText = "received: " + packetText
#        print(printText)


    #if supervisor.runtime.serial_bytes_available:
    #    value = input().strip()
    #    # Sometimes Windows sends an extra (or missing) newline - ignore them
    #    if value == "":
    #        continue
    #    print("RX: {}".format(value))
