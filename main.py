from tabulate import tabulate
from calculations import get_the_numbers, get_over_all_result

totalSubject = int(input("Total subject : "))
subjNums = []

# Table Headers
head = ["Subjects", "Total Number", "Number Got", "Grade"]

if __name__ == '__main__':
    get_the_numbers(totalSubject,subjNums)
    get_over_all_result(subjNums)
    print(tabulate(subjNums, headers=head, tablefmt="grid"))
