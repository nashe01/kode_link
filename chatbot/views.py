from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.generic import TemplateView

from .filters import is_in_domain
from .rag import generate_company_answer

# Create your views here.

@csrf_exempt
def chat_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)
    try:
        data = json.loads(request.body)
        user_query = data.get('query', '')
    except Exception:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    if not is_in_domain(user_query):
        return JsonResponse({'response': "I'm only trained to answer questions about [Company]."})

    answer = generate_company_answer(user_query)
    return JsonResponse({'response': answer})


def test_chat_view(request):
    return render(request, 'test_chat.html')
