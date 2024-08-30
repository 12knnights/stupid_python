def read_file(filename):
    '''read the content of a file and return it'''
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def write_file(filename, content):
    '''write the content to a file'''
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Prompting the user for the filename
    filename = input("Enter the filename you want to read: ")
    content = read_file(filename)  # Read the file contents
    assert content is not None
    if content is not None:
        print("\nCurrent content of the file:")
        print(content)

        # Prompting the user for new content to append
        new_content = content + input("Enter the content you want to write: ")
        
        # Write the modified content back to the file
        write_file(filename, new_content)
        print(f"\nNew content has been written to '{filename}'.")
    else:
        print("No content to modify. Exiting.")

if __name__ == "__main__":
    main()
