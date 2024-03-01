import os
import csv

def read_data_from_files():
    data = []
    input_files = ["DATA.dat", "DATA1.dat"]
    for file in input_files:
        with open(file, "r") as f:
            next(f)
            for line in f:
                fields = line.strip().split("\t")
                if len(fields) != 7:
                    print("Issue with row: " + fields)
                    continue
                data.append(fields)
    return data

def calculate_salary(data):
    salaries = []
    for row in data:
        basic_salary = float(row[5])
        allowances = float(row[6])
        gross_salary = basic_salary + allowances
        row.append(str(gross_salary))
        salaries.append(gross_salary)
    salaries.sort()
    second_highest_salary = round(salaries[-2], 2)
    average_salary = round(sum(salaries) / len(salaries), 2)
    return second_highest_salary, average_salary

def write_to_csv(data, second_highest_salary, average_salary):
    with open("RESULT.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "first_name", "last_name", "email", "job_title", "basic_salary", "allowances", "Gross Salary"])
        writer.writerows(data)
        writer.writerow(["Second Highest Salary = " + str(second_highest_salary), "Average Salary = " + str(average_salary)])

def remove_duplicates(data):
    unique_data = []
    seen = set()
    for row in data:
        row_tuple = tuple(row[:-1])
        if row_tuple not in seen:
            unique_data.append(row)
            seen.add(row_tuple)
        else:
            print("Duplicate entry found: " + row)
    return unique_data

def file_processor():
    data = read_data_from_files()
    unique_data = remove_duplicates(data)
    second_highest_salary, average_salary = calculate_salary(unique_data)
    write_to_csv(unique_data, second_highest_salary, average_salary)

file_processor()
