# generate_numbers.py
import sys


def main():
    filename = sys.argv[1]
    file = open(filename, 'r')
    text = file.read()
    numbers = text.split(' ')
    return sum([int(i) for i in numbers[1:]])

print (main())
if __name__ == '__main__':
    main()
