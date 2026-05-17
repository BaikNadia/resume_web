# Мой сайт-визитка | Портфолио на Django

Современный, адаптивный сайт-визитка для фрилансера, предлагающего услуги по созданию сайтов, рекламных роликов, анимации и карточек товаров.

## 📸 Скриншоты

<!-- Добавьте позже реальные скриншоты -->
![Главная страница](screenshots/home.png)
![Портфолио](screenshots/portfolio.png)

## ✨ Возможности

- 🔐 **Безопасные формы заявок** — данные клиентов сохраняются в базе PostgreSQL
- 🖼️ **Адаптивный дизайн** — красиво смотрится на всех устройствах
- 📂 **Портфолио** — загрузка и отображение проектов через админ-панель
- 🧭 **Фиксированное меню** — удобная навигация по сайту
- 📧 **Разделы**: Обо мне, Услуги, Портфолио, Контакты, Форма заявки
- 🎨 **Стилизация** — Bootstrap 5 + кастомные CSS-анимации

## 🛠️ Технологии

- **Backend:** Django 4.x, Python 3.10+
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, Bootstrap 5, Font Awesome 6
- **Images:** Pillow (обработка изображений)

## 📁 Структура проекта
resume_web/
├── config/ # Настройки проекта
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── main/ # Основное приложение
│ ├── migrations/ # Миграции базы данных
│ ├── templates/ # HTML-шаблоны
│ │ ├── base.html # Базовый шаблон (шапка + футер)
│ │ └── main/
│ │ └── home.html # Главная страница
│ ├── admin.py # Настройка админ-панели
│ ├── models.py # Модели БД (Услуги, Проекты, Заявки)
│ ├── views.py # Логика отображения страниц
│ └── forms.py # Форма заявки
├── static/ # Статические файлы (CSS, JS, изображения)
├── media/ # Загруженные пользователем файлы (портфолио)
├── manage.py
└── requirements.txt # Зависимости проекта

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/ваш-username/ваш-репозиторий.git
cd ваш-репозиторий

### 2. Создание виртуального окружения
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Установка зависимостей
pip install -r requirements.txt

4. Настройка базы данных PostgreSQL
CREATE DATABASE my_site_db;
CREATE USER my_user WITH PASSWORD 'my_password';
ALTER ROLE my_user SET client_encoding TO 'utf8';
ALTER ROLE my_user SET default_transaction_isolation TO 'read committed';
GRANT ALL PRIVILEGES ON DATABASE my_site_db TO my_user;

5. Настройка переменных окружения
SECRET_KEY=ваш-секретный-ключ
DB_NAME=my_site_db
DB_USER=my_user
DB_PASSWORD=my_password
DB_HOST=localhost
DB_PORT=5432

Обновите settings.py для чтения переменных:
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

6. Применение миграций
python manage.py makemigrations
python manage.py migrate

7. Создание суперпользователя (админ-панель)
python manage.py createsuperuser

8. Запуск сервера разработки
python manage.py runserver

🔧 Управление контентом
Через админ-панель (/admin) вы можете:

➕ Добавлять/редактировать услуги

🖼️ Загружать проекты в портфолио

📋 Просматривать заявки от клиентов

📝 Список зависимостей (requirements.txt)
txt
Django==4.2.7
psycopg2-binary==2.9.9
Pillow==10.1.0
python-dotenv==1.0.0

🎨 Кастомизация
Изменение текста и изображений
Обо мне — отредактируйте main/templates/main/home.html (секция #about)

Услуги — добавьте через админ-панель

Портфолио — загружайте картинки в админке

Контакты — измените в base.html (футер)

Фоновое изображение hero-секции — замените URL в home.html

Стили
Кастомные стили находятся в base.html (блок <style>). При желании вынесите их в отдельный static/css/style.css.

🚢 Деплой
Подготовка к продакшену:
# Сбор статики
python manage.py collectstatic

# Отключите DEBUG
# В settings.py: DEBUG = False

Рекомендуемые хостинги:

Timeweb Cloud (Россия)

Beget (Россия)

Hetzner (Германия, дёшево)

📄 Лицензия
MIT License — свободно используйте, модифицируйте и распространяйте.

📬 Контакты
Автор: Надежда Байкова
Email: baikowa.nadia@email.com
Telegram: @BaikNadia

🗺️ Планы по доработке (TODO)
Добавить отправку уведомлений в Telegram при новой заявке

Сделать анимацию появления блоков при скролле

Добавить фильтрацию портфолио по категориям

Настроить кэширование для ускорения работы

Добавить SEO-теги (meta description, keywords)

Создать карту сайта (sitemap.xml)
