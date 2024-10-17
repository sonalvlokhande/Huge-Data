from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import crud
import random
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

'''@app.post("/signup", response_model=schemas.CustomerResponse)
def signup(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_mobile(db, customer.mobile)
    if db_customer:
        raise HTTPException(status_code=400, detail="Mobile number already registered")
    otp = str(random.randint(1000, 9999))  # Generate a 4-digit OTP
    db_customer = crud.create_customer(db, customer)
    db_customer.otp = otp  # Save OTP to the database
    db.commit()  # Commit the changes to the database
    return db_customer '''

@app.post("/signup", response_model=schemas.CustomerResponse)
def signup(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_mobile(db, customer.mobile)
    if db_customer:
        raise HTTPException(status_code=400, detail="Mobile number already registered")
    
    otp = str(random.randint(1000, 9999))  # Generate a 4-digit OTP
    db_customer = crud.create_customer(db, customer, otp)  # Pass OTP to the CRUD function
    
    print(f"Generated OTP for {customer.mobile}: {otp}")

    return db_customer  # Return the customer object (without OTP for security)

@app.post("/login")
def login(customer: schemas.CustomerLogin, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_mobile(db, customer.mobile)
    if not db_customer:
        raise HTTPException(status_code=400, detail="Customer not found")
    if db_customer.otp != customer.otp:
        raise HTTPException(status_code=400, detail="Incorrect OTP")
    db_customer.otp = None  # Clear OTP after successful login
    db.commit()  # Commit the changes to the database
    return {"message": "Login successful"}