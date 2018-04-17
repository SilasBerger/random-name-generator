import numpy as np
import sys


# all lower-case chars as string
chars = "abcdefghijklmnopqrstuvwxyz"

# so we can use characters as array indices
INDEX_OFFSET = ord('a')
        

# generate random name with given length, for given model
def generate(length, model_base_name):
    # convert chars string into list of separate chars
    choices = []
    for c in chars:
        choices.append(c)

    # load numpy model parts
    initial = np.load(model_base_name + "_initial.npy")  # initial char likelihoods
    follow = np.load(model_base_name + "_follow.npy")  # follow likelihoods

    # find a random initial char
    current_char = initial_char(choices, initial)

    # start random name with initial char (as upper case)
    name = current_char.upper()

    # append length-1 follow-chars
    for i in range(length-1):
        follow_c = next_char(current_char, choices, follow)  # choose random next char, weighted by model, depending on current char
        name += follow_c  # append new char to name
        current_char = follow_c  # new char is now current char
        
    return name


# get next random char based on likelihoods for current char (given by loaded model)
def next_char(current, choices, model):
    likelihood_vector = model[char_to_index(current)]
    return np.random.choice(choices, p=likelihood_vector)


# get random starting char based on initial char likelihoods (given by loaded model)
def initial_char(choices, model):
    return np.random.choice(choices, p=model)


# convert char value to array index
def char_to_index(c):
    return ord(c) - INDEX_OFFSET


def main(argv):
    try:
        # check and parse cmd args
        if len(argv) == 2:
            length = int(argv[0])
            model_base_name = argv[1]
            num_names = 1  # assume 1 name by default
        elif len(argv) == 3:
            num_names = int(argv[0])
            length = int(argv[1])
            model_base_name = argv[2]
        else:
            raise ValueError("invalid number of arguments")

        # generate and print desired number of random names
        for i in range(num_names):
            print(generate(length, model_base_name))

    except Exception:
        print("Usage: random-name-generator.py [num_names=1] <length> <model_base_name>")
        exit(0)
    

if __name__ == "__main__":
    main(sys.argv[1:])