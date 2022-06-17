# Where to go

Интерактивная карта Москвы, на которой отмечаны интересные виды и места активного отдыха с подробными описаниями и комментариями.

# Демка сайта
https://agoncharov.pythonanywhere.com/
# Запуск локально
- склонировать себе репозиторий
```
   git clone https://github.com/AloneRD/where_to_go.git
```
- установмить необходимые зависимости
```
   pip install -r requirements.txt
```
- перейти в директорию проекта **whete_to_go**
- запустить миграции
```
   python./manager makemigrations
   python./manager migrate 
```
- для доступа в админку создать пользователя выполив команду 
```
   python./manager createsuperuser
```
- запустить сервер выполнив команду 
```
   python./manager runserver
```
- перейти по адрессу http://127.0.0.1:8000/
- увидеть карту Москвы!
# Демка сайта
Переменные окружения
* DEBUG
* ALLOWED_HOSTS
* SECRET_KEY 
* SECURE_HSTS_SECONDS 
* SESSION_COOKIE_SECURE
 Информацию по переменным окружения можно найти в документации Django https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts
 # Добавления новых локаций на сайт
 Есть два способа:
 1. Зайти в админку сайта /admin и заполнять все руками.
 2. Из json файла  с данными по локации,выполнив команду  
```
 python manage.py import_new_place https://адрес_файла/имя_файла.json
```

Пример JSON файла:
```
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```
