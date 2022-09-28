

# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills ():
    skills=["coding", "python", "gaming"]
    return skills
    # (lailas answers) return ["coding", "python", "gaming"]]

#print (get_skills())

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    index=1
    print ("skills:")
    for skill in skills:
        print (index,skill)
        index= index+1
# (lailas answers)
'''print ("skills")
for index,skill in enumarate (skills, 1): 
    print(f"{index}. {skill}")'''
#the number one is it will start from 1 instead of 0
        #print (index,skill)
       
#show_skills(get_skills ())





# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    skill1= int (input("Choose a skill from above by entering its number:"))
    skill2= int (input("Choose another skill from above by entering its number:"))
    skillsinput=[skills[skill1-1], skills[skill2-1]]
    #the -1 so that the index is correct index 0 = 1 in list
    return (skillsinput)

    #laila answer you can use return=[skills[skill1-1], skills[skill2-1]]

#get_user_skills(get_skills())




# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skillsinput):
    name= input ("What's your name?")
    age=int(input ("How old are you?"))
    experience=int(input ("How many years of experience do you have?"))
    cv= {"name":name,
    "age":age,
    "experience": experience,
    "skills": get_user_skills(get_skills()) }
    return cv
    #print (cv)
 #lailas answer 
 '''cv={}
 cv["name]=input ("whats your name ?)
 cv ["age"]=int(input("age?")
 cv["experiemce"]=int(input(how many years exp?")
 cv["skills']= get_user_skills(get_skills)
 return cv"'''   
#get_user_cv(get_user_skills(get_skills()))

# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if cv["age"] >= 25: 
        if cv["age"]<= 40:
             if cv["experience"]>3:
                for skill in cv["skills"]:
                    if desired_skill == skill:
                        return True
                        # cv==True
                        #break
                else:
                    return False 
                    #cv==False
 #laila answers 
  ''' if  25 <= cv["age"] <= 40 and cv["experience"]>3 and desired_skill in cv["skills"]:
            return true 
        else :
            return False  
#check_acceptance(get_user_cv(get_user_skills(get_skills())),"python")'''

def main():
    print("Welcome to the special recruitment program")
    show_skills(get_skills())
    skillsinput= get_user_skills(get_skills())
    cv= get_user_cv
    check_acceptance((get_user_cv(skillsinput)), "python")
    if cv== True:
        print ("you have been accepted")
    else:
        print ("you werent accepted ")
    #laila answer 
    # use in instead of loop an dit will check in all the list 
    ''' skills=get_skills()
    user_cv=get_user_cv(skills)
    is_accepted= check_acceptance(user_cv, "python")
    if is_accepted:
        print(f"youve been accepted, {user_cv['name']}")
        else:
            print ("youve been rejected")'''       
    # Write your main logic here by combining the functions above into the
    # desired outcome
    
    
    
    
    ...
    


if __name__ == "__main__":
    main()
