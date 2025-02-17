import copy
from person import Address, Person
from employee import EmployeeFactory


if __name__ == '__main__':
    john = Person("John", Address("1 Way Street", "Utopia", "United States"))
    jane = copy.deepcopy(john)
    jane.name = "Jane"
    jane.address.street_address = "1B Way Street"

    print(john)
    print(jane)

    print ("Factory -------------")
    john = EmployeeFactory.new_main_office_employee("John", 101)
    print(john)
    jane = EmployeeFactory.new_aux_office_employee("Jane", 505)
    print(jane)

