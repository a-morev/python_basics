"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
"""


class ValError(Exception):  # Создание класса-исключения
    def __init__(self, txt: str):
        self.txt = txt


class OfficeEquipment:
    def __init__(self, model, part_number, quantity: int):
        self.model = model
        self.part_number = part_number
        self.quantity = quantity
        self.unit_tech = {
            'Наименование': self.model,
            'Количество': self.quantity,
            'Артикул': self.quantity
        }
        self.list_tech = []

    def reception_on_storage(self):  # Передача техники на склад
        try:
            unique = {
                'Наименование': input(f'Введите наименование: '),
                'Количество': int(input(f'Введите количество: ')),
                'Артикул': input(f'Введите артикул: ')
            }
            self.unit_tech.update(unique)
            self.list_tech.append(self.unit_tech)
            print(f'Текущий список:\n {self.list_tech}')
            if unique.get('Количество') < 0:
                raise ValError('Некорректное значение!')
        except ValError as err:
            print(err)

    def to_make(self):
        return f'Проверка техники {self.model}'


class Company:
    def __init__(self, other_list_tech):
        self.other_list_tech = other_list_tech

    def __getattr__(self, item):
        return self.other_list_tech, item


class Printer(OfficeEquipment):
    def __init__(self, model, part_number, quantity, *args):
        super().__init__(model, part_number, quantity)
        self.model = model
        self.part_number = part_number
        self.quantity = quantity
        self.args = args

    def to_make(self):  # Переопределение метода класса
        return f'Техника {self.model} выводит на печать.'


class Scanner(OfficeEquipment):
    def __init__(self, model, part_number, quantity, *args):
        super().__init__(model, part_number, quantity)
        self.model = model
        self.part_number = part_number
        self.quantity = quantity
        self.args = args

    def to_make(self):  # Переопределение метода класса
        return f'Техника {self.model} делает электронные копии.'


class Copier(OfficeEquipment):
    def __init__(self, model, part_number, quantity, *args):
        super().__init__(model, part_number, quantity)
        self.model = model
        self.part_number = part_number
        self.quantity = quantity
        self.args = args

    def to_make(self):  # Переопределение метода класса
        return f'Техника {self.model} создает бумажные экземпляры.'
