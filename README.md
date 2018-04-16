# Random Name Generator

The goal of this project is to create a random name generator that learns from a data set of existing words (e.g. English dictionary, list of names, etc.) and establishes a Follow Likelihood Matrix to determine the likelihood of each letter to be the next one in a sequence. Since each next character only depends on the current character, random name generation can then be expressed as a Markov chain based on these likelihood values, and should result in mostly pronounceable names. The model can be trained on any plain-text list of words, which may yield different results in the random name generation.

## Data Set Sources
english-words-dwyl.txt: [https://github.com/dwyl/english-words/blob/master/words.txt](https://github.com/dwyl/english-words/blob/master/words.txt)

