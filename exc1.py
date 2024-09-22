# START
# create empty list, input 10 numbers from user and append them into the list
# print len, max, min, mean
# find max without using max
import statistics

x: list[int] = []
counter = 0
while counter < 10:
    x.append(int(input('enter a number: ')))
    counter += 1
else:
    print(len(x))
    print(max(x))
    print(min(x))
    print(statistics.mean(x))
# END

