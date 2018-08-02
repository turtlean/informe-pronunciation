import sys

def string_for_column(value):
	if value[0] ==	"%":
		return "\\%" + value[1:]
	elif value[0:2] == "-%":
		return "-\\%" + value[2:]
	else:
		return value

mode = sys.argv[1]

filename, output_filename, mcnemar_phones = (None, None, None)
if mode == "features_combination":
	filename = "features_combination.csv"
	output_filename = "output_features_combination"
	mcnemar_phones = ['m', 's', 'y', 'o', 'l', 'e', 'n']
elif mode == "score_combination":
	filename = "score_combination.csv"
	output_filename = "output_score_combination"
	mcnemar_phones = ['m', 's', 'y', 'o', 'l', 'e', 'n', 'z', 't', 'rr']
else:
	raise ValueError("Invalid parameter. Should be features_combination or score_combination")

with open(filename, "r") as f:
	lines = f.readlines()

header = lines[0].strip().split(",")

n_columns = len(header)
colums_schema = "|c| |c|c|c|c|c|c| |c|c|c|c|c|c| |c|" 
first_line = "\\begin{tabular}{" + colums_schema + "}\n"
second_line = "\hline\n"

header = (" & ").join(header) + " \\\\ \hline\n"

end_line = "\\end{tabular}\n"

parsed_lines = []
for line in lines[1:]:
	line = line.strip().split(",")
	line = [string_for_column(value) for value in line]
	prefix = ""
	if line[0] in mcnemar_phones:
		prefix = "\\rowcolor{lightgray} "
	line = prefix + " & ".join(line) + " \\\\ \\hline\n"
	parsed_lines.append(line)

with open(output_filename, "w") as f:
	f.write(first_line)
	f.write(second_line)
	f.write(header)
	for line in parsed_lines:
		f.write(line)
	f.write(end_line)
