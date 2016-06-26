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
	