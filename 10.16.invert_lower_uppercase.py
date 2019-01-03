# À partir de cette relation, écrivez une fonction qui convertit tous les caractères minuscules 
# en majuscules, et vice-versa (dans une phrase fournie en argument). 

inputSentence = "This IS aN EXAmpLe oF a reAlLy stRANge sentence À à Ý ý"
outputSentence = ""

# First try :
""" 
for i in inputSentence:
    c = ord (i)

    # don't change spaces
    if c == 32 or c == 160:
        outputSentence = outputSentence + chr (c)

    # without accent
    if c >= 65 and c <= 90 :                                        # uppercase change to lower / L = U + 32
        outputSentence = outputSentence + chr (c+32) 
    if c >= 97 and c <= 122 :                                       # lower change to upper / U = L - 32
        outputSentence = outputSentence + chr (c-32) 

    # with accent
    if c >= 192 and c <= 221 :                                      # uppercase change to lower / L = U + 36
        outputSentence = outputSentence + chr (c+36) 
    if c >= 224 and c <= 253 :                                      # lower change to upper / U = L - 36
        outputSentence = outputSentence + chr (c-36)
 """

# Second try - more optimized and beautiful :)
for c in inputSentence:
    i = ord (c)
    # without accent
    if i >= 65 and i <= 90 :                                        # uppercase change to lower / L = U + 32
        i += 32 
    if i >= 97 and i <= 122 :                                       # lower change to upper / U = L - 32
        i -= 32 
    # with accent
    if i >= 192 and i <= 221 :                                      # uppercase change to lower / L = U + 32
        i += 32 
    if i >= 224 and i <= 253 :                                      # lower change to upper / U = L - 32
        i -= 32                                                  
    outputSentence = outputSentence + chr (i)

print(inputSentence)
print(outputSentence)
