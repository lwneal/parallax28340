#!/usr/bin/env python
import serial
import os
import sys

# See docs at https://www.parallax.com/sites/default/files/downloads/28140-28340-RFID-Reader-Documentation-v2.3.pdf
START_BYTE = 0x0A
END_BYTE = 0x0D


def find_device():
  devices = [d for d in os.listdir('/dev/') if d.startswith('tty.usbserial')]
  if len(devices) == 0:
    sys.stderr.write('Error: No tty.usbserial device is connected. Ensure drivers are installed.\n')
    exit(1)
  elif len(devices) > 1:
    device = random.choice(devices)
    sys.stderr.write('Warning: multiple tty.usbserial devices detected. Using {0}\n'.format(device))
  else:
    device = devices[0]
  return '/dev/{0}'.format(device)


def read_tags(ser):
  tag = []
  while True:
    # Read one byte at a time, starting with 0x0A and ending with 0x0D
    d = ser.read()
    if len(d) == 0:
      continue
    elif ord(d) == START_BYTE:
      tag = []
    elif ord(d) == END_BYTE:
      hex_tag = ''.join(['%02X' % (v) for v in tag])
      print(hex_tag)
    else:
      tag.append(ord(d))


if __name__ == '__main__':
  device_name = find_device()
  ser = serial.Serial(device_name, 2400, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=3)
  sys.stderr.write("Successfully connected to {0}\n".format(device_name))
  read_tags(ser)
