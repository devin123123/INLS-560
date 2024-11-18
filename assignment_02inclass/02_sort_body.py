def sort_lines(input_file, output_file):
    # Read all lines from the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Separate header and body
    header = lines[:2]          # First two lines are the header
    body = lines[2:]            # The rest are the body

    # Sort the body lines in reverse alphabetical order (case insensitive)
    sorted_body = sorted(body, key=lambda line: line.lower(), reverse=True)

    # Combine the header and the sorted body
    sorted_lines = header + sorted_body

    # Write the sorted lines to the output file
    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

# Specify the input and output file paths
input_file = 'md_list.md'
output_file = '00_results.md'

# Call the function to sort the lines
sort_lines(input_file, output_file)