from nltk.parse.generate import generate
from nltk import Nonterminal  as NT
import pickle
import os
import sys

n_sentence = 100

def get_rhslist(lhs):
    result = grammar.productions(lhs=lhs)
    rhslist = []
    probs = []
    for e in result:
        rhslist.append(e.rhs())
        probs.append(e.prob())
    return rhslist,probs

if os.path.exists('./penn_grammar.pcfg'):
    with open('./penn_grammar.pcfg') as r:
        grammar = pickle.load(r)
elif os.path.exists('./ptb_grammar.pcfg'):
    with open('./ptb_grammar.pcfg') as r:
        grammar = pickle.load(r)
else:
    print('Need to construct PCFG grammar file')
    sys.exit(1)

print('grammar loaded')
s = NT('S')

def update_sentence(sen):
    def sample_rhs(lhs):
        a,p = get_rhslist(lhs)
        c = np.random.choice(len(a),p=p)
        return a[c]
    def get_idx(sen):
        for k in range(len(sen)):
            if type(sen[k]) == type(NT('S')):
                return k
        return None
    def update(sen,idx):
        x = sample_rhs(sen[idx])
        sen = sen[:idx] + [e for e in x] + sen[idx+1:]
        return sen
    idx = get_idx(sen)
    while idx != None:
        sen = update(sen,idx)
        idx = get_idx(sen)
    return sen

with open('pcfg_ptb_sentences.txt','w') as w:
    for i in range(n_sentence):
        if i % 1000:
            print('%i/%i sentences generated'%(i,n_sentence))
        sentence = [s]
        sentence = update_sentence(sentence)
        sentence = " ".join(sentence)
        w.write(sentence)
        w.write("\n")

