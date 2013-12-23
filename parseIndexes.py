def index_list(f_name, f_output):
    
    # f_name: the index file to parse (with page numbers)
    # f_output: the cleaned file of keywords (without page numbers)
    
    import csv

    # open file and read it in lines
    with open(f_name) as fin:
        k=fin.readlines()

    # remove line-break "\n"
    s=[j.strip("\n") for j in k]

    # remove everything after first comma (page numbers)
    # create list of keywords
    stripped_s=[]
    for line in s:
        print line
        f_ind=line.index(",")
        stripped_s.append(line[0:f_ind])

    # write keywords list to .csv
    fout=open(f_output, "wb")
    csv_file=csv.writer(fout, dialect='excel')
    csv_file.writerow(stripped_s)
    fout.close()

    # return list of keywords
    return stripped_s
