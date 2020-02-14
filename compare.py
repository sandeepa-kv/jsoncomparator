import sys
import json
from urllib.request import Request, urlopen

def check_argv_len():
    if (len(sys.argv) < 3):
        print("Usage: python3 compare.py <file_1> <file_2>")
        sys.exit(1)

def open_file(file_path):
    try:
        file = open(file_path)
    except Exception as exc:
        print("Error: Cannot open \"%s\" due to %s" % (file_path, exc))
        sys.exit(1)

    return file

def compare(node1, node2):
    # return node1 == node2 is deep search by default.
    # Below shows code in case it was not.
    if type(node1) != type(node2):
        return False

    # Lists
    if type(node1) is list:
        if len(node1) != len(node2):
            return False
        for index in range(len(node1)):
            if (not compare(node1[index], node2[index])):
                return False

    # Dictionaries
    elif type(node1) is dict:
        if len(node1) != len(node2):
            return False
        for key in node1:
            if (key not in node2) or (not compare(node1[key], node2[key])):
                return False

    # Everything else
    else:
        return str(node1) == str(node2)

    return True

def compare_links(file_1, file_2):
    timeout_s = 5
    headers = { "User-Agent": "Python" }
    error_file = open('errors.log', 'w')

    line_no = 1
    for url_1 in file_1:
        try:
            url_1 = url_1.strip()
            url_2 = file_2.readline().strip()

            if not url_1 or not url_2:
                continue

            req_1 = Request(url_1, headers = headers)
            res_1 = urlopen(req_1, timeout = timeout_s)
            json_1 = json.loads(res_1.read())

            req_2 = Request(url_2, headers = headers)
            res_2 = urlopen(req_2, timeout = timeout_s)
            json_2 = json.loads(res_2.read())

            if compare(json_1, json_2):
                print ("%s equals %s" % (url_1, url_2))
            else:
                print ("%s not equals %s" % (url_1, url_2))
        except Exception as exc:
            error_file.write("Error in line %s: %s\n" % (line_no, exc))
            line_no += 1
            continue

        line_no += 1

    error_file.close()

if __name__ == "__main__":
    check_argv_len()

    file_1 = open_file(sys.argv[1])
    file_2 = open_file(sys.argv[2])

    compare_links(file_1, file_2)

    file_1.close()
    file_2.close()
