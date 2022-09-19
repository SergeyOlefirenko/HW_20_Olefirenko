# Задание 1 Класс очереди для работы с символьными значениями

class Queue:
    __data = list()
    __size = 0
    __capacity = 0
    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity
    def get_capacity(self):
        return self.__capacity
    def get_size(self):
        return self.__size
    def funk_isEmpty(self):
        if self.__size == 0:
            print('empty')
        else:
            print(f'\nQueue is not empty and has {self.__size} of elements')

    def funk_isFull(self):
        if self.__size == self.__capacity:
            print('overflow')
    def funk_enQueue(self, element: any):
        if self.__size < self.__capacity:
            self.__data.append(element)
            self.__size += 1
        else:
            print('переполнение/overflow')
    def funk_deQueue(self):
        if self.__size > 0:
            pop_it = self.__data.pop(0)
            self.__size -= 1
            return pop_it
        else:
            print('empty')
            return None
    def funk_show(self):
        for item in self.__data:
            print(item, end=',')
        print()

queue = Queue(10)
while True:
    menu = ('Проверить очередь на пустоту', 'Проверить очередь на заполнение',
            'Добавить элемент в очередь', 'Удалить элемент из очереди',
            'Отобразить все элементы очереди на экран')
    count = 0
    print('-------------------------------------------------------------------------------')
    for i in menu:
        count += 1
        print(count, " - ", i)
    print()
    x = int(input('Выберите действие которое вы хотите выполнить: '))
    print()
    if x == 1:
        queue.funk_isEmpty()
    elif x == 2:
        queue.funk_isFull()
    elif x == 3:
        data = input('Введите новое значение:')
        queue.funk_enQueue(data)
    elif x == 4:
        data = queue.funk_deQueue()
        print('deleted element:', data)
    elif x == 5:
       queue.funk_show()
    else:
        break


# Задание 2 Приоритет

class Queue_priority:
    __data = list()
    __priority = list()
    __size = 0
    __capacity = 0

    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    def funk_isEmpty(self):
        if self.__size == 0:
            print('Empty')
        else:
            print(f'\nQueue is not empty and has {self.__size} of elements')

    def funk_isFull(self):
        if self.__size == self.__capacity:
            print('Overflow')
        else:
            print('Queue has an available space')

    def insert_with_priority(self, element: any, value: int):

        if self.__size < self.__capacity:
            self.__data.append(element)
            self.__priority.append(value)
            self.__size += 1
        else:
            print('Overflow')

    def pull_highest_priority_element(self):
        if self.__size > 0:
            max_priority = max(self.__priority)
            index_max_priority = self.__priority.index(max_priority)
            popit = self.__data.pop(index_max_priority)
            self.__priority.pop(index_max_priority)
            self.__size -= 1
            return popit
        else:
            print('Empty')
            return None

    def peek(self):
        if self.__size > 0:
            max_priority = max(self.__priority)
            index_max_priority = self.__priority.index(max_priority)
            return self.__data[index_max_priority]
        else:
            print('Empty, need add value and priority value')
            print()

    def funk_show(self):
        for item in range(self.__size):
            print(self.__data[item], ' - ', self.__priority[item])
        if self.__size == 0:
            print('Queue is empty')
            print()

    def get_capacity(self):
        return self.__capacity

    def get_size(self):
        return self.__size


qP = Queue_priority(10)

# qP.insert_with_priority(2, 10)
# qP.insert_with_priority(9, 2)
# qP.insert_with_priority(5, 15)
# qP.pull_highest_priority_element()
# print(qP.peek())

while True:
    menu = ('Проверить очередь на пустоту', 'Проверить очередь на заполнение',
            'Добавить элемент c приоритетом в очередь', 'Удалить элемент с самым высоким приоритетом из очереди',
            'Отобразить элемент с самым высоким приоритетом', 'Отобразить все элементы очереди на экран')
    count = 0
    print('-------------------------------------------------------------------------------')
    for i in menu:
        count += 1
        print(count, " - ", i)
    print()
    x = int(input('Выберите действие которое вы хотите выполнить: '))
    print()
    if x == 1:
        qP.funk_isEmpty()
    elif x == 2:
        qP.funk_isFull()
    elif x == 3:
        data = input('Введите новое значение: ')
        value = input('Ведите значение приоритета: ')
        qP.insert_with_priority(data, int(value))
    elif x == 4:
        data = qP.pull_highest_priority_element()
        print('Deleted element:', data)
    elif x == 5:
        print('Элемент с самым большим приоритетом:', qP.peek())
    elif x == 6:
        print('Очередь имеет следующие значения и приоритет: ')
        qP.funk_show()
    else:
        break

# Задание 3

data1 = {
    'Логин': ' Vasya01@mail.com#',
    'Пароль': ' Vasy1#'
}
data2 = {
    'Логин': ' Vasya01#',
    'Пароль': ' Vasy1#'
}
data3 = {
    'Логин': ' Vasya01#',
    'Пароль': ' Vasy1#'
}
data4 = {
    'Логин': ' Vasya01#',
    'Пароль': ' Vasy1#'
}
data5 = {
    'Логин': ' Vasya01#',
    'Пароль': ' Vasy1#'
}
data6 = {
    'Логин': ' Vasya01#',
    'Пароль': ' Vasy1#'
}
data7 = {
    'Логин': ' Vasya01#',
    'Пароль': ' Vasy1#'
}
data8 = {
    'Логин': ' Vasya01#',
    'Пароль': ' Vasy1#'
}
users = {
    'Вася Пупкин': data1,
    'Вася Котов': data2,
    'Михаил Котовасин': data3,
    'Иван Заяц': data4,
    'Фемистокл Алкивиадович': data5,
    'Павло Гыря': data6,
    'Мыкола Пидколодный': data7,
    'Валентин Самохвалов': data8
}

def funk_add():
    userName = str(input('Введите имя пользователя: '))
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    data = {
        'Логин': login,
        'Пароль': password
    }
    users.update({userName: data})
    print(users)

def funk_delete():
    print('Что вы хотите удалить: 0 - все данные, 1 - часть данных')
    answer = int(input('Выберите действие: '))
    if answer == 0:
        userName = str(input('Имя: '))
        users.pop(userName)
    print(users)
    if answer == 1:
        userName = str(input('Имя: '))
        count = 0

        for key in users[userName]:
            count +=1
            print(count, ' - ', key, ' - ', users[userName][key])
        index = int(input('Значение которое хотите удалить : '))
        key = ''
        count = 0
        for i in users[userName]:
            count += 1
            if count == index: key = i
        users[userName].pop(key)
        print(users)

list1 = ['Логин', 'Пароль']

def funk_check():
    print(users)
    userName = (input('Введите имя для поиска : '))
    if userName in users:
        print(users[userName])
    else:
        print('Данный пользователь отсутствует')
def funk_change_login():
    print(users)
    userName = str(input('Введите имя пользователя: '))
    value = (input('Введите новый логин : '))
    users[userName]['Логин'] = value
    print(users)
def funk_change_password():
    print(users)
    userName = str(input('Введите имя пользователя: '))
    value = (input('Введите новый пароль : '))
    for key in users[userName]:
        for iKey in users[userName]:
            key = iKey
        users[userName].update({key: value})
    print(users)
def funk_output():
    for person in users:
        print(person, ': ')
        for item in users[person]:
            print(item, '-', users[person][item])
        print()
while True :
    menu = ('Добавить пользователя', 'Удалить пользователя', 'Проверить пользователя',
            'Изменить логин пользователя', 'Изменить пароль пользователя', 'Вывести всех пользователей')
    count = 0
    print('-------------------------------------------------------------------------------')
    for i in menu:
        count += 1
        print(count, " - ", i)
    print()
    x = int(input('Выберите действие которое вы хотите выполнить: '))
    print()
    if x == 1:
        funk_add()
    elif x == 2:
        funk_delete()
    elif x == 3:
        funk_check()
    elif x == 4:
        funk_change_login()
    elif x == 5:
        funk_change_password()
    elif x == 6:
       print('Список пользователей:')
       print()
       funk_output()
    else:
        break



