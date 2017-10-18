
# coding: utf-8

# <h2>Birth Dates In The United States</h2>
# The raw data behind the story Some People Are Too Superstitious To Have A Baby On Friday The 13th.
# 
# We'll be working with the data set from the Centers for Disease Control and Prevention's National National Center for Health Statistics. The data set has the following structure:
# 
# year - Year
# month - Month
# date_of_month - Day number of the month
# day_of_week - Day of week, where 1 is Monday and 7 is Sunday
# births - Number of births

# In[1]:


f = open("births.csv", 'r')
text = f.read()
print(text)

lines_list = text.split("\n")
lines_list

data_no_header = lines_list[1:len(lines_list)]
days_counts = dict()

for line in data_no_header:
    split_line = line.split(",")
    day_of_week = split_line[3]
    num_births = int(split_line[4])

    if day_of_week in days_counts:
        days_counts[day_of_week] = days_counts[day_of_week] + num_births
    else:
        days_counts[day_of_week] = num_births

days_counts

