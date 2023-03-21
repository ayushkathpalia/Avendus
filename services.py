import database as _database
import sqlalchemy.orm as _orm
import models as _models
import schemas as _schemas
import datetime as _dt

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db =  _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_deal(db:_orm.Session,deal:_schemas.BulkdealsSchema):
    db_deal = _models.Bulkdeals(deal_date = deal.deal_date,security_code = deal.security_code,security_name = deal.security_name,client_name = deal.client_name,deal_type = deal.deal_type,quantity = deal.quantity,price = deal.price,created_on=_dt.datetime.now())
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal

def get_deal(client_name,db):
    return db.query(_models.Bulkdeals).filter(_models.Bulkdeals.client_name == client_name).first()


def update_deal(db:_orm.Session,client_name,data):
    db_data = get_deal(client_name,db)
    db_data.deal_date = data.deal_date
    db_data.deal_type = data.deal_type
    db_data.price = data.price
    db_data.quantity = data.quantity
    db_data.security_code = data.security_code
    db_data.security_name = data.security_name
    db_data.updated_on = _dt.datetime.now()
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_deal(client_name,db):
    db.query(_models.Bulkdeals).filter(_models.Bulkdeals.client_name == client_name).delete()
    db.commit()