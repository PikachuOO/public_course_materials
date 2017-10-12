#!/usr/bin/python
import fileinput,re, collections

words = [word for line in fileinput.input() for word in re.findall(r'\w+', line.lower())]
word_counts = collections.defaultdict(int)
ngram_counts = collections.defaultdict(int)
n = 2
for ngram in [words[i:i+n] for i in range(0, len(words) - (n - 1))]:
    word_counts[ngram[0]] += 1
    ngram_counts[tuple(ngram)] += 1
print(ngram_counts)
print(word_counts)
for word in sorted(word_counts.keys()):
    following_word_counts = [(ngram_counts[ngram],ngram[1]) for ngram in list(ngram_counts.keys()) if ngram[0] == word]
    (following_word,frequency) = max(following_word_counts)
    print("%s(%s), %s(%s)" % (word,word_counts[word],following_word,frequency))
