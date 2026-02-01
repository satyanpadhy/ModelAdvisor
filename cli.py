import argparse
from system_probe import get_system_info
from advisor import recommend

def main():
    parser = argparse.ArgumentParser(
        description="Local AI Model Advisor"
    )

    parser.add_argument(
        "--category",
        choices=["coding", "generic", "image", "video", "overall"],
        default="overall"
    )

    parser.add_argument(
        "--mode",
        choices=["fast", "balanced", "quality"],
        default="balanced"
    )

    parser.add_argument(
        "--backend",
        choices=["ollama", "diffusers", "any"],
        default="any"
    )

    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    system = get_system_info()
    results = recommend(system, args.category, args.mode, args.backend)

    if args.json:
        import json
        print(json.dumps(results, indent=2))
    else:
        print_results(system, results)


def print_results(system, results):
    print("\nSYSTEM")
    print(f"RAM: {system['ram_gb']} GB")
    print(f"GPUs: {system['gpus']}")
    print(f"Acceleration: {system['acceleration']}\n")

    for r in results:
        print(f"✅ {r['name']}")
        print(f"   Backend: {r['backend']}")
        print(f"   Score: {r['score']}")
        if "run_cmd" in r:
            print(f"   Run: {r['run_cmd']}")
        else:
            if r["backend"] == "ollama":
                print(f"   Run: ollama run {r['name']}")
            elif r["backend"] == "diffusers":
                print("   Run: python -m diffusers (see docs)")
            else:
                print("   Run: see backend documentation")

        print()



if __name__ == "__main__":
    main()
