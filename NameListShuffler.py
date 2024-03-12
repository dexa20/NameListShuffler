# Uclan ID - G21236306
# Name - Dinira Pathirana

import random
from pathlib import Path

# Reads all lines from the specified file and returns them as a list.
def read_lines_from_file(file_name):
    try:
        # Attempt to open the file in read ('r') mode
        with open(Path(__file__).parent / file_name, 'r') as file:

            # Read all lines from the file and store them in the 'lines' list
            lines = file.readlines()

        # Return the list of lines read from the file
        return lines

    # Handle the specific exception when the file is not found
    except FileNotFoundError:

        # Print an error message indicating the file was not found at the specified path
        print(f"Error: File not found at path '{file_name}'")

        # Return an empty list to signify that no lines were read (or handle it differently based on your needs)
        return []


# Writes the provided lines to the specified file.
def write_lines_to_file(file_name, lines):
    try:

        # Attempt to open the file in write ('w') mode
        with open(Path(__file__).parent / file_name, 'w') as file:

            # Write the joined lines to the file, separating them by newline characters
            file.write('\n'.join(lines))

    # Handle the specific exception when there is a permission error
    except PermissionError:

        # Print an error message indicating that permission is denied for writing to the specified file
        print(f"Error: Permission denied for writing to '{file_name}'")


# Trims whitespace from each line and retains the first 'limit' non-empty lines in the specified file.
def trim_lines(lines, limit, file_name):

    # Create a new list 'trimmed_lines' by stripping whitespace from each line
    # and taking only the first 'limit' non-empty lines
    trimmed_lines = [line.strip() for line in lines[:limit] if line.strip()]

    # Write the trimmed lines back to the specified file using the existing function
    write_lines_to_file(file_name, trimmed_lines)

    # Return the list of trimmed lines
    return trimmed_lines



# Generates a specified number of random combinations of first names and last names.
def generate_random_combinations(first_names, last_names, count):

    # List to store generated full names
    full_names = []

    # Sets to keep track of selected first and last names to ensure uniqueness
    selected_first_names = set()
    selected_last_names = set()

    # Loop 'count' times to generate the specified number of random combinations
    for _ in range(count):

        # Randomly choose a first name and strip leading/trailing whitespace
        random_first_name = random.choice(first_names).strip()

        # Ensure the selected first name is unique; choose another if needed
        while random_first_name in selected_first_names:
            random_first_name = random.choice(first_names).strip()
        selected_first_names.add(random_first_name)

        # Randomly choose a last name and strip leading/trailing whitespace
        random_last_name = random.choice(last_names).strip()

        # Ensure the selected last name is unique; choose another if needed
        while random_last_name in selected_last_names:
            random_last_name = random.choice(last_names).strip()
        selected_last_names.add(random_last_name)

        # Combine the selected first and last names to form a full name
        full_name = f"{random_first_name} {random_last_name}"

        # Add the generated full name to the list
        full_names.append(full_name)

    # Return the list of generated full names
    return full_names


#  Prints the number of lines before and after trimming, along with the file path.
def print_stats_before_and_after(file_name, original_count, trimmed_lines):

    # Print the number of lines before trimming and the file path
    print(f"Number of lines before trim ({file_name}): {original_count}")

    # Print the number of lines after trimming and the file path
    print(f"Number of lines after trim ({file_name}): {trimmed_lines}")


# Finds the longest names in the file specified by 'file_path'
def find_longest_names(file_name):

    # Read all lines from the file using the read_lines_from_file function
    names = [name.strip() for name in read_lines_from_file(file_name)]

    # Initialize variables to keep track of the maximum length and corresponding names
    max_length = 0
    max_length_names = []

    # Iterate through each name in the list
    for name in names:

        # Calculate the length of the current name
        current_length = len(name)

        # Check if the current name has more characters than the current maximum
        if current_length > max_length:

            # Update the maximum length and reset the list of names
            max_length = current_length
            max_length_names.clear()
            max_length_names.append(name)

        elif current_length == max_length:

            # If the current name has the same length as the maximum, add it to the list
            max_length_names.append(name)

    # Print the longest names and their length
    print(f"The longest names are: {max_length_names}")
    print(f"They have {max_length} characters.")


# Main function
def main():

    # Constants
    MAX_LINES = 4000
    FIRST_NAMES_FILE = 'firstNames.txt'
    LAST_NAMES_FILE = 'lastNames.txt'
    FULL_NAMES_FILE = 'FullNames.txt'

    try:
        # Read first names and last names from their respective files
        first_names = read_lines_from_file(FIRST_NAMES_FILE)
        last_names = read_lines_from_file(LAST_NAMES_FILE)

        # Trim the lists of names to the specified maximum number of lines
        trimmed_first_names = trim_lines(first_names, MAX_LINES, FIRST_NAMES_FILE)
        trimmed_last_names = trim_lines(last_names, MAX_LINES, LAST_NAMES_FILE)

        # Print statistics before and after trimming for both first and last names
        print_stats_before_and_after(FIRST_NAMES_FILE, len(first_names), len(trimmed_first_names))
        print_stats_before_and_after(LAST_NAMES_FILE, len(last_names), len(trimmed_last_names))

        # Generate random full names using the trimmed lists of first and last names
        random_full_names = generate_random_combinations(trimmed_first_names, trimmed_last_names, MAX_LINES)
        
        # Write the generated random full names to a file
        write_lines_to_file(FULL_NAMES_FILE, random_full_names)
        
        # Finds the longest names
        find_longest_names(FULL_NAMES_FILE)

    except Exception:
        print("ERROR FOUND IN PROGRAM!")

# This block ensures that the 'main' function is called only if the script is executed as the main program.
if __name__ == "__main__":
    main()
