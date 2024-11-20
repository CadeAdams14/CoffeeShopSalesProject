# import packages
import pandas as pd
import mplcyberpunk
from matplotlib import pyplot as plt

# import data
data = pd.read_csv('coffee_sales_data.csv')

# change the data from long to wide format using a pivot table
data_wide = data.pivot_table(index='Date', columns='Category', values=['Forecasted Amount', 'Actual Amount'])

file_path = r'C:\Users\cadeadams\Downloads\coffee_shop_project\pivot_table.csv'
data_wide.to_csv(file_path, index=False)

# preview data
print(data_wide.head)

# resample data by month 
data_wide.index = pd.to_datetime(data_wide.index)
monthly_data = data_wide.resample('ME').sum()

# find and print sum of each column
column_sums = data_wide.sum()
print("Column Sums:\n", column_sums)

# find and print mean of each column
column_means = data_wide.mean()
print("Column Means:\n", column_means)

# separate list of column sums between actual and forcasted
act_half = column_sums[:7]  
fcst_half = column_sums[7:] 

# drop the first level of the index for both Series
act_half_dropped = act_half.droplevel(0)
fcst_half_dropped = fcst_half.droplevel(0)

# calculate and print difference in forcasted numbers as a percent 
percent_diff = ((fcst_half_dropped - act_half_dropped) / act_half_dropped) * 100
print("Percent Difference:\n", percent_diff)

# use IndexSlice to access the 'Actual Amount' and 'Coffee Sales' columns
idx = pd.IndexSlice
actual_sales_coffee = data_wide.loc[:, idx['Actual Amount', 'Coffee Sales']]

# resample the selected data by month and calculate the sum
monthly_sum_coffee = actual_sales_coffee.resample('M').sum()

# access the sum for a August 2023
aug_23_sum = monthly_sum_coffee.loc['2023-08']
print("Total Actual Coffee Sales for August 2023:", aug_23_sum)

# use IndexSlice to access the 'Actual Amount' and 'Food Sales' columns
idx = pd.IndexSlice
actual_sales_food = data_wide.loc[:, idx['Actual Amount', 'Food Sales']]

# resample the selected data by month and calculate the sum
monthly_sum_food = actual_sales_food.resample('M').sum()

# access and print the sum for a June 2023
jun_23_sum = monthly_sum_food.loc['2023-06']
print("Total Actual Food Sales for June 2023:", jun_23_sum)

# create visual for Actual and Forcasted Coffee Sales using matplotlib
plt.style.use('cyberpunk')
plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Coffee Sales')], marker='o', label='Actual Coffee Sales', color='fuchsia')

plt.plot(monthly_data.index, monthly_data[('Forecasted Amount', 'Coffee Sales')], marker='o', label='Forecasted Coffee Sales', color='darkturquoise')

plt.title('Actual vs. Forecasted Coffee Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='lower right')
plt.ylim(14000,21000)
mplcyberpunk.add_underglow()
plt.show()

# create visual for Actual and Forcasted Food Sales 
plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Food Sales')], marker='o', label='Actual Food Sales', color='darkturquoise')

plt.plot(monthly_data.index, monthly_data[('Forecasted Amount', 'Food Sales')], marker='o', label='Forecasted Food Sales', color='fuchsia')

plt.title('Actual vs. Forecasted Food Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='lower right')
plt.ylim(15500,20500)
mplcyberpunk.add_underglow()
plt.show()

# create visual for Actual and Forcasted Ingredients Cost

plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Ingredients Cost')], marker='o', label='Actual Ingredients Cost', color='darkturquoise')

plt.plot(monthly_data.index, monthly_data[('Forecasted Amount', 'Ingredients Cost')], marker='o', label='Forecasted Ingredients Cost', color='yellow')


plt.title('Actual vs. Forecasted Ingredients Cost')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='lower right')
plt.ylim(7500,10000)
mplcyberpunk.add_underglow()
plt.show()

# create visual for Actual and Forcasted Labor Cost

plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Labor')], marker='o', label='Actual Labor Cost', color='limegreen')

plt.plot(monthly_data.index, monthly_data[('Forecasted Amount', 'Labor')], marker='o', label='Forecasted Labor Cost', color='fuchsia')

plt.title('Actual vs. Forcasted Labor Cost')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='lower right')
plt.ylim(6000,11000)
mplcyberpunk.add_underglow()
plt.show()

# create visual for Actual and Forcasted Rent Cost

plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Rent')], marker='o', label='Actual Rent Cost', color='yellow')

plt.plot(monthly_data.index, monthly_data[('Forecasted Amount', 'Rent')], marker='o', label='Forecasted Rent Cost', color='limegreen')

plt.title('Actual vs. Forcasted Rent Cost')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='lower right')
plt.ylim(7000,10500)
mplcyberpunk.add_underglow()
plt.show()

# create visual for Actual and Forcasted Utilities Cost

plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Utilities')], marker='o', label='Actual Utilities Cost', color='yellow')

plt.plot(monthly_data.index, monthly_data[('Forecasted Amount', 'Utilities')], marker='o', label='Forecasted Utilities Cost', color='teal')

plt.title('Actual vs. Forcasted Utilities Cost')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='lower right')
plt.ylim(7000,11000)
mplcyberpunk.add_underglow()
plt.show()

# create visual for Actual and Forcasted Marketing Cost

plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Marketing')], marker='o', label='Actual Marketing Cost', color='yellow')

plt.plot(monthly_data.index, monthly_data[('Forecasted Amount', 'Marketing')], marker='o', label='Forecasted Marketing Cost', color='teal')

plt.title('Actual vs. Forcasted Marketing Cost')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='lower right')
plt.ylim(7000,10500)
mplcyberpunk.add_underglow()
plt.show()

# create visual to view all actual expense categories 
plt.style.use('cyberpunk')
plt.figure(figsize=(10, 6))

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Ingredients Cost')], marker='o', label='Actual Ingredients Cost', color='yellow')

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Labor')], marker='o', label='Actual Labor Cost', color='darkturquoise')

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Rent')], marker='o', label='Actual Rent Cost', color='teal')

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Utilities')], marker='o', label='Actual Utilities Cost', color='fuchsia')

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Marketing')], marker='o', label='Actual Marketing Cost', color='limegreen')

plt.title('Actual Expense Categories')
plt.xlabel('Date')
plt.ylabel('Expenses')
plt.legend(loc='lower right')
plt.ylim(0,12000)
mplcyberpunk.add_underglow()
plt.show()

# create visual to compare all actual expense categories (close up view)
plt.style.use('cyberpunk')
plt.figure(figsize=(10, 6))

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Ingredients Cost')], marker='o', label='Actual Ingredients Cost', color='yellow')

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Labor')], marker='o', label='Actual Labor Cost', color='darkturquoise')

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Rent')], marker='o', label='Actual Rent Cost', color='teal')

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Utilities')], marker='o', label='Actual Utilities Cost', color='fuchsia')

plt.plot(monthly_data.index, monthly_data[('Actual Amount', 'Marketing')], marker='o', label='Actual Marketing Cost', color='limegreen')

plt.title('Actual Expense Categories')
plt.xlabel('Date')
plt.ylabel('Expenses')
plt.legend(loc='lower right')
plt.ylim(5000,12000)
mplcyberpunk.add_underglow()
plt.show()

