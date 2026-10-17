# 🎨 Мой сайт-визитка | Портфолио на Django

<div align="center">

![Django](https://img.shields.io/badge/Django-4.2.7-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**Современный, адаптивный сайт-визитка для фрилансера**  
Услуги: создание сайтов, рекламные ролики, анимация, карточки товаров

</div>

---

## 👩‍💻 Об авторе

| | |
|---|---|
| **Автор** | BaikNadia (Надежда Байкова) |
| **Репозиторий** | `resume_web` |
| **Лицензия** | ![License](https://img.shields.io/badge/License-MIT-yellow.svg) |

---

## 📸 Скриншоты

> 📌 *Добавьте сюда скриншоты главной страницы и раздела «Портфолио»*

| Главная страница | Портфолио |
|:---:|:---:|
| *screenshot-home.png* | *screenshot-portfolio.png* |

---

## ✨ Возможности

- 🔐 **Безопасные формы заявок** — данные клиентов сохраняются в базе PostgreSQL
- 🖼️ **Адаптивный дизайн** — красиво смотрится на всех устройствах
- 📂 **Портфолио** — загрузка и отображение проектов через админ-панель
- 🧭 **Фиксированное меню** — удобная навигация по сайту
- 📧 **Разделы:** Обо мне, Услуги, Портфолио, Контакты, Форма заявки
- 🎨 **Стилизация** — Bootstrap 5 + кастомные CSS-анимации

---

## 🛠️ Технологический стек

<div align="center">

| Категория | Технологии |
|:---:|:---|
| **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) |
| **Database** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![Bootstrap](https://img.shields.io/badge/Bootstrap_5-7952B3?style=flat-square&logo=bootstrap&logoColor=white) ![Font Awesome](https://img.shields.io/badge/Font_Awesome_6-528DD7?style=flat-square&logo=fontawesome&logoColor=white) |
| **Images** | ![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Environment** | ![dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?style=flat-square&logo=dotenv&logoColor=black) |

</div>

---

## 📁 Структура проекта

```
resume_web/
├── config/                     # Настройки проекта
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                       # Основное приложение
│   ├── migrations/             # Миграции базы данных
│   ├── templates/              # HTML-шаблоны
│   │   ├── base.html           # Базовый шаблон (шапка + футер)
│   │   └── main/
│   │       └── home.html       # Главная страница
│   ├── admin.py                # Настройка админ-панели
│   ├── models.py               # Модели БД (Услуги, Проекты, Заявки)
│   ├── views.py                # Логика отображения страниц
│   └── forms.py                # Форма заявки
├── static/                     # Статические файлы (CSS, JS, изображения)
├── media/                      # Загруженные пользователем файлы (портфолио)
├── manage.py
└── requirements.txt            # Зависимости проекта
```

---

## 🚀 Быстрый старт

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/ваш-username/ваш-репозиторий.git
cd ваш-репозиторий
```

### 2️⃣ Создание виртуального окружения

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4️⃣ Настройка базы данных PostgreSQL

```sql
CREATE DATABASE my_site_db;
CREATE USER my_user WITH PASSWORD 'my_password';
ALTER ROLE my_user SET client_encoding TO 'utf8';
ALTER ROLE my_user SET default_transaction_isolation TO 'read committed';
GRANT ALL PRIVILEGES ON DATABASE my_site_db TO my_user;
```

### 5️⃣ Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
SECRET_KEY=ваш-секретный-ключ
DB_NAME=my_site_db
DB_USER=my_user
DB_PASSWORD=my_password
DB_HOST=localhost
DB_PORT=5432
```

Обновите `settings.py` для чтения переменных:

```python
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
```

### 6️⃣ Применение миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Создание суперпользователя (админ-панель)

```bash
python manage.py createsuperuser
```

### 8️⃣ Запуск сервера разработки

```bash
python manage.py runserver
```

🎉 Откройте [http://127.0.0.1:8000](http://127.0.0.1:8000) в браузере!

---

## 🔧 Управление контентом

Через админ-панель (`/admin`) вы можете:

| Действие | Описание |
|:---:|:---|
| ➕ | Добавлять/редактировать услуги |
| 🖼️ | Загружать проекты в портфолио |
| 📋 | Просматривать заявки от клиентов |

---

## 📝 Список зависимостей (requirements.txt)

```txt
Django==4.2.7
psycopg2-binary==2.9.9
Pillow==10.1.0
python-dotenv==1.0.0
```

---

## 🎨 Кастомизация

| Что изменить | Где |
|:---|:---|
| **Обо мне** | `main/templates/main/home.html` (секция `#about`) |
| **Услуги** | Через админ-панель |
| **Портфолио** | Загружайте картинки в админке |
| **Контакты** | `base.html` (футер) |
| **Фон hero-секции** | Замените URL в `home.html` |
| **Стили** | Кастомные стили в `base.html` (блок `<style>`) — при желании вынесите в `static/css/style.css` |

---

## 🚢 Деплой

### Подготовка к продакшену

```bash
python manage.py collectstatic
```

Отключите `DEBUG` в `settings.py`:

```python
DEBUG = False
```

### 🌐 Рекомендуемые хостинги

- 🇷🇺 **Timeweb Cloud** (Россия)
- 🇷🇺 **Beget** (Россия)
- 🇩🇪 **Hetzner** (Германия, дёшево)

---

## 🗺️ Планы по доработке (TODO)

- [ ] 📬 Отправка уведомлений в Telegram при новой заявке
- [ ] ✨ Анимация появления блоков при скролле
- [ ] 🔍 Фильтрация портфолио по категориям
- [ ] ⚡ Кэширование для ускорения работы
- [ ] 🔎 SEO-теги (`meta description`, `keywords`)
- [ ] 🗺️ Карта сайта (`sitemap.xml`)

---

## 📄 Лицензия

Проект распространяется под лицензией **MIT License** — свободно используйте, модифицируйте и распространяйте.

---

## 📬 Контакты

<div align="center">

| | |
|:---:|:---|
| 👤 **Автор** | Надежда Байкова |
| 📧 **Email** | [baikowa.nadia@email.com](mailto:baikowa.nadia@gmail.com) |
| 💬 **Telegram** | [@BaikNadia](https://t.me/BaikNadia) |

</div>

---

<div align="center">

⭐ **Если проект оказался полезным — поставьте звёздочку!** ⭐

</div>
