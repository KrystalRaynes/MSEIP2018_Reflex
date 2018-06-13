#Starter code to import the CSV file

import csv


with open('setosa_v_versicolor.csv', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	
	for row in csvreader:
		slength = row[0]
		swidth = row[1]
		plength = row[2]
		pwidth = row[3]
		species = row[4]
		#shouldn't this be column?
	int flower = 0
	while flower < 100:
		if csvreader[flower] [plength] >= 3:
			#this means that the speciese is Iris Virginica, speciecs 1
		
		
		
	
		
