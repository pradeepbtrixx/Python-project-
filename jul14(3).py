import re 
class most_react_tweets:

	@staticmethod
	def repeatedwordchecker(x = input('enter tweet:')):
		data = {}
		d = x.lower()
		a = re.findall(r'[\w]+',d)
		for i in a:
			if i in data:
				data[i] += 1
			else:
				data[i] = 1
		sort_orders = sorted(data.items(), key=lambda x: x[1], reverse=True)
		return f"most repeated word in the tweet is : {sort_orders[0][0]}"

if __name__ == "__main__":
print(most_react_tweets.repeatedwordchecker())


#===========================================================
from itertools import permutations
import re
x = '#Wise wish his #work #get organised. so that I can work in peace #WishMe'
d = x.lower()
a = re.findall(r'[\w]+',d)
d = ''.join(a)
#print(d)
f = [1,2,3]
g = permutations(d,2)
data = {}
for i in g:
    a,b = i
    s = a+b
    if s in data:
        data[s] += 1
    else:
        data[s] = 1

sort_orders = sorted(data.items(), key=lambda x: x[1], reverse=True)
print(sort_orders[0][0])
#=========================================================
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









