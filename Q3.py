list1 = input("Enter numbers (using ',' or ' 'as separators):")
if (' ' in list1) : numbers = list1.split(' ')
elif(',' in list1) :numbers = list1.split(',')

final_list = []
for i in numbers:
    final_list.append((int(i),int(i)**2))

print(final_list)