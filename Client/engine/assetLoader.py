from pathlib import Path

def getAsset(nameOfAsset: str):
    return Path(__file__).resolve().parent.parent / "assets" / nameOfAsset 