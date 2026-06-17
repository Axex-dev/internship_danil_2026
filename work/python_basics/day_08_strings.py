def search_word(word, text1):
    if  word in text1:return True
    else: return False
text = input("Enter a text: ")
if text == "": text = "Hello World, I am very happy to learn Python!"
print(search_word(word=input("Введите слово: "), text1=text))
clean_text = text.strip(text)
print(clean_text)
def normalize_text(text1):
    return text1.strip().lower()
def find_keywords(text1, keywords):
    normalized_text = normalize_text(text1)
    found_keywords = []
    for keyword in keywords:
        if keyword in normalized_text:
            found_keywords.append(keyword)
    return found_keywords
_keywords = input("Enter keywords: ").lower()
__keywords = _keywords.split()
print(find_keywords(text1 = text,keywords=__keywords))