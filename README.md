# TCM_NER  (Charcter-enhanced TCM books NER)
This project is built on the project "[LexiconAugmentNER](https://github.com/v-mipeng/LexiconAugmentedNER)".
We incorporate information from lexicon and dictionary into the character representations to augment the performance.

# Source code description
## Requirement:
Python 3.6

Pytorch 0.4.1

[Jiayan0.0.21](https://github.com/jiaeyan/Jiayan)

## Input format:
With each character and its label split by a whitespace in a line. The "BIOES" tag scheme is prefered.

发 B-SYM 

热 E-SYM

汗 B-SYM

多 E-SYM

者 O


## Trained model
The best performance model can be downloaded from the link below:

[TCM_DSET](https://pan.baidu.com/s/1gNHknUq4XSjkkxLUanN0XQ) Extracting code:l3y3

[best model](https://pan.baidu.com/s/1OXJWpozUz7Y-nEQE3w7tfg) Extracting code:jl93


## Run the code:
1. Download the character embeddings and word embeddings from [Lattice LSTM](https://github.com/jiesutd/LatticeLSTM) and put them in the `data` folder.
2. Download the dataset from .
3. To train on the dataset:


4. To train/test your own data: modify the command with your file path and run.

