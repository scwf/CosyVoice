# CosyVoice/tools/download_models.py
from modelscope import snapshot_download

def main():
    models_to_download = [
        "iic/CosyVoice2-0.5B",
        "iic/CosyVoice-300M",
        "iic/CosyVoice-300M-SFT",
        "iic/CosyVoice-300M-Instruct",
        "iic/CosyVoice-ttsfrd",
    ]

    print("Starting download of specified models to ModelScope default cache directory...")

    for model_id in models_to_download:
        print(f"Downloading {model_id}...")
        snapshot_download(model_id) # local_dir 参数已被移除
        print(f"Finished downloading {model_id}.")

    print("All specified models downloaded successfully to ModelScope default cache directory.")

if __name__ == "__main__":
    main() 