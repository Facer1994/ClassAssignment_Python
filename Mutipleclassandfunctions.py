class SubfieldsInAI:
    def Subfields():
        a =['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for val in a:
            print(val)
            
class OddEven:
    def OddEven():
        num =int(input("Enter a number:" ))
        if(num%2==1):
            print(num ,"is  Odd number")
        else:
            print(num, "is  Even number")
        
class EligibilityForMarriage:
    def Elegible():
        gender =input("Your Gender :")
        age =int(input("Your Age: "))
        gender_List =['Male','male','Female','female']
        for a in gender_List:
            if((gender in gender_List) and (age>=21)):
                print("ELIGIBLE")
                break
            else:
                print("NOT ELIGIBLE")
        
class FindPercentage:
    def percentage():
        Subject1 =int(input("Subject1= "))
        Subject2 =int(input("Subject2= "))
        Subject3 =int(input("Subject3= "))
        Subject4 =int(input("Subject4= "))
        Subject5 =int(input("Subject5= "))
        Total = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total :" ,Total)
        Percentage= (Total)/5
        print(Percentage)
    
class  triangle:
    def triangle():
        Height = int(input("Height: "))
        Breadth = int(input("Breadth: "))
        print("Area formula: Height*Breadth)/2")
        print("Area of Triangle:" ,(0.5*Breadth*Height))
        Height1 = int(input("Height1: "))
        Height2 = int(input("Height2: "))
        Breadth1 = int(input("Breadth: "))
        Perimeter_formula=Height1+Height2+Breadth1
        print("Perimeter formula: Height1+Height2+Breadth1")
        print("Perimeter of Triangle: ",Perimeter_formula)