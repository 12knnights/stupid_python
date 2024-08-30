filename = input('enter the filename you want to create:')

with open(filename,'w') as file:
    print('enter the content you want to write with 3 lines')
    line1 = input('> ')
    line2 = input('> ')
    line3 = input('> ')
    file.write(f'{line1}\n{line2}\n{line3}\n')

print(f'your file {filename} has been written successfully')

print(f'now let\'s read the file {filename}\n')

with open(filename,'r') as file:
    content = file.read()
    print(content)

