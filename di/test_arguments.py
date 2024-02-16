# This implementation is not possible using function

from fastapi import FastAPI, Depends

app = FastAPI()

dummy_db = {
    '1':"SDE1 at Google",
    '2':"SDE2 at Amazon",
    '3':"Backend Dev. at Spotify",
    '4':"Senior Engineer at Alphabet",
    '5':"Devops Eng. at Microsoft",
}

def get_object_or_featured(id:str, featured_job:str):
    value = dummy_db.get(id)
    if not value:
        value = dummy_db.get("featured_job")
    return value


@app.get("/job/{id}")
def get_job_by_id(job_title: str= Depends(get_object_or_featured('2'))):
    return job_title

# This program will give error
# https://fastapitutorial.com/blog/class-based-dependency-injection/