# ASFERO_test_mail_sending
Тестовое задание на должность QA Automation Engineer в ASFERO

Написать тестовый проект с использованием Python, Selenium.

# Тест должен уметь следующее:

- залогиниться на почтовый сервис
- отправить любое колличество писем (в данном случае самому себе) с заполненными полями: head, body
- проверить статус получения этих писем
- собрать данные с писем в словарь ({head:body})
- сгенерировать новое количество писем (соответствующие колличеству отправленных писем) и отправить их в новом теле письма:
"Received mail on theme {'head'} with message: {'body'}. It contains {'Count of letters'} letters and {'Count of numbers'} numbers"
- удалить все полученные письма кроме последнего

# Копирование репозитория и установка зависимостей
```
git clone https://github.com/MrIvanDii/ASFERO_test_mail_sending
cd ASFERO
python -m venv rest_env
rest_env\Scripts\activate (для OS Windows)
source rest_env/bin/activate (для OS Mac/Linux)
pip install -r requirements.txt
```
# Запуск тестов

Перед запуском тестов необходимо перейти в каталог проекта ASFERO


# Аргументы запуска:

'-s' - показывать принты в процессе выполнения

'-v' - verbose режим, чтобы видеть, какие тесты были запущены

# команда запуска
```
py.test -s -v tests
```
