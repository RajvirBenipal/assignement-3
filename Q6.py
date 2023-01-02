conti = False

list_students = {1:'z',2:'a', 3:'b' }
while conti:
    list_students[int(input("Enter SID : "))] = ' '.join(input("Enter name : ").split())
    yn = input("Add more entries(Y/N): ").lower()
    if yn == 'y' : conti = True
    elif yn == 'n' : conti = False
    else: raise RuntimeError("Please enter Y or N only")


for i in list_students.keys():
    print("SID :", i, "Name :", list_students[i])


list_sorted_nam = sorted(list_students.items(), key = lambda ls:ls[1])
print(list_sorted_nam)
list_sorted_sid = sorted(list_students.items(), key = lambda ls:ls[0])
print(list_sorted_sid)

sid = int(input("Enter SID of registered student: "))
if sid in list_students.keys() :
    print("Name: ", list_students[sid])
else :
    print("Given SID not registered")