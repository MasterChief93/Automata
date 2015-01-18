__author__ = 'MasterChief93'
from chomsky import chomsky

def find_prod(term,prod,char):
    all_term = []
    for pro in prod:
        if pro[1] in term and char == pro[1]:
            all_term.append(pro[0])
    return all_term

def cocke_younger_kasami(term,nonterm,prod,string):
    result = chomsky(term,nonterm,prod)
    term = result[0]
    nonterm = result[1]
    prod = result[2]
    recog_matrix = []
    for i in range(0,len(string)):
        recog_matrix.append([[]]*len(string))
    print recog_matrix
    k = 0
    for i in range(0,len(string)):
        recog_matrix[0][i] = string[i]
    for i in range(0,len(string)):
        recog_matrix[1][i] = find_prod(term,prod,string[i])
    print recog_matrix

term = ['a','b']
nonterm = ['S','A','B','C','D','E','F']
prod = [['S','CB'],['S','FA'],['S','FB'],['A','CS'],['A','FD'],['A','a'],['B','FS'],['B','CE'],['B','b'],['C','a'],['D','AA'],['E','BB'],['F','b']]

cocke_younger_kasami(term,nonterm,prod,'aababb')