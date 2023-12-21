# #Write OOP classes to handle the following scenarios
# """ .A user can create and view 2D coordinates
#     .A user can find out the distance between 2 cordinates
#     .A user can  find the distance of a coordinate from origin
#     .A user can check if a point lies on a given line
#     .A user can find the distance between a given 2D point and 
#     a given line"""

# class Point:
#     def __init__(self,x,y):
#         self.x_cod = x
#         self.y_cod = y

#     def __str__(self):
#         return'<{},{}>'.format(self.x_cod,self.y_cod)
    
#     def euclidean_distance(self,other):
#         return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
#     def distance_from_origin(self):
#         #return (self.x_cod**2 + self.y_cod**2)**0.5
#         return self.euclidean_distance(Point(0,0))
    
    
# p1=Point(0,0)
# p2=Point(1,1)
# print(p1.euclidean_distance(p2))
# print(p1.distance_from_origin())
# #<x,y>
# # print(p1)
# # print(p2)


# class Line:

#     def __init__(self,A,B,C):
#         self.A =A
#         self.B =B
#         self.C =C

#     def __str__(self):
#         return '{}x + {} y + {} = 0'.format(self.A,self.B,self.C)

#     def point_on_line(line,point):
#         if line.A*point.x_cod+line.B*point.y_cod+line.C==0:
#             return "lies on the line"
#         else:
#             return "does not lies on the line"
        
#     def shortest_distance (line,point):
#         return(line.A*point.x_cod +  line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)
    
    
# l1=Line(1,1,-2)
# p1=Point(1,1)
# print(l1)
# print(p1)

# #print(l1.point_on_line(p1))
# print(l1.shortest_distance(p1))


#How objects access attributes

class Person:
    def __init__(self,name_input,country_input):
        self.name=name_input
        self.country=country_input

    def greet(self):
        if self.country=='India':
            print('Namaste,',self.name)
        else:
            print('Hello',self.name)

#how to acess attributes
p=Person('nitish','India')
print(p.name)
print(p.country)

#how to acess methods
print(p.greet())

#What if i try to acess non-existent attributes
#p.gender-->error

#Attribute creatin from outside the class
#using object you can create attribute outside the class
p.gender='male'
print(p.gender)

#Refrence Variable
"""Refrence variables hold the objects
   We can create objects without refrence vairable as well
   An object can have multiple refrence
   Assigning a new refrence variable to an exisiting object 
   does not create a new object """

# object without a refrence
class Person:
    
    def __init__(self):
        self.name ='nitish'
        self.gender ='male'

print(Person())
#p is not the object it is the refrence variable which contain the adress of the object
#that has been created
p=(Person())
print(p)
q=p

#Multiple ref
print(id(p))
print(id(q))

#change attribute value with the help of 2nd obj
print(p.name)
print(q.name)
#both point same obj make q change p also change bec q=p
q.name='ankit'
print(q.name)
print(p.name)


#Pass by refrence
#class obj input to the func
class Person:

    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
#outside the class it is a function
def greet(person):
    print("Hi my name is",person.name,'and I am',person.gender)
    #func return class obj (possible)
    p1=Person('ankit','male')
    return p1

p=Person('nitish','Male')
print(greet(p))
x=greet(p)
print(x.name,x.gender)


#object Ki Mutability
#when we make changes the adress not changes it is mutable
class Person:

    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

def greet(person):
    person.name='ankit'
    return person

p=Person('nitish','Male')
print(id(p))
p1=greet(p)
print(id(p1))


#Instance Vairable
#instance variable is a special kind of variable
#in which the value is depend on the object
#for every object the value of the instance variable is different

class Peson:
    def __init__(self,name_input,country_input):
        self.name=name_input
        self.country=country_input

p1=Person('nitish','India')
p2=Person('Yash','India')

print(p2.name)
print(p1.name)

#Encapsulation--> A data atribute and two method getter and setter 
#inshort data and method comb is known as encapsulation
#Getter-->show value outside
#setter->private value change from outside


class  Atm:
#constructor(special function)-->superpower->
    def __init__(self):
        print(id(self))
        self.pin = ''
        #__private
        self.__balance = 0
        #self.menu()
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,new_value):
        if type(new_value)==int:
            self.__balance=new_value
        else:
            print('Bhout marege')



    def __menu(self):
        user_input=input("""
    Hi how can I help You?
    1.Press 1 to create pin
    2.Press 2 to change pin
    3.Press 3 to check balance
    4.Press 4 to withdraw
    5.Aything else to exit 
                      """)
        if user_input== '1':
            #create pin
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
            #change pin
        elif user_input=='3':
            self.checek_balance()
            #check balance
        elif user_input=='4':
            self.withdraw()
            #check withdraw
        else:
            exit()

    def create_pin(self):
        user_pin=input("Enter your pin")
        self.pin=user_pin

        user_balance=int(input("enter balance"))
        self.__balance =user_balance

        print("pin created sucessfully")
        #self.menu()

    def change_pin(self):
       old_pin= input("enter old pin")
       
       if old_pin==self.pin:
           #let him change the pin
           new_pin=input("enter new pin")
           self.pin=new_pin
           print("pin change sucessful")
           #self.menu()
       else:
           print("wrong old pin")
           #self.menu()

    def checek_balance(self):
        user_pin=input("enter pin")
        if user_pin==self.pin:
            print("your balance is ",self.__balance)
            #self.menu()
        else:
            print('chal nikal')
    
    def withdraw(self):
        user_pin=input("enter pin")
        if user_pin==self.pin:
            #allow to withdraw
            amount=int(input("enter amount"))
            if amount<=self.__balance:
                self.__balance=self.__balance - amount
                print("Withdraw sucessful.balance is",self.__balance)
            else:
                print("insufficent balance")

        else:
            print('pass incorrect')
        #self.menu()

#obj=Atm()
# obj.create_pin()
# obj._Atm__balance = 'hehe'
# obj.withdraw()
obj=Atm()
#obj.create_pin()
print(obj.get_balance())
print(obj.set_balance(1000))
print(obj.get_balance())
print(obj.set_balance(1))


#Collection of objects

#list of Objecrs
class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

p1=Person('nitishh','male')
p2=Person('ankit','male')        
p3=Person('ankkita','female')

L=[p1,p2,p3]
for i in L:
    print(i.name,i.gender)

d={'p1':p1,'p2':p2,'p3':p3}
for i in d:
    print(d[i].gender)

#Static Varibles (Vs Instance variables)
#static variable:it is a class var . FOr all obj value is same (declares-inside class outside method)
#instance : obj var (declares inside constructor)fetch-obj(self.name).variablename
#need for static vars
    
class  Atm:
#constructor(special function)-->superpower->
    __counter = 1
    def __init__(self):
        print(id(self))
        self.pin = ''
        #__private
        self.__balance = 0
        self.cid=Atm.__counter
        Atm.__counter=Atm.__counter+1
        #self.menu()
    #utility function
    @staticmethod
    #when we use these dont need to create obj we can acees with class name.
    def get_counter():
        return Atm.__counter
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,new_value):
        if type(new_value)==int:
            self.__balance=new_value
        else:
            print('Bhout marege')



    def __menu(self):
        user_input=input("""
    Hi how can I help You?
    1.Press 1 to create pin
    2.Press 2 to change pin
    3.Press 3 to check balance
    4.Press 4 to withdraw
    5.Aything else to exit 
                      """)
        if user_input== '1':
            #create pin
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
            #change pin
        elif user_input=='3':
            self.checek_balance()
            #check balance
        elif user_input=='4':
            self.withdraw()
            #check withdraw
        else:
            exit()

    def create_pin(self):
        user_pin=input("Enter your pin")
        self.pin=user_pin

        user_balance=int(input("enter balance"))
        self.__balance =user_balance

        print("pin created sucessfully")
        #self.menu()

    def change_pin(self):
       old_pin= input("enter old pin")
       
       if old_pin==self.pin:
           #let him change the pin
           new_pin=input("enter new pin")
           self.pin=new_pin
           print("pin change sucessful")
           #self.menu()
       else:
           print("wrong old pin")
           #self.menu()

    def checek_balance(self):
        user_pin=input("enter pin")
        if user_pin==self.pin:
            print("your balance is ",self.__balance)
            #self.menu()
        else:
            print('chal nikal')
    
    def withdraw(self):
        user_pin=input("enter pin")
        if user_pin==self.pin:
            #allow to withdraw
            amount=int(input("enter amount"))
            if amount<=self.__balance:
                self.__balance=self.__balance - amount
                print("Withdraw sucessful.balance is",self.__balance)
            else:
                print("insufficent balance")

        else:
            print('pass incorrect')
        #self.menu()
c1=Atm()
c2=Atm()
c3=Atm()
Atm.get_counter()

print(c1.cid)
print(c2.cid)