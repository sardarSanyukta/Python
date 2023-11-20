# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
current_age = int(age)
max_age = 90
left_age = max_age - current_age

no_of_days = (365 * left_age)
no_of_weeks = 52 * left_age
no_of_months = 12 * left_age

print(f"You have {no_of_days} days, {no_of_weeks} weeks, and {no_of_months}, months left.")
