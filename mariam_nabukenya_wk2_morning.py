class employee:
    def __init__(self,name,salary) -> None:
        self._name=name
        self._salary=salary
    
    #using getters to obtain name and salary
    def get_name(self):
        return self._name
    def get_salary(self):
        return self._salary
    
    #using setters to set salary
    def set_salary(self,newSalary):
        self._salary = newSalary
    
    #method to increase salary
    def salary_increment(self,amount):
        self._salary+=amount
    
    #creating object to initialize values
    employee = employee("Mary",850000)
    #outputting name and salary
    print("Name is ",employee.get_name())
    print("Initial salary ",employee.get_salary())
        
    employee.salary_increment(150000)
    print("Current salary is ",employee.get_salary())
