import sys

phonemes = sys.argv[1]
features_type = sys.argv[2]

base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/kappa_experiments/score_combination/"
output_dir = base_dir + "single/" + features_type + "/"
phonemes_dir = base_dir + "original/" + features_type + "/"

for current_phoneme in phonemes.split("_"):
	if current_phoneme in ['g', 'y', 'd', 'b', 'n']:
		output_filename = output_dir + current_phoneme + "_lowercase"
	else:
		output_filename = output_dir + current_phoneme
	with open(output_filename, "w") as output_file:
		for fold in range(1, 5):
			fold_file = phonemes_dir + str(fold)
			with open(fold_file, "r") as f:
				for line in f.readlines():
					words = line.split(" ")
					phoneme = words[2]
					if phoneme == current_phoneme:
						output_file.write(line)