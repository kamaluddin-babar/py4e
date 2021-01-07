

text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find('.')
#print(atpos)
finaltext = text[atpos-1 : ]
print(float(finaltext))
