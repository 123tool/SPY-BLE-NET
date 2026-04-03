#!/bin/bash
# SPY-BLE-NET Auto Installer
# 123Tool Premium Security

echo "[*] Installing Dependencies..."
if [[ -d /data/data/com.termux ]]; then
    pkg update && pkg upgrade -y
    pkg install python bluez tsu libpcap-dev -y
    pip install bluepy
else
    sudo apt update
    sudo apt install -y python3-pip bluez hcitool libpcap-dev
    sudo pip3 install bluepy
fi

chmod +x *.py
echo "[+] Done. Jalankan: sudo python3 spy_master.py"
