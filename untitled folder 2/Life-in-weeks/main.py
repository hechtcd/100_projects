#using math and f-strings to tell how many weeks are left till 90 years old
age = input()

years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
