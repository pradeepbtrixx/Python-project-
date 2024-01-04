
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

	def most_tweeted_word():
	    x = input('enter : ')
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
	    print(sort_orders[1][0])




most_tweeted_wordchecker.most_tweeted_word()




