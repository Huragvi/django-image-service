http://localhost:8000/images/ — страница загрузки изображения (Django UI).

http://localhost:8000/images/list/ — список загруженных изображений.

http://localhost:8000/api/images/ — API загрузки изображения (POST, multipart file).

http://localhost:8000/api/image/{uuid}/ — API деталей изображения (GET).

http://localhost:8000/api/image/{uuid}/delete/ — API удаления изображения (DELETE).

http://localhost:8010/health — healthcheck analyzer-сервиса.

http://localhost:8010/docs — Swagger UI для FastAPI.

http://localhost:8010/redoc — ReDoc документация FastAPI.

http://localhost:8010/api/v1/analyze_doc — запустить OCR через Celery (POST).

http://localhost:8010/api/v1/send_message_to_email — отправить email с текстом через Celery (POST).

http://localhost:8025 — MailHog UI (просмотр отправленных писем).
