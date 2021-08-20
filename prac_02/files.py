# Question 1
user_name = input('Enter name: ')
file_out = open('name.txt', 'w')
print(user_name, file=file_out, end='')
file_out.close()

# Question 2
name_file = open('name.txt')
name = name_file.read()
name_file.close()
print(f'Your name is {name}')

# Question 3
number_file = open('numbers.txt')
number_1 = int(number_file.readline().strip())
number_2 = int(number_file.readline().strip())
number_file.close()
print(number_1 + number_2)

# Question 4
number_file = open('numbers.txt')
total = sum(int(line.strip()) for line in number_file)
number_file.close()
print(total)
