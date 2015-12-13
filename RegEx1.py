import re

file = open('regex_sum_204510.txt')
sum = 0
for line in file:
	list_of_numbers = re.findall('[0-9]+', line)
	if len(list_of_numbers) != 0:
		numlist = [int(x) for x in list_of_numbers]
		for i, val in enumerate(numlist):
			sum += val
print sum
