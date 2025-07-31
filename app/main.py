from fastapi import FastAPI, Query
from typing import List
from app.recommender import Recommender
from app.scraper import scrape_jobs, scrape_courses

app = FastAPI(title="AI Job/Course Recommender")

recommender = Recommender()

@app.on_event("startup")
def load_data():
    # Optionally, trigger scraping here or load existing data
    recommender.load_data()

@app.get("/recommend/jobs")
def recommend_jobs(skills: List[str] = Query(..., description="List of user's skills")):
    return recommender.recommend_jobs(skills)

@app.get("/recommend/courses")
def recommend_courses(skills: List[str] = Query(..., description="List of user's skills")):
    return recommender.recommend_courses(skills)

@app.post("/scrape/jobs")
def scrape_and_update_jobs():
    scrape_jobs()
    recommender.load_data()
    return {"status": "Jobs scraped and recommender updated."}

@app.post("/scrape/courses")
def scrape_and_update_courses():
    scrape_courses()
    recommender.load_data()
    return {"status": "Courses scraped and recommender updated."}
