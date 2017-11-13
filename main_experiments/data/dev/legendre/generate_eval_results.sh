#!/bin/bash
echo "Copying eval results for $1"

base_dir="/home/turtle-monroe/pronunciation-scoring/spanish_adults/experiments_svms/output/exp1/svm_features_25_10_13"
results_dir="$base_dir/$1"
output_dir="$base_dir/eer_results"
phonemes_output_dir="$output_dir/$1"
mkdir $phonemes_output_dir

cp "$results_dir/fold1/eval_results_fold" "$phonemes_output_dir/fold1"
cp "$results_dir/fold2/eval_results_fold" "$phonemes_output_dir/fold2"
cp "$results_dir/fold3/eval_results_fold" "$phonemes_output_dir/fold3"
cp "$results_dir/fold4/eval_results_fold" "$phonemes_output_dir/fold4"
