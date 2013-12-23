import csv
from parseIndexes import *

#set file names
f_name="book.txt"
f_index="index_of_book.txt"
f_output="book_output.csv"
f_keywords="keywords.csv"

#set keywords and write them to 'f_keywords'
keyword_list=index_list(f_index, f_keywords)

# open file and read it in lines
with open(f_name) as fin:
    k=fin.readlines()

# remove line break "\n"
s=[j.strip("\n") for j in k]

# split it in words
stripped_s=[]
for line in s:
    line_text=line.split()
    for word in line_text:
        stripped_s.append(word)

# find keyword positions
indices=[]
freqs=[]
for ind in range(0,len(keyword_list)):
    indices.append([i for i, x in enumerate(stripped_s) if (x.startswith(keyword_list[ind]))])
    #print str(ind)+": " + keyword_list[ind] + ": " + str(len(indices[ind]))
    freqs.append(len(indices[ind]))

# write keyword positions in .csv 
fout = open(f_output, "wb")
csv_file = csv.writer(fout)
increm=0
for item in indices:  
    csv_file.writerow(item)
    #print increm
    increm+=1
fout.close()
    

