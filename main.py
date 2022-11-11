import os
import csv
#file path
budget_data = os.path.join("resources", "budget_data.csv")

#Variables
month=0
total=0
date=[]
change_average=[]
profits_losses=[]
profit_loss_change=[]

with open (budget_data) as csvfile:
     Budget = csv.reader(csvfile)
     header = next(Budget)
     print(header)

     for row in Budget:
          month = month + 1
          total = total + int(row[1])
          profits_losses.append(row[1])
          date.append(row[0])
          print(profits_losses)
          print(f"month:{month}")
          print(f"Total: {total}")

     for x in range(1,len(profits_losses)):
         profit_loss_change.append(int(profits_losses[x]) -int(profits_losses[x-1]))

     change_average = sum(profit_loss_change) / len(profit_loss_change)
     profit_increase = max(profit_loss_change)
     profit_decrease = min(profit_loss_change)
     profit_increase_date = date[profit_loss_change.index(profit_increase)+1]
     profit_decrease_date = date[profit_loss_change.index(profit_decrease)+1]
     print(f"Greatest Increase of Profits: {profit_increase_date} (${profit_increase_date})")
     print(f"Greatest Decrease of Profits: {profit_decrease_date} (${profit_decrease_date})")
    
#Summary

print(f'summary')
print(f'Financial Analysis')
print(f'----------------------')
print(f'Total Months : {month}')
print(f'Total: ${total}')
print(f'Average Change: ${change_average}')
print(f'Greatest Increase of Profits: {profit_increase_date} (${profit_increase}')
print(f'Greatest Decrease of Profits:{profit_decrease_date} (${profit_decrease}')
path_to_file = os.path.join("Analysis", "Pybank_code.txt")
with open (path_to_file, "w") as txtfile:
     txtfile.write(f'summary\n')
     txtfile.write(f'Financial Analysis\n')
     txtfile.write(f'----------------------\n')
     txtfile.write(f'Total Months : {month}\n')
     txtfile.write(f'Total: ${total}\n')
     txtfile.write(f'Average Change: ${change_average}\n')
     txtfile.write(f'Greatest Increase of Profits: {profit_increase_date} (${profit_increase}\n')
     txtfile.write(f'Greatest Decrease of Profits:{profit_decrease_date} (${profit_decrease}\n')