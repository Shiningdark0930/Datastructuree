from collections import Counter

def calculatee(filename1, filename2):
    with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
        text1 = file1.read().lower()
        text2 = file2.read().lower()

    words1 = text1.split()
    words2 = text2.split()

    counter1 = Counter(words1)
    counter2 = Counter(words2)

    return counter1, counter2

def printingg(counter1, counter2):
    common_words = counter1 & counter2
    print("공통된 단어와 각 파일에서의 빈도:")
    for word in common_words.keys():
        count1 = counter1[word]
        count2 = counter2[word]
        print(f"'{word}': 파일1 - {count1}, 파일2 - {count2}")

if __name__ == "__main__":
    filename1 = "file01.txt"
    filename2 = "file02.txt"

    counter1, counter2 = calculatee(filename1, filename2)

    printingg(counter1, counter2)