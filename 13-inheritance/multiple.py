class Person:
    _name = ''
    _gender = ''

    def __init__(self,*args,**kwargs):
        self._name = kwargs['name']
        self._gender = kwargs['gender']


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

    def __init__(self, *args,**kwargs):
        super(Customer,self).__init__(*args,**kwargs)
        self._balance = kwargs['balance']

    @property
    def balance(self):
        return self._balance


    def generation(self):
        return 'second generation'


class Employee(Person):
    _department = ''

    def __init__(self, *args,**kwargs):
        super(Employee,self).__init__(*args,**kwargs)
        self._department = kwargs['department']


    @property
    def department(self):
        return self._department


class InternalCustomer(Employee,Customer):
    def __init__(self,*args,**kwargs):
        super(InternalCustomer,self).__init__(*args,**kwargs)

print(InternalCustomer.mro())

ic = InternalCustomer(name='Rodrick',gender='Male',balance=513.6,department='Engineering')

print(f'The internal customer is {ic.gender}, and the name is {ic.name}. The balance is {ic.balance}')