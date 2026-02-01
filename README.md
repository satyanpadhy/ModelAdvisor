# Local AI Model Advisor

A small CLI tool that inspects the host system and recommends locally-usable AI models from a static catalog.

Quick summary
- Detects system resources (RAM, GPUs, VRAM, acceleration) via [`system_probe.get_system_info`](system_probe.py) — [system_probe.py](system_probe.py).
- Uses a static model inventory defined in [`model_catalog.MODEL_CATALOG`](model_catalog.py) — [model_catalog.py](model_catalog.py).
- Scores models using resource heuristics in [`benchmarks.score_model`](benchmarks.py) — [benchmarks.py](benchmarks.py).
- Assembles recommendations in [`advisor.recommend`](advisor.py) — [advisor.py](advisor.py).
- CLI entry point: [`cli.main`](cli.py) — [cli.py](cli.py).

Requirements
- Python 3.8+
- psutil (for RAM/cpu detection): install with:
  ```sh
  pip install psutil
  ```
- Optional system tools for improved detection:
  - `nvidia-smi` (NVIDIA GPU detection)
  - `rocminfo` (ROCm/AMD detection)
  - macOS: `system_profiler` for Metal detection

Installation
1. Clone or copy the repository files into a directory.
2. Install dependencies:
   ```sh
   pip install psutil
   ```

Usage
- Show recommendations (default):
  ```sh
  python cli.py
  ```
- Filter by category, mode, and backend:
  ```sh
  python cli.py --category generic --mode balanced --backend any
  ```
- Output JSON:
  ```sh
  python cli.py --json
  ```

How recommendations are computed
- System info is gathered by [`system_probe.get_system_info`](system_probe.py) which returns RAM, GPU list, max VRAM, CPU cores and acceleration flags.
- The static catalog [`model_catalog.MODEL_CATALOG`](model_catalog.py) contains model metadata: name, category, min RAM, min VRAM, backend, quality and speed.
- Each candidate model is filtered by category, backend, and minimum resource requirements.
- Remaining candidates are scored via [`benchmarks.score_model`](benchmarks.py) using RAM/VRAM factors and acceleration bonuses. Results are sorted in [`advisor.recommend`](advisor.py).

Project files (overview)
- [cli.py](cli.py) — CLI entry and output formatting. Symbol: [`cli.main`](cli.py)
- [system_probe.py](system_probe.py) — System inspection helpers. Symbol: [`system_probe.get_system_info`](system_probe.py)
- [backends.py](backends.py) — Hardware/backend detection helpers. Symbol: [`backends.detect_acceleration`](backends.py)
- [model_catalog.py](model_catalog.py) — Static model catalog. Symbol: [`model_catalog.MODEL_CATALOG`](model_catalog.py)
- [model_families.py](model_families.py) — Family metadata (currently unused). Symbol: [`model_families.MODEL_FAMILIES`](model_families.py)
- [benchmarks.py](benchmarks.py) — Scoring heuristics. Symbol: [`benchmarks.score_model`](benchmarks.py)
- [advisor.py](advisor.py) — Recommendation assembly. Symbol: [`advisor.recommend`](advisor.py)

Limitations
- The catalog is static: recommendations are limited to entries in [`model_catalog.MODEL_CATALOG`](model_catalog.py).
- No runtime availability checks for installed models or model artifacts.
- GPU detection is best-effort and relies on external tools (`nvidia-smi`, `rocminfo`, macOS system profiler).
- No tests included; scoring and filters can be tuned in [`benchmarks.score_model`](benchmarks.py) and [`advisor.recommend`](advisor.py).

