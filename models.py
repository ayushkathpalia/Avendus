import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _database
import datetime as _dt

class Bulkdeals(_database.Base):
    __tablename__ = "bulkdeals"
    id = _sql.Column(_sql.Integer, primary_key = True, autoincrement = True, index = True,nullable = False)
    deal_date = _sql.Column(_sql.String(100), nullable = False)
    security_code = _sql.Column(_sql.String(100), nullable = False)
    security_name = _sql.Column(_sql.String(100), nullable = False)
    client_name = _sql.Column(_sql.String(100), nullable = False)
    deal_type = _sql.Column(_sql.String(100), nullable = False)
    quantity = _sql.Column(_sql.String(100), nullable = False)
    price = _sql.Column(_sql.String(100), nullable = False)
    created_on = _sql.Column(_sql.DateTime, default = _dt.datetime.now())
    updated_on = _sql.Column(_sql.DateTime, default = _dt.datetime.now())