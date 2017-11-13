import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import errno
import copy

phoneme = sys.argv[1]

histogram_output_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/" + phoneme + "/histograms/" 

correctly_tagged_output_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/" + phoneme + "/correctly_tagged_lists/" 

incorrectly_tagged_output_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/" + phoneme + "/incorrectly_tagged_lists/" 

try:
	os.makedirs(histogram_output_dir)
except OSError as exception:
	if exception.errno != errno.EEXIST:
		raise

try:
	os.makedirs(correctly_tagged_output_dir)
	os.makedirs(incorrectly_tagged_output_dir)
except OSError as exception:
	if exception.errno != errno.EEXIST:
		raise

n_negatives_per_phoneme = {
	"Y": 10,
	"f": 10,
	"c": 105,
	"x": 153,
	"G": 643,
	"d": 89,
	"b": 395,
	"g": 114,
	"z": 997,
	"w": 500,
	"N": 443,
	"B": 1169,
	"rr": 1739,
	"u": 482,
	"p": 1055,
	"D": 2009,
	"y": 574,
	"k": 1472,
	"m": 686,
	"t": 1542,
	"l": 1373,
	"i": 1238,
	"r": 2617,
	"n": 476,
	"s": 480,
	"o": 2077,
	"a": 2069,
	"e": 3484
}

n_positives_per_phoneme = {
	"Y": 53,
	"f": 682,
	"c": 405,
	"x": 590,
	"G": 222,
	"d": 773,
	"b": 528,
	"g": 887,
	"z": 189,
	"w": 743,
	"N": 911,
	"B": 428,
	"rr": 491,
	"u": 1948,
	"p": 1657,
	"D": 920,
	"y": 2453,
	"k": 1708,
	"m": 3234,
	"t": 2938,
	"l": 3505,
	"i": 4929,
	"r": 3650,
	"n": 7152,
	"s": 7555,
	"o": 8040,
	"a": 10144,
	"e": 10597
}


def plot_and_save_histogram(positives_negatives, output_file):
	n_bins = 25
	percentil = 0.05
	positives_negatives = [ line.strip() for line in positives_negatives ]
	positives_negatives = [ line.split() for line in positives_negatives ]
	n_instances = len(positives_negatives)
	positives_negatives_distances = [ float(line[4]) for line in positives_negatives ]
	positives_negatives_labels = [ line[3] == 'True' for line in positives_negatives]

	counts_positives_negatives, bins_positives_negatives, patches_positives_negatives = plt.hist(positives_negatives_distances, n_bins)

	positives = []
	negatives = []
	for i in range(0, n_instances):
	    if positives_negatives_labels[i]:
	        positives.append(positives_negatives_distances[i])
	    else:
	        negatives.append(positives_negatives_distances[i])

	#############
	# POSITIVES # 
	#############

	total_positives = len(positives)
	n_positives, bins_positives, patches_positives = plt.hist(positives, bins=bins_positives_negatives)
	plt.clf()
	normalized_positives = n_positives/total_positives

	#############
	# NEGATIVES #
	#############

	total_negatives = len(negatives)
	n_negatives, bins_negatives, patches_positives = plt.hist(negatives, bins=bins_positives_negatives)
	normalized_negatives = n_negatives/total_negatives

	normalized_bins = []
	for i in range(0, len(bins_positives_negatives) - 1):
		mean = (bins_positives_negatives[i] + bins_positives_negatives[i+1]) / 2
		normalized_bins.append(mean)


	plt.clf()

	## Graficar los percentiles 
	draw_positive_percentiles(n_positives, bins_positives, normalized_bins, percentil)
	draw_negative_percentiles(n_negatives, bins_negatives, normalized_bins, percentil)

	plt.title("Phoneme: " + phoneme + ". Positives: " + str(n_positives_per_phoneme[phoneme]) + ", Negatives: " + str(n_negatives_per_phoneme[phoneme]) + ", percentil: " + str(percentil))
	plt.plot(normalized_bins, normalized_positives, color="red", label="positives")   
	plt.plot(normalized_bins, normalized_negatives, color="blue", label= "negatives")
	plt.legend()
	plt.xticks(normalized_bins, rotation='vertical')
	plt.tight_layout()
	plt.savefig(output_file)
	plt.clf()

def draw_positive_percentiles(values, bins, normalized_bins, percentil):
	covered_instances = 0
	total = sum(values)
	for i in range(len(values)):
	    percentil_index = i
	    covered_instances = covered_instances + values[i]
	    if covered_instances >= total * percentil:
	        break
	text = "Positives tail: " + str(int(sum(values[:percentil_index + 1]))) + " instances"
	y_position = values[percentil_index] / float(total)
	xy = (normalized_bins[percentil_index], y_position)
	xy_text = (normalized_bins[0], y_position)
	plt.annotate(text, xy=xy, xytext=xy_text)
	plt.axvline(x=normalized_bins[percentil_index], linestyle="--", color="black", linewidth=.75)

def draw_negative_percentiles(values, bins, normalized_bins, percentil):
	covered_instances = 0
	total = sum(values)
	for i in range(1, len(values)+1):
	    percentil_index = i
	    covered_instances = covered_instances + values[-i]
	    if covered_instances >= total * percentil:
	        break

	text = "Negatives tail: " + str(int(sum(values[-percentil_index:]))) + " instances"
	y_position = values[-percentil_index] / float(total)
	xy = (normalized_bins[-percentil_index], y_position)
	xy_text = (normalized_bins[-percentil_index-2], y_position)
	plt.annotate(text, xy=xy, xytext=xy_text)

	plt.axvline(x=normalized_bins[-percentil_index], linestyle="--", color="black", linewidth=.75)

def histograms_per_fold():
	n_folds = 4
	for i in range(1, n_folds + 1):
		base_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/" + phoneme + "/"
		fold_str = 'fold' + str(i)
		output_file = output_dir + fold_str
		fold_dir = fold_str + '/'
		dir = base_dir + fold_dir + "eval_results_fold"
		with open(dir) as f:
		    positives_negatives = f.readlines()
		plot_and_save_histogram(positives_negatives, output_file)

def generate_lists(folds_dicc, type, base_dir):
	percentil = 0.05

	# fold annotation. To which fold does the instance belong?
	for k,v in folds_dicc.iteritems():
		v = [line + " " + str(k) for line in v]
		folds_dicc[k] = v

	positives_negatives = []
	for v in folds_dicc.values():
		positives_negatives = positives_negatives + v

	## PRE-PROCESSING
	positives_negatives = [ line.strip() for line in positives_negatives ]
	positives_negatives = [ line.split() for line in positives_negatives ]
	positives = [ line for line in positives_negatives if line[3] == 'True']
	negatives = [ line for line in positives_negatives if line[3] == 'False']
	positives = np.array(positives)
	negatives = np.array(negatives)

	columns = ['logid', 'position', 'phoneme', 'label', 'score', 'fold']

	## POSITIVES
	positives_dataframe = pd.DataFrame(data=positives, columns=columns)
	positives_dataframe['score'] = positives_dataframe['score'].apply(pd.to_numeric)
	if type == "correct":
		positives_dataframe = positives_dataframe.sort_values('score', ascending=False)
	else:
		positives_dataframe = positives_dataframe.sort_values('score')
	total_positives = positives.shape[0]
	percentil_positives = int(total_positives * percentil)
	positives_dataframe = positives_dataframe[['logid','position', 'score', 'fold']][:percentil_positives]
	positives_filename = base_dir + "corrects_lists"
	positives_dataframe.to_csv(positives_filename, index=False, header=True)

	## NEGATIVES
	negatives_dataframe = pd.DataFrame(data=negatives, columns=columns)
	negatives_dataframe['score'] = negatives_dataframe['score'].apply(pd.to_numeric)
	if type == "correct":
		negatives_dataframe = negatives_dataframe.sort_values('score')
	else:
		negatives_dataframe = negatives_dataframe.sort_values('score', ascending=False)
	total_negatives = negatives.shape[0]
	percentil_negatives = int(total_negatives * percentil)
	negatives_dataframe = negatives_dataframe[['logid', 'position', 'score', 'fold']][:percentil_negatives]
	negatives_filename = base_dir + "incorrects_lists"
	negatives_dataframe.to_csv(negatives_filename, index=False, header=True)


def generate_histograms_and_lists():
	base_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/" + phoneme + "/eval_results/" 
	output_file = histogram_output_dir + phoneme + "_all_folds"
	n_folds = 4
	integrated_histogram = []
	folds_dicc = {}
	for i in range(1, n_folds+1):
	    filename = base_dir + "fold" + str(i)
	    with open(filename) as f:
	    	folds_dicc[i] = f.readlines()

	positives_negatives = []
	dicc_values = folds_dicc.values()
	for v in dicc_values:
		positives_negatives = positives_negatives + v
	plot_and_save_histogram(positives_negatives, output_file)
	generate_lists(copy.deepcopy(folds_dicc), "correct", correctly_tagged_output_dir)
	generate_lists(copy.deepcopy(folds_dicc), "incorrect", incorrectly_tagged_output_dir)

# histograms_per_fold()
os.system("./generate_eval_results.sh " + phoneme)
generate_histograms_and_lists()
print "Plotted histograms for phoneme " + phoneme
