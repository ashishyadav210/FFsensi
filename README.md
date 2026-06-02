# URxFF Extreme Sensi Engine

**Made by @ZenDesh | Developer Sandesh & @URxFF team**



<p align="center">
  <a href="https://instagram.com/6_hf0">
    <img src="https://img.shields.io/badge/Instagram-@6_hf0-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
  </a>

  <a href="https://t.me/Unknown_Reason">
    <img src="https://img.shields.io/badge/Telegram-@Unknown_Reason-26A5E4?style=for-the-badge&logo=telegram&logoColor=white">
  </a>

  <a href="https://youtube.com/@Unknown_Reason">
    <img src="https://img.shields.io/badge/YouTube-@Unknown_Reason-FF0000?style=for-the-badge&logo=youtube&logoColor=white">
  </a>
</p>

Free Fire ke liye **real sensitivity**. Koi saved/random sensi nahi — tumhare phone ki **specs + live power test** se values aati hain, headshot / ADS ke liye tuned.

---

## Fayde (kya milega)

| Fayda | Detail |
|--------|--------|
| **Real sensi** | Phone model, RAM, screen, Hz, DPI, chipset + CPU/RAM/GFX benchmark se calculate |
| **Headshot mode (HS)** | Strong phone + kam touch latency par General / Red Dot thodi zyada aggressive |
| **ADS smooth ladder** | Red Dot → 2x → 4x → Sniper automatically step-down (recoil control) |
| **3-run average** | Ek baar ka glitch kam — 3 baar test karke average |
| **Power index** | Phone abhi kitna fast hai (0–100) — garmi / background apps ka effect dikhta hai |
| **Touch & gameplay probe** | Touch sampling, battery, system load check |
| **Phone boost scripts** | Optional: animations off, game mode, Free Fire performance boost (`b0x.sh`, `g0x.sh`) |
| **Output files** | `o0x/` me `.txt` (copy-paste) + `.json` (record) |

> **Legal & safe:** Game hack nahi. Files modify nahi hoti — sirf tum game settings me values daalte ho.

---

## Zaroori: phone par chalao

PC/laptop par test chalega lekin **asli specs + touch nahi padhenge**. Best result ke liye **Android phone + Termux** use karo.

---

## Install (Termux)

1. Play Store se **Termux** install karo  
2. Project folder phone me copy karo (USB / Telegram / Git)  
3. Termux me:
```termux-change-repo
pkg update && pkg upgrade -y
termux-setup-storage```

Open Folder Jis Folder Mein All Codes Hain
```cd /storage/shared/FFsensi```
Run 
```python z_run.py```

---

## Use kaise karein

### 1) Full scan (recommended)

Game **band** rakho, charging / cool phone better hai.

```bash
python z_run.py```

~8–10 second benchmark → screen par sensi → files `o0x/` me save.

### 2) Quick scan (kam time)

```bash
python z_run.py --q
```

### 3) Sirf phone info

```bash
python z_run.py --i
```

### 4) Phone boost scripts banao

```bash
python z_run.py --qp
```

Ye banata hai:

- `o0x/b0x.sh` — performance boost (animations, game mode, FF whitelist)  
- `o0x/g0x.sh` — background apps kill (pre-game)

**Boost apply** (root ya PC se ADB):

```bash
su -c 'sh o0x/b0x.sh'
```

Ya PC:

```bash
adb push o0x/b0x.sh /sdcard/
adb shell su -c 'sh /sdcard/b0x.sh'
```

Bina root ke kuch settings nahi lagengi — jo ho sake wo script try karti hai.

### 5) Zyada accurate benchmark (5 runs)

```bash
python z_run.py --rn 5
```

---

## Game me sensi lagana

1. Free Fire kholo → **Settings** → **Sensitivity**  
2. `o0x/x_<tumhara_phone>.txt` kholo (Files / Termux)  
3. Har line game me same number daalo:

| Output me | Game me |
|-----------|---------|
| General | General |
| Red Dot | Red Dot |
| 2x | 2x Scope |
| 4x | 4x Scope |
| Sniper | AWM / Sniper Scope |
| Free Look | Free Look |

4. **Training Ground** me 5–10 min test:
   - Aim zyada tez → sab values **−5**
   - Aim slow → sab values **+5**

---

## Output samajhna

| Line | Matlab |
|------|--------|
| `PWR xx/100` | Phone power score (benchmark) |
| `TIER` | budget / mid / upper_mid / flagship |
| `LAT` | Touch latency estimate (kam = better) |
| `HS_MODE ON` | Headshot tuning active (strong device) |
| `BOOST` | Boost readiness score |

---

## Project structure

```
freefire-sensi-pro/
  z_run.py      ← main command (yahi chalao)
  i0x.sh         ← Termux quick start
  x9k/          ← engine (internal)
  o0x/          ← tumhari sensi files + boost scripts (auto banenge)
  README.md     ← ye guide
```

---

## Tips

- Background apps band rakho scan se pehle  
- Battery 40%+ rakho  
- Game Turbo / Game Space me Free Fire ko **Performance** mode do  
- Har major update / naye phone par dubara scan chalao  
- Sensi **official Garena** nahi — smart baseline hai, thumb se ±5 fine-tune karo  

---

## Credits

**@ZenDesh | Developer Sandesh & @URxFF team**

## 🎥 Tutorial Video

[![Watch Tutorial](https://img.shields.io/badge/YouTube-Watch_Tutorial-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](YOUR_YOUTUBE_VIDEO_LINK)
