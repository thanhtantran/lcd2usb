#!/usr/bin/env python
# encoding: utf8

'''getip.py - display system ip
    Author: Tran Thanh Tan
'''
import netifaces as ni

from lcd2usb import LCD

def main(lcd):
  lcd.hello()
  lcd.clear()
  
  import datetime
  lcd.home()
  lcd.fill(str(datetime.datetime.now())[:19], 0)
  ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

  getip = "IP: " + ip
  lcd.fill(getip, 1)
  
  return lcd

if __name__ == '__main__':
    lcd = LCD.find_or_die()
    lcd.info()
    try:
        main(lcd)
    except KeyboardInterrupt:
        pass