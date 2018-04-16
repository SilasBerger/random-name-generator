import numpy as np
import sys


chars = "abcdefghijklmnopqrstuvwxyz"

# so we can use characters as array indices
INDEX_OFFSET = ord('a')
        

def generate(length, model_base_name):
    choices = []
    for c in chars:
        choices.append(c)

    initial = np.load(model_base_name + "_initial.npy")
    follow = np.load(model_base_name + "_follow.npy")
    current_char = initial_char(choices, initial)
    name = current_char.upper()
    for i in range(length-1):
        follow_c = next_char(current_char, choices, follow)
        name += follow_c
        current_char = follow_c
    return name


def next_char(current, choices, model):
    likelihood_vector = model[char_to_index(current)]
    return np.random.choice(choices, p=likelihood_vector)


def initial_char(choices, model):
    return np.random.choice(choices, p=model)


def char_to_index(c):
    return ord(c) - INDEX_OFFSET


def main(argv):
    try:
        if len(argv) == 2:
            length = int(argv[0])
            model_base_name = argv[1]
            num_names = 1
        elif len(argv) == 3:
            num_names = int(argv[0])
            length = int(argv[1])
            model_base_name = argv[2]
        else:
            raise ValueError("invalid number of arguments")

        for i in range(num_names):
            print(generate(length, model_base_name))
    except Exception:
        print("Usage: random-name-generator.py <length> <model_base_name>")
        exit(0)
    

if __name__ == "__main__":
    main(sys.argv[1:])