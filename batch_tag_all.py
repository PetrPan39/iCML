from pathlib import Path
from datetime import datetime
import hashlib
import socket
from cml_s_storage import log_activation

DRIVES = ["C:/", "D:/", "E:/", "F:/", "I:/"]
DEVICE_ID = socket.gethostname()
LOCATION = "81.2.69.160"

def calc_hash(filepath):
    h = hashlib.md5()
    with open(filepath, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def process_folder(folder):
    print(f"[CML_S] Skenuji {folder} ...")
    for f in Path(folder).rglob("*.*"):
        if f.is_file() and f.stat().st_size < 5e6:  # max 5 MB
            try:
                file_hash = calc_hash(f)
                log_activation(
                    file_hash=file_hash,
                    file_name=f.name,
                    device_id=DEVICE_ID,
                    location=LOCATION,
                    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    event_type="batch",
                    notes=f"Hromadné značení z {folder}"
                )
                print(f"  ✅ {f}")
            except Exception as e:
                print(f"  ⚠️ Chyba u {f.name}: {e}")

def main():
    for drive in DRIVES:
        try:
            process_folder(drive)
        except Exception as e:
            print(f"[chyba]: {e}")

if __name__ == "__main__":
    main()
