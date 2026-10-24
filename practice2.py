students_name = {"name":"Aliar", "age": 18, "grades":4.4,"name1":"Ali", "age1": 16, "grades1":3.9,"name2":"Alia", "age2": 21, "grades2":4.8,"name3":"Aisha", "age3": 21, "grades3":4.2,"name4":"Alia", "age4": 21, "grades4":4.6}

def  average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)



