import os
import csv

csvpath = os.path.join ("Resources","election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    Votes = []
    Candidates = []
    County = []
    Khan= []
    Correy= []
    Li = []
    Otooley = []


#adding to lists
    for row in csvreader:
        Votes.append(row[0])
        Candidates.append(row[1])
        County.append(row[2])

    #Sum of all Votes
    all_votes = (len(Votes))
    print('Total Votes:', all_votes)
    
    #Candidates that received votes

    for person in csvreader:
        if person == "Khan":
            len(Khan.append(csvreader))
        
        elif person == "Correy":
            Correy.append(csvreader)
        
        elif person == 'Li':
            Li.append(csvreader)
        
        else: 
            person =='Otooley'
            Otooley.append(csvreader)

    print (Khan)

    






        
        



