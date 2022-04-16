from Bio import Entrez, Medline
import math
import numpy as np
import matplotlib.pyplot as plt


def obtain_years(term):
    Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
    handle = Entrez.egquery(term=term)
    record = Entrez.read(handle)
    for row in record["eGQueryResult"]:
        if row["DbName"]=="pubmed":
            print(row["Count"])

    Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
    handle = Entrez.esearch(db="pubmed", term=term, retmax=2836)
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
        # To prevent an error when the source is ?.
        if " " in split_source:
            print("split_source")
            specific_source = (split_source[1].split(" "))
            #print(specific_source[1])
            year = specific_source[1][0:4]
            #print(year)
            #print("")
            list_of_years.append(year)

    print(list_of_years)
    return list_of_years


def count_per_period(list_of_years):
    dictionary = {}
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
            dictionary.update({timeperiod : counter})
            top_year += 5
            bottom_year += 5
        else:
            for year2 in list_of_years:
                if int(year2) >= bottom_year and int(year2) <= top_year:
                    #print(year2)
                    counter += 1
            timeperiod = str(bottom_year) + "-" + str(top_year)
            print(timeperiod)
            dictionary.update({timeperiod : counter})

    print(dictionary)
    print(len(list_of_years))
    return dictionary

def barplot(dictionary):
    keys = dictionary.keys()
    values = dictionary.values()
    plt.bar(keys, values, color='maroon', width=0.4)

    plt.xlabel("Period")
    plt.ylabel("Amount of hits")
    plt.title("Amount of hits per period")
    plt.show()

def barplot_combined(dictionary, dictionary2, term, term2):
    keys = dictionary.keys()
    values = dictionary.values()
    keys2 = dictionary2.keys()
    values2 = dictionary2.values()

    x = np.arange(len(dictionary.keys()))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, dictionary.values(), width, label=term)
    rects2 = ax.bar(x + width / 2, dictionary2.values(), width, label=term2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Period')
    ax.set_ylabel('Amount of hits')
    ax.set_title('Amount of hits per period')
    ax.set_xticks(x, dictionary.keys())
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()
if __name__ == '__main__':
    term = input("Enter a term: ")
    list_of_years = obtain_years(term)
    dictionary = count_per_period(list_of_years)
    barplot(dictionary)
    compare = input("Do you want to compare this to another term? y/n: ")
    if compare == "y":
        term2 = input("Enter another term: ")
        list_of_years2 = obtain_years(term2)
        dictionary2 = count_per_period(list_of_years2)
        barplot_combined(dictionary, dictionary2, term, term2)
