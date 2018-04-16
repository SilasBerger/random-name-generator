# Random Name Generator

The goal of this project is to create a random name generator that learns from a data set of existing words (e.g. English dictionary, list of names, etc.) and establishes a Follow Likelihood Matrix to determine the likelihood of each letter to be the next one in a sequence. Random name generation can then be expressed as a Markov chain based on these likelihood values, and should result in mostly pronounceable names. To create different styles of names (say, English-sounding, German-sounding, ...), the model can be trained on different sets of words.

## Data Set Sources
english-words-dwyl.txt: [https://github.com/dwyl/english-words/blob/master/words.txt](https://github.com/dwyl/english-words/blob/master/words.txt)

