from Bio import Entrez, Medline
import math

#term = input("Enter a term: ")

Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
#handle = Entrez.egquery(term=term)
handle = Entrez.egquery(term="orchid")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"]=="pubmed":
        print(row["Count"])

Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
handle = Entrez.esearch(db="pubmed", term="orchid", retmax=463)
record = Entrez.read(handle)
handle.close()
idlist = record["IdList"]
print(idlist)

handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
records = Medline.parse(handle)

list_of_years = []
for record in records:
    #print("title:", record.get("TI", "?"))
    #print("authors:", record.get("AU", "?"))
    #print("source:", record.get("SO", "?"))
    source = record.get("SO", "?")
    #print(source.split("."))
    split_source = (source.split("."))
    #print(split_source[1])
    specific_source = (split_source[1].split(" "))
    #print(specific_source[1])
    year = specific_source[1][0:4]
    #print(year)
    #print("")
    list_of_years.append(year)

print(list_of_years)



dictionairy = {}
bottom_year = 2001
top_year = 2005
current_year = 2025
amount_of_periods = math.ceil((current_year-top_year)/5 + 1)
#print(amount_of_periods)
#print(range(amount_of_periods))
for period in range(amount_of_periods):
    counter = 0
    if top_year < current_year:
        for year2 in list_of_years:
            if int(year2) >= bottom_year and int(year2) <= top_year:
                #print(year2)
                counter += 1
        timeperiod = str(bottom_year) + "-" + str(top_year)
        print(timeperiod)
        dictionairy.update({timeperiod : counter})
        top_year += 5
        bottom_year += 5
    else:
        for year2 in list_of_years:
            if int(year2) >= bottom_year and int(year2) <= top_year:
                #print(year2)
                counter += 1
        timeperiod = str(bottom_year) + "-" + str(top_year)
        print(timeperiod)
        dictionairy.update({timeperiod : counter})

print(dictionairy)
print(len(list_of_years))

compare = input("Do you want to compare this with something else? y/n: ")
if compare == "y":
    Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
    # handle = Entrez.egquery(term=term)
    handle = Entrez.egquery(term="orchid")
    record = Entrez.read(handle)
    for row in record["eGQueryResult"]:
        if row["DbName"] == "pubmed":
            print(row["Count"])

    Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
    handle = Entrez.esearch(db="pubmed", term="orchid", retmax=463)
    record = Entrez.read(handle)
    handle.close()
    idlist = record["IdList"]
    print(idlist)

    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                           retmode="text")
    records = Medline.parse(handle)

    list_of_years = []
    for record in records:
        # print("title:", record.get("TI", "?"))
        # print("authors:", record.get("AU", "?"))
        # print("source:", record.get("SO", "?"))
        source = record.get("SO", "?")
        # print(source.split("."))
        split_source = (source.split("."))
        # print(split_source[1])
        specific_source = (split_source[1].split(" "))
        # print(specific_source[1])
        year = specific_source[1][0:4]
        # print(year)
        # print("")
        list_of_years.append(year)

    print(list_of_years)

    dictionairy = {}
    bottom_year = 2001
    top_year = 2005
    current_year = 2025
    amount_of_periods = math.ceil((current_year - top_year) / 5 + 1)
    # print(amount_of_periods)
    # print(range(amount_of_periods))
    for period in range(amount_of_periods):
        counter = 0
        if top_year < current_year:
            for year2 in list_of_years:
                if int(year2) >= bottom_year and int(year2) <= top_year:
                    # print(year2)
                    counter += 1
            timeperiod = str(bottom_year) + "-" + str(top_year)
            print(timeperiod)
            dictionairy.update({timeperiod: counter})
            top_year += 5
            bottom_year += 5
        else:
            for year2 in list_of_years:
                if int(year2) >= bottom_year and int(year2) <= top_year:
                    # print(year2)
                    counter += 1
            timeperiod = str(bottom_year) + "-" + str(top_year)
            print(timeperiod)
            dictionairy.update({timeperiod: counter})

    print(dictionairy)
    print(len(list_of_years))

