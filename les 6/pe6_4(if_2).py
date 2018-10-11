import re

def new_password(oldpassword,newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6 and re.search('[0-9]',newpassword):
        return True
    else:
        return False

print(new_password('je','olwerer3werwk'))