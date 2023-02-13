'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
ifile = open("employee_data.csv", 'r')
reader = csv.reader(ifile)



#create an empty dictionary
salary_dict = {}

#use a loop to iterate through the csv file
next(reader)
for line in reader:
    #check if the employee fits the search criteria
    if line[3] == "Marketing" and line[4] == "CSR":
        salary_dict[line[1] + ' ' + line[2]] = float(line[5]) * 1.1
        print(f"Manager Name: {line[1]} {line[2]} Current Salary: ${format(float(line[5]), ',.2f')} ")    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for i, j in salary_dict.items():
    print(f"Manager Name: {i} New Salary: ${format(j, ',.2f')} ")       
        
    
ifile.close()
