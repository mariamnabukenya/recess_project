#if statement
b= 30
if b%2==0:
    print("b is even")
#if else condition
#if the condition is false the elseif code executes then
b=30
if b%2==0:
    print("b is even")
else:
    print("b is odd ")
    #nested ifs
    #when an is statement is inside another if statement
    mark=80
    if mark>=90:
        print("A+")
        if mark>=80:
            print("A")
            if mark>=70:
                print("B")
                if mark>=60:
                    print("C")
                else:
                    print("D")
                    #Loops
                    #for loop
                    fruits=["apple","banana","cherry"]
                    for x in fruits:
                        print(x)
                        #while loop
                        #keeps executing the code untill the condition is false
                        i=1
                        while i<6:
                            print(i)
                            i+=1
                            #break and continue statements
                            #breaks gets out of the loop if the condition is true
                            for number in range(1,10):
                                if number==5:
                                    break
                                print(number)
                                #continue statement
                                for number in range(1,10):
                                    if number==5:
                                        continue
                                    print(number)
                                    #exception handling(try catch and finally)
                                    #try allows you to catch a specific error 
                                    #finally is executed regardless of expection that occur while running the program

                                    emotion={
                                        'happy':"exicted about something",
                                        'sad': "being down",
                                        'angry':"extremly mad",
                                        'fearful':"afraid of something",
                                        'disgusted':"getting tired of something easily"
                                    }
                                    #user input prompt of their emotions
                                    user_input=input("How are you feeling")
                                    emotion =emotion.lower()
                                    #try catch example with use of finally
                                    fruits =["mango","apple","grapes","berries"]
                                    try:
                                        index=int(input("enter the index of the fruit you want"))
                                        selected_fruit= fruit[index]
                                        print("selected friut",selected_fruit)
                                    except IndexError:
                                        print("invalid index the selected element is not in the list")
                                    except ValueError:
                                        print("invalid input please enter a correct interger")
                                    except Exception as error:
                                        print("an error occured",str(error))
                                    finally:
                                        print("exception handling completed")
                                        #excrise write a program to ask students about their mental health
                                        response=[]
                                        while True:
                                            name =input("please enter your name")
                                            if name.lower()=='h':
                                                break
                                            rating =int(input("on the scale of 1 to 10, how do you rate your mental health"))
                                            response =input("how are you feeling")
                                            student_bio={"name":name,"rating":rating,"response":response}
                                            response.append(student_bio)
                                            print("\nresponses")
                                            for student in response:
                                                print(f"student:{student['name']}")
                                                print(f"rating:{student['rating']}")
                                                print(f"response:{student['response']}")
                                                print()


