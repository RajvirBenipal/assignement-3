grade = int(input("Enter The Grade Points "))

if (grade==10):
     lg= "'A+'"
     p = "Outstanding"
     print("Your Grade is",lg,"and",p,"Performance")
elif (grade==9):
     lg= "'A'"
     p = "Excellent"
     print("Your Grade is",lg,"and",p,"Performance")
elif (grade==8):
     lg= "'B+'"
     p = "Very Good"
     print("Your Grade is",lg,"and",p,"Performance")
elif (grade==7):
     lg= "'B'"
     p = "Good"
     print("Your Grade is",lg,"and",p,"Performance")
elif (grade==6):
     lg= "'C+'"
     p = "Average"
     print("Your Grade is",lg,"and",p,"Performance")
elif (grade==5):
     lg= "'C'"
     p = "Below Average"
     print("Your Grade is",lg,"and",p,"Performance")
elif (grade==4):
     lg= "'D'"
     p = "Poor"
     print("Your Grade is",lg,"and",p,"Performance")
else:
     print ("You have Failed this Semester")