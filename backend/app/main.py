from fastapi import FastAPI, HTTPException, BackgroundTasks
from backend.app.database import SessionLocal, engine
from backend.app.models import Base, Record
from backend.app.schemas import RecordCreate, RecordResponse
from backend.app.tasks import process_file_task

app = FastAPI()

# Створення бази даних
Base.metadata.create_all(bind=engine)

@app.post("/generate", response_model=RecordResponse)
def create_record(record: RecordCreate, background_tasks: BackgroundTasks):
    """
    Збереження тексту у файл, завантаження у S3, створення запису у базі даних і запуск фонової задачі.
    """
    db = SessionLocal()
    try:
        # Створення запису в базі даних
        new_record = Record(text=record.text, status="processing")
        db.add(new_record)
        db.commit()
        db.refresh(new_record)

        # Додати фонову задачу
        background_tasks.add_task(process_file_task, new_record.id, record.text)

        return new_record
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
