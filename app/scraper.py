import json

def scrape_jobs():
    # Dummy data for demo. Replace with real scraping logic.
    jobs = [
        {"id": 1, "title": "Data Scientist", "skills": ["python", "machine learning", "statistics"], "url": "https://example.com/job1"},
        {"id": 2, "title": "Frontend Developer", "skills": ["javascript", "react", "css"], "url": "https://example.com/job2"},
    ]
    with open("app/data/jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

def scrape_courses():
    # Dummy data for demo. Replace with real scraping logic.
    courses = [
        {"id": 1, "title": "Machine Learning Bootcamp", "skills": ["machine learning", "python"], "url": "https://example.com/course1"},
        {"id": 2, "title": "Modern React", "skills": ["react", "javascript"], "url": "https://example.com/course2"},
    ]
    with open("app/data/courses.json", "w") as f:
        json.dump(courses, f, indent=2)
