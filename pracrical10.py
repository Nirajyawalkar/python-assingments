# <<<<<<<<<<,lab assignments 1>>>>>>>>>>>>>>>
# import pandas as pd
#
# # Load CSV file
# df = pd.read_csv("books.csv")
#
# # a) Print complete report
# print("\n--- Complete Book Report ---")
# print(df)
#
# # b) Books by author
# author_name = input("\nEnter author name: ")
# print("\nBooks by author:")
# print(df[df['author'] == author_name])
#
# # c) Books by publisher
# publisher_name = input("\nEnter publisher name: ")
# print("\nBooks by publisher:")
# print(df[df['publisher'] == publisher_name])
#
# # d) Cheapest & Costliest books
# print("\nCheapest Book:")
# print(df[df['price'] == df['price'].min()][['title', 'price']])
#
# print("\nCostliest Book:")
# print(df[df['price'] == df['price'].max()][['title', 'price']])
#
# # e) Sort by year
# print("\nBooks sorted by year:")
# print(df.sort_values(by='year'))

# <<<<<<<<<,lab 2 assignments >>>>>>>>>>

# import pandas as pd
#
# # Create Data
# data = {
#     'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'Karnataka', 'Tamil Nadu'],
#     'Area': [307713, 196244, 342239, 191791, 130058],  # in sq km
#     'Population': [112374333, 60439692, 68548437, 61095297, 72147030]
# }
#
# df = pd.DataFrame(data)
#
# # a) Complete info
# print("\n--- State Information ---")
# print(df)
#
# # b) Largest Area
# print("\nState with Largest Area:")
# print(df.loc[df['Area'].idxmax(), 'State'])
#
# # c) Largest Population
# print("\nState with Largest Population:")
# print(df.loc[df['Population'].idxmax(), 'State'])
#
# # d) Population Density
# df['Density'] = df['Population'] / df['Area']
# print("\nPopulation Density:")
# print(df[['State', 'Density']])
#
# # e) Highest Density
# print("\nState with Highest Population Density:")
# print(df.loc[df['Density'].idxmax(), 'State'])