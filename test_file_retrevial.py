
def display(filename):
    # if file exist
    f = open(f'Logs//{filename}')
    file_contents = ''
    for each in f:
        file_contents += f'{each}'

    return file_contents

print(display('logs.txt'))

