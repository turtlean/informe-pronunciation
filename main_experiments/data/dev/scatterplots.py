import matplotlib.pyplot as plt

supervectors_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/main_experiments/scatter-plots/data/dev/supervectors/supervectors_single_phonemes/"
legendre_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/main_experiments/scatter-plots/data/dev/legendre/legendre_single_phonemes/"
output_dir = "/Users/lmatayoshi/Documents/Projects/tesis_notebooks/main_experiments/scatter-plots/data/dev/output/"

phonemes = ["Y", "f", "c", "x", "G", "d", "b", "g", "z", "w", "N", "B", "rr", "u", "p", "D", "y", "k", "m", "t", "l", "i", "r", "n", "s", "o", "a", "e"]
positive_values = [53, 682, 405, 590, 222, 773, 528, 887, 189, 743, 911, 428, 491, 1948, 1657, 920, 2453, 1708, 3234, 2938, 3505, 4929, 3650, 7152, 7555, 8040, 10144, 10597]
negative_values = [10, 10, 105, 153, 643, 89, 395, 114, 997, 500, 443, 1169, 1739, 482, 1055, 2009, 574, 1472, 686, 1542, 1373, 1238, 2617, 476, 480, 2077, 2069, 3484]
positives_dict = dict(zip(phonemes, positive_values))
negatives_dict = dict(zip(phonemes, negative_values))

#all_phonemes = ["Y", "f", "c", "x", "G", "d", "b", "g", "z", "w", "N", "B", "rr", "u", "p", "D", "y", "k", "m", "t", "l", "i", "r", "n", "s", "o", "a", "e"]
all_phonemes = ["Y", "f", "c", "x", "G", "d", "b", "g", "z", "w", "N", "B", "rr", "u", "p", "D", "y", "k", "m", "t", "l", "i", "r", "n", "s", "o"]

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
    title = phoneme + " dev, positives: " + str(positives_dict[original_phoneme]) + ", negatives: " + str(negatives_dict[original_phoneme])
    plt.xlabel("supervectors score")
    plt.ylabel("legendre score")
    plt.title(title)
    plt.savefig(output_dir + phoneme)

