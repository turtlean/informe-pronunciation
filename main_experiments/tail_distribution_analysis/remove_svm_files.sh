#!/bin/bash

# rm fold1/eval_results_fold fold1/log_eval fold1/svm_model
# rm fold2/eval_results_fold fold2/log_eval fold2/svm_model
# rm fold3/eval_results_fold fold3/log_eval fold3/svm_model
# rm fold4/eval_results_fold fold4/log_eval fold4/svm_model
# rm svm_eer_results
phoneme=$1
phoneme_dir="/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/$phoneme"
rm -rf "$phoneme_dir/histograms"
rm -rf "$phoneme_dir/eval_results"
