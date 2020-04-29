import time

x = int(input('What number would you like to factorial? '))
    
while x < 1:
    print('Nice try. This number can\'t be factorialed.')
    time.sleep(2)
    x = int(input('What number that can be factorialed do you want to be factorialed?' ))

y = x

while x-1 > 0:
    y = (x-1)*y
    x -= 1
    
print(y)
input("Press any key to exit.")
       
       



