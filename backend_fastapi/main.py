from fastapi import FastAPI,HTTPException

api=FastAPI()

# GET, POST, PUT, DELETE
# GET INFO FROM SERVER
# POST CREATE SOMETHING SUBMIT SOMETHING TO SERVER
# PUT CHANGE SOMETHING
# DELETE 

users = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "role": "admin",
        "created_at": "2025-03-12T10:30:00Z"
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "email": "bob@example.com",
        "role": "user",
        "created_at": "2025-03-12T10:35:00Z"
    },
      {
        "id": 3,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "role": "admin",
        "created_at": "2025-03-12T10:30:00Z"
    },
    {
        "id": 4,
        "name": "Bob Smith",
        "email": "bob@example.com",
        "role": "user",
        "created_at": "2025-03-12T10:35:00Z"
    },
      {
        "id": 5,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "role": "admin",
        "created_at": "2025-03-12T10:30:00Z"
    },
    {
        "id": 6,
        "name": "Bob Smith",
        "email": "bob@example.com",
        "role": "user",
        "created_at": "2025-03-12T10:35:00Z"
    },
      {
        "id": 7,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "role": "admin",
        "created_at": "2025-03-12T10:30:00Z"
    },
    {
        "id": 8,
        "name": "Bob Smith",
        "email": "bob@example.com",
        "role": "user",
        "created_at": "2025-03-12T10:35:00Z"
    },
      {
        "id": 9,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "role": "admin",
        "created_at": "2025-03-12T10:30:00Z"
    },
    {
        "id":10,
        "name": "Bob Smith",
        "email": "bob@example.com",
        "role": "user",
        "created_at": "2025-03-12T10:35:00Z"
    }
]



# home
@api.get('/')
def index():
    return {"testing":"runs"}

# async 
@api.get('/async')
def async_function():
    return {"message":"this is an async function"}

# query parameter: filter a request
# /users/?head=5

# query parameter: optional, filtering 
# path parameter: mandatory, identifying a specific resource


@api.get('/users')
async def user_details(head=5):
    if head:
        return users[:head]
    else:
        return users
    
# getting the details based on the id: path parameter
@api.get('/users/id/{user_id}')
async def user_details_id(user_id:int):
    user=next((user for user in users if user["id"]==user_id),None)
    if user:
        return {"msg":"found","user":user}
    else:
      raise HTTPException(status_code=404, detail="user not found")
    

# detail by name
@api.get('/users/name/{user_name}')
async def user_detail_name(user_name:str):
    user=next((user for user in users if user["name"]==user_name),None)
    if user:
        return {"user":user["role"]}
    else:
        raise HTTPException(status_code=404,detail="the user of the specified name was not found in the data")
    

# query parameter: only admins
# user/role/?role="some_role"

@api.get('/users/role')
async def user_details_role(user_role:str):
    user=next((user for user in users if user["role"]==user_role),None)
    if user:
        return{"user":user["name"]}
    raise HTTPException(status_code=404,detail="nhi hai bhai koi")



# get where role={user_role} and name={user_name}

@api.get('/users/filter')
async def user_details_name_role(name:str=None,role:str=None):
    user=[user for user in users if user["role"]==role and user["name"]==name]
    if user:
        # return{"email": [u["email"]for u in user]}
        return {"email":user[0]['email']}
    raise HTTPException(status_code=404,detail="no user with the name and role")


# post methods
# adding a new user with name:Shrek email:shrek@examole.com role:HR "created_at": "2025-03-12T10:35:00Z"

@api.post('/new_user')
async def create_user(user:dict):
    new_user_id=max(user["id"] for user in users)+1

    new_user={
        'id':new_user_id,
        'name': user["name"],
        'email':user['email'],
        'role': user['role'],
        'created_at':user['created_at']
    }
    
    users.append(new_user)

    return {'msg': 'added new_user'}

@api.put('/user/update/{user_id}')
async def user_update(user_id:int,update:dict):
    for user in users:
        if user['id']==user_id:
            user['name']=update['name']
            user['email']=update['email']
            user['role']=update['role']
            return user
    raise HTTPException(status_code=404,detail="not found")

