import datetime
import dateFunctions


def getListOfFosterCarers(mainFosterCarers):
    allCarers = " &amp; ".join(mainFosterCarers)
    return str(allCarers)


def findDataFromArrayAndDate(dateObj: datetime.datetime, array):
    arrayi = 0
    for x in array:
        visitDate = datetime.datetime.strptime(x['visit'], '%Y-%m-%d')
        try:
            nextVistDate = datetime.datetime.strptime(array[arrayi+1]['visit'], '%Y-%m-%d')
        except:
            nextVistDate = datetime.datetime.now() + datetime.timedelta(days=2*365)
        # If date is in the past
        if dateObj <= visitDate:
            return '(none)'
        # Last visited date
        if visitDate <= dateObj <= nextVistDate:
            virtual = ""
            if bool(x['virtual']):
                virtual = " (Virtual)"
            return x['name'] + " - " + dateFunctions.custom_strftime(visitDate, True) + virtual
        arrayi = arrayi + 1
    return '(none)'
