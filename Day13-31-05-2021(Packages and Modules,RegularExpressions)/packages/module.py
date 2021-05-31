#even or odd
def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd" 

    
#leapyears within a range
def leapyears(l,u):
    for year in range(l,u+1):
        if year%400==0 or (year%100!=0 and year%4==0):
            print(year,end=" ")            
            
#unique elements
def unique(l):
    li=[]
    for i in l:
        if l.count(i)==1:
            li.append(i)
    return li