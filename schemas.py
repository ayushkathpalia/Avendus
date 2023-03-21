import pydantic as _pydantic


class BulkdealsSchema(_pydantic.BaseModel):
    deal_date : str
    security_code : str
    security_name : str 
    client_name : str
    deal_type : str
    quantity : str
    price : str