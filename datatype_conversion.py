#converting datatype

weekly_rate = input("Enter your weekly pay: ")

weekly_rate = float(weekly_rate)

print("Your weekly pay is", weekly_rate)

#See what the datatype is for a variable
print(type(weekly_rate))

# Display bi-weekly pay
print("Every two weeks you make", "$" + str(weekly_rate * 2) , "dollars" )

...

#In hw, do not hardcore. Get values from user. Remember to convert to a number datatype

num1 = 3
num2 = 5

print(num1, "*", num2, "=", num1 * num2 )
# Using exponents
print(num1**num2)