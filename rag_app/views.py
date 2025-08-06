from django.shortcuts import render
from django.http import JsonResponse
from .rag_utils import generate_answer

# Create your views here.

def rag_chat(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = generate_answer(question)
        return JsonResponse({'answer': answer})
    return render(request, 'rag_app/chat.html')