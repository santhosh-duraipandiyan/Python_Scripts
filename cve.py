import os
import csv
import json
from os import walk


def getFilesList(path):

    files = []

    for (dirpath, dirnames, filenames) in walk(path):
        for file in filenames:
            if file.endswith(".json"):
                files.append(os.path.join(dirpath+"/"+file))

    return files


def readJson(files):

    listOfDictionary = []

    for file in files:
        with open(file, "r", encoding="latin-1") as f:
            jsonData = json.load(f)
            listOfDictionary.append(jsonData)
    return listOfDictionary


def filterData(listOfDictionary):

    data = []

    for record in listOfDictionary:
        cveId = " "
        title = " "
        description = " "
        credits = " "
        email = " "

        try:
            cveId = record["CVE_data_meta"]["ID"]
        except KeyError:
            pass

        try:
            title = record["CVE_data_meta"]["TITLE"]
        except KeyError:
            pass

        try:
            description = record["description"]["description_data"][0]["value"]
        except KeyError:
            pass

        try:
            email = record["CVE_data_meta"]["ASSIGNER"]
        except KeyError:
            pass

        try:
            credits = record["source"]["discovery"]
        except KeyError:
            pass

        data.append((cveId, title, description, email, credits))

    return data


def writeToCsv(filteredData, year):

    try:
        with open("/Users/santhosh/documents/output/"+year+".csv", "wt") as fp:
            writer = csv.writer(fp, delimiter=",")
            writer.writerow(["CVE-ID", "TITLE", "DESCRIPTION",
                            "EMAIL", "CREDITS"])  # write header
            writer.writerows(filteredData)

        return "Process complete"

    except:

        return "Error while processing"


def main():

    basePath = "/Users/santhosh/documents/cvelist/"
    years = ["1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010",
             "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
    for year in years:
        print("processing year : "+year)
        files = getFilesList(basePath+year+"/")
        listOfDictionary = readJson(files)
        filteredData = filterData(listOfDictionary)
        status = writeToCsv(filteredData, year)

    return status


if __name__ == "__main__":
    try:
        output = main()
        print(output)
    except:
        print("error occured while processinf=g.")
