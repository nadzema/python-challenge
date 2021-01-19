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

    for person in Candidates:
        if person == "Khan":
            Khan.append('Khan')
            Votes_Khan = len(Khan)
        
        elif person == "Correy":
            Correy.append(Candidates)
            Votes_Correy = len (Correy)
        
        elif person == 'Li':
            Li.append(Candidates)
            Votes_Li = len(Li)
        
        else: 
            person =='Otooley'
            Otooley.append(Candidates)
            Votes_Otooley = len(Otooley)

    print (Votes_Khan)
    print (Votes_Correy)
    print (Votes_Li)
    print (Votes_Otooley)

    PercentageKhan = ((Votes_Khan/all_votes)*100)
    PercentageCorrey = ((Votes_Correy/all_votes)*100)
    PercentageLi = ((Votes_Li/all_votes) *100)
    PercentageOtooley = ((Votes_Otooley/all_votes) *100)
    
    print (round(PercentageKhan,2))
    print (round(PercentageCorrey))
    print (round(PercentageLi,2))
    print (round(PercentageOtooley,2))


    if PercentageCorrey >  max(PercentageKhan,PercentageLi,PercentageOtooley):
        winner = "Correy"
    elif PercentageKhan > max (PercentageCorrey,PercentageLi, PercentageOtooley):
        winner = "Khan"
    elif PercentageOtooley > max (PercentageLi, PercentageKhan, PercentageCorrey):
        winner = "Otooley"
    else:
        winner = "Li"

    print ('Winner:', winner)



    






        
        



