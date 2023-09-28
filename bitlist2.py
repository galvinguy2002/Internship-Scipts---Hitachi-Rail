import re


def map_col1_to_col2(col1_value):

    if re.match(r'[AB]\d+_(ON|OFF)LINEKE', col1_value):
        prefix = re.search(r'[AB]\d+_(ON|OFF)', col1_value).group()
        return f"mlkHotSby {prefix}"

    elif re.match(r'MISMATCH_C\d+', col1_value):
        return "mlkHotSby " + col1_value

    elif re.match(r'\d+(\.\d+)?UBHACK', col1_value):
        numeric_part = re.search(r'\d+(\.\d+)?', col1_value).group()
        numeric_part = numeric_part.replace('.', '/')
        return f"signalRoute UBHACK {numeric_part}"

    elif col1_value == "17AGMGKE":
        return "autoMode AGMGKE 17/117"

    else:
        return None


def main():
    col1_value = input("Enter value for Col1: ")
    col2_value = map_col1_to_col2(col1_value)
    if col2_value:
        print(f"Col1: {col1_value} -> Col2: {col2_value}")
    else:
        print("No valid mapping found for Col1 value.")


if __name__ == "__main__":
    main()
