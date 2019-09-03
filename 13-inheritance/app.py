class Person:
    _name = ''
    _gender = ''

    def __init__(self,name,gender):
        self._name = name
        self._gender = gender


    @property
    def name(self):
        return self._name


    @property
    def gender(self):
        return self._gender


    def generation(self):
        return 'first generation'


class Customer(Person):
    _balance = 0

    def __init__(self, name, gender,balance):
        super().__init__(name, gender)
        self._balance = balance

    @property
    def balance(self):
        return self._balance


    def generation(self):
        return 'second generation'


class Employee(Person):
    _department = ''

    def __init__(self, name, gender,department):
        super().__init__(name, gender)
        self._department = department


    @property
    def department(self):
        return self._department


customer = Customer('John Smith','Male',513.6)
employee = Employee('Amanda Kazembe','Female','Finance')

print(f'The customer is {customer.gender}, and the name is {customer.name}. The balance is {customer.balance}')
print(f'The employee is {employee.gender}, and the name is {employee.name}. The department is {employee.department}')

print(f'i am a direct descend of the {customer.generation()}')
print(f'i am a direct descend of the {employee.generation()}')