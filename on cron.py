# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:45:09 2022

@author: Vivek's MI Book
"""
import requests
import datetime
import broadlink
global data
now=datetime.datetime.now()
time=str(now.hour+1)+":00"
date=now.strftime("%d-%m-%Y")
req=requests.get("https://script.google.com/macros/s/AKfycbxpzgzm0k_q20Sh7K087dEeTMrQY_t07oPKmj6U3PSliOJQVJ2UIa2ZIZmw6n-mWWs/exec?time="+str(time)+"&date="+str(date)+"&func=on_off&CR=CR 3")
print(req.text)
if req.text=="on":
    on=[b"&\x00\x16\x01f5\x0f'\x0c)\x0e\r\x0e\r\x0c\x0e\x0c*\r\x0e\x0c\x0e\x0c)\x0e'\r\x0e\x0f'\x0c\x0e\x0c\x0f\x0e'\r(\x0e\r\x0f&\r)\r\x0e\x0c\x0e\x0c)\x0e\r\r\r\r)\x0e\r\x0c\x0e\x0c\x0f\x0f\x0c\x0f&\x0c\x0f\x0e\x0c\x0f\x0c\r\r\r\x0e\x0f\x0c\x0f\x0c\x0c\x0e\x0c\x0f\x0f\x0c\x0f\x0c\x0c\x0e\x0c\x0f\x0e\x0c\x0f\x0c\r\r\r)\r\x0e\x0c)\x10\x0b\x0f\x0c\x0c\x0e\x0c)\x0f&\r)\x0e\r\x0c)\x0e\r\x0e'\x0c\x0e\x0f'\x0c)\x0f\x0c\x0f\x0c\x0c\x0e\x0c\x0f\x0e'\r\x0e\x0c\x0e\x0f\x0c\x0f\x0c\r\r\r\x0e\x0f\x0c\x0f\x0c\x0c\x0e\x0c\x0f\x0e\r\x0e\x0c\r\r\r\x0e\x0f\x0c\x0f\x0c\x0c\x0e\x0c\x0f\x0f\x0c\x0f\x0c\x0c\x0e\x0c)\x0e(\x0c)\x0e'\x0c*\r(\x0c\x0f\x0e'\r\r\r)\r(\x0c*\r\x0e\x0c\x0e\x0c\x0e\x0e(\r\r\r)\r\x0e\x0c)\r\x0e\r\x0e\x0c(\x0e(\x0c)\x0e(\x0c\x0e\x0c*\r(\x0c)\x0e'\r)\r(\x0c*\r(\x0c)\x0e'\r)\r(\x0c)\x0e'\r)\x0e'\x0c*\r(\x0c)\x0e'\r)\r\x00\r\x05",'23 C fan-:3']
    #data=b'&\x00\xe6\x00z0\x11)\x11)\x11\x11\x11\x11\x11\x11\x11)\x11\x11\x11\x11\x12(\x12(\x12\x10\x12(\x12\x10\x12\x10\x12)\x11)\x11\x11\x11)\x11)\x11\x11\x11\x11\x11)\x11\x11\x11\x11\x11)\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x12\x10\x12\x10\x12\x10\x12\x10\x12\x10\x12\x10\x12\x10\x12\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11)\x11\x11\x11\x11\x11)\x11)\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x12(\x12(\x12\x10\x12\x10\x12\x10\x12\x10\x12\x10\x12\x10\x12\x10\x12)\x11\x10\x12(\x12(\x12(\x12\x10\x12\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11)\x11)\x11)\x11)\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11)\x11\x11\x11\x11\x11\x11\x11\x11\x12\x10\x12\x10\x12\x10\x12\x10\x12(\x12\x10\x12\x10\x12\x10\x12(\x12\x00\r\x05'
    devices = broadlink.hello(timeout=5)
    devices[0].auth()
    devices[0].send_data(on)

