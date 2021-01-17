import os
import csv

csvpath = os.path.join ("Resources", "budget_data.csv") 

with open(csvpath) as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ",")
    csvheader = next(csvreader)
    total = 0
    months = []
    net_total = []
    net_change = []
    
    #print(csvheader)

#Adding Total Months
    for row in csvreader:
        months.append(row[0])
        net_total.append(row[1])
    print("Total Months:", len(months))

# Adding Net Total
    #List of Int for Revenue
    int_net_total = [int(number) for number in net_total]
    #Total Sum of Revenue called 'TotalSum'
    TotalSum = sum(int_net_total[0:])   
    print('Total:', '$', TotalSum)

# Net Change
    x = 0
        #Subtract 1 because of index at 0
    for x in range(len(net_total)-1):
        profitlosses = int(net_total[x+1])-int(net_total[x])
        net_change.append(profitlosses)
    #Sum of Net Changes throughout period
    Total_Net_Change = sum(net_change)
#Average per month
    Average_Net_Change = Total_Net_Change / len(net_change)
    print ('Average Change','$', round(Average_Net_Change,2))

    #Greatest Incr/Decr
    biggest_incr = max(net_change)

    biggest_decr = min(net_change)

    #Finding the Month

    incrindex = net_change.index(biggest_incr)
    decrindex = net_change.index(biggest_decr)
    #print(incrindex) outcome == 24
    #print(decrindex) outcome == 43

    Bestmonth = months[incrindex + 1]
    Worstmonth = months[decrindex + 1]

    print ('Greatest Increase in Profits:', Bestmonth, '$',biggest_incr)
    print ('Greatest Decrease in Profits:', Worstmonth, '$',biggest_decr )
    

    
    




    


   

