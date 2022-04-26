#Write a function named divisible_by_three that accepts a number n and prints all numbers from 1 to n that are divisible by 3. 

divisible_by_three=int(input("Enter a number:"))
if(divisible_by_three%3==0):
    print("{} is divisible by:".format(divisible_by_three))
else:
        print("{} is not divisible by:".format(divisible_by_three))

        #Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list. Example:
#smallest([3,6,8,2,4,1,5,7]) returns 1
smallest=[3,4,5,6,10,8,1]
small=min(smallest)
print(small)

#Given the nested list x = [[1,2],[3,4],[5,6]], write a function that flattens the list and returns it as [1,2,3,4,5,6]
nestedlistx = [[1,2],[3,4],[5,6]]
flatlist=nestedlistx[0]+nestedlistx[1]+nestedlistx[2]
print(flatlist)

#Given list x = [100,110,120,130,140,150], use list comprehension to create another list containing each number in the list multiplied by 5.  
listx = [100,110,120,130,140,150]
newlist=[n*5 for n in listx]
print(newlist)

#Write a function that accepts list x below and uses a set to remove the duplicate letters and returns the list without duplicates
#x = ['a','b','a','e','d','b','c','e','f','g','h']
x = ['a','b','a','e','d','b','c','e','f','g','h']
xx=list(set(x))
print(xx)

#Write a function named divisible_by_seven that; using the range function and a for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.
divisible_by_seven=[]
for num in range(100,200):
    if(num%7==0):
        divisible_by_seven.append(num)
print(divisible_by_seven)

#Given this list of students containing age and name,  students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}], write a function that greets each student and tells them the year they were born. e.g Hello Eunice, you were born in the year 2002.
#students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
#std=students.update([])

#https://docs.google.com/document/d/1Dsvgf_SlY8NAZlHRY2j3ukwLAZhxQO5SKdRZMH82pnE/edit
def rectangle(width,height):
    area_of_a_rectangle= width*height
    perimetre = 2*(height+width)
    # print(input("area of a rectangle is : %2f" %area))
    print(input("perimetre of a rectangle is : %2f" %perimetre))
width =(float(input("Enter the width of a rectangle:")))
height =(float(input("Enter the height of a rectangle:")))
rectangle(width,height)









    
