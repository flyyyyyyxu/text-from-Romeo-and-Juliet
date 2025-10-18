### This Python script reads a .txt file, counts lines and a specific word, and outputs the results to a new txt file

# Define the word to count
target_word_1 = "Romeo"  # Replace with the word you want to count
target_word_2 = "Juliet" 

# Read the txt file
fhand = open('/Users/flyyyyyyxu/Documents/python fall/exercise/romeo-full.txt', 'r')

# Define variables to count things
line_count = 0  # Count lines
word_count_Romeo = 0  # Count occurrences of the target word
word_count_Juliet = 0

# Loop through each line to count things
for line in fhand:
    line_count += 1
    word_count_Romeo += line.lower().split().count(target_word_1.lower())  # Count the target word (case-insensitive)
    word_count_Juliet += line.lower().split().count(target_word_2.lower())
# Close the input file
fhand.close()

# Create an output.txt file
fout = open('output.txt', 'w')
fout.write(f"Total lines: {line_count}\n")
fout.write(f"Occurrences of '{target_word_1}': {word_count_Romeo}\n")
fout.write(f"Occurrences of '{target_word_2}': {word_count_Juliet}\n")

# Close the output file
fout.close()