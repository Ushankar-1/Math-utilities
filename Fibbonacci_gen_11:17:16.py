import time

#REMEMBER: FUNCTION-F5 TO START

#Intro
print('Welcome to your Fibbonacci sequence thing.')
time.sleep(2)
qwer = input('\nIf you want me to print the ENTIRE Fibbonacci sequence,\n'
             'reply "Print". Otherwise, reply "No".')
#Avoids invalid responses
while qwer != 'No' and qwer!= 'no' and qwer!= 'NO' and qwer != 'Print' and qwer!= 'print' and qwer!= 'PRINT':
       qwer = input('Either "Print" or "No". Simple. ')#lol
#Printing function
if qwer == 'Print' or 'print' or 'PRINT':
        #Warning
        print('\nWarning: I have a high processor speed that will print literally\n'
              'EVERY number in the sequence very, very fast, so you have to\n'
              'press the keys "control" and "c" together to get this program\n'
              'to stop.')
        time.sleep(6)
        print('\nAnd if you let it run up till the point where the numbers get\n'
              'ridiculously large, you\'ll just have to force quit this thing.')
        time.sleep(6)
        print('\nAnd you might have to scroll up a bit to see the first\n'
              'few numbers.')
        time.sleep(3)
        print('\nLoading...\n')
        time.sleep(2)
        #Infinite loop-maker
        a = 'TRUE'
        x = 0
        y = 1
        #First two values
        print(x)
        print(y)
        #main function
        while a == 'TRUE':
            z = (x+y)
            print(z)
            x = y
            y = z
#Not-to-printing function:
elif qwer == 'No' or 'no' or 'NO':
       #Which term?
       b = int(input('\nWhat term number in the Fibbonacci sequence do you want?\n'
                  'Ex: 1, 3, 6, 58. '))
       #Anti-screwup machine
       while b < 1:
            b = int(input('Seriously. Do you want me to help you or not? Do it again. '))#lol
        #Just the one or all up to it?
       time.sleep(1)
       asdf = input('\nOkay. If you want me to print all terms up to and including\n'
                     'that term, reply "Yes". If you want me to print just that term,\n'
                    ' reply "No". Case sensitive. ')
       #Anti-screwup machine
       if asdf != 'No' and asdf != 'no' and asdf != 'NO' and asdf != 'Yes'and asdf != 'yes' and asdf != 'YES':
           while asdf != 'No' and asdf != 'Yes':
                asdf = input('Either "Yes" or "No". Not too complicated. ')#lol
       #Just that term
       if asdf == 'No' or asdf == 'no' or asdf == 'NO':
            x = 0
            y = 1
            c = 0
            #This is sad... I needed the first three values
            if b == 1:
                time.sleep(1)
                print('\n0')
            if b == 2:
                time.sleep(1)
                print('\n1')
            if b > 2:
               c = 2
               #Main equation
               while c < b:
                   z = (x+y)
                   x = y
                   y = z
                   c += 1
               print('\n',z)
               time.sleep(1)
	       print('Hope this helped.')#NOT

       #Everything up to & including that term
       elif asdf == 'Yes'or asdf == 'yes' or asdf == 'YES':
            x = 0
            y = 1
            c = 0
            time.sleep(1)
            #Initailizing first value
            print('\n0')
            if b == 1:
               time.sleep(1)
               print('Really? Considering your grade level, it\'s kind of sad that you\n'
                      'needed me for this.')#lol
            c += 1
            #Initializing second value
            print('1')
            #This is sad... I needed the first two values
            if b == 2:
                time.sleep(1)
                print('Really? Considering your grade level, it\'s kind of sad that you\n'
                      'needed me for this.')#lol
            c += 1
            #Rest of the equation
            if b > 2:
                while c < b:
                    z = (x+y)
                    x = y
                    y = z
                    c += 1
                    print(z)
                time.sleep(1)
                print('Hope this helped.')#NOT
    
            
                    
                
                
                
        
    

                
                


    
      



