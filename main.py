import fastapi as _fastapi
import services as _services
import schemas as _schemas
import sqlalchemy.orm as _orm

app = _fastapi.FastAPI()

_services.create_database()

# api to create deal
@app.post("/create_deals/")
def create_deal(deal: _schemas.BulkdealsSchema,db:_orm.Session=_fastapi.Depends(_services.get_db)):
    return _services.create_deal(db=db,deal=deal)

#api to get deal with client name
@app.get("/get_deal/{client_name}")
def get_deals(client_name:str,db:_orm.Session=_fastapi.Depends(_services.get_db)):
    deal = _services.get_deal(client_name=client_name,db=db)
    if deal is None:
        raise _fastapi.HTTPException(
            status_code=404,detail="Deal doesnot Exists"
        )
    return deal

#api to update deal with client name
@app.put("/update_deal/{client_name}")
def update_deals(client_name:str,deal:_schemas.BulkdealsSchema,db:_orm.Session=_fastapi.Depends(_services.get_db)):
    return _services.update_deal(db=db,client_name=client_name,deal=deal)

#api to delete deal with client name
@app.delete("/delete_deal/{client_name}")
def delete_deal(client_name:str,db:_orm.Session=_fastapi.Depends(_services.get_db)):
    _services.delete_deal(client_name=client_name,db=db)
    return {"message":"Deal Deleted Successfully"}