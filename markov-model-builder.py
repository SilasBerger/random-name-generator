import numpy as np
import sys
from tqdm import tqdm


# so we can use characters as array indices
INDEX_OFFSET = ord('a')


def train(file):
	# init counts with 0
	initial_state_vector = np.zeros(26, dtype=np.float32)
	follow_matrix = np.zeros([26, 26], dtype=np.float32)

	# iterate through lines in training set
	for line in tqdm(file):
		line = line.lower().strip()
		initial_state_vector[char_to_index(line[0])] += 1  # increment count for starting char in initial chars
		for c, c_follow in zip(line[0:-1], line[1:]):  # iterate through all chars of the line and their respective follow char
			follow_matrix[char_to_index(c), char_to_index(c_follow)] += 1  # increment count for "after c follows c_follow"

	initial_state_likelihood_vector = normalize(initial_state_vector)  # convert counts to likelihoods
	follow_likelihood_matrix = normalize(follow_matrix)  # convert counts to likelohoods (row-wise)
	return initial_state_likelihood_vector, follow_likelihood_matrix


# convert char value to array index
def char_to_index(c):
	return ord(c) - INDEX_OFFSET


def normalize(x):
	# normalize initial state vector
	if(len(x.shape) == 1):
		return x / x.sum()
	# otherwise, normalize follow matrix, row-wise
	for i in range(x.shape[0]):
		x[i] = x[i] / x[i].sum()
	return x 


# if args count doesn't match expected count, print usage and terminate
def verify_args_or_die(argv):
	if len(argv) != 2:
		print("Usage: markov-model-builder.py <input_filename> <output_filename_no_extension>")
		exit(0)


def main(argv):
	verify_args_or_die(argv)
	input_filename = argv[0]
	output_filename = argv[1]
	
	print("reading input file")
	with open(input_filename, "r") as infile:
		print("training Markov model")
		initial_states, follow = train(infile)
	
	print("saving model")
	# export np arrays
	np.save(output_filename + "_initial", initial_states)
	np.save(output_filename + "_follow", follow)
	
	print("done")


if __name__ == "__main__":
	main(sys.argv[1:])