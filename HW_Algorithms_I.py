
1.1
def bingo():
     for i in range(1, 101):
          if i % 3 == 0 and i % 7 == 0:
               print('Bingo')
          elif i % 3 == 0:
               print('Bin')
          elif i % 7 == 0:
               print('Go')
          else:
               print(i)

bingo()

#1.2
def factorial(n: int):
     final_sum = 0
     for i in range(n+1):
          final_sum  = final_sum + i
     print(f'the factorial of {n} is {final_sum}')


factorial(5)
#
#2.1
list = [34, 64,98]
max = list[0]
for num in list:
     if (num > max):
          max = num
print('Max:', max)

#2.2
input_year = int(input('Enter a year:'))
def is_leap(year):
     if (year%4==0) or (year%400==0 and year%100!=0):
          return True
     else:
          return False

if is_leap(input_year):
     print('It is a leap year')
else:
     print('It is not a leap year')



def generate_fibonacci_sequence(n: int):
    fib_sequence = [0, 1]
    for i in range(2, n):
         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
print(generate_fibonacci_sequence(16))

