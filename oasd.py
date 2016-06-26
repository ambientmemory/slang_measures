import numpy as np
'''
Runs the optimal string alignment distance algorithm
This computes the number of edit operations needed to
make the strings equal under the condition that no
substring is edited more than once
'''

def osa_dist(cn_word, sl_word):
	'''
	Computes the string distance using an extension
	of the Wagner-Fischer algorithm
	:param cn_word: Canonical or correct English word
	:param sl_word: Slang known English word
	:return: integer distance between two strings
	'''
	d = np.zeros((len(cn_word)+1,len(sl_word)+1))

	for i in range(0, len(cn_word)):
		d[i, 0] = i

	for j in range(0, len(sl_word)):
		d[0, j] = j

	for i in range(1, len(cn_word)):
		for j in range(1, len(sl_word)):
			if cn_word[i] == sl_word[j]:
				cost = 0
			else:
				cost = 1
			d[i, j] = min([d[i-1, j]+1,
			               d[i, j-1]+1,
			               d[i-1, j-1]+cost])
			if i>1 and j>1 and cn_word[i] == sl_word[j-1] and cn_word[i-1]==sl_word[j]:
				d[i, j] = min([d[i,j], d[i-2, j-2]+cost])
	return d[len(cn_word), len(sl_word)]


sl_word = input("Please enter slang word: ")
cn_word = input("Please enter canon word: ")
output = osa_dist(cn_word, sl_word)
print('Output of OASD is:'+'\n')
print(output)
