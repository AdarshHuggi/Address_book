
from geopy.geocoders import Nominatim
from fastapi import APIRouter, Depends, status, HTTPException, Response
from database.db_connection import get_db
from sqlalchemy.orm import Session
from models.orm_model import Address
from logger.logger import logger

router = APIRouter()

@router.get("/get_address/")
async def get_address(latitude: float, longitude: float,db: Session = Depends(get_db)):
    try:
            
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        print("address",location.address)
        address =location.address.split(",")
        new_address = Address(town=address[0], district=address[1],state=address[2],pincode=address[3],country=address[4])
        db.add(new_address)
        db.commit()
        db.close()
        
        
        logger.info(f"suceessfully inserted the address ")
        return {"address": location.address}
    except Exception as e:
        logger.error(f"Not found the exact address for cordinates {str(e)}")
        raise HTTPException(status_code=500, detail=f" Not found the exact address for cordinates")
        


