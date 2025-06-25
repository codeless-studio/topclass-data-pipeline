fhand = input('Enter the file name: ')

try:
    fhand = open(fhand, encoding="utf8")
except:
    print('File cannot be opened:', fhand)
    exit()

# go through the file line by line and print the  lines starting with a number 

for line in fhand:
    line = line.rstrip()
    if len(line) < 1 or not line[0].isdigit():
        continue
    print(line)

# create a new file to write the lines to
new_fhand = input('Enter the new file name: ')
try:
    new_fhand = open(new_fhand, 'w', encoding="utf8")
except:
    print('File cannot be opened:', new_fhand)
    exit()  

# write the lines to the new file
fhand.seek(0)  # Reset file pointer to the beginning    
for line in fhand:
    line = line.rstrip()
    if len(line) < 1 or not line[0].isdigit():
        continue
    new_fhand.write(line + '\n')
