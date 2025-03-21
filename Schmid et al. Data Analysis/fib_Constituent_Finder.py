import csv
import pandas as pd

# Read the CSV file
df = pd.read_csv('fibGen12.csv')

# Extract the column values into an array
column_values = df['Item'].values

#Constituent sequences
sequences1 = []
sequences2 = []
sequences3 = []
sequences4 = []
sequences5 = []

#First level constituents
def constOne(column_values):
    k = 0
    i = 0
    while k <= 1:
        string = []
        for i in range(0, 233):
            if column_values[i - 1] == None and column_values[i] == 0:
                pass
            elif column_values[i - 1] == 0 and column_values[i] == 1:
                sequences1.append('[01]')
            elif column_values[i - 1] == 1 and column_values[i] == 1:
                sequences1.append('[1]')
            elif column_values[i - 1] == 1 and column_values[i] == 0:
                pass
            k += 1
        if k >= len(column_values):
            break
    print(sequences1)
    print(len(sequences1))

constOne(column_values)

#Second level constituents
def constTwo(sequences1):
    k = 0
    i = 0
    while k <= 1:
        string = []
        for i in range(0, len(sequences1)):
            if sequences1[i - 1] == None and sequences1[i] == '[01]':
                sequences2.append('[01]')
            elif sequences1[i - 1] == '[01]' and sequences1[i] == '[1]':
                pass
            elif sequences1[i - 1] == '[1]' and sequences1[i] == '[01]':
                sequences2.append('[101]')
            elif sequences1[i - 1] == '[01]' and sequences1[i] == '[01]':
                sequences2.append('[01]')
            k += 1
        if k >= len(sequences1):
            break
    print(sequences2)
    print(len(sequences2))

constTwo(sequences1)

#Third level constituents
def constThree(sequences2):
    k = 0
    i = 0
    while k <= 1:
        string = []
        for i in range(0, len(sequences2)):
            if sequences2[i - 1] == None and sequences2[i] == '[01]':
                pass
            elif sequences2[i - 1] == '[01]' and sequences2[i] == '[101]':
                sequences3.append('[01101]')
            elif sequences2[i - 1] == '[101]' and sequences2[i] == '[101]':
                sequences3.append('[101]')
            elif sequences2[i - 1] == '[101]' and sequences2[i] == '[01]':
                pass
            k += 1
        if k >= len(sequences2):
            break
    print(sequences3)
    print(len(sequences3))

constThree(sequences2)

#Ambiguity
ambiguity0 = []
ambiguity1 = []
ambiguity2 = []
ambiguity3 = []
ambiguity4 = []


#Zero level ambiguity
def ambiguityZero(column_values):
    k = 0
    i = 0
    while k <=1:
        string = []
        for i in range(0, 233):
            if column_values[i - 1] == None and column_values[i] == 0:
                ambiguity0.append('')
            elif column_values[i - 1] == 0 and column_values[i] == 1:
                ambiguity0.append('0')
            elif column_values[i - 1] == 1 and column_values[i] == 1:
                ambiguity0.append('1')
            elif column_values[i - 1] == 1 and column_values[i] == 0:
                ambiguity0.append('')
            k += 1
        if k >= len(column_values):
            break
    print(ambiguity0)
    print(len(ambiguity0))

ambiguityZero(column_values)

#First level ambiguity
def ambiguityOne(sequences1):
    k = 0
    i = 0
    while k <= 1:
        string = []
        for i in range(0, 144):
            if sequences1[i - 1] == None and sequences1[i] == '[01]':
                ambiguity1.append('')
                ambiguity1.append('')
            elif sequences1[i - 1] == '[01]' and sequences1[i] == '[01]':
                ambiguity1.append('1')
                ambiguity1.append('')
            elif sequences1[i - 1] == '[1]' and sequences1[i] == '[01]':
                ambiguity1.append('0')
                ambiguity1.append('')
            elif sequences1[i - 1] == '[01]' and sequences1[i] == '[1]':
                ambiguity1.append('')
            k += 1
        if k >= len(sequences1):
            break
    print(ambiguity1)
    print(len(ambiguity1))

ambiguityOne(sequences1)

#Second level ambiguity

def ambiguityTwo(sequences2):
    k = 0
    i = 0
    while k <= 1:
        string = []
        for i in range(0, len(sequences2)):
            if sequences2[i - 1] == None and sequences2[i] == '[01]':
                ambiguity2.append('')
                ambiguity2.append('')
            elif sequences2[i - 1] == '[101]' and sequences2[i] == '[01]':
                ambiguity2.append('')
                ambiguity2.append('')
            elif sequences2[i - 1] == '[01]' and sequences2[i] == '[101]':
                ambiguity2.append('0')
                ambiguity2.append('')
                ambiguity2.append('')
            elif sequences2[i - 1] == '[101]' and sequences2[i] == '[101]':
                ambiguity2.append('1')
                ambiguity2.append('')
                ambiguity2.append('')
            k += 1
        if k >= len(sequences2):
            break
    print(ambiguity2)
    print(len(ambiguity2))

ambiguityTwo(sequences2)

def ambiguityThree(sequences3):
    k = 0
    i = 0
    while k <= 1:
        string = []
        for i in range(0, len(sequences3)):
            if sequences3[i - 1] == None and sequences3[i] == '[01101]':
                ambiguity3.append('1')
                ambiguity3.append('')
                ambiguity3.append('')
                ambiguity3.append('')
                ambiguity3.append('')
            elif sequences3[i - 1] == '[01101]' and sequences3[i] == '[101]':
                ambiguity3.append('')
                ambiguity3.append('')
                ambiguity3.append('')
            elif sequences3[i - 1] == '[101]' and sequences3[i] == '[01101]':
                ambiguity3.append('0')
                ambiguity3.append('')
                ambiguity3.append('')
                ambiguity3.append('')
                ambiguity3.append('')
            elif sequences3[i - 1] == '[01101]' and sequences3[i] == '[01101]':
                ambiguity3.append('1')
                ambiguity3.append('')
                ambiguity3.append('')
                ambiguity3.append('')
                ambiguity3.append('')
            k += 1
        if k >= len(sequences3):
            break
    print(ambiguity3)
    print(len(ambiguity3))

ambiguityThree(sequences3)

#Print
def write_to_csv(column_values, ambiguity0, ambiguity1, ambiguity2, ambiguity3):
    with open('constituents.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Column Values', 'Ambiguity0', 'Ambiguity1', 'Ambiguity2', 'Ambiguity3'])
        max_length = max(len(column_values), len(ambiguity0), len(ambiguity1), len(ambiguity2), len(ambiguity3))
        for i in range(max_length):
            col_val = column_values[i] if i < len(column_values) else ''
            amb0 = ambiguity0[i] if i < len(ambiguity0) else ''
            amb1 = ambiguity1[i] if i < len(ambiguity1) else ''
            amb2 = ambiguity2[i] if i < len(ambiguity2) else ''
            amb3 = ambiguity3[i] if i < len(ambiguity3) else ''
            writer.writerow([col_val, amb0, amb1, amb2, amb3])

write_to_csv(column_values, ambiguity0, ambiguity1, ambiguity2, ambiguity3)
