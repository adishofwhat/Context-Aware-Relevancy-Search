# Context-Aware Relevancy Search
A highly scalable, production-ready semantic search solution designed for retrieving relevant news articles based on user queries. This system leverages Sentence-BERT (SBERT) for deep semantic understanding and Annoy for efficient similarity search, delivering accurate results with low-latency and high scalability.
### Features
- Utilizes SBERT embeddings to capture the meaning of user queries, delivering highly relevant search results.
- Option to filter results based on specific news categories.
- Built with Annoy for fast and scalable approximate nearest neighbor searches.
- Supports adding new articles and updating the index in real-time.
- Built with FastAPI, providing endpoints for search and adding new articles.

## Directory Structure
    Context-Aware-Relevancy-Search/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── model.py
    │   ├── utils.py
    │   ├── logger.py
    ├── data/
    │   ├── news.json
    ├── requirements.txt
    └── Dockerfile

## Installation
Follow these steps to set up the project on your local machine:
### Prerequisites
- Python 3.8 or higher
- pip
- Docker (if using Docker)
### Clone the Repository
```
$ git clone https://github.com/yourusername/Context-Aware-Relevancy-Search.git
$ cd context-aware-news-search
```
### Install Dependencies
```
$ pip install -r requirements.txt
```
### Docker Setup
To simplify the setup, a Dockerfile is included for containerizing the application. You can build and run the application using Docker for an isolated environment.
```
docker build -t context-aware-news-search .
docker run -p 8000:8000 context-aware-news-search
```
The application will be available at ```http://localhost:8000```

## Usage
### Running the Application
Start the FastAPI server:
```
$ uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The application will be available at ```http://localhost:8000```
### API Endpoints
#### 1. Search for News
Retrieve news articles based on a query and optional category filter.
- Endpoint: ```/search```
- Method: GET
- Parameters:
  - ```query``` (str): The search query.
  - ```category``` (str, optional): Filter results by category.
  - ```top_k``` (int, optional): Number of results to retrieve (default: 5).
Example:
```
curl -X GET "http://localhost:8000/search?query=climate+change&category=Science&top_k=5"
```
#### 2. Add Articles
Add new articles to the dataset and update the search index.
- Endpoint: /add
- Method: POST
- Payload: JSON list of articles in the following format:
```
[
    {
        "headline": "Article Title",
        "short_description": "Brief summary of the article.",
        "link": "https://example.com/article",
        "category": "Category Name"
    }
]
```
Example:
```
curl -X POST "http://localhost:8000/add" -H "Content-Type: application/json" -d '[{"headline": "New Tech Trends", "short_description": "Exploring the 
```

## Technical Details
### Core Technologies
- Sentence-BERT: For generating semantic embeddings of articles and queries.
- Annoy: Efficient approximate nearest neighbor search for low-latency performance.
- FastAPI: High-performance web framework for API development.
- JSON: Lightweight format for storing and transferring article data.
### Workflow
- Data Loading: Articles are loaded from a JSON file.
- Index Creation: Embeddings for articles are generated using Sentence-BERT and stored in an Annoy index.
- Search: For each query, embeddings are generated and used to retrieve the most similar articles from the index.
- Dynamic Updates: New articles can be added dynamically, and the index is rebuilt.


