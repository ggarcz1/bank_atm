
# just grep it or save it to an .xlsx file when want to load/search it


def display():
    underlines = '___________________________________________________________________________________'
    f = open('logs.txt')
    # print (underlines+'\n\tDate & Time      \t| IP Address | Username | Password\n'+underlines)

    for line in f:
        arr = line.replace('\t',  ' | ')
        arr += '\n'+underlines
        print(arr)

display()