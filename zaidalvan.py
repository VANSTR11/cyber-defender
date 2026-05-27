import os
import time
import platform

def banner():
    os.system('clear')
    print("\033[91m")
    print("""
 ███████╗ █████╗ ██╗██████╗ █████╗ ██╗ ██╗ ██╗ █████╗ ███╗ ██╗
 ╚══███╔╝██╔══██╗██║██╔══██╗██╔══██╗██║ ██║ ██║██╔══██╗████╗ ██║
   ███╔╝ ███████║██║██║ ██║███████║██║ ██║ ██║███████║██╔██╗ ██║
  ███╔╝ ██╔══██║██║██║ ██║██╔══██║██║ ╚██╗ ██╔╝██╔══██║██║╚██╗██║
 ███████╗██║ ██║██║██████╔╝██║ ██║███████╗ ╚████╔╝ ██║ ██║██║ ╚████║
 ╚══════╝╚═╝ ╚═╝╚═╝╚═════╝ ╚═╝╚══════╝ ╚═══╝ ╚═╝ ╚═╝╚═╝ ╚═══╝
    """)
    print("\033[93m Platform Belajar Cyber Security Lengkap untuk Pemula")
    print("\033[92m Untuk Tujuan Edukasi dan Etika Hacking")
    print("\033[96m Language: Indonesia | By: VANSTR11")
    print("\033[0m" + "="*65)

def pause():
    input("\n\033[93mTekan Enter untuk kembali ke menu...\033[0m")

def menu_utama():
    banner()
    print("\033[96m" + "MENU UTAMA ZAIDALVAN".center(65) + "\033[0m")
    print("="*65)
    print("""\033[92m
[1] Teori Dasar Cyber Security [10] Wireless Security - Teori
[2] Reconnaissance & Info Gathering [11] Forensik Digital - Pengenalan 
[3] Network Scanning - Konsep [12] Malware Analysis - Awareness
[4] Vulnerability Assessment [13] CTF & Tantangan Latihan
[5] Web Application Security [14] Tools & Cheatsheet Lengkap
[6] Kriptografi & Enkripsi [15] Laporan & Progress Belajar
[7] Password Security [16] Training Arena - Soal
[8] Social Engineering Awareness [17] Sistem Misi - Simulasi
[9] Network Security & Firewall 
\033[0m""")
    print("="*65)
    print("\033[91m[0] Keluar\033[0m")
    print("="*65)

# ISI MENU 1-17
def menu1():
    os.system('clear')
    print("\033[96m[1] TEORI DASAR CYBER SECURITY\033[0m\n")
    print("1. CIA Triad: Confidentiality, Integrity, Availability")
    print("2. White Hat = Hacker Baik, Black Hat = Kriminal")
    print("3. Golden Rule: Test hanya di lab/asset milik sendiri")
    print("4. 3 Pilar: People, Process, Technology")
    pause()

def menu2():
    os.system('clear')
    print("\033[96m[2] RECONNAISSANCE - TEORI\033[0m\n")
    print("Passive: Google Dorking, Whois, Cek Sosmed")
    print("Active: Ping, Traceroute - Butuh izin")
    print("Tool legal: whois domain.com, nslookup")
    print("\033[91mINGAT: Scan target orang tanpa izin = ILEGAL\033[0m")
    pause()

def menu3():
    os.system('clear')
    print("\033[96m[3] NETWORK SCANNING - KONSEP\033[0m\n")
    print("Tujuan: Cek port apa yang kebuka di server")
    print("Port umum: 80 HTTP, 443 HTTPS, 22 SSH")
    print("Simulasi aman: netstat -tuln di Termux lu sendiri")
    print("Tool nyata: Nmap - hanya untuk server sendiri")
    pause()

def menu4():
    os.system('clear')
    print("\033[96m[4] VULNERABILITY ASSESSMENT\033[0m\n")
    print("Cari kelemahan sistem. Contoh: Password lemah, Software jadul")
    print("Framework: OWASP Top 10 untuk Web")
    print("Penting: Wajib ada izin tertulis sebelum test")
    pause()

def menu5():
    os.system('clear')
    print("\033[96m[5] WEB APP SECURITY\033[0m\n")
    print("Kerentanan umum: SQL Injection, XSS, CSRF")
    print("Cara belajar: Pakai lab DVWA/Mutillidae di lokal")
    print("Defence: Validasi input, Update framework")
    pause()

def menu6():
    os.system('clear')
    print("\033[96m[6] KRIPTOGRAFI & ENKRIPSI\033[0m\n")
    print("Simetris: AES - 1 kunci buat enkrip & dekrip")
    print("Asimetris: RSA - Public & Private Key")
    print("Hash: MD5, SHA256 - Satu arah, buat cek integritas")
    os.system('echo "zaidalvan" | md5sum')
    pause()

def menu7():
    os.system('clear')
    print("\033[96m[7] PASSWORD SECURITY\033[0m\n")
    print("Ciri password kuat: 12+ karakter, Ada simbol, Gak pake tanggal lahir")
    print("Contoh generate aman:")
    os.system('openssl rand -base64 12')
    print("Tools: Bitwarden, 2FA wajib aktif")
    pause()

def menu8():
    os.system('clear')
    print("\033[96m[8] SOCIAL ENGINEERING AWARENESS\033[0m\n")
    print("Teknik: Phishing, Pretexting, Baiting")
    print("Ciri email phising: Link aneh, Maksa buru-buru, Typo")
    print("Defence: Jangan asal klik, Cek pengirim")
    pause()

def menu9():
    os.system('clear')
    print("\033[96m[9] NETWORK SECURITY & FIREWALL\033[0m\n")
    print("Firewall = Satpam jaringan. Blokir traffic jahat")
    print("Jenis: Network Firewall, Host Firewall")
    print("Cek firewall Android: Settings > Security")
    pause()

def menu10():
    os.system('clear')
    print("\033[96m[10] WIRELESS SECURITY\033[0m\n")
    print("WEP = Lemah, WPA2/WPA3 = Aman")
    print("Bahayanya WiFi publik: Sniffing, Evil Twin")
    print("Tips: Pake VPN, Matikan auto-connect")
    pause()

def menu11():
    os.system('clear')
    print("\033[96m[11] FORENSIK DIGITAL\033[0m\n")
    print("Tujuan: Cari bukti digital kasus kejahatan")
    print("Proses: Identifikasi > Preservasi > Analisis > Laporan")
    print("Tools: Autopsy, FTK - Dipake polisi/BSSN")
    pause()

def menu12():
    os.system('clear')
    print("\033[96m[12] MALWARE ANALYSIS - AWARENESS\033[0m\n")
    print("Jenis: Virus, Worm, Trojan, Ransomware")
    print("Ciri HP kena malware: Batre boros, Kuota jebol, Iklan aneh")
    print("Defence: Install dari Play Store aja, Update OS")
    pause()

def menu13():
    os.system('clear')
    print("\033[96m[13] CTF & TANTANGAN\033[0m\n")
    print("CTF = Capture The Flag. Lomba hacking legal")
    print("Platform latihan: picoCTF.org, TryHackMe.com")
    print("Tipe soal: Web, Crypto, Forensic, Reverse")
    pause()

def menu14():
    os.system('clear')
    print("\033[96m[14] TOOLS & CHEATSHEET\033[0m\n")
    print("Termux: nmap, sqlmap, metasploit - HANYA DI LAB")
    print("Web: VirusTotal.com, Censys.io, Exploit-DB")
    print("Belajar: Portswigger Academy, OWASP Cheat Sheet")
    pause()

def menu15():
    os.system('clear')
    print("\033[96m[15] LAPORAN & PROGRESS\033[0m\n")
    print("User: VANSTR11")
    print("Level: Newbie Ethical Hacker")
    print("EXP: 150/500")
    print("Misi Selesai: 3/17")
    print("Lanjut belajar biar naik level bro!")
    pause()

def menu16():
    os.system('clear')
    print("\033[96m[16] TRAINING ARENA\033[0m\n")
    print("Level: Newbie | Soal 1/3")
    jawab = input("Apa kepanjangan DDoS? ")
    if "distributed denial of service" in jawab.lower():
        print("\033[92mBenar! +50 EXP\033[0m")
    else:
        print("\033[91mSalah. Jawaban: Distributed Denial of Service\033[0m")
    pause()

def menu17():
    os.system('clear')
    print("\033[96m[17] SISTEM MISI - SIMULASI\033[0m\n")
    print("MISI 1: Cek IP Publik lu sendiri")
    print("Perintah: curl ifconfig.me")
    os.system('curl -s ifconfig.me')
    print("\n\033[92mMisi Selesai! Ini IP publik lu. Jangan sebarin ya.\033[0m")
    pause()

def main():
    while True:
        menu_utama()
        pilih = input("Pilih menu [0-17]: ")
        
        if pilih == "1": menu1()
        elif pilih == "2": menu2()
        elif pilih == "3": menu3()
        elif pilih == "4": menu4()
        elif pilih == "5": menu5()
        elif pilih == "6": menu6()
        elif pilih == "7": menu7()
        elif pilih == "8": menu8()
        elif pilih == "9": menu9()
        elif pilih == "10": menu10()
        elif pilih == "11": menu11()
        elif pilih == "12": menu12()
        elif pilih == "13": menu13()
        elif pilih == "14": menu14()
        elif pilih == "15": menu15()
        elif pilih == "16": menu16()
        elif pilih == "17": menu17()
        elif pilih == "0":
            print("\033[91mStay Ethical Hacker, Zaidalvan! Tools ini 100% edukasi.\033[0m")
            break
        else:
            print("\033[91mPilihan gak ada bro\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    main()
