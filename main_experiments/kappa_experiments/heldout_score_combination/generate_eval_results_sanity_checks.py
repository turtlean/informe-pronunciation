import os
import errno
import sys
import ipdb

def create_dir(dir_name):
	try:
		os.makedirs(dir_name)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

phonemes = "G_b_w_B_D_m_i_s"
features_type = sys.argv[1]

base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/kappa_experiments/heldout_score_combination/"
sanity_checks_dir = base_dir + "sanity_checks/"
output_dir = sanity_checks_dir + "single/" + features_type + "/"
create_dir(output_dir)
phonemes_filename = sanity_checks_dir + features_type 

for current_phoneme in phonemes.split("_"):
	if current_phoneme in ['g', 'y', 'd', 'b', 'n']:
		output_filename = output_dir + current_phoneme + "_lowercase"
	else:
		output_filename = output_dir + current_phoneme
	with open(output_filename, "w") as output_file:
		with open(phonemes_filename, "r") as f:
			for line in f.readlines():
				words = line.split(":")
				if current_phoneme == words[0]:
					output_file.write(line)