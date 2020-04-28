import random
x = 'TRUE'
count = 1
a = str(random.randint(0,1))
while x == 'TRUE':
    b = str(random.randint(0,1))
    count += 1
    a = a + b
    if count == 80:
        count = 1
        print(a)

    
    


    
    





        

    
      
