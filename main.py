# length is at least 6
# contains at least one digit
# contains at least one lowercase English character
# contains at least one uppercase English character
# contains at least one special character

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    password = list(password)
    isStrong = 0
    charsNeeded = 0
    hasLower = False
    hasUpper = False
    hasDigit = False
    hasSpecial = False
    for i in range(0, n):
        if(password[i].isdigit() and not hasDigit):
            hasDigit = True
            isStrong += 1
        if(password[i].islower() and not hasLower):
            hasLower = True
            isStrong = 1
        if(password[i].isupper() and not hasUpper):
            hasUpper = True
            isStrong += 1
        if(password[i] in "!@#$%^&*()-+" and not hasSpecial):
            hasSpecial = True
            isStrong += 1
            
    if(isStrong < 5):
        charsNeeded = max(6 - n, 4 - isStrong)
        return charsNeeded
    else:
        return charsNeeded

password = input()
n = len(password)
check = minimumNumber(n, password)
print(check)
