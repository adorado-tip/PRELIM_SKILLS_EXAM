import json as js
import csv as c

with open('./covid_cases.json') as json:
    data = js.loads(json.read())

with open('./retrieved.csv', 'w') as csv:
    parse = c.writer(csv)
    parse.writerow(["dateReported", "countriesAndTerritories", "numberOfCases", "numberOfDeaths"])

    for i in data["records"]:
        parse.writerow([i["dateRep"], i["countriesAndTerritories"], i["cases"], i["deaths"]])
