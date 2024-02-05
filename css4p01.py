#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:16:07 2024

@author: C_Thesner

Please note, this script was written using the python version 3.9.7.  Some newer versions have had issues running the code for questions 10, 11 and 12 and produce errors that I do not experience in the python version 3.9.7
"""

#####################
#
#   Import packages
#
#####################

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


#####################
#
#   Import data
#
#####################

mov_set = pd.read_csv("movie_dataset.csv")

avg_met = mov_set["Metascore"].mean()

# print(avg_met)

mov_set["Metascore"].fillna(avg_met, inplace=True)

# print(mov_set.info())


##############################
#
#   Highest rated movie
#
##############################

high_rat = mov_set["Rating"]

high_rat = pd.DataFrame(high_rat)

high_rat = high_rat["Rating"].max()

high_rat = mov_set[mov_set["Rating"] == high_rat]

high_rat = high_rat.reset_index(drop=True)

high_rat_tit = high_rat.at[0, "Title"] 

# print("\n" "The highest rated movie is:") 
# print(high_rat_tit)


##############################
#
#   Movies released in 2016
#
##############################

rel_2016 = mov_set[mov_set["Year"] == 2016]

rel_2016 = pd.DataFrame(rel_2016)

rel_2016 = len(rel_2016["Year"])

# print("\n" "Movies released in 2016:") 
# print(rel_2016)


##################################################################
#
#   Movies directed by Christopher Nolan and the median rating
#
##################################################################

ChrisN = mov_set[mov_set["Director"] == "Christopher Nolan"]

ChrisN = pd.DataFrame(ChrisN)

direc_ChrisN = len(ChrisN["Director"])

rat_ChrisN = ChrisN["Rating"].mean()

# print("\n" "Movies directed by Christopher Nolan:") 
# print(direc_ChrisN)

# print("\n" "Median rating of movies directed by Christopher Nolan:") 
# print(rat_ChrisN)


##########################################
#
#   Movies w rating at least 8
#
##########################################

rat_8 = mov_set[mov_set["Rating"] >= 8]

rat_8 = pd.DataFrame(rat_8)

rat_8 = len(rat_8["Rating"])

# print("\n" "Number of movies with a rating of at least 8:") 
# print(rat_8)


##########################################
#
#   Year with highest avg rating
#
##########################################

Yr_avg_rat = mov_set.groupby("Year")

Yr_avg_rat = Yr_avg_rat["Rating"].mean()

Yr_avg_rat = pd.DataFrame(Yr_avg_rat)

# # Yr_avg_rat = Yr_avg_rat["Rating"].max()

# print("\n" "Year with highest avg rating:") 
# print(Yr_avg_rat.idxmax()) 

#  # x_Yr_avg_rat = Yr_avg_rat.index

# # plt.bar(Yr_avg_rat.index,Yr_avg_rat["Rating"])
# # plt.ylim(6,7.5)
# # plt.show()


########################################################################
#
#   Percentage increase of movies released in 2016 compared to 2006
#
########################################################################

Yr_perc_2006 = mov_set[mov_set["Year"] == 2006]

Yr_perc_2006= len(Yr_perc_2006["Year"])

per_inc = ((rel_2016-Yr_perc_2006)/Yr_perc_2006)*100

# print("\n" "The % incraese of movies released in 2016 compared to 2006.") 
# print(per_inc) 


##########################################
#
#   Average total revenue
#
##########################################

avg_tot_rev = mov_set

avg_tot_rev = pd.DataFrame(avg_tot_rev)

avg_tot_rev.dropna(inplace=True)

avg_tot_rev = avg_tot_rev.reset_index(drop=True)

avg_tot_rev = avg_tot_rev["Revenue (Millions)"].mean()

# print("\n" "The average revenue over all the movies (Millions):") 
# print(avg_tot_rev) 



##########################################
#
#   Average revenue for range 2015 - 2017
#
##########################################


avg_rev_2015 = mov_set[mov_set["Year"] == 2015]
avg_rev_2016 = mov_set[mov_set["Year"] == 2016]
# avg_rev_2017 = mov_set[mov_set["Year"] == 2017]

avg_rev_2015_2017 = pd.concat([avg_rev_2015,avg_rev_2016], ignore_index=True)

avg_rev_2015_2017 = avg_rev_2015_2017["Revenue (Millions)"].mean()

# print("\n" "The average revenue the movies in 2015 and 2016 (Millions):") 
# print(avg_rev_2015_2017) 


##########################################
#
#   Most common actor
#
##########################################

actors = mov_set["Actors"]

# actors['Actors'].explode().value_counts()

actors = pd.DataFrame(actors)

actors["Actors"] = actors["Actors"].str.replace(r',\s+', ",", regex=True)

actors["Actors"] = actors["Actors"].str.replace(r'\s+,', ",", regex=True)

actors["Actors"] = actors["Actors"].str.split(',')

# actors["Actors"].str.match(...).str.get(0).groupby(lambda x: x).count()
# 
# counted = actors["Actors"].value_counts()

act_count = actors['Actors'].explode().value_counts()

# actors['Actors'].apply(pd.Series).stack().value_counts()

act_count = act_count.reset_index().rename(columns={"index":"act_name"})	

high_act = act_count["Actors"].max()

high_act = act_count[act_count["Actors"] == high_act]

high_act = high_act.reset_index(drop=True)

com_act = high_act.at[0, "act_name"] 

print("\n" "The most common actor is:") 
print(com_act)


##########################################
#
#   Number of unique genres
#
##########################################

gen = mov_set["Genre"]

gen = pd.DataFrame(gen)

gen["Genre"] = gen["Genre"].str.split(',')

gen_count = gen["Genre"].explode().value_counts()

gen_count = gen_count.reset_index().rename(columns={"index":"gen_name"})		

gen_count = len(gen_count["gen_name"])

# print("\n" "The number of unique genres is;") 
# print(gen_count) 


##########################################
#
#   Correlation of numerical features
#
##########################################

Mov_set_corr = mov_set.corr() 

fig, ax = plt.subplots(figsize=(10, 6))

sn.heatmap(Mov_set_corr.corr(), ax=ax, annot=True)

ans1 = "\n Correlation observation: \n \n 1.  The rank and year data showed very low and negative correlation overall.  This low correlation indicates that the rank and year have no influence on audience opinions. \n \n 2.  A relatively high positive correlation is seen between the votes and the runtime.  This indicates that how long a movie is has an influence on the audience's opinion.\n \n 3.The runtime however has a lower positive correlation with revenue, meaning that the runtime does not necessarily affect the revenue produced by the movie. \n \n 4. Rating and votes have a high positive correlations, which makes sense because something that has a high rating should have more votes. \n \n 5. Rating and revenue show very high positive correlation. The high rating will lead to more people watching the movies producing higher revenue values. \n \n  6. The Metascore only shows a positive high correlation with ratings, meaning that the audience and movie critics typically agree on the 'quality' of movies. \n \n"

ans2 = "\n Advice to directors: \n \n 1. Directors should consider genres and actors from those titles which had high votes, basing more movies on those statistics could imporove audience voting and, consequently, the revenue. \n \n 2. Directors should consider doing analysis on the runtime-vote and vote-revenue correlations in order to find the runtime 'sweetspot' which could potentially increase renevue due to increased votes. \n \n 3. The high correlation between the Metascore and the votes indicate that directors should pay attention to reviews from critics when planning future movies."







##########################################
#
#   Answers to Questions in order
#
##########################################

print("\n" "The answer to Q1 is:") 
print("(The highest rated movie) \n", high_rat_tit)

print("\n" "The answer to Q2 is:") 
print("(The average revenue over all the movies (Millions)) \n", avg_tot_rev) 

print("\n" "The answer to Q3 is:") 
print("(The average revenue the movies in 2015 and 2016 (Millions))", avg_rev_2015_2017) 

print("\n" "The answer to Q4 is:") 
print("(Movies released in 2016) \n", rel_2016)

print("\n" "The answer to Q5 is:") 
print("(Movies directed by Christopher Nolan) \n", direc_ChrisN)

print("\n" "The answer to Q6 is:") 
print("(Number of movies with a rating of at least 8) \n", rat_8)

print("\n" "The answer to Q7 is:") 
print("(Median rating of movies directed by Christopher Nolan) \n", rat_ChrisN)

print("\n" "The answer to Q8 is:") 
print("(Year with highest avg rating) \n", Yr_avg_rat.idxmax()) 

print("\n" "The answer to Q9 is:") 
print("(The % incraese of movies released in 2016 compared to 2006.) \n", per_inc) 

print("\n" "The answer to Q10 is:") 
print("(The most common actor is) \n", com_act)

print("\n" "The answer to Q11 is:") 
print("(The number of unique genres) \n", gen_count) 

print("\n" "The answer to Q12 is:") 
print("(The correlation of numerical data, insights from correlation and advice to directors) \n", ans1, ans2) 


