# checker.py
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict

def check_url(url: str, timeout: float = 5.0) -> Dict:
    try:
        r = requests.get(url, timeout=timeout)
        return {"url": url, "status": r.status_code, "ok": r.ok}
    except Exception as e:
        return {"url": url, "status": None, "error": str(e), "ok": False}

def bulk_check(urls: List[str], workers: int = 10):
    results = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for res in ex.map(check_url, urls):
            results.append(res)
    return results

if __name__ == "__main__":
    urls = ["https://google.com","https://example.com"]
    import json
    print(json.dumps(bulk_check(urls), indent=2))
