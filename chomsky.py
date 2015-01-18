__author__ = 'MasterChief93'
from unit_prods import unitprod

def check(prod):
    for pro in prod:
        if len(pro[1]) > 2:
            return 0
    return 1

def create_new(nonterms):
    newterm = 'A'
    while True:
        if newterm in nonterms:
            newterm = chr(ord(newterm) + 1)
        if newterm not in nonterms:
            nonterms.append(newterm)
            return newterm


def chomsky(term,nonterm,prod):
    result = unitprod(term,nonterm,prod)
    terms = result[0]
    nonterms= result[1]
    prods = result[2]
    W = []
    W.extend(nonterms)
    R = []
    for pro in prods:
        if pro != ['S','e']:
            R.append(pro)
    while True:
        for i in range(0,len(R)):
            if len(R[i][1][1:]) >= 2:
                for symb in R[i][1]:
                    newnonterm = create_new(nonterms)
                    if R[i][1][1:] != '':
                        R.append([R[i][0],R[i][1][0] + newnonterm])
                        R.append([newnonterm,R[i][1][1:]])
                        R.remove(R[i])
        if check(R):
            break
    while True:
        for i in range(0,len(R)):
            if len(R[i][1]) == 2:
                for symb in R[i][1]:
                    if symb in term:
                        newnonterm = create_new(nonterms)
                        R[i][1] = R[i][1].replace(symb,newnonterm)
                        R.append([newnonterm,symb])
        if check(R):
            break

    return [term,W,R]
    # for production in R:

term = ["+","x",'(',')','a']
nonterm = ["S","T","F"]
prod = [["S","S+T"],["S","T"],["T","TxF"],["T","F"],["F","(S)"],["F","a"]]


#print chomsky(term,nonterm,prod)
