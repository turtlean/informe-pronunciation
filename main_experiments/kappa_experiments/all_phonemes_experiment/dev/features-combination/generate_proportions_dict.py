import os
import cPickle

factors = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

def all_phonemes_empty_dict(phonemes):
    return dict(zip(phonemes, [0.0 for p in phonemes]))

phonemes = [
	"Y", "f", "c", "x", "G", "d", "b", "g", 
	"z", "w", "N", "B", "rr", "u", "p", "D", 
	"y", "k", "m", "t", "l", "i", "r", "n", 
	"s", "o", "a", "e"
]

files = [
	'i_r',
	'n',
	'o',
	'p_D_y_k',
	's',
	't_l',
	'x_d_G_b_g_z_w_N_B_rr_u',
	'a',
	'e'
]

base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/kappa_experiments/all_phonemes_experiment/features-combination/"
output_filename = base_dir + "eers_dict_supervectors_dct"
eers_supervectors_dct = base_dir + "eers_supervectors_dct/"

factors_dict_dct = dict(zip(factors, [all_phonemes_empty_dict(phonemes) for f in factors]))

for phs in files:
	phonemes_factors_dir = eers_supervectors_dct + phs + "/"
	current_phonemes = phs.split("_")
	for factor in factors:	
		factor_filename = phonemes_factors_dir + str(factor)
		with open(factor_filename, "r") as f:
			lines = f.readlines()
			lines = [l.strip().split(":") for l in lines]
			lines = [l for l in lines if len(l)==2 ]
			lines = [[l[0], float(l[1])] for l in lines]
			for l in lines:
				for p in current_phonemes:
					if l[0] == p:
						factors_dict_dct[factor][p] = l[1]

with open(output_filename, "wb") as f:
	cPickle.dump(factors_dict_dct, f, protocol=2)