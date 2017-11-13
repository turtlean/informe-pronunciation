import matplotlib.pyplot as plt

supervectors_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/main_experiments/scatter-plots/data/heldout/supervectors/supervectors_single_phonemes/"
legendre_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/main_experiments/scatter-plots/data/heldout/legendre/legendre_single_phonemes/"
output_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/main_experiments/scatter-plots/data/heldout/output_legendre_2/"

all_phonemes = ["Y", "f", "c", "x", "G", "d", "b", "g", "z", "w", "N", "B", "rr", "u", "p", "D", "y", "k", "m", "t", "l", "i", "r", "n", "s", "o", "a", "e"]
positive_values = [9, 172, 89, 137, 37, 176, 115, 226, 29, 148, 205, 84, 107, 436, 332, 222, 559, 326, 677, 623, 744, 1094, 811, 1594, 1683, 1725, 2305, 2314]
negative_values = [1, 4, 38, 37, 149, 16, 91, 27, 220, 106, 112, 299, 391, 125, 261, 473, 143, 417, 168, 376, 362, 277, 597, 118, 115, 555, 479, 826]
positives_dict = dict(zip(all_phonemes, positive_values))
negatives_dict = dict(zip(all_phonemes, negative_values))

for phoneme in all_phonemes:
    original_phoneme = phoneme
    if phoneme in ['g', 'y', 'd', 'b', 'n']:
        phoneme = phoneme + "_lowercase"
    supervectors_filename = supervectors_dir + phoneme
    legendre_filename = legendre_dir + phoneme
    with open(supervectors_filename, "r") as f_supervectors:
        lines = f_supervectors.readlines()
        logids_supervectors = [line.split(" ")[0] for line in lines]
        scores_supervectors = [float(line.split(" ")[4]) for line in lines]
    with open(legendre_filename, "r") as f_legendre:
        lines = f_legendre.readlines()
        logids_legendre = [line.split(" ")[0] for line in lines]
        scores_legendre = [float(line.split(" ")[4]) for line in lines]
    if not logids_supervectors == logids_legendre:
        raise Exception(phoneme + " instances problem")
    plt.clf()
    plt.plot(scores_supervectors, scores_legendre, marker=".", linestyle="", color="blue")
    title = phoneme + " heldout, positives: " + str(positives_dict[original_phoneme]) + ", negatives: " + str(negatives_dict[original_phoneme])
    plt.xlabel("supervectors score")
    plt.ylabel("legendre score")
    plt.title(title)
    plt.savefig(output_dir + phoneme)