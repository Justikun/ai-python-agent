from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from functions.get_files_info import get_files_info

def test():
    result = get_file_content('calculator', 'lorem.txt')
    print(result)
    result = write_file('calculator', 'lorem.txt', "OOOOOOOGA BOOGA")
    print(result)
    result = run_python_file('calculator', 'main.py')
    print(result)
    result = get_files_info('calculator', 'pkg')
    print(result)

if __name__ == "__main__":
    test()
