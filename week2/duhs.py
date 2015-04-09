import sys
import os


def bytes_to_gb(b):
    return b / (10 ** 9)


def has_arguments(arg=1):
    return len(sys.argv[1:]) >= arg


def main():
    if has_arguments():
        path = sys.argv[1]
        total_bytes_size = 0

        for root, subsirs, files in os.walk(path):
            for file_to_count in files:
                try:
                    total_bytes_size += os.path.getsize(os.path.join(root, file_to_count))
                except FileNotFoundError as error:
                    print(error)

        print(bytes_to_gb(total_bytes_size))
    else:
        print("No arguments were given.")
if __name__ == '__main__':
    main()
