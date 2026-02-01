import subprocess
import platform

def detect_cuda():
    try:
        subprocess.check_output(["nvidia-smi"])
        return True
    except Exception:
        return False

def detect_rocm():
    try:
        subprocess.check_output(["rocminfo"])
        return True
    except Exception:
        return False

def detect_metal():
    if platform.system() != "Darwin":
        return False
    try:
        out = subprocess.check_output(["system_profiler", "SPDisplaysDataType"])
        return b"Metal" in out
    except Exception:
        return False

def detect_acceleration():
    return {
        "cuda": detect_cuda(),
        "rocm": detect_rocm(),
        "metal": detect_metal()
    }
