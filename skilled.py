


# n = len(t)
# m = len(w)

# time => O(n) 
# space => O(1)

def stringFinding(w,t):
	wordFind = 0
	lastWord = 0
	for i in range(len(t)):
		if t[i] == ' ':
			if w == (t[lastWord: lastWord + wordFind + 1]).strip(): 
				return True
			#print("*" + t[lastWord: lastWord + wordFind + 1] + "*")
			lastWord = i
			wordFind = 0

		else:
			wordFind += 1
	return False
		

print(stringFinding("nest","i built a nest and tested it "))
print(stringFinding("test","i built a nest and tested it "))

def stringFinding2(w,t):
	wordFind = 0
	lastWord = 0
	boolList = []
	t_dict = set(t.split(" "))

	for word in w:
		boolList.append(word in t_dict)
	return boolList

		

print(stringFinding2(["nest", "best", "test"],"i built a nest and tested it "))