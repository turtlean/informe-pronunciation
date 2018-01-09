import sys
import os
import errno

def create_dir(dir_name):
	try:
		os.makedirs(dir_name)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

phonemes = sys.argv[1]
kind = sys.argv[2]

if kind == "supervectors":
	base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/final_experiments/heldout/score_combination/"
	input_dir = base_dir + "supervectors/"
	input_filename = input_dir + phonemes
	output_dir = base_dir + "supervectors_single_phonemes/"
else:
	if kind == "features_combination":
		base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/final_experiments/heldout/features_combination/"
		input_dir = base_dir 
		input_filename = input_dir + phonemes
		output_dir = base_dir + "single/"
create_dir(output_dir)

for current_phoneme in phonemes.split("_"):
	if current_phoneme in ['g', 'y', 'd', 'b', 'n']:
		output_filename = output_dir + current_phoneme + "_lowercase"
	else:
		output_filename = output_dir + current_phoneme
	with open(output_filename, "w") as output_file:
		with open(input_filename, "r") as f:
			for line in f.readlines():
				words = line.split(" ")
				phoneme = words[2]
				if phoneme == current_phoneme:
					output_file.write(line)
