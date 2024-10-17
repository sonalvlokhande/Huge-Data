from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    mobile: str

class CustomerLogin(BaseModel):
    mobile: str
    otp: str

class CustomerResponse(BaseModel):
    id: int
    name: str
    mobile: str

    class Config:
        from_attributes = True