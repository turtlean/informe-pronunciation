#!/bin/bash

echo "Generating eval_results structure for histograms of phoneme $1"
phoneme_dir="/Users/lmatayoshi/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13/$1"
eval_results_dir="$phoneme_dir/eval_results"
mkdir $eval_results_dir
cp "$phoneme_dir/fold1/eval_results_fold" "$eval_results_dir/fold1"
cp "$phoneme_dir/fold2/eval_results_fold" "$eval_results_dir/fold2"
cp "$phoneme_dir/fold3/eval_results_fold" "$eval_results_dir/fold3"
cp "$phoneme_dir/fold4/eval_results_fold" "$eval_results_dir/fold4"