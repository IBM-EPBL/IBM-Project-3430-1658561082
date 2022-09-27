import random
import time

while(True):
     
    T = random.randint(-40,100)
    H = random.randint(0,100)
    print("Temperature = ",T)
    print("Humidity = ",H)



    if T>80:
        if H>90:
            print("Hazard... Alarm On with Max sound")
        else:
            print("High Temperature... Alarm On")
    elif T==80:
        print("Temp at Max level... Alarm On")
    else:
        print("Normal... No Alarm")
    
    time.sleep(6)
