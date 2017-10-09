import string,sys
sys.setrecursionlimit(2000)

Scores={}
for c in string.ascii_lowercase: Scores[c]=1
for c in string.ascii_uppercase: Scores[c]=2

score = lambda string:(string,sum(Scores[c] for c in string if c in Scores)) #lambda function that generates (string,string score) tuple 
null_points = set((' ','.',',',';',':'))

def LCS(s1,s2,D=None,l1=0,e1=None,l2=0,e2=None,slen=None):
	if e1 is None:
		e1 = len(s1) #last index for string one
		e2 = len(s2) #last index for string 2
		slen = min(len(s1)-1,len(s2)-1)
		if D is None: D = {} #hashmap to dynamically store recursive results
	if (s1,l1,e1,l2,e2) in D: #return results of argument tuple if it has already been calculated
		return D[(s1,l1,e1,l2,e2)]
	if l1 == e1 or l2 == e2: # gets rid of weird edge case
		return ("",0) # if any indices are equal to each other  we will declare there is no subtring
	while s1[l1] in null_points and l1 < slen: l1+=1 #skips spaces for string 1 makes code slightly faster
	while s2[l2] in null_points and l2 < slen: l2+=1 #skips spaces for string 2 makes code slightly faster
	if s1[l1] == s2[l2]: # if the starts of both strings are equal
		item = score(((s1[l1] if s1[l1] not in null_points else "" )+LCS(s1,s2,D,l1+1,e1,l2+1,e2,slen)[0])) 
		D[(s1,l1,e1,l2,e2)] = item #you have to make a new string regardless I also want to push forward one index for each string;I also want the ends to stay the same
		return item
	else: # strings will start the same,different,or will be nothing
		lcs1 = LCS(s1,s2,D,l1,e1,l2+1,e2,slen)  # LCS of s1 and s2 remainder
		lcs2 = LCS(s1,s2,D,l1+1,e1,l2,e2,slen)   # LCS of s1 remainder and s2
		lcs = max(lcs1,lcs2,key=lambda Stuple:Stuple[1])
		D[s1,l1,e1,l2,e2] = lcs #returns the substring with the maximum length and score
		return lcs
