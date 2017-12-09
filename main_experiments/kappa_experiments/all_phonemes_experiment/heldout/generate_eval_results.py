import sys
import os
import errno

def create_dir(dir_name):
	try:
		os.makedirs(dir_name)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

phonemes = ("_").join(['N', 'rr', 'u', 'y', 'l', 'n'])

type = sys.argv[1]
base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/kappa_experiments/all_phonemes_experiment/heldout/"
score_combination_dir = base_dir + "features_combination/"
type_score_combination_filename = score_combination_dir + type
output_dir = score_combination_dir + "single/"
create_dir(output_dir)
score_combination_type_dir = output_dir + type + "/"
create_dir(score_combination_type_dir)

for current_phoneme in phonemes.split("_"):
	if current_phoneme in ['g', 'y', 'd', 'b', 'n']:
		output_filename = score_combination_type_dir + current_phoneme + "_lowercase"
	else:
		output_filename = score_combination_type_dir + current_phoneme
	with open(output_filename, "w") as output_file:
		with open(type_score_combination_filename, "r") as f:
			for line in f.readlines():
				words = line.split(" ")
				phoneme = words[2]
				if phoneme == current_phoneme:
					output_file.write(line)
