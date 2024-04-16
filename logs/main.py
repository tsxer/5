from pathlib import Path
import collections

def parse_log_line(line: str) -> dict:
    splited = line.split()
    keys = ["date", "time", "lvl", "msg"]
    values = [splited[0], splited[1], splited[2], " ".join(splited[3:])]
    parced_line = dict(zip(keys, values))
    return parced_line

def load_logs(file_path: str) -> list:
    logs_lst = []
    try:
        with open(file_path, "r") as log_file:
            for line in log_file:
                logs_lst.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Помилка: файл журналу '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу журналу: {e}")
    return logs_lst

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = []
    print(f"Деталі логів для рівня '{level}':")
    for item in logs:
        if item["lvl"] == level:
            filtered_logs.append(item["date"] + " " + item["time"] + " - " + item["msg"])
    for item in filtered_logs:
        print(item)
  
def count_logs_by_level(logs: list) -> dict:
    counted_logs_by_level = collections.Counter()
    for item in logs:
        counted_logs_by_level[item["lvl"]] += 1
    return counted_logs_by_level

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for key, value in counts.items():
        print (f"{key.ljust(17)}| {value}")

