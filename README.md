# Simple RFID Tag Reader for OSX

Ingredients:
- One Parallax 28340 USB RFID reader
- One Macbook

- Step 1: Install the driver `FTDIUSBSerialDriver_v2_3.dmg`
- Step 2: Connect the reader to the macbook
- Step 3: Run the terminal command `python reader.py`

The contents of any 125 kHz RFID tag in range of the reader will be printed in hex, one tag per line.
