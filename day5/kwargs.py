# def person(**details):
#     print(details)
#     print(details['name'])    #for name mtra print hunalai
# person(name="abc",age="13")



#task
#add more attribute and print in proper string 
def person(**details):
    
    print(f"""
          my name is{details['name']} , age is {details[31]} and I'm from {details['pokhara']}
          
          """)
    
    # age = details.get("age")
    # if age is not None:
    #  print(f"I am {age} years old.")
     
    # address = details.get("address")
    # if address is not None:
    #     print("f I am from {address} ")
        
print(name = "ram", age = 31, address = "pokhara")
    
 