'''Andrew has a string N consisting of lowercase English letters representing respective grades of N 
students in his class. His grade is at Pth index. He can swap any two adjacent grades.
Your task is to help Andrew find and return a string value, representing maximized grade by 
bringing lexicographically smallest character on the Pth index after doing at most K swaps
Sample Input:
abcdefg
3
Sample Output:
a
2'''

n=int(input('total no of students: '))
input2=input('grades: ')
pos=int(input("andrew's grade: "))
grade=input2[n-1] #index of a student if n=6 abdrew g =3 [0,1,2,3,4]index ie,2
if (n-pos)>1: # diff b/w grade and pos = 0 ....6-3=3>1
    start=n-pos-1   # start=6-3-1=>2
else:
    start=0
if(n+pos<=len(input2)): #6+3<=6==>9<=6 
    end=n+pos
else:
    end=len(input2)     #end=6
print( min(input2[start:end],key=lambda x: ord(x)),pos)  #ord  func is to sort lowest to highest  
# lambda func is used to create a anonymous func

