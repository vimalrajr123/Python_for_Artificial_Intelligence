class MultipleFunctions:

    def subfield():
        sub_fields = ["Machine Learning", "Neural Networks", "Vision", "Robotics","Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for l in sub_fields:
            print (l)

    def odd_even():
        num = int(input("Enter a number"))
        if num %2==0:
            print(f"{num} is Even number")
        else:
            print(f"{num} is Odd number")

    def eligible():
        gender = input("your Gender(Male/Female): ").capitalize()
        age = int(input("your Age: "))
        if gender=="Male" and age >= 21:
            print("Eligible")
        elif gender=="Male" and age < 21:
            print("Not Eligible")
        elif gender=="Female" and age >= 18:
            print("Eligible")
        elif gender=="Female" and age < 18:
            print("Not Eligible")   
        else:
            print("invalid gender or age")

    def percentage():
        sub_marks = 0
        marks = 0
        percentage = 0

        
        for i in range(5):
            marks = int(input(f"Subject {i+1}: "))
            sub_marks += marks
            
        print(f"Total : {sub_marks}")
        percentage = (sub_marks / 500) * 100
        print(f"Percentage : {percentage}")

    def calculate():
        height = 0
        breadth = 0
        h1 = 0
        h2 = 0
        b1 = 0

        height = int(input(f"Height : "))
        breadth = int(input(f"Breadth : "))
        print("Area formula: (Height*Breadth)/2")
        print(f"Area of Triangle : {(height*breadth)/2}")
        h1 = int(input(f"Height1 : "))
        h2 = int(input(f"Height2 : "))
        b1 = int(input(f"Breadth : "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print(f"Perimeter of Triangle : {h1+h2+b1}")