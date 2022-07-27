import os
import shutil
import docxtpl
import datetime
import json

# Extensions files
import dataFunctions
import dateFunctions

# Populate data
with open("data.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

carers_local_Authority = jsonObject['local_Authority']
carers_mainCarers = jsonObject['mainFosterCarers']
carers_SSW_array = jsonObject['FosterCarers_SSW']

child_firstname = jsonObject['child']['firstname']
child_middlename = jsonObject['child']['middlename']
child_lastname = jsonObject['child']['lastname']
child_social_worker_array = jsonObject['child_social_worker']

generate_start_date = jsonObject['generate_start_date']
generate_end_date = jsonObject['generate_end_date']

start_date = dateFunctions.get_start_of_week(generate_start_date)
end_date = datetime.datetime.strptime(generate_end_date, '%Y-%m-%d')
weekDelta = datetime.timedelta(weeks=1)
dayDelta = datetime.timedelta(days=1)

# Main Code & Loop
print("Starting generation of records for " +
      child_firstname + " " + child_lastname)

# Remove generated directory
try:
    shutil.rmtree("generated")
except:
    print("No directory removed")
fileCount = 1

while start_date <= end_date:

    end_of_week = start_date + datetime.timedelta(days=6)

    # Populate week ahead data
    week_dates_data = []
    weekStart = start_date
    for i in range(0, 7):
        week_dates_data.append({
            'weekdate_formatted': weekStart.strftime('%A') + " - " + dateFunctions.custom_strftime(weekStart, False)
        })
        weekStart += dayDelta

    context = {
        'childFullName': child_firstname + " " + child_lastname,
        'local_Authority': carers_local_Authority,
        'allFosterCarers': dataFunctions.get_list_of_foster_carers(carers_mainCarers),
        'weekCommencingDate': dateFunctions.custom_strftime(start_date, True),
        'week_dates_data': week_dates_data,
        'supervising_social_worker_info': dataFunctions.find_data_from_array_and_date(start_date, carers_SSW_array),
        'child_social_worker_info': dataFunctions.find_data_from_array_and_date(start_date, child_social_worker_array)
    }

    directory = "generated/" + \
                start_date.strftime("%Y") + "/" + start_date.strftime("%B")
    if not os.path.exists(directory):
        os.makedirs(directory)

    doc = docxtpl.DocxTemplate("templates/_template_Weekly Recording.docx")
    doc.render(context)
    doc.save(directory + "/Records " + start_date.strftime("%m-%d") +
             " - " + end_of_week.strftime("%m-%d") + "_" + start_date.strftime("%Y") + ".docx")

    start_date += weekDelta
    fileCount = fileCount + 1

print("Finished, generated " + str(fileCount) + " records")
