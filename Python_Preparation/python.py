
# finds the duplicates

def function_one():
    # Create all the variables 
    #list_one = y
    list_one = [1,2,4,4,3,4,5,7]
    list_two = []
    
    for a in range(0,len(list_one)):
        print(a)
        for b in range(a+1,len(list_one)):
            print(b)
            if list_one[a]== list_one[b]:
                print("finds a duplicate")
                return 0

#y=[]
#y=input("please enter an array")
#print(y[0],"h")
function_one()
#print(z)



RESULT:
  0
1
2
3
4
5
6
7
1
2
3
4
5
6
7
2
3
finds a duplicate
