# TCM_NER  (Charcter-enhanced TCM books NER)
This project is built on the project "[LexiconAugmentNER](https://github.com/v-mipeng/LexiconAugmentedNER)".
We incorporate information from lexicon and dictionary into the character representations to augment the performance.

# Source code description
## Requirement:
Python 3.6

Pytorch 0.4.1

Jiayan0.0.21

## Input format:
CoNLL format, with each character and its label split by a whitespace in a line. The "BMES" tag scheme is prefered.

别 O 

错 O

过 O

邻 O

近 O

大 B-LOC

鹏 M-LOC

湾 E-LOC

的 O

湿 O

地 O

## Pretrain embedding:
The pretrained embeddings(word embedding, char embedding and bichar embedding) are the same with [Lattice LSTM](https://www.aclweb.org/anthology/P18-1144)

## Run the code:
1. Download the character embeddings and word embeddings from [Lattice LSTM](https://github.com/jiesutd/LatticeLSTM) and put them in the `data` folder.
2. Download the four datasets in `data/MSRANER`, `data/OntoNotesNER`, `data/ResumeNER` and `data/WeiboNER`, respectively.
3. To train on the four datasets:



4. To train/test your own data: modify the command with your file path and run.

