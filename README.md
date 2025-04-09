<div align="center">

<h1>WIFISHOT</h1>

**Your Advanced Wi-Fi Security Auditing Toolkit.**

**Coded by Jcrist Orhen (jcrvnx)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![OS Compatibility](https://img.shields.io/badge/OS-Linux%20%7C%20UNIX-orange?style=for-the-badge&logo=linux)](https://www.kali.org/)

</div>

---

## ⚠️ WARNING & DISCLAIMER ⚠️

<div align="center">
<img src="https://raw.githubusercontent.com/jcrvnx/wifishot/main/assets/warning-pulse.gif" alt="Warning Animation" width="100px">
</div>

**WIFISHOT is intended STRICTLY for educational purposes and legal security testing scenarios where you have EXPLICIT PERMISSION to test the target network.**

Unauthorized access to computer systems and networks is **ILLEGAL** and **UNETHICAL**. The author, Jcrist Orhen (jcrvnx), is not responsible for any misuse or damage caused by this tool. **Use responsibly and ethically.**

> **Tampering Warning:**
> This code contains advanced countermeasures. Any unauthorized modifications, tampering, or reverse-engineering attempts will trigger built-in failsafes — rendering the code inoperable and permanently deleted. **Consider this your only warning.**

**By using WIFISHOT, you agree to these terms and take full responsibility for your actions.**

---

## 🚀 Features

<div align="center">
<img src="https://raw.githubusercontent.com/jcrvnx/wifishot/main/assets/features-spin.gif" alt="Features Animation" width="150px">
</div>

WIFISHOT provides a comprehensive, menu-driven interface for various Wi-Fi security tasks:

*   ✅ **Monitor Mode Management:** Easily start and stop monitor mode.
*   ✅ **Network Scanning:** Scan for available wireless networks.
*   ✅ **Targeted Scanning:** Focus scans on specific targets.
*   ✅ **WPS Scanning:** Specifically identify WPS-enabled networks.
*   ✅ **Handshake Capture:** Capture WPA/WPA2 handshakes.
*   ✅ **Automated Deauthentication:** Speed up handshake capture.
*   ✅ **Multiple Cracking Methods:** Wordlists (default/custom) & Crunch piping.
*   ✅ **WPS Attacks:** Leverage `reaver`, `bully`, `pixiewps`, `wifite`.
*   ✅ **Custom Wordlist Generation:** Create tailored wordlists via `crunch`.
*   ✅ **Wireless Tool Installer:** Quickly install supplementary tools.
*   ✅ **Dependency Management:** Auto-installs core tools (Debian/Ubuntu).

---

## 📋 Requirements

<div align="center">
<img src="https://raw.githubusercontent.com/jcrvnx/wifishot/main/assets/system-check.gif" alt="Requirements Animation" width="120px">
</div>

Before launching WIFISHOT, ensure you have:

1.  **OS:** Linux/UNIX (Kali, Parrot, Ubuntu recommended).
2.  **Privileges:** `root` or `sudo` access.
3.  **Wireless Adapter:** Monitor Mode & Packet Injection capable. (*Verify your hardware!*)
4.  **Python:** Python 3.x.
5.  **Core Dependencies:** `aircrack-ng`, `crunch`, `xterm`, `wordlists`, `reaver`, `pixiewps`, `bully`, `wifite` (Script attempts auto-install).

---

## 🛠️ Installation & Setup

<div align="center">
<img src="https://raw.githubusercontent.com/jcrvnx/wifishot/main/assets/terminal-typing.gif" alt="Installation Animation" width="200px">
</div>

1.  **Clone:**
    ```bash
    git clone https://github.com/jcrvnx/wifishot.git
    cd wifishot
    ```

2.  **Permissions (Optional):**
    ```bash
    chmod +x wifishot.py
    ```

3.  **Run as Root:**
    ```bash
    sudo python3 wifishot.py
    ```
    Follow on-screen prompts for dependency installation.

---

## ⚙️ How to Use

<div align="center">
<img src="https://raw.githubusercontent.com/jcrvnx/wifishot/main/assets/menu-nav.gif" alt="Usage Animation" width="180px">
</div>

1.  **Launch:** `sudo python3 wifishot.py`.
2.  **Main Menu:** Select options numerically.
3.  **Follow Prompts:** Enter required info (interfaces, BSSIDs, paths).
4.  **Monitor Mode:** Use options `(1)` & `(2)` to manage monitor mode.
5.  **Exit:** Use `(00)` or `CTRL+C` (interrupts current task).

---

## 📜 Menu Options Explained

| Option | Action                              | Description & Notes                                                                 |
| :----- | :---------------------------------- | :---------------------------------------------------------------------------------- |
| `1`    | Start Monitor Mode                | Puts interface into monitor mode via `airmon-ng`. Kills interfering processes.      |
| `2`    | Stop Monitor Mode                 | Stops monitor mode & restarts NetworkManager.                                       |
| `3`    | Scan Networks                     | General scan using `airodump-ng`. `CTRL+C` to stop.                                 |
| `4`    | Get Handshake                     | Captures WPA/WPA2 handshakes. Needs BSSID, Channel, Path. Optional deauth in `xterm`. |
| `5`    | Install Wireless Tools            | Sub-menu to install tools like Hashcat, John, hcxtools.                             |
| `6`    | Crack Handshake (rockyou.txt)     | Cracks `.cap` using `rockyou.txt`.                                                  |
| `7`    | Crack Handshake (Wordlist)        | Cracks using a custom wordlist.                                                     |
| `8`    | Crack Handshake (No Wordlist)     | Pipes `crunch` output to `aircrack-ng`. **Potentially VERY slow!**                  |
| `9`    | Create Wordlist (Crunch)          | Generates wordlist file using `crunch`.                                             |
| `10`   | WPS Network Attacks               | Sub-menu for WPS attacks (`reaver`, `bully`, etc.). Needs BSSID & monitor interface.  |
| `11`   | Scan for WPS Networks             | Uses `airodump-ng --wps` to find WPS networks.                                      |
| `0`    | About Me                          | Author info (jcrvnx) & contact details.                                             |
| `CTRL+C`   | Exit                              | Exits WIFISHOT.                                                                     |

---

## 🌱 Contributing

<div align="center">
<img src="https://raw.githubusercontent.com/jcrvnx/wifishot/main/assets/code-contribution.gif" alt="Contributing Animation" width="150px">
</div>

Found a bug? Have an idea? Open an **Issue** or submit a **Pull Request** on GitHub!

---

## 📄 License

This project is licensed under the **MIT License**. See `LICENSE` file.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 🌐 Connect With Me (jcrvnx)

<div align="center">

[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://facebook.com/jcrvnx)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com/jcrvnx)
[![Threads](https://img.shields.io/badge/Threads-black?style=for-the-badge&logo=threads&logoColor=white)](https://threads.net/@jcrvnx)
[![Twitter (X)](https://img.shields.io/badge/Twitter--X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://twitter.com/jcrvnx)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jcrvnx)
[![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?style=for-the-badge&logo=tiktok&logoColor=white)](https://tiktok.com/@jcrvnx)
[![Pinterest](https://img.shields.io/badge/Pinterest-%23E60023.svg?style=for-the-badge&logo=Pinterest&logoColor=white)](https://pinterest.com/jcrvnx)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/jcrvnx)

**Professional Inquiries:** `orhenjcrist@gmail.com` | `+63 962 797 2598`

</div>

---

## ❤️ Support the Project

<div align="center">
<img src="https://raw.githubusercontent.com/jcrvnx/wifishot/main/assets/heart-beat.gif" alt="Support Animation" width="100px">
</div>

If WIFISHOT helps you, consider supporting its development!

**[💖 Support the Project (Donate)](https://github.com/sponsors/jcrvnx)**

---

<div align="center">

**Remember: Hack Ethically & Unethically. Smoke some blunt, and enjoy the mothef******* show.**

<img src="https://raw.githubusercontent.com/jcrvnx/wifishot/main/assets/shield-pulse.gif" alt="Footer Animation" width="80px">

</div>
