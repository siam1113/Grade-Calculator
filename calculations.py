def get_the_numbers(total_subject, subject_numbers):
    count = 0
    while count < total_subject:
        subj_name = input(f"Subject Name {count} (First 5 letters) : ")
        total_number = int(input(f"Total number in {subj_name} : "))
        number_got = int(input(f"Your number in {subj_name} : "))
        grade = calculate_the_grade(total_number, number_got)

        # Storing information
        subject_numbers.append([subj_name, total_number, number_got, grade])

        # Subject count
        count += 1


def calculate_the_grade(total_num, num):
    percentage = (num * 100) / total_num
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A-"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage <= 40:
        return "F"


def get_over_all_result(subject_numbers):
    total_number_got = 0;
    total_number_of_subjects = 0;
    for subj in subject_numbers:
        total_number_of_subjects += subj[1]
        total_number_got += subj[2]

    # Total number and overall grade based on that
    overall_grade = calculate_the_grade(total_number_of_subjects, total_number_got)
    subject_numbers.append(["Total", total_number_of_subjects, total_number_got, overall_grade])