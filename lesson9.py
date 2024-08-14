# def most_common_word_in_line(line):
#     words = line.lower().split()
#     word_counts = {}

#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1

#     most_common_word = max(word_counts, key=word_counts.get)
#     return most_common_word, word_counts[most_common_word]


# def main():
#     input_file_path = "l9.txt"
#     output_file_path = "result.txt"

#     with open(input_file_path, "r") as inf:
#         lines = inf.readlines()

#     with open(output_file_path, "w") as outf:
#         for line in lines:
#             most_common, count = most_common_word_in_line(line)
#             outf.write(f"{most_common} {count}\n")


# if __name__ == "__main__":
#     main()

import json
import csv

json_file_path = "employees.json"
csv_file_path = "employees.csv"


def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def json_to_csv(json_data, csv_file_path):
    if json_data:
        headers = json_data[0].keys()
    else:
        headers = []

    with open(csv_file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(json_data)


def add_employee_to_json(file_path, new_employee):
    employees = read_json(file_path)
    employees.append(new_employee)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(employees, file, ensure_ascii=False, indent=4)


def main():
    json_data = read_json(json_file_path)
    json_to_csv(json_data, csv_file_path)
    print(f"Данные успешно преобразованы и сохранены в {csv_file_path}")

    new_employee = {}
    new_employee["name"] = input("Введите имя сотрудника: ")
    new_employee["birthday"] = input("Введите дату рождения (дд.мм.гггг): ")
    new_employee["height"] = float(input("Введите рост (в см): "))
    new_employee["weight"] = float(input("Введите вес (в кг): "))
    new_employee["car"] = (
        input("Есть ли у сотрудника автомобиль? (да/нет): ").strip().lower() == "да"
    )

    languages = input("Введите языки программирования через запятую: ")
    new_employee["languages"] = [lang.strip() for lang in languages.split(",")]

    add_employee_to_json(json_file_path, new_employee)
    print("Новый сотрудник успешно добавлен в JSON файл.")


if __name__ == "__main__":
    main()
