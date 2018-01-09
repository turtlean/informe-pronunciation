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
print phonemes

base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/final_experiments/dev/"
features_combination_dir = base_dir + "features_combination/"
# type_feature_combination_filename = features_combination_dir + type
output_dir = features_combination_dir + "single/"
create_dir(output_dir)
# feature_combination_type_dir = output_dir + type + "/"
# create_dir(feature_combination_type_dir)

for current_phoneme in phonemes.split("_"):
	if current_phoneme in ['g', 'y', 'd', 'b', 'n']:
		output_filename = output_dir + current_phoneme + "_lowercase"
	else:
		output_filename = output_dir + current_phoneme
	with open(output_filename, "w") as output_file:
		for i in range(1, 5):
			fold_str = "fold" + str(i)
			features_combination_filename = features_combination_dir + phonemes + "/" + fold_str
			with open(features_combination_filename, "r") as f:
				for line in f.readlines():
					words = line.split(" ")
					phoneme = words[2]
					if phoneme == current_phoneme:
						output_file.write(line)
