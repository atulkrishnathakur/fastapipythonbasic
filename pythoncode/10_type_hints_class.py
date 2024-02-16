from typing import Optional,List

class Job:
    def __init__(self,title:str,description:Optional[str]) -> None:
        self.title = title
        self.description = description

    def __repr__(self):
        return self.title


job1 = Job(title="Atul1",description="My India")
job2 = Job(title="Atul2", description="My Bharat")

Jobob = List[Job]  #notice the List[Job] , Job is our custom class
J: List[Job] = [job1,job2] # Use colon(:) to define and assign
def myobjlist(myobj: Jobob)->List:
    title_list = []
    for ob in myobj:
        title_list.append(ob.title)
    return title_list

#print(myobjlist([obj1,obj2]))
print(myobjlist(J))