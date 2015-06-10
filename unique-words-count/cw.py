# load source text file
tm = open('timemachine.txt', 'r')

# word dictionary
dict = {}

for line in tm:
	# Remove punctuation and case
	line = line.strip()
	line = line.translate(None, '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
	line = line.lower()
	list = line.split(' ')
	# Count words
	for word in list:
		if word in dict:
			dict[word] = dict[word] + 1
		else:
			dict[word] = 1

# close source text file
tm.close()

# load result text file
result = open('result.txt', 'w')
for word,count in dict.iteritems():
	result.write(word + "," + str(count) + "\n")

# close result text file
result.close()