# Election_analysis

## Project Overview
A Colorado Board of Elections employee has give you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Generate a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calcluate the percentage of votes each candidate received.
5. Determine the winner of the election based on total number of votes received.

## Resources
- Data Source: election_results.csv
 - Software: Python 3.6.7, Visual Studio Code 1.71.2

 ## Summary
 The analysis of the election results show:
 - 369,711 votes were cast in this election.
 - There were 3 candidates:
    - Charles Casper Stockham
    - Diana DeGette
    - Ramon Anthony Doane
- The results by candidate were:
    - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
    - Diana DeGette received 73.8% of the vote with 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote with 272,892 votes.

## Challenge Overview
The election commission has requested additional information for this election audit, creating the following additional tasks to the original list.

6. Calculate the voter turnout for each county.
7. Calculate the percentage of votes from each county out of the total count.
8. Determine the county with the highest voter turnout.

## Challenge Summary
The analysis of the election results for the additional tasks requested by the election board show:
- Voters in three counties cast votes in this election:
    - Arapahoe
    - Denver
    - Jefferson
- The voter turnout by county was:
    - Jefferson County: 10.5% of the total votes cast with 38,855 votes.
    - Denver County: 82.8% of the total votes cast with 306,055 votes.
    - Arapahoe County: 6.7% of the total votes cast with 24,801 votes.
- Denver County had the largest voter turnout.

Below are the full results of the election audit, as produced in the text file "election_analysis.txt" and in GitBash:
![Election Audit Results, text file](https://github.com/bnidam/Election_analysis/blob/main/Resources/ElectionAuditResults_textfile.png)
![Election Audit Results, Git Bash](https://github.com/bnidam/Election_analysis/blob/main/Resources/ElectionAuditResults_GitBash.png)

## Election Audit Summary
This script can be used to audit election results for any election where the votes cast have unique identifiers, such as the BallotID in this election. With a few modifications, this script could also be used to audit other elections results.

One example would be for a referendum, if the voter reponses to the referendum are included in the data. Yes votes, No votes, and Did Not Answer votes could be totalled, reported as a percentage of all votes cast, and the winning choice declared in the same way that election results for the candidates is calculated in this audit. The script would have to be modified to identify the location of the referendum responses in the data in line 48: candidate_name = row[2].

A second example would be to track voter turnout by school district instead of by county, if the school district of the voter casting the vote are in the data. The number of votes cast by each school district could be totalled, reported as a percentage of all votes cast, and the school district with the largest voter turnout declared. The script would have to be modified to identify the location of the school district names in the data in line 51: county_name = row[1].
