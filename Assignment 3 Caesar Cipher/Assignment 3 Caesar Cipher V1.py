import math

# Create an empty list
freqs_en = []

# Read the file and extract letters and their frequencies
f = open('/TU Delft Aerospace Engineering/Python/projects/ch-freq-en.txt', 'r')

for line in f:
    line=line.strip()

    lines = line.split('\t') # Split the letters and the frequencies
    letters = lines[0].strip() # Creates the sublists of letters
    frequency = lines[1].strip() # Creates the sublists of frequencies from corresponding letters
    freqs_en.append([letters,frequency]) # Appends the letter and frequency sublists to the freq_en list
    
f.close

# Sort the list in alphabatical order
freqs_en = sorted(freqs_en, key=lambda x: x[0]) 

# Convert the frequency values to floats and devide it by 10
for sublist in freqs_en:
    sublist[1] = float(sublist[1]) 
    sublist[1] = sublist[1] / 100

print(freqs_en)


# Count the number of letters there are in the text
def getfreq(text):
    frequency_list = []
    for char in text:
        if char.isalpha(): # Consider only alphabetic characters
            char = char.lower() # Convert the character to lowercase to avoid case sensitivity
            letter_found = False # Check if the letter already exists in the frequency list
            for sublist in frequency_list:
                if sublist[0] == char:
                    # If found, increment its frequency
                    sublist[1] += 1
                    letter_found = True
                    break
            # If the letter is not found, add it to the frequency list
            if not letter_found:
                frequency_list.append([char, 1])

    # Count the total number of letters in the text
    def count_letters(text):
        letter_count = 0
        for char in text:
            if char.isalpha():
                letter_count += 1
        return letter_count

    num_letters = count_letters(text)

    # Convert the number of letters that are counted in the frequency_list to the ratio between the amount of times the letter is used and the total number of letters in the text
    for sublist in frequency_list:
        sublist[1] = sublist[1] / num_letters
        
    return frequency_list




text=input('Enter the text of which the frequency of letters needs to be determined:')

# Get the frequency_list of the text input and sort the frequency_list in alphabatical order
frequency_list = getfreq(text)
frequency_list = sorted(frequency_list, key=lambda x: x[0])

print(frequency_list)

#def calcdiff(table1, table2):
#
#    def subtract_lists(table1, table2):
#        table1_substract_table2 = []
#        for i in range(len(table1)):
#            # Subtract the second element of each sublist from the first element and append to the result
#            table1_substract_table2.append([table1[i][0], table1[i][1] - table2[i][1]])
#        return table1_substract_table2
#
#    table1_substract_table2 = subtract_lists(table1, table2)
#
#    table1_substract_table2_value = 0
#
#    for subset in table1_substract_table2:
#        table1_substract_table2_value += (sublist[1])**2
#
#    difference = math.sqrt(table1_substract_table2_value)
#    
#    return difference

def calcdiff(table1, table2):
    #If the length of table1 is not equal to 26 it gives an error because table2 is 26 so I need to then append the table1 with 0's      
    difference = sum(abs(table1[i][1] - table2[i][1]) for i in range(26))
    return difference
difference = calcdiff(frequency_list, freqs_en)

print(difference)


