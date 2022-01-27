
def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    try:
        score = float(input("Enter score:"))  
        grade = ""

        match score:
            case score if score >= 0.9:
                grade = "A"
            case score if score >= 0.8:
                grade = "B"
            case score if score >= 0.7:
                grade = "C"
            case score if score >= 0.6:
                grade = "D"
            case score if score < 0.6:
                grade = "F"
        
        print(grade)
    except:
        print("Bad score")



    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()