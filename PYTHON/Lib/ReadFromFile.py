txt_file = 'PYTHON\Projects\ContentMaker\MessageIndex.txt'

#varible that stores current line text form the .txt file
linemessage = ""

with open(txt_file, 'r') as file:
    # Read the file line by line
    for line in file:
        linemessage = line.strip()
        print(linemessage + " [LINE]")


