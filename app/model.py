from sentence_transformers import SentenceTransformer
from annoy import AnnoyIndex
import json
import os

class NewsSearchModel:
    def __init__(self, embedding_model='all-MiniLM-L6-v2', annoy_index_path='index.ann', dimension=384):
        self.model = SentenceTransformer(embedding_model)
        self.annoy_index = AnnoyIndex(dimension, 'angular')
        self.articles = []
        self.index_path = annoy_index_path

    def load_articles(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file {file_path} not found.")
        with open(file_path, 'r') as file:
            self.articles = json.load(file)

    def create_index(self):
        self.annoy_index.unbuild() 
        for i, article in enumerate(self.articles):
            embedding = self.model.encode(article['headline'] + ' ' + article['short_description'])
            self.annoy_index.add_item(i, embedding)
        self.annoy_index.build(20) 
        self.annoy_index.save(self.index_path)

    def search(self, query, category=None, top_k=5):
        query_embedding = self.model.encode(query)
        indices, distances = self.annoy_index.get_nns_by_vector(query_embedding, top_k, include_distances=True)
        results = []
        for idx, dist in zip(indices, distances):
            article = self.articles[idx]
            if category and article['category'].lower() != category.lower():
                continue
            results.append({
                "headline": article['headline'],
                "link": article['link'],
                "category": article['category'],
                "distance": dist
            })
        return results

    def add_articles(self, new_articles):
        self.articles.extend(new_articles)
        self.create_index()
