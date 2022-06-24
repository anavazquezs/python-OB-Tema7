import datetime

x = datetime.datetime.now()
hour = x.strftime("%H")
minutes = x.strftime("%M")

if(int(hour) > 11 and int(hour) <= 19):
    print("Faltan ", 18-int(hour), " horas y ", 59-int(minutes), " para ir a casa")
else:
    print("Es hora de ir a casa")
