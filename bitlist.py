import re


def map_col1_to_col2(col1_value, name):

    if re.match(r'[AB]\d+_(ON|OFF)LINEKE', col1_value):
        return f"mlkHotSby {name} {name}"

    elif re.match(r'MISMATCH_C\d+', col1_value):
        return f"mlkHotSby {name} {name}"

    elif re.match(r'\d+(\.\d+)?UBHACK', col1_value):
        numeric_part = re.search(r'\d+(\.\d+)?', col1_value).group()
        numeric_part = numeric_part.replace('.', '/')
        return f"signalRoute UBHACK {numeric_part} {name}"

    elif col1_value == "17AGMGKE":
        return f"autoMode AGMGKE 17/117 {name}"

    else:
        return None


def main():
    name = input("Enter the name to be used in Col2: ")
    num_values = int(input("Enter the number of values in Col1: "))
    col1_values = []

    for i in range(num_values):
        value = input(f"Enter value {i+1} for Col1: ")
        col1_values.append(value)

    # Applying the mapping to each value in Col1
    for col1_value in col1_values:
        col2_value = map_col1_to_col2(col1_value, name)
        print(f"Col1: {col1_value} -> Col2: {col2_value}")


if __name__ == "__main__":
    main()
