import re

def datadetect(textgiven) :
    mnth = [[4,6, 9, 11], 2]
    regex = re.compile('(\d\d)/(\d\d)/(\d\d\d\d)')
    extract = regex.search(textgiven)
    date, month, year = extract.groups()
    date, month, year = int(date), int(month), int(year)

    print(date,month,year, sep='-' , end = ' ')

    if month in mnth[0] and 30 < date :
        print('INVAlID DATE')
    elif ((month == 2 and year % 400 != 0 and 28 < date) or (month == 2 and year % 4 != 0 and 28 < date))  or (month == 2 and year % 400 == 0 and 29 < date):
            print('INVAlID DATE')
    elif month not in mnth[0] and mnth != 2 and 31 < date :
        print('INVAlID DATE')
    else :
        print('VAlID DATE')
            

day = '29/02/2000'
datadetect(day)






