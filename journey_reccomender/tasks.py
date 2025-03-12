from celery import shared_task
from .models import Request, Answer
from mysite import celery_app

@shared_task
def test_task():
    print("Тестовая задача выполнена!")

@shared_task
def generate_recommendation(request_id):
    request = Request.objects.get(id=request_id)

    response = generate_recomendation(request.region, request.purpose, request.duration)
    Answer.objects.create(request=request, response=response)


from openai import OpenAI
from .config import API_KEY

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY,
)

def generate_recomendation(region: str, purpose: str, duration: str) -> str:
    completion = client.chat.completions.create(
    model="deepseek/deepseek-chat",

    messages=[
        {
        "role": "user",
        "content": f"Я хочу посетить {region}. Цель моей поездки - {purpose}. У меня {duration} на поездку. Порекомендуй мне места для посещения в обозначенном мной регионе для моей цели и скажи, что стоит взять с собой. Расскажи какую комфортную сумму в рублях мне стоит иметь при себе в этой поездке из рассчета на одного человека."
        }
    ]
    )

    result = completion.choices[0].message.content
    print(result)
    return result