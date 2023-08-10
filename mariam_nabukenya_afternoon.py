#excrise one 
# number one 
myList =["Mary","Adam","Hade","Sakina","Sherry"]
print(myList[1])
#number two
myList[0]="Annie"
print(myList)
#number three
myList.append("Fatuma")
print(myList)
#number four
myList[2]="Bathel"
print(myList)
#number five
myList.remove("Sakina")
print(myList)
#number six
print(myList[-1])
#number seven
    #number eight
countryList=["Uganda","Kenya","Angola"]
klist=countryList.copy()
print(klist)
    #number nine
for x in countryList:
        print(x)
        #number 11
newLList=["cow","goat","lion","giraffe","wolf"]
newLList.sort()
print(newLList)
newLList.sort(reverse=True)
print(newLList)
firstList=["mariam","halima","honiffer"]
lastList=["nalukwago","makubuya"]
firstList.extend(lastList)
print(firstList)
#excrise twoturples
xturple=["samsung","iphone","techno","redmi"]
print(xturple[1])
print(xturple[-2])
y=list(xturple)
y[1]="itel"
y.append("huawei")
y.remove("samsung")
xturple=tuple(y)
print(xturple)
for x in xturple:
        print(x)
        #number seven
        cities=(["kampala","masaka","jinja","mbarara"])
        (kampala,masaka,jinja,mbarara)=cities
        print(kampala)
        print(masaka)
        print(jinja)
        print(mbarara)
        print(cities[1:4])
        #number10
        firstname=["mariam","daine","shadia","juma"]
        lastname=["makula","matovu","ssebatta"]
        names=firstname+lastname
        print(names)
        #number11
        colours=["red","green","yellow","blue"]
        myclour=colours*3
        print(myclour)
#number 12
thistuple=[1,3,7,8,7,5,4,6,8,5]
count=thistuple.count(8)
print(count)
#exercise 3 sets
#number1
beverages=({"juice","soda","water"})
print(beverages)
#number2
beverages.add("smoothie")
beverages.add("milkshake")
print(beverages)
#number 3
mySet={"oven","kettle","microwave","refigerator"}
if "microwave" in mySet:
        print("true ")
mySet.remove("kettle")
print(mySet)
for x in mySet:
        print(x)
        #number 6
        setof_four={4,5,7,8}
        listof_two=["y","e"]
        newset=setof_four.union(*listof_two)
        print(newset)
        #number7
        first={"mary","jane","chidera"}
        age={20,22,25}
        set3=first.union(age)
        print(set3)
        #exercise 4 string
        #number1
        w=8
        y="kawempe"
        z=str(w)+y
        print(z)
#number2
txt="  Hello,     Uganda    "
print(txt.strip())
print(txt.upper())
print(txt.replace("U","V"))
#NUMBER5
y="Iam proudly Ugandan"
#number6
x="All Data Scientists are cool"
#exercise
shoes= {
 "brand":"Nick",
 "color":"black",
 "size":40
}
shoes["brand"]="Adidas"
print(shoes)
shoes["type"]="sneakers"
print(shoes)
d=shoes.keys()
print(d)
n=shoes.values()
print(n)
if "size" in shoes:
        print("true")
        for x in shoes:
                print(x)
                shoes.pop("color")
                shoes.pop("brand")
                shoes.pop("type")
                shoes.pop("size")
                print(shoes)
                #number10
                coursemate={
                        "name":"hade",
                        "place":"muk",
                        "course":"bsse"
                }
                mydict=coursemate.copy()
                print(mydict)
                #number11
                friends={
                        "coursemate":{
                        "name":"hade",
                        "place":"muk",
                        "course":"bsse"
                },
                       "oldgirl":{
                        "name":"Jamila",
                        "place":"mhs",
                        "course":"bsq"
                }
                }