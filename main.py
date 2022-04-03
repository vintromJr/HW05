import random

# Я добавив поле класу гроші (self.money) і методи працювати (def to_work) та вечірка (def party)

class Student:
    def __init__(self, name, money=0):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.status = True
        self.money = money

    def to_work(self):
        print('Time to work')
        self.money += 100
        self.happiness -= 2

    def to_study(self):
        print('Time to study')
        self.progress += 0.2
        self.happiness -= 3

    def to_sleep(self):
        print('Time to sleep')
        self.happiness += 3

    def to_chill(self):
        print('Time to chill')
        self.happiness += 5
        self.progress -= 0.1
        self.money -= 50

    def party(self):
        print('Time for crazy party')
        self.happiness += 10
        self.progress -= 0.1
        self.money -= 100

    def check(self):
        if self.progress < -0.3:
            print('Get out, stupid idiot')
            self.status = False
        elif self.happiness <= 0:
            print('I go away')
            self.status = False
        elif self.progress > 5:
            print('You are too clever')
            self.status = False
        elif self.money < -100:
            print('You are bankrupt')
            self.status = False

    def end_of_day(self):
        print('Підсумок дня')
        print('Твій рівень щастя: ' + str(self.happiness))
        print('Твій прогрес: ' + str(round(self.progress, 2)))
        print('Вміст твого гаманця: $' + str(self.money))

    def live(self, day):
        day = 'Day of ' + str(day) + ' of ' + self.name + ' life'
        print(day)
        rand = random.randint(1, 5)
        if rand == 1: self.to_study()
        elif rand == 2: self.to_sleep()
        elif rand == 3: self.to_work()
        elif rand == 4: self.party()
        else: self.to_chill()
        self.end_of_day()
        self.check()
        print()
        print('-' * 20)
        print()

student1 = Student('Roman', 300)
for day in range(1, 366):
    if student1.status == False: break
    student1.live(day)