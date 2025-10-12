from random import randint
from random import choice

class Die:

    def __init__(self, sides = 6):

        self.sides = sides

    def roll_die(self):

        self.roll = randint(1, self.sides)
        print(f'{self.roll}')


die_6 = Die()
print(f'6 граней: ')
die_6.roll_die()

die_10 = Die(10)
print(f'10 граней: ')
die_10.roll_die()

print(f'\n--------------------------------------------------------------\n')

nums = (1,2,3,13,65)
num = choice(nums)
print(num)

print(f'\n--------------------------------------------------------------\n')

nums = (1,2,3,13,65)
time = 0

while nums:

    x = choice(nums)
    time +=1
    if x == 2:
        break

print(time)

print(f'\n--------------------------------------------------------------\n')

numbers = [0, 1, 'A', 2, 3, 'B', 4, 5, 'C', 6, 7, 'D', 8, 9, 'E']

def get_sim(*args):
    number = str(choice(args))
    return number

win_ticket = get_sim(*numbers) + get_sim(*numbers) + get_sim(*numbers) + get_sim(*numbers)

print(f'Выиграл билет №: {win_ticket}')
