 
filename = input('enter the filename you want to open:')

try:
    file = open(filename,'r')
    content = file.read()
    file.close()#close the file after reading，avoid memory leak
    print(content)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")