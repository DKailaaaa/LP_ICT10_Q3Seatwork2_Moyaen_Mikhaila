from pyscript import display, document

registered = "yes"
medical = "yes"
grade = 7
section = "Emerald"

# Check if the student is registered online
if registered != "yes":
    print("Please register online first.")

# Check if the student has medical clearance
elif medical != "yes":
    print("Please secure a medical clearance.")

# Check grade level and assign team
elif grade == 7:
    print("Congratulations!")
    print("Grade 7 -", section)
    print("You are part of the Yellow Tigers!")

elif grade == 8:
    print("Congratulations!")
    print("Grade 8 -", section)
    print("You are part of the Green Hornets!")

elif grade == 9:
    print("Congratulations!")
    print("Grade 9 -", section)
    print("You are part of the Blue Bears!")

elif grade == 10:
    print("Congratulations!")
    print("Grade 10 -", section)
    print("You are part of the Red Bulldogs!")

else:
    pass