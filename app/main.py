from fastapi import FastAPI, Query
from model import NewsSearchModel
from utils import validate_query
import time
import logging

app = FastAPI()
model = NewsSearchModel()
model.load_articles('data/news_category_dataset.json')
model.create_index()

logging.basicConfig(level=logging.INFO)

@app.get("/search")
def search_news(query: str, category: str = None, top_k: int = 5):
    start_time = time.time()
    results = model.search(query, category, top_k)
    duration = time.time() - start_time
    logging.info(f"Search completed in {duration:.2f} seconds.")
    return {"query": query, "results": results, "response_time": f"{duration:.2f} seconds"}

@app.post("/add")
def add_articles(new_articles: list):
    model.add_articles(new_articles)
    return {"status": "success", "message": "Articles added and index updated."}
