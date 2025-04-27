import os
import re
import math
import csv

def analyze_code(directory):
    operators = set()
    operands = set()
    total_operators = 0
    total_operands = 0
    total_lines = 0

    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.php', '.js', '.html', '.css')):
                with open(os.path.join(subdir, file), 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    code = ''.join(lines)
                    ops = re.findall(r'[\+\-\*/=<>!]+', code)
                    ids = re.findall(r'\b\w+\b', code)

                    operators.update(ops)
                    operands.update(ids)
                    total_operators += len(ops)
                    total_operands += len(ids)
                    total_lines += len([line for line in lines if line.strip() != ''])  # Non-empty lines

    # Halstead Metrics
    n1 = len(operators)
    n2 = len(operands)
    N1 = total_operators
    N2 = total_operands

    vocabulary = n1 + n2
    length = N1 + N2
    volume = length * math.log2(max(vocabulary, 1)) if vocabulary > 0 else 0
    difficulty = (n1 / 2) * (N2 / n2) if n2 > 0 else 0
    effort = difficulty * volume

    # Ask for defects manually
    print("\n------------------------")
    print("Analysis Complete!")
    print("------------------------")
    print(f"Total Lines of Code (LOC): {total_lines}")
    print(f"Program Vocabulary (n): {vocabulary}")
    print(f"Program Length (N): {length}")
    print(f"Program Volume (V): {volume:.2f}")
    print(f"Program Difficulty (D): {difficulty:.2f}")
    print(f"Program Effort (E): {effort:.2f}")

    defects = input("Enter number of known defects/bugs: ")
    try:
        defects = int(defects)
        defect_density = defects / (total_lines / 1000) if total_lines else 0
        print(f"Defect Density (bugs per 1000 LOC): {defect_density:.2f}")
    except ValueError:
        print("Invalid input for defects, skipping defect density calculation.")

    # Export to CSV
    with open('software_quality_report.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Metric", "Value"])
        writer.writerow(["Total LOC", total_lines])
        writer.writerow(["Program Vocabulary", vocabulary])
        writer.writerow(["Program Length", length])
        writer.writerow(["Program Volume", f"{volume:.2f}"])
        writer.writerow(["Program Difficulty", f"{difficulty:.2f}"])
        writer.writerow(["Program Effort", f"{effort:.2f}"])
        if isinstance(defects, int):
            writer.writerow(["Defect Density (bugs/1000 LOC)", f"{defect_density:.2f}"])

    print("\n✅ Report saved as 'software_quality_report.csv'!")

# Main Execution
if __name__ == "__main__":
    project_directory = input("Enter the path to your project folder: ")
    analyze_code(project_directory)
