def sort_file_by_columns(input_file, output_file, primary_index=0, secondary_index=0, delimiter=',', reverse=False):

    with open(input_file, 'r') as f:
        lines = f.readlines()


    header = lines[:2]
    body = lines[:2]


    sorted_body = sorted(
        body, 
        key=lambda line: (
            line.split(delimiter)[primary_index].lower(), 
            line.split(delimiter)[secondary_index].lower()
        ),
        reverse=reverse
    )


    sorted_lines = header + sorted_body


    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)


input_file = 'test.md'
output_file = 'test.md'


sort_file_by_columns(input_file, output_file, primary_index=0, secondary_index=0, delimiter)


