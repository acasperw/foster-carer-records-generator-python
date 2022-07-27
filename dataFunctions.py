import datetime
import dateFunctions


def get_list_of_foster_carers(main_foster_carers):
    all_carers = " &amp; ".join(main_foster_carers)
    return str(all_carers)


def find_data_from_array_and_date(date_obj: datetime.datetime, array):
    array_i = 0
    for x in array:
        visit_date = datetime.datetime.strptime(x['visit'], '%Y-%m-%d')
        try:
            next_vist_date = datetime.datetime.strptime(array[array_i+1]['visit'], '%Y-%m-%d')
        except:
            next_vist_date = datetime.datetime.now() + datetime.timedelta(days=2*365)
        # If date is in the past
        if date_obj <= visit_date:
            return '(none)'
        # Last visited date
        if visit_date <= date_obj <= next_vist_date:
            virtual = ""
            if bool(x['virtual']):
                virtual = " (Virtual)"
            return x['name'] + " - " + dateFunctions.custom_strftime(visit_date, True) + virtual
        array_i = array_i + 1
    return '(none)'
