## Установка и запуск

Обязательно установить git и python  

### Установите Git  

1. Скачайте Git с [официального сайта](https://git-scm.com/downloads).  
2. Установите Git, следуя инструкциям установщика.  

### Клонируйте репозиторий

Откройте командную строку (cmd) и выполните следующую команду:

```bash  
cd имя-локальной-директории  
git clone https://github.com/morozooff/journey-generator.git  
```

```bash  
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
```

### Установите RabbitMQ  
Установите RabbitMQ c [официального сайта](https://www.rabbitmq.com/docs/install-windows), следуя инструкциям установщика. Затем в терминале запустите сервер.

```bash  
rabbitmq-server  
```

### Настройте базу данных  
```bash  
python manage.py createsuperuser  
python manage.py makemigrations  
python manage.py migrate  
```

### Запуск celery  
Запустите celery в отдельном терминале  
```bash  
celery -A myproject worker --loglevel=info  
```

### Запуск проекта
В главном терминале запустите сервер  
```bash  
python manage.py runserver  
```