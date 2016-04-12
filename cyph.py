# py Cypher
def sub(inAlph,outAlph, strin):
	if (len(inAlph)!=len(outAlph))
			return None
	else:
		strinList = list(strin)
		outstring = ''
		i = 0
		while i < len(strinList):
			outstring = outstring+outAlph[inAlph.find(strinList[i])]
			i = i+1
		return outstring

def makeSafe(strin, allowedChars):
	out = ''
	for e in strin.lower():
		if e in allowedChars:
			out = out + e
		else:
			continue
	return out

def phrase2key(strin):
	out = ''
	for e in strin:
		if e in out:
			continue
		else:
			out = out + e
	return out

def VigenereAlph(character,alph):
	pos = alph.find(character)
	return alph[pos:]+alph[:pos]

def VigenereAlphList(key,alph):
	charList = list(key)
	i = 0
	while i < len(charList):
		charList[i] = VigenereAlph(charList[i],alph)
		i = i + 1
	return charList


