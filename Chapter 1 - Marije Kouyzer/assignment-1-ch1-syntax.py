from collections import Counter

# read in English file
with open("./en_pud-ud-test.conllu") as f:
	english_pud = f.read()
english_raw_list = english_pud.split('\n')
english_list = []
for x in english_raw_list:
	if x:
		if x[0].isdigit():
			english_list.append(x.split('\t'))

# read in Spanish file
with open("./es_pud-ud-test.conllu") as g:
	spanish_pud = g.read()
spanish_raw_list = spanish_pud.split('\n')
spanish_list = []
for x in spanish_raw_list:
	if x:
		if x[0].isdigit():
			spanish_list.append(x.split('\t'))

# frequency of POS tags English
english_POS = []
for x in english_list:
	english_POS.append(x[3])
english_POS_count = Counter(english_POS)
english_POS_top_20 = english_POS_count.most_common(20)

# frequency of dependency labels of English
english_dependency_labels = []
for x in english_list:
	english_dependency_labels.append(x[7])
english_dependency_labels_count = Counter(english_dependency_labels)
english_dependency_labels_top_20 = english_dependency_labels_count.most_common(20)

# frequency of POS tags Spanish
spanish_POS = []
for x in spanish_list:
	spanish_POS.append(x[3])
spanish_POS_count = Counter(spanish_POS)
spanish_POS_top_20 = spanish_POS_count.most_common(20)

# frequency of dependency labels of Spanish
spanish_dependency_labels = []
for x in spanish_list:
	spanish_dependency_labels.append(x[7])
spanish_dependency_labels_count = Counter(spanish_dependency_labels)
spanish_dependency_labels_top_20 = spanish_dependency_labels_count.most_common(20)

# compare POS tags English and Spanish
print('Top 20 of English Part of Speech tags:')
for x in english_POS_top_20:
	print(x[0], '\t', x[1])
print()
print('Top 20 of Spanish Part of Speech tags:')
for x in spanish_POS_top_20:
	print(x[0], '\t', x[1])
print()

# compare dependency labels of English and Spanish
print('Top 20 of English dependency labels:')
for x in english_dependency_labels_top_20:
	print(x[0], '\t', x[1])
print()
print('Top 20 of Spanish dependency labels:')
for x in spanish_dependency_labels_top_20:
	print(x[0], '\t', x[1])
print()