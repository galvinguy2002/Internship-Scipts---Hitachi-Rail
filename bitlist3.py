import re


def map_col1_to_col2(col1_value, name, entry_number):
    if(entry_number % 32 != 0):
        entry_number = entry_number % 32

    if re.match(r'[AB]\d+_(ON|OFF)LINEKE', col1_value):
        prefix = re.search(r'[AB]\d+_(ON|OFF)', col1_value).group()
        return f"Bit {entry_number} mlkHotStandby {prefix} {name}"

    elif re.match(r'MISMATCH_C\d+', col1_value):
        return f"Bit {entry_number} mlkHotStandby {col1_value} {name}"

    elif re.match(r'\d+(\.\d+)?UBHACK', col1_value):
        numeric_part = re.search(r'\d+(\.\d+)?', col1_value).group()
        numeric_part = numeric_part.replace('.', '/')
        return f"Bit {entry_number} signalRoute UBHACK {numeric_part} {name}"

    else:
        return None


def main():
    name = input("Enter the Station name to be used in Column 2: ")
    num_entries = int(input("Enter the number of entries in Column 1: "))

    col1_values = []
    for i in range(num_entries):
        value = input(f"Enter value {i+1} for Column 1: ")
        col1_values.append(value)

    for i, col1_value in enumerate(col1_values, 1):
        col2_value = map_col1_to_col2(col1_value, name, i)
        if col2_value:
            print(f"Column 1: {col1_value} -> Column 2: {col2_value}")
        else:
            print(
                f"No valid mapping found for Column 1 value,::wrong input {col1_value}.")


if __name__ == "__main__":
    main()
