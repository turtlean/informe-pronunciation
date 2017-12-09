import sys
import os
import errno

def create_dir(dir_name):
	try:
		os.makedirs(dir_name)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

phonemes = ("_").join(['G', 'b', 'w', 'B', 'D', 'm', 'i', 's'])

type = sys.argv[1]
base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/kappa_experiments/heldout/"
sanity_checks_dir = base_dir + "sanity_checks/"
type_score_combination_filename = sanity_checks_dir + type
output_dir = base_dir + "score_single_phonemes/"
score_type_dir = output_dir + type + "/"
create_dir(score_type_dir)

for current_phoneme in phonemes.split("_"):
	if current_phoneme in ['g', 'y', 'd', 'b', 'n']:
		output_filename = score_type_dir + current_phoneme + "_lowercase"
	else:
		output_filename = score_type_dir + current_phoneme
	with open(output_filename, "w") as output_file:
		with open(type_score_combination_filename, "r") as f:
			for line in f.readlines():
				words = line.split(" ")
				phoneme = words[2]
				if phoneme == current_phoneme:
					output_file.write(line)
