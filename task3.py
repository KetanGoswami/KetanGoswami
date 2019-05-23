# help from https://stackoverflow.com/questions/19007383/compare-two-different-files-line-by-line-in-python

with open('Book1.txt', 'r') as file1:
    with open('20k.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('notin20kforBook1.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

with open('Book2.txt', 'r') as file3:
    with open('20k.txt', 'r') as file2:
        same = set(file3).intersection(file2)

same.discard('\n')

with open('notin20kforBook2.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

with open('Book3.txt', 'r') as file4:
    with open('20k.txt', 'r') as file2:
        same = set(file4).intersection(file2)

same.discard('\n')

with open('notin20kforBook3.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
