import csv


csvFile1 = open('MasterExtraClean.csv', 'a', newline='')
csvWriter = csv.writer(csvFile1)

List = []
with open('Master.csv', newline='') as csvfile:
    Data = csv.reader(csvfile)
    for row in Data:
        Sentance = row[1].split(" ")
        for word in Sentance:
            if word in List:
                Pointer = List.index(word)
                List[Pointer+1] = List[Pointer+1]+1
            else:
                List.append(word)
                List.append(1)
    csvfile.close()

print("Finsihed loading...")

with open('Master.csv', newline='') as csvfile:
    Data1 = csv.reader(csvfile)
    for row in Data1:
        Sentance = row[1].split(" ")
        for word in Sentance:
            Pointer = List.index(word)
            if List[Pointer+1] < 3:
                Sentance.remove(word)
                print("Deleted word, ", word)
        csvWriter.writerow([row[0], " ".join(Sentance)])
    csvfile.close()
    csvFile1.close()
    
        
        
        
