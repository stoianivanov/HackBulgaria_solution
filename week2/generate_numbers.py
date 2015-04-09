import sys
from random import randint


def main():
    filename = sys.argv[1]
    file = open(filename, 'w')
    result = ""
    for i in range(0, int(sys.argv[2])):
        result += " " + str(randint(0, int(sys.argv[2])))
    file.write(result)
    file.close()

if __name__ == '__main__':
    main()
