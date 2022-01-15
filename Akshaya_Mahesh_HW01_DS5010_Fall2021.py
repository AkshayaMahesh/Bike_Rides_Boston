#prompting user for name
user_name = input('Hello my name is John. What is your name? ')
print('Nice to meet you',user_name,'!')
my_height = 169
# prompting user for height
user_height=input('You look tall! How tall are you exactly, '+user_name +'? ')
# To convert user's height to feet and inches
user_height_ft_inch = str(user_height).strip().split()
# To print user's height in feet and inches
print('I am',user_height_ft_inch[0]+"'",user_height_ft_inch[1]+'"')
print('What is that in metric system ?')
#  To convert user's total height to centimeters
user_height_metric = round((int(user_height_ft_inch[0])*12 + int(user_height_ft_inch[1])) * 2.54)
# To calculate height in meter and centimeters
user_height_mt = user_height_metric//100
user_height_cm = user_height_metric % 100
# To print user's height in meter and centimeters
print('It is',str(user_height_mt)+'m',str(user_height_cm)+'cm')
# To calculate height difference in centimeters
height_diff = (user_height_metric - my_height)
if height_diff > 10:
    print('Omg! You are', height_diff, 'cm taller than me !')
    # prompt to know if user plays basketball or not
    b_ball = input('Do you play basketball? ')
    if (b_ball == 'Yes' or b_ball == 'yes'):
        print('You must be the favourite player in the team!')
    elif (b_ball == 'No' or b_ball == 'no'):
        print('I definitely would if I was that tall!')
    else:
        print('Uhm, what was that?')
else:
    print('Oh, the difference is only',height_diff,'cm')

















