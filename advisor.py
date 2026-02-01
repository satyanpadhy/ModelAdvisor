from model_catalog import MODEL_CATALOG
from benchmarks import score_model




def recommend(system, category, mode, backend):
    results = []

    for model in MODEL_CATALOG:
        if category not in model["category"]:
            continue
        if backend != "any" and model["backend"] != backend:
            continue
        if system["ram_gb"] < model["min_ram"]:
            continue
        if system["max_vram"] < model.get("min_vram", 0):
            continue

        score = score_model(model, system, mode)

        results.append({
            **model,
            "score": score
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)
