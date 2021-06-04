from tabulate import tabulate               #import table
import datetime

for_schedule = ['Time', 'Day', 'Activity']  #heading of the table
schedule = []

def see_schedule():
    a = sorted(schedule)                 #to sort the dates
    total = [for_schedule]
    for i in a:
        if i[0] > datetime.datetime.now():
            total.append(i)
    print(tabulate(total, headers='firstrow', tablefmt='fancy_grid', showindex=range(1, len(total)), missingval='N/A') + '\n')
    
def input_schedule():
    print('Please input the data in number:')
    year    = int(input('Year     : '))
    month   = int(input('Month    : '))
    date    = int(input('Date     : '))
    hour     = int(input('Hour     : '))
    minute   = int(input('Minute   : '))
    activity = input('Activity : ')
    x = datetime.datetime(year, month, date, hour, minute)      #arrange all the input into a single time
    y = datetime.datetime.now()
    if x > y:                                                   #to filter the inputted time
        u = [x, x.strftime('%A'), activity]                     #following list for_schedule
        schedule.append(u) 
        print('Thank you, the schedule has already inputted')
        print('--------------------------------------------')
    else:
        print('Sorry, the time has passed \n')

def see_history():
    a = sorted(schedule)                 #to sort the dates
    total = [for_schedule]
    for i in a:
        if i[0] < datetime.datetime.now():
            total.append(i)
    print(tabulate(total, headers='firstrow', tablefmt='grid', showindex=range(1, len(total)), missingval='N/A') + '\n')

def main():
    while True:
        x = datetime.datetime.now()
        print(x.strftime('%A') +',', x.strftime('%B'), x.strftime('%d') + ',', x.year)
        print('Hello, Welcome to To Do List!')
        print('Please choose the menu')
        print('1. See Schedule')
        print('2. Input Schedule')
        print('3. See History')
        print('4. Exit')
        n = int(input('>> '))

        if n == 1:
            see_schedule()
        elif n == 2:
            input_schedule()
        elif n == 3:
            see_history()
        elif n == 4:
            break
        else:
            print("Sorry, there's no '{}' option".format(n))

main()