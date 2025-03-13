from pydantic import BaseModel,Field
from typing import Optional, List
from fastapi import FastAPI,HTTPException

api=FastAPI()

# pydantic schema
# parent class- basic schema and data types:

class EmployeeBase(BaseModel):
    name:str=Field(...,min_length=1,description='name of the employee')
    role:str=Field(...,min_length=1,description='name of the role')
    email:str=Field(...,min_length=4,description='email id for the employee')

# response model
class Employee(EmployeeBase):
    id:int

# creating a new emp emp_id auto-generat [Inpout model]
class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name:Optional[str]=Field(None,min_length=1,description='name of the employee')
    role:Optional[str]=Field(None,min_length=1,description='name of the role')
    email:Optional[str]=Field(None,min_length=4) 


# endpoints:
# get method:
db=[]
emp_counter=0

@api.get('/')
def welcome():
    return "welcome to home page"


# crud on employee
# creating a new emp
@api.post('/emp/new',response_model=Employee)
def add_employee(employee:EmployeeCreate):
    global emp_counter
    new_employee=Employee(id=emp_counter,**employee.model_dump())
    db.append(new_employee)
    emp_counter+=1
    return new_employee


# get: list of users:
@api.get('/emp/list',response_model=List[Employee])
def list_employee():
    return db

# get by name
@api.get('/emp/name/{name}', response_model=List[Employee])
def list_name_emp(name: str):
    result=[emp for emp in db if emp.name == name]
    if not result:
        raise HTTPException(status_code=404, detail="not found")
    return result


# get by role 
@api.get('/emp/role/{role}',response_model=List[Employee])
def list_role_emp(role:str):
    result=[emp for emp in db if emp.role==role]
    if not result:
        raise HTTPException(status_code=404, detail="not found")
    return result

# update
@api.put('/emp/update_details/{id}', response_model=Employee)
def update_emp(id:int,data:EmployeeUpdate):
    for index, emp in enumerate(db):
        if emp.id==id:
            update_fields=data.model_dump(exclude_unset=True)
            updated_emp=emp.model_copy(update=update_fields)
            db[index]=updated_emp
            return updated_emp
    raise HTTPException(status_code=404,detail="Employee not found")


# delete
@api.delete('/emp/delete/{emp_id}')
def delete_emp(emp_id:int):
    for index,emp in enumerate(db):
        if emp.id==emp_id:
            db.pop(index)
            return{"message":"Employee deleted"}
    raise HTTPException(status_code=404, detail="emp id does not exist")