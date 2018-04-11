import nltk
from nltk import Nonterminal as NT
from nltk.grammar import PCFG
from nltk.corpus import ptb
from nltk import induce_pcfg
import pickle


productions = []
for i,tree in enumerate(ptb.parsed_sents()):
    tree.collapse_unary(collapsePOS = False)
    tree.chomsky_normal_form(horzMarkov = 2)
    productions += tree.productions()

S = NT('S')
grammar = induce_pcfg(S,productions)

with open('ptb_grammar.pcfg','wb')  as w:
    pickle.dump(grammar,w)

