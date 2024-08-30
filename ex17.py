import sys

def copy_file(src_file, dest_file):
    try:
        with open(src_file, 'r') as src:
            content = src.read()
        with open(dest_file, 'w') as dest:
            dest.write(content)
    except FileNotFoundError:
        print(f'Error: File {src_file} not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    if len(sys.argv) != 3:
        print('Usage: python ex17.py <source_file> <destination_file>')
        sys.exit(1)
    copy_file(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()


