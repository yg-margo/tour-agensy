# Веб-приложение для туристической фирмы на Django

## Описание проекта

Этот проект представляет собой веб-приложение для туристической фирмы, разработанное на **Python** с использованием фреймворка **Django 3** и СУБД **PostgreSQL**. Основная цель проекта — предоставить пользователям удобный интерфейс для поиска, бронирования туров и оставления отзывов, а также администратору — инструменты для управления резервированиями и контентом.

---

## Цель проекта

Разработать полноценное веб-приложение для туристической фирмы, которое позволит пользователям:
- Просматривать доступные туры.
- Бронировать туры и управлять своими бронированиями.
- Оставлять отзывы и оценивать туры.
- Просматривать статистику проданных туров.

Администратор получает возможность управлять турами, бронированиями и отзывами через удобный интерфейс Django-admin.

---

## Функционал проекта

### Для пользователей:
1. **Регистрация и авторизация**:
   - Пользователи могут зарегистрироваться и войти в систему.
2. **Просмотр туров**:
   - Пользователи могут просматривать список доступных туров с информацией о названии, турагенстве, описании, периоде проведения и условиях оплаты.
3. **Бронирование туров**:
   - Пользователи могут бронировать туры, а также редактировать и удалять свои бронирования.
4. **Отзывы и рейтинг**:
   - Пользователи могут оставлять отзывы к турам, указывая рейтинг (от 1 до 10) и текст комментария.
5. **Таблица проданных туров**:
   - В клиентской части отображается таблица с информацией о проданных турах по странам.

### Для администратора:
1. **Управление бронированиями**:
   - Администратор может подтверждать бронирования через Django-admin.
2. **Управление турами и отзывами**:
   - Администратор может добавлять, редактировать и удалять туры, а также управлять отзывами.

---

## Технологии и инструменты

- **Язык программирования:** Python 3.6+
- **Фреймворк:** Django 3
- **База данных:** PostgreSQL
- **Фронтенд:** HTML, CSS, Bootstrap (для улучшения интерфейса)
- **Дополнительные библиотеки:** 
  - `django-crispy-forms` для улучшения форм.
  - `django-tables2` для отображения таблиц.

---

## Структура проекта

### Основные компоненты

1. **Модели данных**:
   - **Tour**: Модель для хранения информации о турах (название, описание, период проведения, условия оплаты и т.д.).
   - **Reservation**: Модель для хранения бронирований пользователей.
   - **Review**: Модель для хранения отзывов и рейтингов туров.
   - **User**: Стандартная модель пользователя Django с дополнительными полями, если необходимо.

2. **Представления (Views)**:
   - Просмотр списка туров.
   - Бронирование туров.
   - Управление бронированиями (редактирование, удаление).
   - Добавление и просмотр отзывов.

3. **Шаблоны (Templates)**:
   - Главная страница с списком туров.
   - Страница деталей тура.
   - Страница бронирования.
   - Страница отзывов.

4. **Админка (Django-admin)**:
   - Управление турами, бронированиями и отзывами.

---

## Как запустить проект

### Предварительные требования

1. Установите **Python** (версия 3.6 или выше).
2. Установите **PostgreSQL** и создайте базу данных для проекта.
3. Установите зависимости, выполнив команду:
   ```bash
   pip install -r requirements.txt
   ```

### Настройка базы данных

1. Создайте базу данных в PostgreSQL.
2. Настройте подключение к базе данных в файле `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Запуск проекта

1. Примените миграции:
   ```bash
   python manage.py migrate
   ```
2. Создайте суперпользователя для доступа к админке:
   ```bash
   python manage.py createsuperuser
   ```
3. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```
4. Перейдите по адресу `http://127.0.0.1:8000/` для доступа к сайту и `http://127.0.0.1:8000/admin/` для доступа к админке.

---

## Особенности проекта

- **Регистрация и авторизация**: Пользователи могут регистрироваться и входить в систему для бронирования туров и оставления отзывов.
- **Управление бронированиями**: Пользователи могут редактировать и удалять свои бронирования.
- **Отзывы и рейтинг**: Пользователи могут оставлять отзывы и оценивать туры.
- **Админка**: Администратор может управлять всеми данными через Django-admin.
- **Статистика**: В клиентской части отображается таблица с информацией о проданных турах по странам.
