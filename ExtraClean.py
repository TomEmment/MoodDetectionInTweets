import enchant
d = enchant.Dict("en_GB")
import csv
from nltk.tokenize import word_tokenize


csvFile1 = open('Master1.csv', 'a', newline='')
csvWriter = csv.writer(csvFile1)


with open('Master.csv', newline='') as csvfile:
    Position = 0
    Data = csv.reader(csvfile)
    for row in Data:  # add predict for miss spelt
        english_words = []
        Text = word_tokenize(row[1])
        for word in Text:
            if d.check(word):
                english_words.append(word)
        Position = Position +1
        csvWriter.writerow([row[0], " ".join(english_words)])
    csvfile.close()











