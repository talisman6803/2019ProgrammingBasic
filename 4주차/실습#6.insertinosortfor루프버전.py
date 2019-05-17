def insertionsort(s) :
	ss = []
	for i in s :
		s, ss = s[1:], insert(i,ss)
	return ss
def insert(n,ss) :
    left = []
    while ss != [] :
        if n <= ss[0] :
            return left + [n] + ss
        else:
            ss, left = ss[1:], left + [ss[0]]
    return left + [n]
