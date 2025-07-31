# AI-Powered Job/Course Recommender System

This project scrapes job and course data, vectorizes skills using state-of-the-art embeddings, and provides recommendations via a REST API.

## Features

- Scrapes job/course data (easily extendable for real sources)
- Embeds skill data using [sentence-transformers](https://www.sbert.net/)
- Fast recommendations via cosine similarity
- REST API endpoints for recommendations and data refresh

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Ahmad-Khalil-LEEA/job-course-recommender.git
cd job-course-recommender
```

### Build & Run with Docker

```bash
docker build -t recommender .
docker run -p 8000:8000 recommender
```

### API Usage

- `GET /recommend/jobs?skills=python&skills=machine learning`
- `GET /recommend/courses?skills=react&skills=javascript`
- `POST /scrape/jobs` — Trigger (re-)scraping of jobs
- `POST /scrape/courses` — Trigger (re-)scraping of courses

### Local Development

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Extending

- Add real scraping logic in `app/scraper.py`
- Extend data model as needed
- Replace or fine-tune the embedding model in `app/embeddings.py`

---

**License:** MIT
