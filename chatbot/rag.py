import os
from django.conf import settings
import openai

def generate_company_answer(query):
    openai.api_key = settings.OPENROUTER_API_KEY
    openai.base_url = settings.OPENROUTER_BASE_URL
    model = getattr(settings, 'OPENROUTER_MODEL', 'openai/gpt-3.5-turbo')
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an assistant for the company. Only answer questions related to the company. If the question is off-topic, reply with 'I can only answer company-related questions.'"},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error contacting OpenRouter: {str(e)}]" 