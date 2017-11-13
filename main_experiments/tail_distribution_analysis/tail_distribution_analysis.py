import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import errno
sys.path.insert(0, os.path.expanduser("~") + '/pronunciation-scoring/code/toolkit')
import cPickle
from features import Features
from labels import Labels
from alignments import Alignments

phoneme = sys.argv[1]

lists_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/lists/dev/fold_n4/folds/"

def calculate_window(start, end, first_time, last_time):
	if start- 1 < first_time or end + 1 > last_time:
		if start - 0.5 < first_time or end + 0.5 > last_time:
			if start - 0.25 < first_time or end + 0.25 > last_time:
				if start - 0.1 < first_time or end + 0.1 > last_time:
					return 0
				return 0.1
			else:
				return 0.25
		else:
			return 0.5
	else:
		return 1

#generate alignments_dicc
alignments_dicc = {}
for i in range(1, 5):
	fold_str = "fold" + str(i)
	fold_filename = "nonnative_" + fold_str + "_alignments_eval"
	alignments_fold_file = lists_dir + fold_filename
	with open(alignments_fold_file, "r") as f:
		for line in f:
			line = line.strip().split()
			alignments_dicc[line[0]] = line[1]

## Loading alignments dicc
alignments_per_fold_dicc = {}
alignments_per_fold_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/read_filter_deltas_normalize/features_25_10_13/eval/"

#normalized_features, alignments, labels
for i in range(1,5):
	fold_str = "fold" + str(i)
	fold_filename = "read_filter_deltas_normalize_" + fold_str
	fold_filename = alignments_per_fold_dir + fold_filename
	with open(fold_filename, "rb") as f:
		_, alignments, _ = cPickle.load(f)
	alignments_per_fold_dicc[i] = alignments

refs_dicc = {}
for i in range(1, 5):
	fold_str = "fold" + str(i)
	fold_filename = "nonnative_" + fold_str + "_refs_eval"
	refs_fold_file = lists_dir + fold_filename
	with open(refs_fold_file, "r") as f:
		for line in f:
			line = line.strip().split()
			refs_dicc[line[0]] = line[1]

def main(type):
	if type == "correct":
		lists_samples_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/" + phoneme + "/correctly_tagged_lists/" 
		files_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/" + phoneme + "/correctly_tagged_files/" 
	else:
		lists_samples_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/" + phoneme + "/incorrectly_tagged_lists/" 
		files_dir = "/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/" + phoneme + "/incorrectly_tagged_files/" 

	corrects_files_dir = files_dir + "corrects/"
	incorrects_files_dir = files_dir + "incorrects/"

	corrects_alignments_dir = corrects_files_dir + "alignments/"
	incorrects_alignments_dir = incorrects_files_dir + "alignments/"
	corrects_labels_dir = corrects_files_dir + "labels/"
	incorrects_labels_dir = incorrects_files_dir + "labels/"
	corrects_waveforms_dir = corrects_files_dir + "waveforms/"
	incorrects_waveforms_dir = incorrects_files_dir + "waveforms/"
	corrects_trimmed_waveforms_dir = corrects_files_dir + "trimmed_waveforms/"
	incorrects_trimmed_waveforms_dir = incorrects_files_dir + "trimmed_waveforms/"

	waveforms_dir = "/Users/lmatayoshi/Documents/Projects/resources_tar_gz/dev-non-natives/waveforms/"

	try:
		os.makedirs(files_dir)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	try:
		os.system("rm -rf " + corrects_files_dir)
		os.system("rm -rf " + incorrects_files_dir)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	try:
		os.makedirs(corrects_files_dir)
		os.makedirs(incorrects_files_dir)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	try:
		os.makedirs(corrects_alignments_dir)
		os.makedirs(incorrects_alignments_dir)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	try:
		os.makedirs(corrects_labels_dir)
		os.makedirs(incorrects_labels_dir)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	try:
		os.makedirs(corrects_waveforms_dir)
		os.makedirs(incorrects_waveforms_dir)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	try:
		os.makedirs(corrects_trimmed_waveforms_dir)
		os.makedirs(incorrects_trimmed_waveforms_dir)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	corrects_samples_filename = lists_samples_dir + "corrects_lists"
	corrects_samples_dataframe = pd.read_csv(corrects_samples_filename)
	for logid in corrects_samples_dataframe['logid']:
		# Alignments
		os.system("cp " + alignments_dicc[logid] + " " + corrects_alignments_dir)
		os.system("gzip -df " + corrects_alignments_dir + logid + ".gz")
		# Labels
		os.system("cp " + refs_dicc[logid] + " " + corrects_labels_dir)
		# Waveforms
		session_number = int(logid[4:7]) / 100
		session_str = 'sess0' + str(session_number)
		waveform_path = waveforms_dir + logid[0:3] + "/" + session_str + "/"
		waveform_file_1 = waveform_path + logid + ".wv1"
		waveform_file_2 = waveform_path + logid + ".wv2"
		waveform_file_3 = waveform_path + logid + ".txt"
		os.system("cp " + waveform_file_1 + " " + waveform_file_2 + " " + waveform_file_3 + " " + corrects_waveforms_dir)

	incorrects_samples_filename = lists_samples_dir + "incorrects_lists"
	incorrects_samples_dataframe = pd.read_csv(incorrects_samples_filename)
	for logid in incorrects_samples_dataframe['logid']:
		# Alignments
		os.system("cp " + alignments_dicc[logid] + " " + incorrects_alignments_dir)
		os.system("gzip -df " + incorrects_alignments_dir + logid + ".gz")
		# Labels
		os.system("cp " + refs_dicc[logid] + " " + incorrects_labels_dir)
		# Waveforms
		session_number = int(logid[4:7]) / 100
		session_str = 'sess0' + str(session_number)
		waveform_path = waveforms_dir + logid[0:3] + "/" + session_str + "/"
		waveform_file_1 = waveform_path + logid + ".wv1"
		waveform_file_2 = waveform_path + logid + ".wv2"
		waveform_file_3 = waveform_path + logid + ".txt"
		os.system("cp " + waveform_file_1 + " " + waveform_file_2 + " " + waveform_file_3 + " " + incorrects_waveforms_dir)

	#alignments_per_fold_dicc[4]._alignments_per_logid['d02c300x'][21].get_symbol()

	#Iterate over dataframe rows and fill trimmed_waveforms folder
	#sox input.wav output.wav trim 0 00:35
	print "Corrects: "
	for index, row in corrects_samples_dataframe.iterrows():
		logid = row['logid']
		input_waveform = corrects_waveforms_dir + logid + ".wv1"
		# output_waveform = incorrects_trimmed_waveforms_dir + logid + "-" + str(position) + ".wav"
		position = row['position']
		output_waveform = corrects_trimmed_waveforms_dir + logid + "-" + str(position) + ".wav"
		fold = row['fold']
		alignment_instance = alignments_per_fold_dicc[fold]._alignments_per_logid[logid]
		alignment = alignment_instance[position]
		first_time = float(alignment_instance[alignment_instance.keys()[0]].get_start_time())/100
		last_time = float(alignment_instance[alignment_instance.keys()[-1]].get_end_time())/100
		print logid
		print alignment.get_symbol()
		print position
		# start one second before
		start = float(alignment.get_start_time())/100
		end = float(alignment.get_end_time())/100 
		window = calculate_window(start, end, first_time, last_time)
		start = start - window
		duration = (float(alignment.get_duration()))/100 + 2 * window
		print window
		print "\n"
		# finish one second after
		os.system("sox " + input_waveform + " " + output_waveform + " trim " + str(start) + " " + str(duration))
	print "\n"

	print "Incorrects: "
	for index, row in incorrects_samples_dataframe.iterrows():
		logid = row['logid']
		input_waveform = incorrects_waveforms_dir + logid + ".wv1"
		position = row['position']
		output_waveform = incorrects_trimmed_waveforms_dir + logid + "-" + str(position) + ".wav"
		fold = row['fold']
		alignment_instance = alignments_per_fold_dicc[fold]._alignments_per_logid[logid]
		alignment = alignment_instance[position]
		alignment = alignment_instance[position]
		first_time = float(alignment_instance[alignment_instance.keys()[0]].get_start_time())/100
		last_time = float(alignment_instance[alignment_instance.keys()[-1]].get_end_time())/100
		print logid
		print alignment.get_symbol()
		print position
		# start one second before
		start = float(alignment.get_start_time())/100
		end = float(alignment.get_end_time())/100 
		window = calculate_window(start, end, first_time, last_time)
		start = start - window
		duration = (float(alignment.get_duration()))/100 + 2 * window
		print window
		print "\n"
		os.system("sox " + input_waveform + " " + output_waveform + " trim " + str(start) + " " + str(duration))

	## COMBINED WAVEFORMS
	os.system("sox " + corrects_trimmed_waveforms_dir + "*.wav " + corrects_files_dir + "all_combined.wav" )
	os.system("sox " + incorrects_trimmed_waveforms_dir + "*.wav " + incorrects_files_dir + "all_combined.wav" )

main("correct")
main("incorrect")
