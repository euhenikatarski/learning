#True
planet = 'Earth'
if planet.lower() == 'earth':
    print('True')
else:
    print("False")

print('\n-------------------------------------------------------------\n')

#False

planet = 'Mars'
if planet.lower() == 'earth':
    print('True')
else:
    print("False")

print('\n-------------------------------------------------------------\n')

#True IN
months = ['februery','marth','june','July']
if 'Marth'.lower() in months:
    print('True')
else:
    print("False")
#True NOT IN
if 'december'.lower() not in months:
    print('True')
else:
    print("False")

print('\n-------------------------------------------------------------\n')

age = 22
if age != 23:
    print('Вам не 23 года')