MODEL_CATALOG = [
    {
        "name": "LLaMA-3 8B",
        "category": ["generic", "overall"],
        "min_ram": 12,
        "min_vram": 0,
        "quantized": True,
        "backend": ["llama.cpp", "ollama"],
        "quality": 8
    },
    {
        "name": "DeepSeek-Coder 6.7B",
        "category": ["coding"],
        "min_ram": 14,
        "min_vram": 0,
        "quantized": True,
        "backend": ["llama.cpp"],
        "quality": 9
    },
    {
        "name": "Stable Diffusion 1.5",
        "category": ["image"],
        "min_ram": 8,
        "min_vram": 4,
        "backend": ["diffusers", "automatic1111"],
        "quality": 7
    },
    {
        "name": "SDXL",
        "category": ["image"],
        "min_ram": 16,
        "min_vram": 8,
        "backend": ["diffusers"],
        "quality": 9
    },
    {
        "name": "Stable Video Diffusion",
        "category": ["video"],
        "min_ram": 32,
        "min_vram": 12,
        "backend": ["diffusers"],
        "quality": 6
    }
]
