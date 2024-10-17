from sqlalchemy.orm import Session
import models
import schemas

def create_customer(db: Session, customer: schemas.CustomerCreate, otp: str):
    db_customer = models.Customer(name=customer.name, mobile=customer.mobile, otp=otp)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer_by_mobile(db: Session, mobile: str):
    return db.query(models.Customer).filter(models.Customer.mobile == mobile).first()