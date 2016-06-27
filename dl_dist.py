import numpy as np
global debug;
debug= True
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

	#size of the alphabet required here
	da = np.zeros((26,))
	d = np.zeros((len(cn_word)+2, len(sl_word)+2))

	maxdist = len(cn_word)+len(sl_word)
	d[0,0] = maxdist

	for i in range(1, len(cn_word)+2):
		d[i, 0] = maxdist
		d[i, 1] = i-1
	for j in range(1, len(sl_word)+2):
		d[0, j] = maxdist
		d[1, j] = j-1
	#if debug:
	#	print("d initialized as: \n")
	#	print(d)

	for i in range(0, len(cn_word)):
		db = 0
		for j in range(0, len(sl_word)):
			k = da[ord(sl_word[j])%97]
			l = db
			if cn_word[i] == sl_word[j]:
				cost = 0
				db = j
			else:
				cost = 1
			d[i, j] = min([ d[i-1,j-1]+cost,
			                    d[i,j-1]+1,
			                    d[i-1,j] +1,
			                    d[k-1, l-1] + (i-k-1)+ 1 + (j-l-1)
			                    ])
			if debug:
				print("Debug: i = ", i, "\n")
				print("Debug: j = ", j, "\n")
				#print("Debug: da = ", da, "\n")
				print("Debug: db = ", db, "\n")
				print("Debug: d = \n")
				print(d)
		da[ord(cn_word[i])%97] = i


	return d[len(cn_word), len(sl_word)]


sl_word = input("Please enter slang word: ")
cn_word = input("Please enter canon word: ")
output = dl_dist(cn_word, sl_word)
print('Output of Damerau-Levenshtein is:'+'\n')
print(output)