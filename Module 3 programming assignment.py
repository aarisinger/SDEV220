#7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella"
things=["mozzarella", "cinderella", "salmonella"]

#7.5 Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
things[1] = "Cinderella"
print(things)
#Yes, it changed cinderella to Cinderella

#7.6 Make the cheesy element of things all uppercase and then print the list
things[0] = "MOZZARELLA"
print(things)
#Yes, it changed mozzarella to MOZZARELLA

#7.7 Delete the disease element from things, collect your Nobel Prize, and print the list
things.remove("salmonella")
print(things)

#9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione']
def good():
    print("Harry", "Ron", "Hermione")
good()
    
#9.2 Define a generator function called get_odds() that returns the odd numbers from range(10).
#    Use a for loop to find and print the third value returned
def get_odds():
    for number in range(10):
        if number %2 != 0:
            yield number
count = 0 
for odd_number in get_odds():
    count +=1
    if count == 3:
        print(f"The third odd number is: ", {odd_number})
        break
        


