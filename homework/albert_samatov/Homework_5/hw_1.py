person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

prog_result1 = 'результат операции: 42'
prog_result2 = 'результат операции: 514'
prog_result3 = 'результат операции: 9'
prg1 = prog_result1.index(':')
prgN1 = int(prog_result1[prg1 + 1:]) + 10
prg2 = prog_result2.index(':')
prgN2 = int(prog_result2[prg2 + 1:]) + 10
prg3 = prog_result3.index(':')
prgN3 = int(prog_result3[prg3 + 1:]) + 10
print(prgN1, '\n', prgN2, '\n', prgN3, sep='')

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print('\n', 'Students ', ', '.join(students), ' study these subjects: ' + ', '.join(subjects), sep='')
