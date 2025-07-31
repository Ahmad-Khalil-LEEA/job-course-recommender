import json
import numpy as np
from app.embeddings import get_embedding_model

class Recommender:
    def __init__(self):
        self.model = get_embedding_model()
        self.jobs = []
        self.courses = []
        self.job_vectors = None
        self.course_vectors = None

    def load_data(self):
        with open("app/data/jobs.json", "r") as f:
            self.jobs = json.load(f)
        with open("app/data/courses.json", "r") as f:
            self.courses = json.load(f)
        self.job_vectors = self._vectorize([j["skills"] for j in self.jobs])
        self.course_vectors = self._vectorize([c["skills"] for c in self.courses])

    def _vectorize(self, skills_list):
        # Each element is a list of skills, join them
        texts = [" ".join(skills) for skills in skills_list]
        return self.model.encode(texts, convert_to_numpy=True)

    def _user_vector(self, skills):
        text = " ".join(skills)
        return self.model.encode([text], convert_to_numpy=True)[0]

    def recommend_jobs(self, user_skills, top_k=5):
        user_vec = self._user_vector(user_skills)
        scores = np.dot(self.job_vectors, user_vec)
        top_indices = scores.argsort()[-top_k:][::-1]
        return [self.jobs[i] for i in top_indices]

    def recommend_courses(self, user_skills, top_k=5):
        user_vec = self._user_vector(user_skills)
        scores = np.dot(self.course_vectors, user_vec)
        top_indices = scores.argsort()[-top_k:][::-1]
        return [self.courses[i] for i in top_indices]
