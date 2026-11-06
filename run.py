import os
import sys
import time
import socket
import subprocess

def is_port_in_use(port: int, host: str = "127.0.0.1") -> bool:
    """ກວດສອບວ່າ Port ນີ້ຖືກເປີດໃຊ້ງານແລ້ວຫຼືບໍ່"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((host, port)) == 0

def kill_process_tree(pid: int):
    """ປິດ process ແລະ child processes ທັງໝົດ (ຮອງຮັບ Windows)"""
    if sys.platform == "win32":
        try:
            subprocess.call(
                ["taskkill", "/F", "/T", "/PID", str(pid)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception:
            pass
    else:
        try:
            os.kill(pid, 9)
        except Exception:
            pass

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(root_dir, "backend")
    frontend_dir = os.path.join(root_dir, "frontend")

    print("=" * 60)
    print("      🚀 J&P AUTO - CAR MANAGEMENT SYSTEM LAUNCHER")
    print("=" * 60)
    print("ກຳລັງກວດສອບ ແລະ ເລີ່ມຕົ້ນລະບົບ...\n")

    # 1. Start Backend (FastAPI / Uvicorn)
    print("[1/2] 🔄 ກຳລັງເປີດ Backend API (FastAPI)...")
    backend_cmd = [
        sys.executable, "-m", "uvicorn", "main:app",
        "--host", "127.0.0.1",
        "--port", "8000",
        "--reload"
    ]
    
    backend_proc = subprocess.Popen(
        backend_cmd,
        cwd=backend_dir
    )

    # ລໍຖ້າ Backend ເປີດ port 8000
    print("      ລໍຖ້າ Backend ເຊື່ອມຕໍ່...", end="", flush=True)
    backend_ready = False
    for _ in range(20):
        # ກວດສອບວ່າ Backend crash ຫຼື ຢຸດເຮັດວຽກກ່ອນຫຼືບໍ່
        if backend_proc.poll() is not None:
            print("\n\n❌ [ERROR] Backend ຢຸດການເຮັດວຽກກະທັນຫັນ! ກະລຸນາກວດສອບ Error ດ້ານເທິງ.")
            backend_ready = False
            break

        if is_port_in_use(8000):
            backend_ready = True
            break
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    if backend_ready:
        print("      ✅ Backend ພ້ອມໃຊ້ງານແລ້ວທີ່: http://127.0.0.1:8000\n")
    else:
        print("⚠️ Backend ບໍ່ສາມາດເລີ່ມຕົ້ນໄດ້. ຈະຍົກເລີກການເປີດ Frontend.")
        kill_process_tree(backend_proc.pid)
        input("\nກົດ Enter ເພື່ອອອກ...")
        return

    # 2. Start Frontend (Flet)
    print("[2/2] 💻 ກຳລັງເປີດ Frontend (Flet UI)...")
    frontend_cmd = [sys.executable, "main.py"]

    try:
        frontend_proc = subprocess.run(frontend_cmd, cwd=frontend_dir)
    except KeyboardInterrupt:
        print("\n\n⚠️ ໄດ້ຮັບຄຳສັ່ງຢຸດການເຮັດວຽກ (Ctrl+C)...")
    finally:
        print("\n🛑 ກຳລັງປິດ Backend API...")
        kill_process_tree(backend_proc.pid)
        print("✅ ປິດລະບົບຮຽບຮ້ອຍແລ້ວ.")

if __name__ == "__main__":
    main()

