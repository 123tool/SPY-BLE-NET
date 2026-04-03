# 🐉 SPY-BLE-NET (NAGA-HITAM)
> **Advanced BLE Mesh Botnet & Signal Injection Framework**

![License](https://img.shields.io/badge/License-GPLv3-red.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Termux%20(Root)%20%7C%20Linux-orange.svg)

**SPY-BLE-NET** adalah framework audit keamanan Bluetooth Low Energy (BLE) yang dirancang untuk mensimulasikan penyebaran Botnet melalui jaringan Mesh. Tool ini mampu melakukan *Deauth*, *Jamming*, dan *Spamming* secara massal ke semua perangkat BLE yang tertangkap oleh sensor.

### 💀 Fitur Ganas (NAGA-HITAM Edition)
- **Zero-Touch Infection:** Secara otomatis mencari dan mengirim perintah ke node terdekat.
- **Turbo Jamming:** Injeksi paket sampah (junk data) ke handle karakteristik secara berkelanjutan.
- **Mesh Command Propagation:** Perintah yang dikirim ke satu Bot akan diteruskan ke Bot lain (Chaining).
- **Multi-Vector Attack:** Mendukung L2Ping Flooding, RFCOMM Hijacking, dan Advertisement Spamming.

## 🛠️ Instalasi

### 💻 Linux / Raspberry Pi
```bash
sudo apt update && sudo apt install -y bluez hcitool python3-pip
sudo pip3 install bluepy
git clone [https://github.com/SPY-E/spy-ble-net.git](https://github.com/SPY-E/spy-ble-net.git)
cd spy-ble-net
sudo python3 spy_master.py
```
### Termux (Root Required)
```bash
pkg install python bluez tsu -y
pip install bluepy
git clone [https://github.com/SPY-E/spy-ble-net.git](https://github.com/SPY-E/spy-ble-net.git)
cd spy-ble-net
sudo python3 spy_master.py
```
### 🚀 Cara Penggunaan
​Jalankan Master: sudo python3 spy_master.py
​Pilih Mode "Become Bot" pada perangkat pendukung untuk memperluas jangkauan.
​Gunakan "Broadcast Command" untuk memerintah semua node melakukan Jamming massal.
​⚠️ Disclaimer
​Hanya untuk tujuan Edukasi dan Audit Penetrasi Resmi. Penggunaan tanpa izin pada perangkat publik adalah tindakan ilegal. SPY-E & 123Tool tidak bertanggung jawab atas kerusakan infrastruktur yang diakibatkan oleh tool ini.
