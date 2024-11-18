def sort_lines(input_file, output_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()


    sorted_lines = sorted(lines, key=lambda line: line[13].lower())

    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

input_file = 'md_list.md'
output_file = '01_results_13.md'

sort_lines(input_file, output_file)