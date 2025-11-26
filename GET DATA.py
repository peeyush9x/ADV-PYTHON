class student:
    def getdata(self):
        self.name = input("Kindly enter your name: ")
        self.rollno = int(input("Kindly enter your rollno: "))
        self.age = int(input("Kindly enter your age: "))
        self.percentage = float(input("Kindly enter your percentage: "))

    def displaydata(self):
        print("Your name is", self.name)
        print("Your roll no is", self.rollno)
        print("Your age is", self.age, "years")
        print("Your percentage is", self.percentage, "%")


print("\nEnter the details of student1.\n")
s1 = student()
s1.getdata()

print("\nEnter the details of student2.\n")
s2 = student()
s2.getdata()

print("\nDetails of student 1 are:\n")
s1.displaydata()

print("\nDetails of student 2 are:\n")
s2.displaydata()
