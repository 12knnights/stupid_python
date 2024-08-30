# ex18.py
# Function to read and print the contents of a file
def print_file_contents(filename):
    """Function to read and print the contents of a file."""
    try:
        with open(filename, 'r') as file:
            print(file.read())  # Read and print the entire content of the file
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Prompting the user for the filename
    filename = input("Enter the filename you want to read: ")
    print_file_contents(filename)  # Call the function to print file contents

# Entry point of the script.If the module is executed directly, the main function is called.
# But if the module is imported, the main function is not called.
if __name__ == "__main__":
    main()
