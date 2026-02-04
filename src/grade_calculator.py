def calculate_grade(marks):
    if len(marks) != 5:
        raise ValueError("Exactly 5 subject marks are required")

    avg = sum(marks) / 5

    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return grade


if __name__ == "__main__":
    marks = []
    for i in range(5):
        marks.append(int(input(f"Enter marks {i+1}: ")))

    avg, grade = calculate_grade(marks)
    print("Average:", avg)
    print("Grade:", grade)
