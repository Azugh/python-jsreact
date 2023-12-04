string = str(input("Введите строку: "))   
print(string)
string = string.lower()
words = string.split()

maxWord = ''        
wordLength = 0;     
mostCommonWord = ''   
countMostCommon = 0  
maxCommonWord = 0    

for word in words:      
    if wordLength < len(word):
        wordLength = len(word) 
        maxWord = word

    for wordPopular in words:   
        if word == wordPopular:
            countMostCommon += 1

    if countMostCommon > maxCommonWord:   
        mostCommonWord = word                  
        maxCommonWord = countMostCommon

    countMostCommon = 0                     

print(f"Самое длинное слово: {maxWord}.")
print(f"Самое частое слово: {mostCommonWord}. Всего таких слов: {maxCommonWord}.")