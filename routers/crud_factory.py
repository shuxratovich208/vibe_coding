from typing import Any, Type

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def build_crud_router(
    *,
    model: Type[Any],
    create_schema: Type[Any],
    response_schema: Type[Any],
    prefix: str,
    tag: str,
):
    router = APIRouter(prefix=prefix, tags=[tag])

    @router.post("/", response_model=response_schema)
    def create_item(payload: create_schema, db: Session = Depends(get_db)):
        item = model(**payload.model_dump())
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    @router.get("/", response_model=list[response_schema])
    def list_items(db: Session = Depends(get_db)):
        return db.query(model).all()

    @router.get("/{item_id}", response_model=response_schema)
    def get_item(item_id: int, db: Session = Depends(get_db)):
        item = db.query(model).filter(model.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail=f"{tag} not found")
        return item

    @router.put("/{item_id}", response_model=response_schema)
    def update_item(item_id: int, payload: create_schema, db: Session = Depends(get_db)):
        item = db.query(model).filter(model.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail=f"{tag} not found")
        for key, value in payload.model_dump().items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item

    @router.delete("/{item_id}")
    def delete_item(item_id: int, db: Session = Depends(get_db)):
        item = db.query(model).filter(model.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail=f"{tag} not found")
        db.delete(item)
        db.commit()
        return {"ok": True}

    return router
