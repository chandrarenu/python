# def number(num=0):
#     print(num)
#     number(num+1)
    
# number()


#recreate the function for range using recursion

def print_range(start, end):
    
    if start > end:
     return
        
    print(start)
    print_range(start+1, end)
    
print_range(1,9)