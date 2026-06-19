#input prompt
name =input("Enter you name: ").strip().lower()
age=int(input("Enter your age:"))
is_developer = bool(input("Are you a developer? (yes/no) :").strip().lower())

#logical conditional assignment
if age<18:
    tier = "Tier 3: Guest"
elif age>=18 and is_developer:
    tier = "Tier 1: Admin Infrastructure Access"
else:
    tier = "Tier 2: Standard Executive Acess"


#printout

print(f"""The final summary of the user is \n 
      Name: {name} \n 
      Age: {age} \n 
      Developer: {"Yes" if is_developer else "No"} \n
      Clearance Level: {tier}"""
      )