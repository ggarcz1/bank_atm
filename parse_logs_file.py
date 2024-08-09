
filename = 'logs.txt'

f = open(f'{filename}', 'r')
count = 0

# ip[X] --> port [X]
ip = []
port = []

print('Printing Failures...')
for each in f:
    # \n is present at the end of each file
    each = each[:-1]
    line = each.split('\t')
    if line[5] == 'FAILURE':
        print(f'{each}')
        count += 1
        if line[1] not in ip:
            # ip[X] --> port [X]
            ip.append(line[1])
            port.append(line[2])

# TODO:
# make a dict to count IP addresses             

for each in ip, port:
    print(ip,port)

print(f'Done.\nFailure Counts: {count}\n')
