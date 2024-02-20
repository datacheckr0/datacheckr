#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the CWD

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the CWD
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            csvRows.append(row)
        csvFileObj.close()

    # Write out the CSV file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerrow(row)
    csvFileObj.close()