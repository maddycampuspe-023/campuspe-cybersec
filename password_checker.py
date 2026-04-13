import re
def check_password(password):
    score=0
    feedback=[]

    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("use at least 8 characters")
    
    if re.search(r"[A-Z]",password):
        score += 1
    else:
        feedback.append("use atleast one uppercase letter")
    
    if re.search(r"[a-z]",password):
        score +=1
    else:
        feedback.append("add lowercase letters ")
    
    if re.search(r"[0-9]",password):
        score +=1
    else:
        feedback.append("add atleast one number ")
    
    if re.search(r"[!@#$%^&*(),.?/:{}|<>]",password):
        score +=1
    else:
        feedback.append("use special characters")
    return score , feedback

def strength_level(score):
    if score <= 2 :
        return "week "
    elif score <= 4 :
        return "Medium"
    else :
        return "Strong "

if __name__ == "__main__" :
    print('password strength checker ')

    password = input("enter your password :")
    score,feedback = check_password(password)
    strength = strength_level(score)

    print(f"\n Strength: {strength}")
    print(f"Score:{score}/5")

    if feedback:
        print("\nReccomedation:")
        for f in feedback:
            print("-",f)
    else:
        print("\n your password is strong!")
