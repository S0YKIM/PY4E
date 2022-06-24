string = 'X-DSPM-Confidence: 0.8475'

pos = string.find(':')
# print(pos)
piece = string[pos + 1:]
# print(piece)
piece = float(piece)
print(piece)
