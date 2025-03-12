from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Request, Answer
from .tasks import generate_recommendation
import markdown


def travel_form(request):
    if request.method == 'POST':
        region = request.POST['region']
        purpose = request.POST['purpose']
        duration = request.POST['duration']
        travel_request = Request.objects.create(region=region, purpose=purpose, duration=duration)
        generate_recommendation.delay(travel_request.id)
        return redirect('waiting', request_id=travel_request.id)
    return render(request, 'form.html')

def waiting(request, request_id):
    return render(request, 'waiting.html', {'request_id': request_id})

def check_status(request, request_id):
    travel_request = Request.objects.get(id=request_id)
    if hasattr(travel_request, 'answers') and travel_request.answers.exists():
        return JsonResponse({'status': 'done', 'response': travel_request.answers.first().response})
    else:
        return JsonResponse({'status': 'pending'})

# def result(request, request_id):
#     travel_request = Request.objects.get(id=request_id)
#     answer = travel_request.answers.first()
#     return render(request, 'result.html', {'response': answer.response if answer else 'No response yet'})

def result(request, request_id):
    travel_request = Request.objects.get(id=request_id)
    answer = travel_request.answers.first()
    response = markdown.markdown(answer.response, extensions=['fenced_code', 'tables'])
    
    return render(request, 'result.html', {
        'request': travel_request,
        'response': response if answer else 'No response yet',
    })

def profile(request):
    requests = Request.objects.all().prefetch_related('answers')
    return render(request, 'profile.html', {'requests': requests})