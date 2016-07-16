import csv
 
with open('test1.csv', 'rb') as csvfile:
  with open('result.csv', 'wb') as csvfile1:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
      spamwriter = csv.writer(csvfile1, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow(row)

    print 'done !!'
