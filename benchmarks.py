def score_model(model, system, mode):
    ram_factor = min(system["ram_gb"] / model["min_ram"], 1.5)

    # VRAM factor
    if model.get("min_vram", 0) > 0:
        vram_factor = min(system["max_vram"] / model["min_vram"], 1.5)
    else:
        vram_factor = 1

    # Acceleration bonus
    accel_bonus = 1.0
    if system["acceleration"].get("cuda"):
        accel_bonus = 1.2
    elif system["acceleration"].get("metal"):
        accel_bonus = 1.1

    # Safe defaults
    quality = model.get("quality", 5)
    speed = model.get("speed", quality * 0.6)

    # Mode-based scoring
    if mode == "fast":
        base = speed
    elif mode == "quality":
        base = quality
    else:
        base = (speed + quality) / 2

    return round(base * ram_factor * vram_factor * accel_bonus, 2)
