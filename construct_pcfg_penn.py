import nltk
from nltk import  Nonterminal as NT
from nltk.grammar import PCFG
from nltk.corpus import treebank
from nltk import induce_pcfg
import pickle

productions = []
for item in treebank.fileids():
    for tree in treebank.parsed_sents(item):
        tree.collapse_unary(collapsePOS = False)
        tree.chomsky_normal_form(horzMarkov = 2)
        productions += tree.productions()

S = NT('S')
grammar = induce_pcfg(S, productions)

with open('penn_grammar.pcfg','wb') as w:
    pickle.dump(grammar,w)
