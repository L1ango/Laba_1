#Дан список list=[...]. В словах посчитать количество гласных и согласных.
my_list = ['Python', 15442, 32, 'QweRty', 34, 19, 'love']

def is_vowel(char):
    vowels = "AEIOUaeiouyY"
    return char in vowels

def count_vowels_and_consonants(word):
    vowels_count = 0
    consonants_count = 0
    for char in str(word):
        if char.isalpha():
            if is_vowel(char):
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count

for item in my_list:
    if isinstance(item, str):
        vowels, consonants = count_vowels_and_consonants(item)
        print("В слове " + str(item) + " " + str(vowels) + " гласных и " + str(consonants) + " согласных.")
    else:
        print(str(item)+ " не является строкой.")
