import re
import pandas as pd

def extract_cohesion_metrics(input_file, output_file):
    # Define a regex pattern to match class names and their cohesion percentages
    class_pattern = re.compile(r"Class: (\w+)" )
    total_pattern = re.compile(r"Total:\s*(\d+\.\d+)%")

    # Initialize lists to store extracted data
    class_names = []
    cohesion_percentages = []

    # Read the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Parse the file line by line
    for i, line in enumerate(lines):
        class_match = class_pattern.search(line)
        if class_match:
            class_name = class_match.group(1)

            # Look for the 'Total' percentage in subsequent lines
            for j in range(i+1, len(lines)):
                total_match = total_pattern.search(lines[j])
                if total_match:
                    cohesion_percentage = float(total_match.group(1))
                    class_names.append(class_name)
                    cohesion_percentages.append(cohesion_percentage)
                    break

    # Create a DataFrame
    data = pd.DataFrame({
        "Class Name": class_names,
        "Cohesion Percentage": cohesion_percentages
    })

    # Save to Excel
    data.to_excel(output_file, index=False)
    print(f"Data successfully extracted to {output_file}")

# Specify input and output files
input_file = "apache_tvm.txt"  # Replace with your input text file
output_file = "apache_tvm.xlsx"  # Replace with your desired output Excel file

# Call the function
extract_cohesion_metrics(input_file, output_file)
