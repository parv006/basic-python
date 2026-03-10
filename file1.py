import math
print("Welcome to the Menu!")
print("1. press if you want to be asked every time u enter a number to enter next number? ")
print("2. press if u want to input 'stop' when u want to stop adding numbers " )
print("3. Exit")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    print("You selected Option 1.")
      
elif choice == '2':
    print("You selected Option 2.")
       
elif choice == '3':
    print("Exiting. Have a great day!")

else:
    print("Invalid choice. Please select a valid option.")
x=1
li=[]
while x==1:
    p=input('enter your input(stop to break the loop if u selected option 2):  ')
    if choice=='1':
       print('do you want to continue adding numbers')
       x=int(input('write 1 for yes and 0 for no  '))
    elif choice=='2':
       print('')   
    
    li.append(p)
    if p=='stop':
        x=0       
if 'stop' in li:
    li.remove('stop')
        

print('here are your entered numbers')
print(li)
if len(li)<2:
    print('''you only entered 1 number , an arithematic operation can not be performed
           on 1 number''')
elif len(li)>=2:
    print('do you want to do arithematic operations on the given list')    
    xi=int(input('write 1 for yes and 0 for no'))
p=0
li1=[]
l=len(li)-1
for p in range(l):
   exp=input('''enter the symbol for mathematical operation you want to do in index ''' + 
            str(p) + ' and index ' + str(p+1) + ''' your options are:
                /,*,//,+,-,(),%,** ''')
   p=p+1
   li1.append(exp)       
print(li1)          
final=[0]
final = []
for r in range(len(li)):
    final.append(li[r])
    if r < len(li1):
        final.append(li1[r])

if 'stop' in final:
    final.remove('stop')

print("Updated 'final' list:", final)

def merge_to_expression(elements):
    expression = ""
    for i, elem in enumerate(elements):
       
        if i % 2 == 1:
            expression += f" {elem} "
        else:
            expression += str(elem)

    return expression

resulting_expression = merge_to_expression(final)
print("Arithmetic expression:", resulting_expression)
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

resulting_expression = merge_to_expression(final)
result = evaluate_expression(resulting_expression)
print("Arithmetic expression:", resulting_expression)
print("Result:", result)
