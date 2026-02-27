import os
import sys
import json
import requests
from dotenv import load_dotenv

from api.config import TMDB_BEARER_TOKEN, TMDB_BASE_URL

HEADERS = {
    'Authorization': f'Bearer {TMDB_BEARER_TOKEN}',
    'Content-Type': 'application/json;charset=utf-8'
}
URL = f"{TMDB_BASE_URL}/search/multi"

def search(query):
    print(f"\n--- Results for query: '{query}' ---")
    params = {'query': query, 'language': 'en-US', 'page': 1, 'include_adult': False}
    try:
        resp = requests.get(URL, params=params, headers=HEADERS)
        resp.raise_for_status()
        results = resp.json().get('results', [])
        print(f"Total results on page 1: {len(results)}")
        for r in results:
            title = r.get('title') or r.get('name')
            rid = r.get('id')
            mtype = r.get('media_type')
            date = r.get('release_date') or r.get('first_air_date')
            print(f"[{mtype}] {title} ({date}) [ID: {rid}]")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search("your name")
    search("your name.")
    search("Your Name")


