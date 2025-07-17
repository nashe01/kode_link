# Company-Specific AI Chatbot

A Django-based AI chatbot that answers only company-related questions using internal documents and data.

## Features

- **Domain Filtering**: Only answers questions related to the company
- **RAG Pipeline**: Retrieval-Augmented Generation for grounded responses
- **REST API**: Simple API endpoint for frontend integration
- **MySQL Support**: Database backend for storing chat logs and metadata

## Project Structure

```
company_agent/
├── company_agent/          # Django project settings
├── chatbot/               # Main chatbot app
│   ├── views.py          # API endpoints
│   ├── filters.py        # Domain filtering logic
│   ├── rag.py           # RAG pipeline
│   └── urls.py          # URL routing
├── test_chat.html        # Testing frontend
├── manage.py            # Django management
└── requirements.txt     # Python dependencies
```

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nashe01ode_link.git
   cd company_agent
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install django mysqlclient
   ```

4. **Configure database:**
   - Update MySQL credentials in `company_agent/settings.py`
   - Run migrations: `python manage.py migrate`

5. **Start the server:**
   ```bash
   python manage.py runserver
   ```

## Usage

### API Endpoint

**POST** `/api/chat/`

**Request:**
```json
[object Object]query": "What is your company policy?"
}
```

**Response:**
```json[object Object]response": "Based on our company policy..."
}
```

### Testing Frontend

Open `test_chat.html` in your browser to test the chatbot interactively.

## Configuration

### Domain Filter

Edit `chatbot/filters.py` to customize which topics are considered company-related:

```python
def is_in_domain(query):
    company_keywords = ['product', service', 'policy', 'employee', 'support', 'company']
    return any(keyword in query.lower() for keyword in company_keywords)
```

### RAG Pipeline

The RAG pipeline in `chatbot/rag.py` is currently a stub. To implement:

1. Document ingestion and chunking
2. Embedding generation3. Vector storage (FAISS recommended)
4. Retrieval and generation with LLM

## Development

- **Domain Filter**: Currently uses keyword-based filtering
- **RAG Pipeline**: Stub implementation - needs real document processing
- **Security**: Basic CSRF protection, HTTPS recommended for production

## Next Steps
1. Implement real RAG pipeline with document ingestion
2. Add admin interface for document management
3. Implement proper vector storage
4. Add authentication and rate limiting
5. Deploy to production with proper security measures

## License

MIT License 