from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from crud import create_user
from schemas import UserCreate
from logger import logger

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, response : Response, db: Session = Depends(get_db)):
    try: 
        data = create_user(user.model_dump(),db)
        if data :
            return JSONResponse({
                "success" : True,
                "message" : "Register successfully !",
                "data" : data
            }, status_code = status.HTTP_201_CREATED
            )
        else:
            return JSONResponse({
                "success" : False,
                "message" : "Register unsuccessfully !"
            }, status_code = status.HTTP_400_BAD_REQUEST
            )
    except Exception as err:
        logger.error(f"Error - {err}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return HTTPException(
            detail= "Unexpected error occur !",
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR
        )

        
        
