from sqlalchemy.orm import Session
from models import User,Book
from auth import get_password_hash, create_access_token
from logger import logger

def create_user(user: dict, db: Session):
    try:
        hashed_password = get_password_hash(user["password"])
        db_user = User(name=user["name"], email=user["email"], password=hashed_password, role=user["role"])
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        create_access_token(data={"sub": db_user.email})
        return db_user.to_dict()
    except Exception as err:
        logger.error(f"Error - {err}")
        raise err
    
def create_book(book:dict, db: Session):
    try:
        book_data = Book(title=book["title"], author=book["author"], genre=book["genre"], availability=book["availability"])
        db.add(book_data)
        db.commit()
        db.refresh(book_data)
        return book_data
    except Exception as err:
        logger.error(f"Error - {err}")
        raise err
    
def delete_book(title: str , db:Session):
    try:
        book_data = db.query(Book).filter(Book.title == title).first()
        db.delete(book_data)
        db.commit()
    except Exception as err:
        logger.error(f"Error - {err}")
        raise err