class Person:

    def __init__(self, name, oth, surname, numbook):
        self.name = name
        self.oth = oth
        self.surname = surname
        self.numbook = numbook

    def get_phone(self, key='private'):
        return self.numbook.get(key)

    def get_name(self):
        return f'{self.surname} {self.name} {self.oth}'

    def get_work_phone(self):
        return self.get_phone('work')

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.oth}! \
Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:

    def __init__(self, name, type_, numbook, *arg):
        self.name = name
        self.type_ = type_
        self.numbook = numbook
        self.person = arg

    def get_phone(self, key='contact'):
        if key in self.numbook:
            return self.numbook.get(key)
        for person in self.person:
            number = person.get_work_phone()
            if number:
                return number

    def get_name(self):
        return f'{self.name}'

    def get_work_phone(self):
        return self.get_phone()

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! \
        Примите участие в нашем беспроигрышном конкурсе для {self.type_}'


def send_sms(*obj):
    for ob in obj:
        number = ob.get_phone()
        if number:
            print(f'Отправлено СМС на номер {number} с текстом: {ob.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {ob.get_name()}')



person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)


