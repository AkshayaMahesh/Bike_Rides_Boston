#Question 1
# Recursive function to get the factorial of an input
print('Question 1')
def my_fact_rec(n):
    if n==0 or n==1:
        return 1
    else:
     return n*my_fact_rec(n-1)
# Prompting user for input
# Factorial Function Called
my_fact_rec(k)
print('The factorial of the number is: ',my_fact_rec(k))
print('\n')

#Question 2
#Taylor series
print('Question 2')
# Recursive function to get the Taylor Series of Exponential Function
print('Exponential function')
def my_exp(x,N):
    if N==0:
        return 1
    else:
        return (x**N/my_fact_rec(N)+my_exp(x,N-1))
a= int(input('Enter the value of x: '))
b= int(input('Enter the value of N: '))
# Calling the created exp() function
my_exp(a,b)
print('The taylor series of Exponential function e^',a,'of order',b,'is',my_exp(a,b))

# b) Recursive function to get the Taylor Series of Cosine Function
print('Cosine Function')
def my_cosine(x,N):
    if N==0:
        return 1
    else:
        return ((-1)**N)*((x**(2*N))/my_fact_rec(2*N))+my_cosine(x,N-1)
a= int(input('Enter the value of x: '))
b= int(input('Enter the value of N: '))
# Calling the created cos() function
my_cosine(a,b)
print('The taylor series of Cosine function cos',a,'of order',b,'is',my_cosine(a,b))

# c) Recursive function to get the Taylor Series of Sine Function
print('Sine Function')
def my_sine(x,N):
    if N==0:
        return 1
    else:
        return ((-1)**(N))*((x**(2*N-1)/(my_fact_rec(2*N-1))))+my_sine(x,N-1)
# Prompting user for input for values x and N
a= int(input('Enter the value of x: '))
b= int(input('Enter the value of N: '))
# Calling the created sin() function
my_sine(a,b)
print('The taylor series of Cosine function cos',a,'of order',b,'is',my_sine(a,b))
print('\n')

#Question 3
print('Question 3')
#Part 1
import math
N=5
my_function_values_exp=[]
my_function_values_sin=[]
my_function_values_cos=[]
for i in range (1,N+1,1):
    my_function_values_exp.append(abs((my_exp(1,i))-(math.exp(1**i))))
    my_function_values_sin.append(abs(my_sine(3.1415/6,i)-math.sin(math.pi/6)))
    my_function_values_cos.append(abs(my_cosine(3.1415/6,i)-math.cos(math.pi/6)))
#To print the difference in values between the created functions and Python built-in functions
print('the difference b/w values for Exponential Taylor Series for x=1 and order N=1 to 5:',(my_function_values_exp))
print('the difference b/w values for Cosine Taylor Series x=pi/6 and order N=1 to 5:',(my_function_values_cos))
print('the difference b/w values for Sine Taylor Series x=pi/6 and order N=1 to 5:',(my_function_values_sin))
print('\n')
print('Question 4 in Akshaya_Mahesh.txt file')
with open ('Akshaya_Mahesh.txt','w')as f:
    f.write("Output Differences between my functions and Python's functions")
    f.write('\n')
    new_str_head = '     %s %s %s' % ('exp(1)','cos(pi/6)','sin(pi/6)')
    f.write(new_str_head)
    f.write('\n')
    for i in range(0,5,1):
     new_str='%s  %.4f   %.4f  %.4f'%(('N='+str(i+1),my_function_values_exp[i],my_function_values_cos[i],my_function_values_sin[i]))
     f.write(new_str)
     f.write('\n')
