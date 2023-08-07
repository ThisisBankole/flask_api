from datetime import datetime
from flask import abort, make_response

#This creates a helper function named get_timestamp() that generates a string representation of the current timestamp.
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
       "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(), 
    },
    
    "Bunny": {
       "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(), 
    }
}


# This is a function used for returning the list of people 

def read_all():
    return list(PEOPLE.values())



#This is a function used for creating a person 
def create(person):
    lname = person.get("lname")
    fname = person.get("fname")
    
    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exist"
        )
        
        
#This is a function used for returning just one person in a list  
        
def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404,
            f"user with last name {lname} do not exist"
        )
        
        
#This is a function used for updating just one person in a list       
def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            406,
            f"Person with last name {lname} do not exist"
        )
        
    
#This is a function used for deleting person from a list

def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            406,
            f"Person with last name {lname} not found"
        )