import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join(".","Resources", "budget_data.csv")
file_to_output = os.path.join(".", "budget_analysis.txt")
# Initializing the parameters ####
total_num_months = 0
total_net_amt_entperiod = 0
Ave_cha_between_months = 0
data_set = [ ] 
number_rows = 0
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)
#Initializing the row next to header as beginning row for calculating net change 
    first_row = next(reader)
    total_num_months+=1
    total_net_amt_entperiod+=int(first_row[1])
    previous_row = first_row
    net_change_period = [ ]
    month_of_change = [ ]
    # initial amount is set to 0 to calculate the largest change
    greatest_change = [" ",0]
    # first value of comparison is set to largest in minimum change calc 
    least_change = [" ",9999999999999]
    
    print ("first_row as previous in the beginning initial ",first_row)
    for row in reader:
        #print ("this is the list with 2 column data--->",row)
        # I increment with every row iteration in loop 
        # Track the entire total amount and the months
        total_num_months+=1
        total_net_amt_entperiod+=int(row[1])
        number_rows+=1
        # Track the change
        net_change = int(row[1]) - int(previous_row[1])
        #print ("net_change",net_change)
        # I m reseting the previous row to current row 
        previous_row = row 
        #print ("previous row",previous_row)
        # By list concatenation we get portable format as columns 
        net_change_period = net_change_period + [net_change]
        month_of_change = month_of_change + [row[0]]
        # we calculate the greatest net increase over the entire period
        if net_change > greatest_change[1]:
            greatest_change[1] = net_change
            greatest_change[0] = row[0]
        # we calculate the least net change over the entire period
        if net_change < least_change[1]:
            least_change[1] = net_change
            least_change[0] = row[0]
total_monthly_ave = sum(net_change_period)/len(net_change_period)
########Printing to console ###############
print (("Total Months > {},Total Net Over the Period = {}").format(total_num_months,total_net_amt_entperiod))
print ("Average change:total monthly average",total_monthly_ave)
print ("greatest increase in profit in the month{}, and $ is {}".format(greatest_change[0],greatest_change[1]))
print ("greatest_decrese in profit with month{},and $ is {}  ".format(least_change[0],least_change[1]))
# generate the output summary 
output = (
    f"\nFinancial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_num_months}\n"
    f"Total: ${total_net_amt_entperiod}\n"
    f"Average change: ${total_monthly_ave:.2f}\n"
    f"Greatest Increse in the profit:{greatest_change[0]} (${greatest_change[1]})\n"
    f"Greatest Decrease in Profits:{least_change[0]} (${least_change[1]})\n"  
)
# print output to file
with open(file_to_output,"w") as txt_file:
    txt_file.write(output)