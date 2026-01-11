import string

def strengthen(pw):
    def length(p):
        if len(p) >= 8:
            return "Length: ok"
        else:
            lack = 8 - len(p)
            return f"Password only has {len(p)} characters. Add {lack} or more"
    def upper_lower(p):
        upper = []
        lower = []
        for item in p:
            if item in string.ascii_uppercase:
                upper.append(item)
        for item in p:
            if item in string.ascii_lowercase:
                lower.append(item)
        if len(upper) > 0:
            if len(lower) > 0:
                return "Uppercase and lowercase letters: ok"
            else:
                return "Add at least 1 lowercase letter"
        elif len(lower) > 0:
            if len(upper) > 0:
                return "Uppercase and lowercase letters: ok"
            else:
                return "Add at least 1 uppercase letter"
        else:
            return "Password needs to have at least 1 uppercase and 1 lowercase letter"
    def digits(p):
        digit = []
        for item in p:
            if item in string.digits:
                digit.append(item)
        if len(digit) > 0:
            return "Digits: ok"
        else:
            return "Password needs to have at least 1 digit"
    def punctuation(p):
        punctuate = []
        for item in p:
            if item in string.punctuation:
                punctuate.append(item)
        if len(punctuate) > 0:
            return "Punctuation: ok"
        else:
            return "Password needs to have at least 1 punctuation"
    return f"{length(pw)}\n{upper_lower(pw)}\n{digits(pw)}\n{punctuation(pw)}"
password = input("Enter password: ")
print(strengthen(password))
