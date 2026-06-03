# URxFF Extreme Sensi Engine

FFsensi is an advanced Free Fire Sensitivity Generator designed to create optimized sensitivity settings based on your device's real performance. Instead of using random sensitivity values from YouTube videos or websites, FFsensi analyzes your device specifications and performs live performance benchmarking to generate the most suitable sensitivity for your phone.

The tool evaluates multiple factors including CPU performance, RAM speed, refresh rate, touch response, battery status, system load, and overall device power to calculate accurate sensitivity values. This helps players achieve smoother gameplay, improved drag control, better recoil management, and a more consistent headshot experience.

Whether you're using a budget device or a flagship smartphone, FFsensi automatically adapts the generated sensitivity according to your hardware capabilities, providing a personalized sensitivity profile for every user.

### ✨ Key Highlights

* 📱 Real Device Detection
* ⚡ Live CPU & RAM Benchmarking
* 🎯 Headshot Optimized Sensitivity
* 📊 Performance Based Calculations
* 📄 TXT & JSON Output Files
* 🚀 Quick Scan & Full Scan Modes
* 🛠 Performance Boost Script Generation
* 📲 Android & Termux Compatible

Simply run the tool, wait for the scan to complete, and apply the generated sensitivity values inside Free Fire.

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white">

<img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white">

<img src="https://img.shields.io/badge/Termux-000000?style=for-the-badge&logo=termux&logoColor=white">

<img src="https://img.shields.io/badge/Free_Fire-FF6A00?style=for-the-badge&logoColor=white">

</p>

# 📹 Tutorial Video

Watch the complete setup and usage tutorial before running the tool.

<p align="center">

<a href="https://youtu.be/TG4_HVtQ7jo">
<img src="https://img.shields.io/badge/▶️%20WATCH%20TUTORIAL%20ON%20YOUTUBE-FF0000?style=for-the-badge&logo=youtube&logoColor=white">
</a>

</p>

---



# 📥 Installation

### Download Required Files

<p align="center">
  <a href="https://f-droid.org/repo/com.termux_118.apk">
    <img src="https://img.shields.io/badge/📱%20Download%20Termux-32CD32?style=for-the-badge">
  </a>

  <a href="https://github.com/ashishyadav210/FFsensi/archive/refs/heads/main.zip">
    <img src="https://img.shields.io/badge/📦%20Download%20FFsensi%20ZIP-1E90FF?style=for-the-badge">
  </a>
</p>

---

### Setup Termux (method 1)

Run the following commands:

```bash
termux-change-repo
pkg update && pkg upgrade -y
pkg install python
termux-setup-storage
```
Allow Storage Permission 
---

### Open FFsensi Folder

```bash
cd storage/shared/Download/FFsensi-main
```

---

### Run FFsensi

```bash
python3 z_run.py
```

---
# Method 2 (Easy)

Run the following commands:

```bash
pkg install git
pkg install python
git clone https://github.com/ashishyadav210/FFsensi.git
cd FFsensi
python z_run.py
```

# 📂 File Structure

```text
FFsensi/
│
├── README.md
│
├── z_run.py
│   └── Main launcher file
│
├── i0x.sh
│   └── Auto install & run script
│
├── x9k/
│   │
│   ├── m7q.py
│   │   └── Device Detection Engine
│   │
│   ├── p4r.py
│   │   └── Benchmark & Performance Engine
│   │
│   ├── s2k.py
│   │   └── Sensitivity Generator
│   │
│   ├── t8n.py
│   │   └── Boost Script Generator
│   │
│   ├── v1u.py
│   │   └── Terminal UI & Colors
│   │
│   └── d8f.json
│       └── Device Tier Database
│
└── o0x/
    │
    ├── x_device.txt
    │   └── Generated Sensitivity
    │
    ├── x_device.json
    │   └── Detailed Scan Report
    │
    ├── b0x.sh
    │   └── Performance Boost Script
    │
    └── g0x.sh
        └── Game Optimization Script
```

---
## 🚀 Available Commands

| Command                            | Description                             |
| ---------------------------------- | --------------------------------------- |
| `python3 z_run.py`                 | Full Device Scan & Generate Sensitivity |
| `python3 z_run.py --q`             | Quick Scan Mode                         |
| `python3 z_run.py --i`             | Show Device Information                 |
| `python3 z_run.py --qp`            | Generate Performance Scripts            |
| `python3 z_run.py --rn 5`          | Run Benchmark 5 Times                   |
| `python3 z_run.py --rn 10`         | Run Benchmark 10 Times                  |
| `python3 z_run.py --m DEVICE_NAME` | Manual Device Name                      |
| `bash i0x.sh`                      | Auto Setup & Run FFsensi                |

---

## 🌐 Follow Us





<p align="center">

<a href="https://t.me/Unknown_Reason">
<img src="https://img.shields.io/badge/@Unknown__Reason-Telegram-blue?style=flat-square&logo=telegram">
</a>

<a href="https://youtube.com/@Unknown_Reason">
<img src="https://img.shields.io/badge/@Unknown__Reason-YouTube-red?style=flat-square&logo=youtube">
</a>

<a href="https://instagram.com/6_hf0">
<img src="https://img.shields.io/badge/@6__hf0-Instagram-purple?style=flat-square&logo=instagram">
</a>

</p>

### 📢 Stay Connected

* 💬 Telegram Community Updates
* 🎥 Tutorial Videos & Guides
* 📸 Project Updates & Sneak Peeks
* 🚀 New Releases & Features
* 🔥 Free Fire Related Tools & Resources

> Follow all social platforms to get the latest updates, tutorials and project releases.
> 

---

## ❤️ Special Thanks

<p align="center">

<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width="180">

</p>

<p align="center">

# 🌟 Sandesh

### Project Developer & Maintainer

<a href="https://t.me/ZenDesh">
<img src="https://img.shields.io/badge/💙%20Telegram-@ZenDesh-229ED9?style=for-the-badge&logo=telegram&logoColor=white">
</a>

</p>

> Huge thanks to **Sandesh** for developing, maintaining and continuously improving this project. Your dedication, hard work and countless hours of development made FFsensi possible. 💙

---



---

<p align="center">

<b>Made with ❤️ for the Free Fire Community</b>

</p>
