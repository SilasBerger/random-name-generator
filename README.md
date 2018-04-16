# Random Name Generator
The goal of this project is to create a random name generator that learns from a data set of existing words (e.g. English dictionary, list of names, etc.) and establishes a Follow Likelihood Matrix to determine the likelihood of each letter to be the next one in a sequence. Since each next character only depends on the current character, random name generation can then be expressed as a Markov chain based on these likelihood values, and should result in mostly pronounceable names. The model can be trained on any plain-text list of words, which may yield different results in the random name generation.

## Usage
Install dependencies with pip:

`pip install -r requirements.txt`

### Generate Random Names
This script takes three parameters, in this order:<br>
`num_names:` number of names to be generated, *int, optional*<br>
`length:` the number of characters in each name, *int*<br>
`model_base_name:` the base name of the Markov model, without *_follow*, *_initial*, or *.npy* extension

Example - Generate 10 names with 6 characters each, using the model *english-words-dwyl*:

`python3 random_name_generator.py 10 6 english-words-dwyl`

Note: The model either has to be in the same directory, or the *model_base_name* must include the path to the model.

### Train a New Model
This script takes two parameters, in this order:<br>
`input_filename:` path to the training file (plain-text list of words)<br>
`output_file_basename:` the desired base name of the output Markov model, without *_follow*, *_initial*, or *.npy* extension

Example - Generate a model *models/english-words-dwyl* based on a list of words *data/english-words-dwyl.txt*:

`python3 markov_model_builder.py data/english-words-dwyl.txt models/english-words-dwyl`

This will create two files: *models/english-words-dwyl\_initial.npy* and *models/english-words-dwyl\_follow.npy*. For random name generation, the *model_base_name* will be *english-words-dwyl*. Note that this model already exists in this repo.

## Data Set Sources
english-words-dwyl.txt: [https://github.com/dwyl/english-words/blob/master/words.txt](https://github.com/dwyl/english-words/blob/master/words.txt)

