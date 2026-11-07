def convert_to_alphabetical(grade, line):
    try:
        gradeint = int(grade)
    except:
        return "\ninvalid number on line: " + line + "\n"
    if gradeint>= 90:
        return "A"
    if gradeint < 90 and gradeint >= 75:
        return "B"
    if gradeint < 75 and gradeint >= 65:
        return "C"
    if gradeint < 65 and gradeint >= 50:
        return "D"
    if gradeint < 50 and gradeint >= 0:
        return "F"


def split_name_and_grade(theLine, nameOrGrade):
    grade_value = 1
    namesNgrades = theLine.split(" ")
    for i in range (0, len(namesNgrades)):
        for x in range (0, len(namesNgrades[i])):
            if namesNgrades[i][x].isnumeric():
                grade_value = i


    fullName = ""
    fullGrade = namesNgrades[grade_value]
    for y in range (0, grade_value):
        fullName = fullName + (namesNgrades[y]) + " "

    

    if nameOrGrade == "name":
        if namesNgrades[0] == "Class":
                return namesNgrades[1]
        else:
            return fullName #Gets the full name only
    if nameOrGrade == "grade":
        if not namesNgrades[0] == "Class":
            return fullGrade #Gets the grade only   
        else:
            return ""
    if nameOrGrade == "alpha":
        if not namesNgrades[0] == "Class":
            return convert_to_alphabetical(fullGrade, theLine) #Turns the numbers to alphabetical grades
        else:
            return "\n"


def write_to_file(nameOfFile, list_name):
    with open(nameOfFile, "w") as wfile:
        wfile.writelines(list_name)
    wfile.close()
    
final_grades_list = []

with open("grades_and_names.txt", "r") as file:
    for line in file:
        single_line = line.strip()

        final_grades_list.append(split_name_and_grade(single_line, "name") + split_name_and_grade(single_line, "grade") + " " + split_name_and_grade(single_line, "alpha")+"\n")
        
file.close()

print(final_grades_list)#debug

write_to_file("alphagrades.txt", final_grades_list)
