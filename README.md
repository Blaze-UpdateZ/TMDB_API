# 🎬 TMDB Movie Details API

A professional Python-based API for fetching comprehensive movie and TV show metadata, including high-resolution posters and backdrops, powered by The Movie Database (TMDB).

---

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
  - [Installation](#installation)
  - [Running Locally](#running-locally)
- [API Usage](#-api-usage)
  - [Search Movie Posters](#search-movie-posters)
- [Deployment](#-deployment)
  - [Vercel](#vercel)
- [Configuration](#-configuration)
- [Credits](#-credits)
- [License](#-license)

---

## ✨ Features

- **Multi-Source Search**: Intelligent search for movies and TV shows with fuzzy matching.
- **Deep Metadata**: Fetches credits, certificates, runtimes, and box office data.
- **Image Intelligence**: Categorizes posters and backdrops by language.
- **Deployment Ready**: Optimized for Vercel and other serverless environments.
- **Centralized Configuration**: easy management of API keys and server settings.

## 🚀 Quick Start

### Installation

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/Blaze-UpdateZ/tmdb_api.git
    cd tmdb_api
    ```

2.  **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables**:
    Create a `.env` file or export your TMDB token. You can obtain your **API Read Access Token (Bearer)** from the [TMDB API Settings](https://www.themoviedb.org/settings/api) page.
    ```bash
    export TMDB_BEARER_TOKEN="your_token_here"
    ```

### Running Locally

```bash
python api/movie_posters.py
```

The API will be available at `http://localhost:5000`.

## 🛠 API Usage

### Search Movie Posters

**Endpoint**: `GET /api/movie-posters`

**Parameters**:

- `query` (required): The name of the movie or TV show (e.g., `Inception 2010`).
- `api_key` (optional): Override the default TMDB API key.

**Example**:

```bash
curl "http://localhost:5000/api/movie-posters?query=Inception"
```

## 🌐 Deployment

### Vercel

This project is configured for seamless deployment on Vercel:

1.  Push your code to GitHub.
2.  Import the project into Vercel.
3.  Add the `TMDB_BEARER_TOKEN` as an Environment Variable in the Vercel dashboard.
4.  Deploy!

## 📝 Configuration

All settings are managed in `api/config.py`.

| Variable            | Description                                         |
| :------------------ | :-------------------------------------------------- |
| `TMDB_BEARER_TOKEN` | Your TMDB Read Access Token (Bearer)                |
| `MIN_RUNTIME`       | Minimum runtime to filter out shorts (default: 40m) |
| `PORT`              | Local server port (default: 5000)                   |
| `HOST`              | Local server host (default: 0.0.0.0)                |

## 🤝 Credits

- **Powered by**: [@Blaze_Updatez](https://t.me/Blaze_Updatez)
- **Created by**: [@Bharath_boy](https://t.me/Bharath_boy)


---

_Disclaimer: This project is for educational purposes only. This product uses the TMDB API but is not endorsed or certified by TMDB._
