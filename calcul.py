from random import randint

choice = int(input('введите длинну пороля:'))

password = ""

spec_ch = False 
 
for i in range(choice):
    if spec_ch == True:
        password += chr(randint(65,90))
    else:
        if randint(1,2,) == 1:
            password += chr(randint(65,90))
        else:
            password += chr(randint(97,122))
            if randint(1,2) == 1:
                password += chr(randint(48,57))
               
print('сгенерированный пороль:', password)