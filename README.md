# Election_Analysis

## Overview

	Project is to assist Tom (Colorado election employee) to audit the results for US congressional recinct in Colorado. 
	Objective is to aggregate and analyze results in an automtated way using Python and standardize/generalize the method 
	in a way that it can be used for any elections (Local, Senate and even presidential).

	Below are some of the key analytics
	1. Total # of votes cast
	2. Total #/% of votes per county/candidate
	3. Winner of election based on popular vote

## Election-Audit Results

	Below are the analytics on election results
	
	- No.of Votes cast in the election: 368,711
	
	- Votes breakdown by county (Number and % of votes)
		Below is the county list sorted by % of votes cast
		- Denver: 306,055 (82.8%)
		- Jefferson: 38,855 (10.5%)
		- Arapahoe: 24,801 (6,7%)
	- Country with largest number of votes: Denver (306,055)
	
	- Votes breakdown by candidate (Number and % of votes)
		Below is the candidate list sorted by % of votes cast
		- Diana DeGette: 272,892 (73.8%)
		- Charles Casper Stockham: 85,213 (23)% 
		- Raymon Anthony Doane: 11,606 (3.1%)
	- Winner 
		- Winning Candidate: Diana DeGette
		- Vote Count: 272,892
		- % of votes: 73.8%
		
![](https://github.com/SuniAnalytics/Election_Analysis/blob/main/Resources/Output_Election_Analysis.jpg)

## Election-Audit Summary

	The automated program enables processing of votes data and 
	aggregated anlytics with a click of the button.	This helped Tom and 
	his manager to audit and attest election results in quick time 
	with accuracy (eliminates any chance of user errors).

	
	Election commision can benefit from this program to speed up processing of election results
	with 100% accuracy. 

	Below are few changes that can be made to the script and data set to standardize it to work for any election
	
### Enhancements to Dataset 
	
		Expand the data set to include few other key attributes
		
		- Total no.of voters in the county 
			Can expand script to show Voters turnout (e.g. % of votes cast)
		- Voting Method
			Voting method column (e.g. Mail in Ballot, punch cards, counting machines) will help 
			provide analytics on voting methods. 
		- Geography Attributes
			Can aggregate and analyse election results for any elections at different levels
			e.g Precint, county, senate, state 
		
### Enhacencements to script

		- Script should be generalized be able to process above dataset changes and also make it dynamic 
		to aggreate results at multiple levels
		- Currently script is fixed to analyse results at a county level as shown below. There is scope to 
		automate it by reading field names from the file
		
	-- insert picture













