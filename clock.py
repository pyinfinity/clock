from operator import truediv


def clock():
    import datetime
    import os
    import time
    #creating a variable to store date and time, i have taken them in string format
    today_date_time = ""
    #running an infinite loop
    a = 1
    while a == 1:
        print(f"The execution time is approx : {str((time.time()))[0:1]} seconds")
        try:
            #stores date and time in the variable we have created
            today_date_time = datetime.datetime.today()
            print(today_date_time)
            '''run the loop in a lag of 1 seconds, means it gives instruction 
            to the terminal with a lag of 1 seconds.'''
            time.sleep(1)        
            #Clears the output so that next time we see refreshed output new time
        except:
            print("An exception occured")
        
        os.system("cls")
              
clock()
    
