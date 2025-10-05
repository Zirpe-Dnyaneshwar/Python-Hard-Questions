# charactor=eval(input("Entre Any Charactor : "))
# if (type(charactor)==int):
#     print('You Enter Integer type Value',charactor)
# elif(type(charactor)==str):
#     print("You Enter String Value", charactor)
# elif(type(charactor)==bool):
#     print("You Enter Boolean Value", charactor)
# elif(type(charactor)==complex):
#     print("You Enter Complex Value", charactor)
# elif(type(charactor)==float):
#     print("You Enter Float Value")
# else:
#     print("You Enter Incorrect Value ")



gender=input("Enter The Gender : ")
if gender=='Male' or gender=='male':
    print("Record Are Not available")
elif gender=='Female' or gender=='female':
    name=input("Please Enter Female Name : ")
    if name=='Neha' or name=='neha':
        print("Neha Working in TCS")
    elif name=='Priya' or name=='priya':
        print("Priya Working in Viprow")
    elif name=='Kamini' or name=="kamini":
        print('Kamini Working Tech Mahendra')
    else:
        print("Female Record are Not available")
else:
    print('Please Enter Correct Value ')