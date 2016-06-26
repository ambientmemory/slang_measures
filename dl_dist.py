import numpy as np
'''
Builds over the OASD (Optimal String Alignment Dist)
to compute the Damerau-Levenshtein distance with
adjacent string transpositions. OASD assumes that
no substring is edited once but DL-distance assumes
that substrings can also be edited multiple times
'''

def dl_dist(cn_word, sl_word):
	'''
	Computes true Damerau-Levenshtein distance
	with adjacent transpositions
	:param cn_word: canonical English word (~OED)
	:param sl_word: Slang English word (~Urban Dict)
	:param (hidden): size of alphabet (sigma)
	:return: int distance
	'''

	#second parameter here is the size of the alphabet
	d_canon = np.zeros((1, 26))
	d = np.zeros((len(cn_word)+1, len(sl_word)+1))

	maxdist = len(cn_word)+len(sl_word)
	d[0,0] = maxdist

	for i in range(0, len(cn_word)):
		d[i, 0] = maxdist
		d[i, 1] = i
	for j in range(0, len(sl_word)):
		d[0, j] = maxdist
		d[1, j] = j

	for i in range(1, len(cn_word)):
		d_slang = 0
		for j in range(1, len(sl_word)):
			k = d_canon[sl_word[j]]
			l = d_slang
			if cn_word[i] == sl_word[j]:
				cost = 0
				d_slang = j
			else:
				cost = 1
			d[i+1, j+1] = min([ d[i,j]+cost,
			                    d[i+1,j]+1,
			                    d[i,j+1] +1,
			                    d[k, l] + (i-k-1)+ 1 + (j-l-1)
			                    ])
		d_canon[cn_word[i]] = i
	return d[len(cn_word)+1, len(sl_word)+1]	