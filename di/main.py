from fastapi import FastAPI, HTTPException, status, Depends

development_db = ["DB for Development"]

def get_db_session():
    return development_db


app = FastAPI()

@app.get('/add-item/')
def add_item(item:str, db = Depends(get_db_session)):
    db.append(item)
    print(db)
    return {"message":f"added item {item}"}


# https://fastapitutorial.com/blog/dependency-injection-fastapi/