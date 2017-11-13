import sys

phonemes = sys.argv[1]
base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/main_experiments/scatter-plots/data/heldout/legendre/"
output_dir = base_dir + "legendre_single_phonemes/"
phonemes_file = base_dir + phonemes 

for current_phoneme in phonemes.split("_"):
	if current_phoneme in ['g', 'y', 'd', 'b', 'n']:
		output_filename = output_dir + current_phoneme + "_lowercase"
	else:
		output_filename = output_dir + current_phoneme
	with open(output_filename, "w") as output_file:
		with open(phonemes_file, "r") as f:
			for line in f.readlines():
				words = line.split(" ")
				phoneme = words[2]
				if phoneme == current_phoneme:
					output_file.write(line)