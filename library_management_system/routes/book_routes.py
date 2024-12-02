from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from crud import create_book
from schemas import BookCreate
from logger import logger

router = APIRouter()

@router.post("/create")
def add_book(book: BookCreate, response: Response, db: Session = Depends(get_db)):
    try:
        data = create_book(db=db, book=book)
        if data :
                return JSONResponse({
                    "success" : True,
                    "message" : "Book added successfully!",
                    "data" : data
                }, status_code = status.HTTP_201_CREATED
                )
        else:
            return JSONResponse({
                "success" : False,
                "message" : "Not able to add book!"
            }, status_code = status.HTTP_400_BAD_REQUEST
            )
    except Exception as err:
        logger.error(f"Error - {err}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return HTTPException(
            detail= "Unexpected error occur !",
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
        
@router.delete("/books/{book_title}")
def delete_book(book_title: str, response : Response, db: Session = Depends(get_db)):
    try:
        data = delete_book(book_title,db)
        if data :
                return JSONResponse({
                    "success" : True,
                    "message" : "Deleted successfully",
                }, status_code = status.HTTP_200_OK
                )
        else:
            return JSONResponse({
                "success" : False,
                "message" : "Not able to delete !"
            }, status_code = status.HTTP_400_BAD_REQUEST
            )
    except Exception as err:
        logger.error(f"Error - {err}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return HTTPException(
            detail= "Unexpected error occur !",
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR
        )
