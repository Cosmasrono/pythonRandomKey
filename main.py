import random
def shuffle(string):
    tempList=list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
uppercaseletter1=chr(random.randint(50, 90))
uppercaseletter2=chr(random.randint(50, 90))
uppercaseletter2=chr(random.randint(50, 90))
uppercaseletter2=chr(random.randint(50, 90))
uppercaseletter2=chr(random.randint(50, 90))
password=uppercaseletter1 + uppercaseletter2
password=shuffle(password)
print('Ouch! you want password,,,cool here is it' + " " +password)


 