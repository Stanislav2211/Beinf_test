from celery import Celery
from time import sleep
from backend.app.database import SessionLocal
from backend.app.models import Record
from backend.app.s3_utils import upload_to_s3

celery_app = Celery("tasks", broker="redis://redis:6379/0")

@celery_app.task
def process_file_task(record_id: int, text: str):
    """
    Емуляція обробки файлу: завантаження в S3, оновлення статусу.
    """
    db = SessionLocal()
    try:
        # Емуляція затримки
        sleep(10)

        # Завантаження у S3
        filename = f"record_{record_id}.txt"
        file_link = upload_to_s3(filename, text)

        # Оновлення запису
        record = db.query(Record).get(record_id)
        record.status = "done"
        record.link = file_link
        db.commit()
    finally:
        db.close()
