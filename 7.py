def val_password(p:str)->bool:
    if len(p)<6:
        print("too short!")
        return False
    elif len(p)>16:
        print("too long!")
        return False
    else:
        small_char = False
        cap_char = False
        num = False
        special_char = False
        for i in p:
            if i>='a' and i<='z':
                small_char = True
            elif i>='A' and i<='Z':
                cap_char = True
            elif i>='0' and i<='9':
                num = True
            elif i in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                special_char = True
            if small_char and cap_char and num and special_char:
                return True
    if not small_char:
        print("Needs atleast 1 small character\n")
    if not cap_char:
        print("Needs atleast 1 capital character\n")
    if not num:
        print("Needs atleast 1 number\n")
    if not special_char:
        print("Needs atleast 1 special character\n")
    return False
print(val_password("      "))