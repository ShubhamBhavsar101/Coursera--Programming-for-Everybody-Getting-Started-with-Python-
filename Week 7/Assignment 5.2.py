# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below. 

largest = None
smallest = None

while True:
    no = input("Enter No or done if done")
    if no == 'done':
        break
    
    try:
        no = int(no)
    except:
        print("Invalid input")
        continue
    
    if largest is None or largest < no:
        largest = no
    if smallest is None or smallest > no:
        smallest = no
        
print("Maximum is", largest)
print("Minimum is", smallest)

# Enter 7, 2, bob, 10, and 4 one by one after pressing enter on each and type "done" and enter on last.