10:45 - 12:15 p.m.
Project #2
Let's do some processing to CSVs, bringing in more loops, I/O and dictionaries.


2014 UPDATE
We'll start with some data from Sean Lahman's excellent baseball database
(http://www.seanlahman.com/baseball-archive/statistics/). The `Master.csv` file contains a wealth of
data about baseball players through the years: names, birthdates, countries of origin, and a unique
identifier used across all of the other Lahman files. The `Salaries.csv` file is one of those files. 
It contains salaries (surprise) and player IDs.

We will join `Master.csv` with `Salaries.csv` using dicts, and then we will calculate the top 10%
of highest-paid players.
