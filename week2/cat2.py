# cat2.py
import sys


def main():
    for i in sys.argv[1:]:
        filename = i
        file = open(filename, "r")
        content = file.read()
        print(content)
        file.close()

if __name__ == '__main__':
    main()
