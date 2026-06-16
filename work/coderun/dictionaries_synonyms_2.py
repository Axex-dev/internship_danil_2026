number_of_pairs = int(input())
synonyms = {}
for i in range(number_of_pairs):
    word1, word2 = input().split()
    synonyms[word1] = word2.lower()
    synonyms[word2] = word1.lower()
print(synonyms[input()])