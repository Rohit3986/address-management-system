
#-------------------------importing necessary libraries----------------------
import database
import models
from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session

app=FastAPI() #creating instance of fastapi

models.database.Base.metadata.create_all(bind=database.engine)

#-------------------------- this endpoint is for adding/creating address entries-------------------
@app.post("/add_address/")
async def create(country:str,state:str,district:str,area:str,house_number:str):
    session=Session(bind=database.engine,expire_on_commit=False)
    db_user = models.Address(house_number=house_number, area=area,district=district,state=state,country=country)
    session.add(db_user)
    session.commit()
    return {"message":"1 entry added","value":db_user}



#-------------------------- this block is for updating address entries-------------------
@app.put("/update_address")
async def update(id: int, country:str,state:str,district:str,area:str,house_number:str):
    session=Session(bind=database.engine,expire_on_commit=False)
    db_user = session.query(models.Address).get(id)
    if db_user==None:
        return {"message":"no records found"}
    db_user.house_number=house_number
    db_user.area=area
    db_user.district=district
    db_user.country=country
    session.commit()
    db_user_new = session.query(models.Address).get(id)
    return {"message":"updated successfully","old_entry":db_user,"new_entry":db_user_new}



#----------- this endpoint is for reading/retriveing a particular address from database-------------------
@app.get("/get_address_by_address_id/")
def get_address_by_house_id(id:int):
    session=Session(bind=database.engine,expire_on_commit=False)
    db_user = session.query(models.Address).get(id)

    if db_user==None: #this condition will check that given id is existed or not in our database
        return {"message":"no records found"}
    return {"message":"scusess","value":db_user}



#----------- this endpoint is for reading/retriveing all address from database-------------------
@app.get("/get_all_entries/")
async def get_address_by_house_id():
    session=Session(bind=database.engine,expire_on_commit=False)
    db_user = session.query(models.Address).all()
    if db_user==None:
        return {"message":"no records found"}
    return {"message":"all records fecthed successfully","value":db_user}



#-------------------------- this endpoint is for reading/retriveing all address from database-------------------
@app.get("/get_address_by_state/")
async def get_address_by_house_id(state:str = None):
    session=Session(bind=database.engine,expire_on_commit=False)
    db_user=session.query(models.Address).filter(models.Address.state==state).all()
    if db_user==None:
        return {"message":"no records found"}
    return {"message":"all records fecthed successfully","value":db_user}

#-------------------------- this endpoint is for deleting address entries-------------------
@app.post("/delete_address")
async def delete(id:int):
    session=Session(bind=database.engine,expire_on_commit=False)
    db_user = session.query(models.Address).get(id)
    if db_user==None:
        return {"message":"no records found"}
    id=db_user.address_id
    session.delete(db_user)
    session.commit()
    return {"message":"entry of address id "+id+"deleted sucessfully"}

if __name__ == "__main__":
    uvicorn.run(app)
