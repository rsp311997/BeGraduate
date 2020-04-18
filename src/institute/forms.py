from django import forms
from institute.models import InstituteModel

def get_city_name_list():
    '''
        Get distinct city names
        Task:
        1. Get all institute objects from database.
        2. Create empty list.
        3. Append city names with lower case.
        4. Type-cast city name list to set to get the distinct values.
        5. Append the distinct city names in list of tupes.
        6. Return list of tupes.
    '''
    #1
    instituties=InstituteModel.objects.all()
    #2
    temp_list=[]
    for institute in instituties:
        #3
        temp_list.append(institute.city.lower())
    #4
    temp_list = set(temp_list)

    lists=[('','Select City')]
    for city in temp_list:
        #5
        lists.append((city,city))
    #6
    return lists

def get_state_name_list():
    '''
        Get distinct state names
        Task:
        1. Get all institute objects from database.
        2. Create empty list.
        3. Append state names with lower case.
        4. Type-cast state name list to set to get the distinct values.
        5. Append the distinct state names in list of tupes.
        6. Return list of tupes.
    '''
    #1
    instituties=InstituteModel.objects.all()
    #2
    temp_list=[]
    for institute in instituties:
        #3
        temp_list.append(institute.state.lower())
    #4
    temp_list = set(temp_list)

    lists=[('','Select State')]
    for state in temp_list:
        #5
        lists.append((state,state))
    #6
    return lists

def get_country_name_list():
    '''
        Get distinct country names
        Task:
        1. Get all institute objects from database.
        2. Create empty list.
        3. Append country names with lower case.
        4. Type-cast country name list to set to get the distinct values.
        5. Append the distinct country names in list of tupes.
        6. Return list of tupes.
    '''
    #1
    instituties=InstituteModel.objects.all()
    #2
    temp_list=[]
    for institute in instituties:
        #3
        temp_list.append(institute.country.lower())
    #4
    temp_list = set(temp_list)


    lists=[('','Select Country')]
    for country in temp_list:
        #5
        lists.append((country,country))
    #6
    return lists

def get_college_name_list():
    '''
        Get college names
        Task:
        1. Get all institute objects from database.
        2. Create empty list.
        3. Append the college names in list of tupes.
        4. Return list of tupes.
    '''
    #1
    instituties=InstituteModel.objects.all()
    #2
    list=[('','All Colleges')]
    for institute in instituties:
        #3
        list.append((institute.abriviation,institute.name))
    #4
    return list


class FilterForm(forms.Form):
    college=forms.CharField(widget=forms.Select(choices=get_college_name_list()),required=False)
    country=forms.CharField(widget=forms.Select(choices=get_country_name_list()),required=False)
    state=forms.CharField(widget=forms.Select(choices=get_state_name_list()),required=False)
    city=forms.CharField(widget=forms.Select(choices=get_city_name_list()),required=False)
