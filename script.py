import re
from openpyxl import Workbook
def parse_report(report):
    # Regex to match entries with file paths and LOC
    file_pattern = re.compile(r"^(\S+.*?)\n.*?LOC: (\d+)", re.MULTILINE)
    # Extract file name and LOC
    data = []
    for match in file_pattern.finditer(report):
        file_path, loc = match.groups()
        class_name = file_path.split('/')[-1].replace('.py', '')
        data.append((class_name, int(loc)))
    return data
# Function to write data to an Excel file
def write_to_excel(data, filename):
    wb = Workbook()
    ws = wb.active
    ws.title = "Radon Report"
    ws.append(["Class Name", "LOC"])
    for class_name, loc in data:
        ws.append([class_name, loc])
    wb.save(filename)
# Read Radon report from a text file
def read_report_from_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()
# Filepath for the Radon report
report_file = "tensorflow_models.txt"
# Read, parse, and generate Excel output
radon_report = read_report_from_file(report_file)
data = parse_report(radon_report)
write_to_excel(data, "radon_report_tensorflow.xlsx")
print("Excel file 'radon_report.xlsx' has been created.")
