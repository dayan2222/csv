import csv

header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]

filename = 'Students_Data.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) # create a csvwriter object
    csvwriter.writerow(header) # write the header
    csvwriter.writerows(data) # write the rest of the data