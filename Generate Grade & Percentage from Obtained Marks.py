print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")
print("__Generate Grade & Percentage of Student__")
print("------------------------------------------")
print("____Enter Obtained Marks in Subjects____")
print("------------------------------------------")
print("1. Total marks of English Subject is: 75 ")
print("2. Total marks of Urdu Subject is: 75 ")
print("3. Total marks of Maths Subject is: 50 ")
print("4. Total marks of Physics Subject is: 100 ")
print("5. Total marks of Islamiat Subject is: 100 ")
print("------------------------------------------")


sub1 = int(input("--Enter Your English Subject Obtained Marks: "))
if sub1>75:
  print ("!! Program is Stopped Working Because Your Marks is not Valid !!")
  (exit(1))
if sub1<25:
        print ("Your'e fail")
        (exit(1))

sub2 = int(input("--Enter Your Urdu Subject Obtained Marks: "))
if sub2>75:
  print ("!! Program is Stopped Working Because Your Marks is not Valid !!")
  (exit(1)) 
if sub2<25:
        print ("Your'e fail")
        (exit(1))

sub3 = int(input("--Enter Your Maths Subject Obtained Marks: "))
if sub3>50:
  print ("!! Program is Stopped Working Because Your Marks is not Valid !!")
  (exit(1))
if sub3<17:
        print ("Your'e fail")
        (exit(1))

sub4 = int(input("--Enter Your Physics Subject Obtained Marks: "))
if sub4>100:
  print ("!! Program is Stopped Working Because Your Marks is not Valid !!")
  (exit(1)) 
if sub4<33:
        print ("Your'e fail")
        (exit(1))

sub5 = int(input("--Enter Your Islamiat Subject Obtained Marks: "))
if sub5>100:
  print ("!! Program is Stopped Working Because Your Marks is not Valid !!")
  (exit(1))
if sub5<33:
        print ("Your'e fail")
        (exit(1))

print("------------------------------------------")


obtainmarks= sub1+sub2+sub3+sub4+sub5
totalmarks = 400
all = obtainmarks/totalmarks
per=all*100


print("------------------------------------------")


if per>=90 and per<=100:
    print("Congratulations you have successfully passed the exam")
    print("Your Grade is: A+")
elif per>=80 and per<90:
    print("Congratulations you have successfully passed the exam")
    print("Your Grade is: A")
elif per>=70 and per<80:
    print("Congratulations you have successfully passed the exam")
    print("Your Grade is: B")
elif per>=60 and per<70:
    print("Congratulations you have successfully passed the exam")
    print("Your Grade is: C")
elif per>=50 and per<60:
    print("Congratulations you have successfully passed the exam")
    print("Your Grade is: D")
elif per>=40 and per<51:
    print("Congratulations you have successfully passed the exam")
    print("Your Grade is: E")
elif per>=33 and per<40:
    print("Congratulations you have successfully passed the exam")
    print("Your Grade is: E")
elif per>=21 and per<33:
    print("You failed the exam")
    print("Your Grade is: F (Fail)")
elif per>=0 and per<21:
    print("You failed the exam")
    print("Your Grade is: F (Fail)")
else:
    print("Input Again")

print("------------------------------------------")

print ('Your Percentage is: ',(per),"%")
print("------------------------------------------")
