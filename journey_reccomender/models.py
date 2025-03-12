from django.db import models

class Request(models.Model):
    region = models.CharField(max_length=100, verbose_name="Регион")
    purpose = models.CharField(max_length=100, verbose_name="Цель")
    duration = models.IntegerField(verbose_name="Продолжительность (дни)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Запрос #{self.id}"

class Answer(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='answers')
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer for Request {self.request.id}"