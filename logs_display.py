# just grep it or save it to an .xlsx file when want to load/search it

# grep admin logs.txt | awk '{split($0,a,"\t"); print a[4], a[5]}'

def display():
    underlines = '___________________________________________________________________________________'
    f = open('logs.txt')
    # print (underlines+'\n\tDate & Time      \t| IP Address | Port | Username | Password\n'+underlines)

    for line in f:
        arr = line.replace('\t', ' | ')
        # arr += '\n' + underlines
        print(arr)


header = '\n\tDate & Time      \t| IP Address | Port | Username | Password\n'
print(header)

display()
