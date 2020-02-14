import random

file_1 = open('file_1', 'w')
file_2 = open('file_2', 'w')
number_of_lines = 1000

count_equal = 0
count_not_equal = 0

for i in range(0, number_of_lines):
    # url_1 = ("https://jsonplaceholder.typicode.com/photos/%s\n" % (random.randint(1, 5000)))
    # url_2 = ("https://jsonplaceholder.typicode.com/photos/%s\n" % (random.randint(1, 5000)))
    url_1 = ("https://reqres.in/api/users/%s\n" % (random.randint(1, 12)))
    url_2 = ("https://reqres.in/api/users/%s\n" % (random.randint(1, 12)))

    if random.choice([True, False]):
        file_1.write(url_1)
        file_2.write(url_1)
        count_equal += 1
    else:
        file_1.write(url_1)
        file_2.write(url_2)
        count_not_equal += 1

print("Equal lines: %s" % (count_equal))
print("Not equal lines: %s" % (count_not_equal))
