from functions.get_file_content import get_file_content

def test():
    result = get_file_content("calculator", "lorem.text")
    print(result)

    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("pkg/calculator: ", result)

    result = get_file_content("calculator", "bin/cat")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)

if __name__ == "__main__":
    test()
