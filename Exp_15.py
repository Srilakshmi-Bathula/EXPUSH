import os

def create_file():
    with open('hello.txt', 'w') as file:
        file.write("Hello World")
    print("File(hello.txt) created with Text(Hello World)")

def append_to_file():
    with open('hello.txt', 'a') as file:
        file.write("\nHello World")
    print("Text(Hello World) appended into File(hello.txt)")

if __name__ == "__main__":
    create_file()
    append_to_file()
    print("File created at:", os.path.abspath('hello.txt'))
