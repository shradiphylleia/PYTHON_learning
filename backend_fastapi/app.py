from pydantic import BaseModel,Field
from typing import Optional, List
from fastapi import FastAPI,HTTPException

api=FastAPI()

# pydantic schema
# parent class- basic schema and data types:

class EmployeeBase(BaseModel):
    name:str=Field(...,min_lenght=1,description='name of the employee')
    role:str=Field(...,min_length=1,description='name of the role')
    email:str=Field(...,min_length=4,description='email id for the employee')


# create the schema employee emp_id auto-generat
class EmployeeCreate(EmployeeBase):
    pass



class EmployeeUpdate(BaseModel):
    name:Optional[str]=Field(None,min_lenght=1,description='name of the employee')
    role:Optional[str]=Field(None,min_length=1,description='name of the role')
    email:Optional[str]=Field(None,min_length=4) 


# endpoints:
# get method:
db=[]

@api.get('/')
def welcome():
    return "welcome to home page"


# crud on employee
# creating a new emp

@api.post('/emp/new',response_model=EmployeeCreate)
def add_emplyee(employee:EmployeeCreate):
    new_employee=EmployeeCreate(**employee.model_dump())
    db.append(new_employee)
    return new_employee


# get: list of users:
@api.get('/emp/list',response_model=List[EmployeeCreate])
def list_employee():
    return db

# get by name
@api.get('/emp/{name}',response_model=List[EmployeeCreate])
def list_name_emp(name:int):
    for emp in db:
        if emp["name"]==name:
            return emp["email"]
    raise HTTPException(status_code=404, detail='not found')

# get by role 
@api.get('/emp/{role}',response_model=EmployeeCreate)
def list_role_emp(role:str):
    for emp in db:
        if emp["role"]==role:
            return emp
    raise HTTPException(status_code=404, detail="not found")

# update

@api.put('/emp/update_details/{id}',response_model=EmployeeCreate)
def update_emp(id:int, data:EmployeeUpdate):
    for index,emp in enumerate(db):
        if emp.id==id:
            update_field=data.dict(exclude_unset=True)
            update_data=emp.copy(update=update_field)
            db[index]=update_data
            return data
    raise HTTPException(status_code=404, detail="not found")