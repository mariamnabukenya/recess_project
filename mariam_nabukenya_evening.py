#Dictionary items 
myDic={
    "name":"Mary",
    "course":"BSSE",
    "duration":"four years"
}
print(myDic)
#length of a dictionary
print(len(myDic))
#accessing items
a= myDic["course"]
print(a)
k=myDic.get("duration")
print(k)
#accessing dictionary keys
w=myDic.keys()
print(w)
#use of values()method
Animal={
    "Name":"cow",
    "sound":"moo",
    "youngone":"calf"
}
x=Animal.values()
print(x)
#checking if the key exists
dict={"k":5,"h":8,"b":4}
if "k"in dict:
    print("It is in the list")
else:
    print("It is not in the list")
    #changing and updating dictionary items
    Person={
        "Name":"Mariam",
        "Nationality":"Ugandan",
        "Gender":"Female"
    }
    #changing an item
    Person["Name"]="Hadijah"
    print(Person)
    Person_Stuff ={
        "Name":"Nalukwago",
        "Natinality":"Turkish",
        "Gender":"Male"
    }
    #updating an item
    Person_Stuff.update({"Nationality":"British"})
    print(Person_Stuff)
    #Adding and removing items
    #Adding items
    dict1={
        "Name":"Adam",
        "Nationality":"Sudanese",
        "Gender":"Male"
    }
    dict1["Name"]="Ssebatta"
    print(dict1)
    #removing an item
    dict1.pop("Gender")
#looping through dictionary
for key,value in dict1.items():
    print(key,value)
    #nesting dictionaries
    dict1={
        "Name":"Adam",
        "Nationality":{
"nation":"Angola",
"continent":"Africa"
        },
        "Gender":"Male"
    }
    print(dict1["Nationality"]["continent"])
    