import sys


def check_argv_len():
    if (len(sys.argv) < 3):
        print("Usage: python3 compare.py <file_1> <file_2>")
        sys.exit(1)

def open_file(file_path):
#code to read file from the given path and return


def compare(node1, node2):
# main comparision logic

def compare_links(file_1, file_2):
# read the link files -> get the respective links -> make http call, parse responses and send them to compare function for comparison


if __name__ == "__main__":
    check_argv_len()

    file_1 = open_file(sys.argv[1])
    file_2 = open_file(sys.argv[2])

    compare_links(file_1, file_2)

    file_1.close()
    file_2.close()