# Remove Duplicate words
def getWord(str):
    word = str.split(' ')
    result = []
    for i in word:
        if i not in result:
            result.append(i)
    return result


word = """Articles combine with noun to form noun phrases and typically specify the grammatical definiteness of the noun phrase
"""
print(getWord(word))