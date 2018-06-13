#Starter code to import the CSV file

import csv


with open('setosa_v_versicolor.csv', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	
	for column in csvreader:
		slength = column[0]
		swidth = column[1]
		plength = column[2]
		pwidth = column[3]
		species = column[4]
	#int flower = 0
	#while flower < 100:
	#	if  >= 3 & cvsreader[flower] [pwidth] >= 1:
			#this means that the species is Iris Virginica, speciecs 1
		#else:
			#this means that it is species -1

		#flower++
		
		
		
	
		
