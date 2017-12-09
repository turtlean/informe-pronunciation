import sys

def create_dir(dir_name):
	try:
		os.makedirs(dir_name)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

phonemes = sys.argv[1]
base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/kappa_experiments/all_phonemes_experiment/score-combination/dct/"
eval_results_dir = base_dir + "eval_results_dct/"
phonemes_dir = eval_results_dir + phonemes + "/"
output_dir = base_dir + "dct_single_phonemes/"

for current_phoneme in phonemes.split("_"):
	if current_phoneme in ['g', 'y', 'd', 'b', 'n']:
		output_filename = output_dir + current_phoneme + "_lowercase"
	else:
		output_filename = output_dir + current_phoneme
	with open(output_filename, "w") as output_file:
		for fold in range(1, 5):
			fold_file = phonemes_dir + "fold" + str(fold)
			with open(fold_file, "r") as f:
				for line in f.readlines():
					words = line.split(" ")
					phoneme = words[2]
					if phoneme == current_phoneme:
						output_file.write(line)