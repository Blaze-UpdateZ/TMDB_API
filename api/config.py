import os

# --- TMDB Configuration ---

# Security tip: Set TMDB_BEARER_TOKEN in your environment variables.
# Get your Bearer Token here: https://www.themoviedb.org/settings/api
TMDB_BEARER_TOKEN = os.environ.get("TMDB_BEARER_TOKEN", "REPLACE_WITH_YOUR_ACTUAL_TOKEN")

TMDB_BASE_URL = 'https://api.themoviedb.org/3'
TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/original'

# Filtering logic
MIN_RUNTIME = 40

# Server configuration
PORT = 5000
HOST = '0.0.0.0'
DEBUG = True
