import os


def main():
    cfg = {k: v for k, v in os.environ.items()}
    print(f"loaded {len(cfg)} settings")


if __name__ == "__main__":
    main()
