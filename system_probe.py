import psutil
from backends import detect_acceleration
import subprocess

def get_system_info():
    info = {}
    info["ram_gb"] = round(psutil.virtual_memory().total / 1e9, 1)
    info["cpu_cores"] = psutil.cpu_count(logical=True)

    # GPU detection
    gpus = []
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=name,memory.total",
             "--format=csv,noheader,nounits"],
            encoding="utf-8"
        )
        for line in out.strip().split("\n"):
            name, mem = line.split(",")
            gpus.append({
                "name": name.strip(),
                "vram_gb": round(int(mem) / 1024, 1)
            })
    except Exception:
        pass

    info["gpus"] = gpus
    info["max_vram"] = max([g["vram_gb"] for g in gpus], default=0)
    info["acceleration"] = detect_acceleration()

    return info
