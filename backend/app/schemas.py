from pydantic import BaseModel

class RecordCreate(BaseModel):
    text: str

class RecordResponse(BaseModel):
    id: int
    text: str
    status: str
    link: str | None

    class Config:
        orm_mode = True
