thonpython
def load_urls(filepath: str) -> list:
    urls = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            clean = line.strip()
            if clean:
                urls.append(clean)
    return urls