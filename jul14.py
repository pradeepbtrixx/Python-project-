
from difflib import SequenceMatcher 
import re

class most_tweeted_wordchecker:

	def longestSubstring(str1,str2):  
	    seqmatch = SequenceMatcher(None,str1,str2)  
	    match = seqmatch.find_longest_match(0, len(str1), 0, len(str2)) 
	    if (match.size >= 2): 
	        return str1[match.a: match.a + match.size]  
	    else:
	        False

	def most_tweeted_word(x):
	    d = x.lower()
	    a = re.findall(r'[\w]+',d)
	    data = {}
	    for i in a:
	        for j in a:
	            d = most_tweeted_wordchecker.longestSubstring(i,j)
	            if d in data:
	                data[d] += 1
	            else:
	                data[d] = 1

	    sort_orders = sorted(data.items(), key=lambda x: x[1], reverse=True)
	    print()
	    print()
	    print(f'THE MOST OCCURED WORD IN THIS TWEET IS : {sort_orders[1][0]}')

def main():
	while True:
		va = input('enter your tweet here : ').split(' ')
		if not va:
			break
		elif len(va)<=1:
			return 'please enter sequence of words'
			continue
		else:
			if va:
				most_tweeted_wordchecker.most_tweeted_word(str(va))
				D = input('DO YOU WANT TO CHECK FOR ANOTHER TWEET [Y/N] : ')
				if D == 'Y':
					continue
				else:
					return'THANK YOU SO MUCH FOR USING THIS CODE '


			
if __name__ == '__main__':
	print(main())






