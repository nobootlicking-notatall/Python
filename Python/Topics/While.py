# While Loop
# ----------
# The 'while' loop executes until a specific condition is met


count = 0
while count <= 5: # Execute the loop until the 'count' variable is lesser or equals to 5
    print(count) # 0 1 2 3 4 5
    count += 1 # Incrementing count's value by 1


max = 3
attempts = 0
while True:
    p = input("Enter password: ") # User input
    if p == "pswd":
        print("Access Granted")
        break # Exit loop if condition is met
    elif attempts == 2:
        print("Account Locked")
        break # Exit loop if 'attempt' count exceeds 2
    else:
        attempts += 1 # Increment the value of 'attempt' by 1
        print(f"Try again. Attempts remaining: {max-attempts}") # 3-1, 3-2, loop terminates


