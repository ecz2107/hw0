import csv
with open ('iowa-liquor-sample.csv', 'r') as csvfile:
        count = 0
        for row in csvfile:
                if 'single malt scotch' in row.lower():
                        count +=1
print count
