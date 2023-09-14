import csv
import sys

file_path = sys.argv[1]
row = int(sys.argv[2])
column = int(sys.argv[3])

with open(file_path, 'r') as read_file:
    csv_file = csv.reader(read_file, delimiter=',')
    print(list(csv_file)[row][column])
