import numpy as np
from statsmodels.sandbox.stats.runs import mcnemar
import cPickle
from sklearn.metrics import roc_curve
from scipy.optimize import brentq
from scipy.interpolate import interp1d
import cPickle

base_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/final_experiments/heldout/sanity_check_heldout/"
mcnemar_vectors_dir = base_dir + "mcnemar_vectors/"

mcnemar_supervectors_m_filename = mcnemar_vectors_dir + "supervectors/m"
mcnemar_dct_m_filename = mcnemar_vectors_dir + "dct/m"
mcnemar_features_combinations_m_filename = mcnemar_vectors_dir + "features_combination/k_m_t"

with open(mcnemar_supervectors_m_filename, "rb") as f:
    mcnemar_supervectors_m = cPickle.load(f)
with open(mcnemar_dct_m_filename, "rb") as f:
	mcnemar_dct_m = cPickle.load(f)
with open(mcnemar_features_combinations_m_filename, "rb") as f:
	mcnemar_fc = cPickle.load(f)

print mcnemar(mcnemar_supervectors_m['m'], mcnemar_fc['m'])
#print mcnemar(mcnemar_supervectors_m['m'], mcnemar_dct_m['m'])