def divider():
    num1=int(input("enter two number: "))
    num2=int(input("enter two number: "))
    if num1 == 5:
        raise Exception("Input Number cannot be 5 ")
    print(num1/num2)
        
while True:
    try:
        divider()
        
    except ZeroDivisionError:
        print('cannot divide any number by 0')
        
    # except ValueError:
    #     print('Invalid Input must intger number')
    except Exception as e:
         print('something went',e)

