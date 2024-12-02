# **Проектная работа к курсу "Python QA Engineer"**

## Тема проектной работы - OpenCart UI + API AT

Для запуска OpenCart можно использовать docker-compose.yml с помощью команды:
docker compose up -d

Для запуска проекта cделать следующее:

1. Склонировать репозиторий и создать виртуальное окружение python3 -m venv venv
2. Активировать виртуальное окружение . venv/bin/activate 
3. Установить необходимые библиотеки pip install -r requirements.txt
4. Актуализировать данные в файле config.json пользователя api (в проекте приложен образец)
5. В панели администратора для пользователя api добавить ip адрес с которого будет выполняться запуск 
6. Для запуска UI+API тестов выполнить команду pytest tests/api_tests/ && pytest tests/ui_tests/

Так же тесты можно запустить в docker-контейнере:
1. Склонировать репозиторий на локальную машину
2. Выполнить сборку образа командой sudo docker build -t <image_name> .
3. Для запуска API тестов выполнить команду sudo docker run --rm <image_name> pytest tests/api_tests/ --url=$OPENCART_URL
4. Для запуска UI тестов выполнить команду sudo docker run --rm <image_name> pytest tests/ui_tests/ -n $THREADS --executor=$EXECUTOR_ADDRESS --url=$OPENCART_URL --browser=$BROWSER --bv=$BROWSER_VERSION

Запуск тестов с помощью Jenkins возможен с помощью Jenkinsfile (комментариями помечено что нужно поменять в самом файле)
- Jenkins можно запустить в контейнере с помощью jenkins/docker-compose.yml -> docker-compose up -d