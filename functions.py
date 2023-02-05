def calculating(a,b,operand):
    if (a.lstrip('-+').isnumeric() and b.lstrip('-+').isnumeric()):
        a = float(a)
        b = float(b)

        if operand =="+":
            result = a+b
        
        elif operand =="/":
            result = a/b

        elif operand =="-":
            result = a-b

        elif operand =="*":
            result = a*b
        
    else:
        result = "Please enter a valid number for a & b"
    
    return result

def quadratic_formula(a,b,c):
    if (a.lstrip('-+').isnumeric()) and (b.lstrip('-+').isnumeric()) and (c.lstrip('-+').isnumeric()):
        a = float(a)
        b = float(b)
        c = float(c)
        # Calculate discriminant
        discriminant = b**2 - 4*a*c

        # Get solutions, x^0.5 = square root
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)

        # Output
        result = (f"Solutions:\n {x1} \nand \n{x2}")
        return result
            
    else:
        result = "Please enter valid numbers"

    return result

def bmi(height, weight):
    if (height.isnumeric() and weight.isnumeric()):
        height = float(height)
        weight = float(weight)
        weight = weight * .453592 # converting pounds to kg

        BMI = weight / (height/100)**2
        BMI = round(BMI, 4)

        if BMI <= 18.4:
            result = f"BMI: {BMI} | You are underweight"
        elif BMI <= 24.9:
            result = f"BMI: {BMI} | You are healthy"
        elif BMI <= 29.9:
            result = f"BMI: {BMI} | You are over weight"
        elif BMI <= 34.9:
            result = f"BMI: {BMI} | You are severely over weight"
        elif BMI <= 39.9:
            result = f"BMI: {BMI} | You are obese"
        else:
            result = f"BMI: {BMI} | You are severely obese"

    else:
        result = "Please enter valid numbers"

    return result

def pythagorean_theorem(a,b,c):
    if (a.lstrip('-+').isnumeric()) and (b.lstrip('-+').isnumeric()) and (c.lstrip('-+').isnumeric()):
        result = "Please enter only 2 valid numbers"
        return result

    elif (a.lstrip('-+').isnumeric()) and (b.lstrip('-+').isnumeric()) and (c == ""):
        a = float(a)
        b = float(b)
        
        c = (a*a) + (b*b)
        c = c**(1/2)


        result = f"C = {c}"

    elif (c.lstrip('-+').isnumeric()) and (b.lstrip('-+').isnumeric()) and (a == ""):
        c = float(c)
        b = float(b)
        
        a = (c*c) - (b*b)
        a = a**(1/2)


        result = f"A = {a}"

    elif (c.lstrip('-+').isnumeric()) and (a.lstrip('-+').isnumeric()) and (b == ""):
        c = float(c)
        a = float(a)
        
        b = (c*c) - (a*a)
        b = b**(1/2)


        result = f"B = {b}"
            
    else:
        result = "Please enter valid numbers"

    return result
