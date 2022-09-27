

# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills ():
    skills=["coding", "python", "gaming"]
    return skills

#print (get_skills())

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    y= enumerate(skills)
    print (list(y))

#show_skills(get_skills ())





# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    skill1= int (input("Choose a skill from above by entering its number:"))
    skill2= int (input("Choose another skill from above by entering its number:"))
    skillsinput=[skills[skill1], skills[skill2]]
    return (skillsinput)

    
    #print (skillsinput)


   
    #return skillsinput

#get_user_skills(get_skills())




# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skillsinput):
    name= input ("What's your name?".capitalize())
    age=int(input ("How old are you?"))
    experience=int(input ("How many years of experience do you have?"))
    cv= {"name":name,
    "age":age,
    "experience": experience,
    "skills": skillsinput }
    return cv
    #print (cv)
    
#get_user_cv(get_user_skills(get_skills()))

# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if cv["age"] >= 25 & cv["age"] <= 40 & cv["experience"]>3:
        for skill in cv["skills"]:
            if skill == desired_skill:
                cv=True
            else:
                cv= False
    
#check_acceptance(get_user_cv(get_user_skills(get_skills())),"python")

def main():
    print("Welcome to the special recruitment program")
    skills=get_skills()
    

    # Write your main logic here by combining the functions above into the
    # desired outcome
    
    
    
    
    ...
    


if __name__ == "__main__":
    main()
