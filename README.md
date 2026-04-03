# 🐉 SPY BLE NET
> **Advanced BLE Mesh Botnet & Signal Injection Framework**

![License](https://img.shields.io/badge/License-GPLv3-red.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Termux%20(Root)%20%7C%20Linux-orange.svg)

**SPY BLE NET**

framework audit keamanan Bluetooth Low Energy (BLE) yang dirancang untuk mensimulasikan penyebaran Botnet melalui jaringan Mesh. Tool ini mampu melakukan *Deauth*, *Jamming*, dan *Spamming* secara massal ke semua perangkat BLE yang tertangkap oleh sensor.

### 💀 Fitur

- **Zero-Touch Infection:** Secara otomatis mencari dan mengirim perintah ke node terdekat.
- **Turbo Jamming:** Injeksi paket sampah (junk data) ke handle karakteristik secara berkelanjutan.
- **Mesh Command Propagation:** Perintah yang dikirim ke satu Bot akan diteruskan ke Bot lain (Chaining).
- **Multi-Vector Attack:** Mendukung L2Ping Flooding, RFCOMM Hijacking, dan Advertisement Spamming.

## 🛠️ Instalasi

### 💻 Linux / Raspberry Pi
```bash
sudo apt update && sudo apt install -y bluez hcitool python3-pip
sudo pip3 install bluepy
git clone https://github.com/123tool/SPY-BLE-NET.git
cd SPY-BLE-NET
sudo python3 spy_master.py
```
### Termux (Root Required)
```bash
pkg install python bluez tsu -y
pip install bluepy
git clone https://github.com/123tool/SPY-BLE-NET.git
cd SPY-BLE-NET
sudo python3 spy_master.py
```
### 🚀 Cara Penggunaan

​Jalankan Master :
```bash
sudo python3 spy_master.py
​Pilih Mode "Become Bot" pada perangkat pendukung untuk memperluas jangkauan.
​Gunakan "Broadcast Command" untuk memerintah semua node melakukan Jamming massal.
```
### Analysis (Differentiator):

**​Multi-Handle Jamming** : 
```bash
Code only targets one handle. My code uses random.choice to target multiple handles at once (0x000b, 0x000c). This is more damaging because we don't know which handle controls which vital device function.​Junk 
```
**Data Injection** :
```bash
Using os.urandom(100), which sends purely random characters that are very difficult for the target device's buffer to process, triggers a memory overflow on the BLE module.​HCI
```
**Hard Reset** :
```bash
Every time a scan or mass attack is performed, the script automatically resets hciconfig hci0 in the background to ensure our Bluetooth adapter doesn't crash due to too many simultaneous connections.
```

​## ⚠️ Disclaimer

**​Hanya untuk tujuan Edukasi dan Audit Penetrasi Resmi. Penggunaan tanpa izin pada perangkat publik adalah tindakan ilegal. SPY-E & 123Tool tidak bertanggung jawab atas kerusakan infrastruktur yang diakibatkan oleh tool ini.**
