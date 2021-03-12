import random
gen=random.randint(000000,100000)
username=input('Enter the username:')
print('hello',username)
print('Here is your OTP:',gen)
password=input("Enter the otp to login:")
if password==str(gen):
    print('Login success')
else:
    password!=str(gen)
    print('login failed')