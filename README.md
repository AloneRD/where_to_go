# Where to go

Интерактивная карта Москвы, на которой отмечаны интересные виды и места активного отдыха с подробными описаниями и комментариями.

# Демка сайта
https://agoncharov.pythonanywhere.com/
# Запуск локально
- git clone https://github.com/AloneRD/where_to_go.git
- активировать виртуальное окружение ./env/Scripts/activate
- перейти в директорию проекта whete_to_go
- запустить миграции 
    * python./manager makemigrations
    * python./manager migrate
- для доступа в админку создать пользователя выполив команду python./manager createsuperuser
- запустить сервер выполнив команду python./manager runserver
- перейти по адрессу http://127.0.0.1:8000/
- увидеть карту Москвы!
