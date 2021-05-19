# -*- coding: utf-8 -*-
#%% About
# Name:    bikeshare_ok.py (based on the template bikeshare_2.py by UDACITY)
# Author:  Octavian Knoll (BMW Group/EP-413)
# Python:  Anaconda/Spyder (Python 3.8)
# Version: v1.1
# History: v1.0: Initial version
#          v1.1: Including function display_data(df)

#%% Import

import time
import pandas as pd
import numpy as np

#%% Available Cities

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv' }

#%% Function "Get Filters from User"

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\n' + '-'*88 + '\n')
    print('Hello! Let\'s explore some US bikeshare data!')
    print('I have data obtained from Chicago, New York City and Washington.')
    print('The data was recorded between January and June 2017.')
    print('\n' + '-'*88)

    # get user input for city (chicago, new york city, washington)
    while True:
        city = input('Which city do you want to analyse?\nPlease type the city [chicago, new york city, washington] and press enter: ').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('\nD\'oh! I haven\'t found the city. Let\'s go again')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month do you want to analyse?\nPlease type the month [jan, feb, mar, apr, may, jun, all] and press enter: ').lower()
        if month in ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all'):
            break
        else:
            print('\nD\'oh! I haven\'t found the month. Let\'s go again')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which weekday do you want to analyse?\nPlease type the weekday [mon, tue, wed, thu, fri, sat, sun, all] and press enter: ').lower()
        if day in ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'all'):
            break
        else:
            print('\nD\'oh! I haven\'t found the day. Let\'s go again!')

    if month == 'all' and day == 'all':
        print('\nOK. Let\'s analye {} without any time filter!'.format(city.title()))
    elif month == 'all' and day != 'all':
        print('\nOK. Let\'s analye {} filtered only by weekday {}!'.format(city.title(), day.title()))
    elif month != 'all' and day == 'all':
        print('\nOK. Let\'s analye {} filtered only by month {}!'.format(city.title(), month.title()))
    else:
        print('\nOK. Let\'s analye {} filtered by month {} and weekday {}!'.format(city.title(), month.title(), day.title()))

    return city, month, day

#%% Function "Load Data"

def load_data(city, month, day):
    """
    Loads data for a specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    print('\n' + '-'*88 + '\n')
    if month == 'all' and day == 'all':
        print('Data from {} without any time filter will be loaded...'.format(city.title()))
    elif month == 'all' and day != 'all':
        print('Data from {} filtered only by weekday {} will be loaded...'.format(city.title(), day.title()))
    elif month != 'all' and day == 'all':
        print('Data from {} filtered only by month {} will be loaded...'.format(city.title(), month.title()))
    else:
        print('Data from {} filtered by month {} and weekday {} will be loaded...'.format(city.title(), month.title(), day.title()))
    start_time = time.time()

    # load data
    df = pd.read_csv(CITY_DATA[city])

    # convert start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # get month, weekday and hour from start time column to create new columns
    df['ST Month'] = df['Start Time'].dt.month
    df['ST Day'] = df['Start Time'].dt.weekday
    df['ST Hour'] = df['Start Time'].dt.hour
    
    # identify month index and day index
    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1
    if day != 'all':
        days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        day = days.index(day)

    # filter data
    if month != 'all' and day != 'all':
        df = df[df['ST Month'] == month]
        df = df[df['ST Day'] == day]
    elif month != 'all' and day == 'all':
        df = df[df['ST Month'] == month]
    elif month == 'all' and day != 'all':
        df = df[df['ST Day'] == day]

    # convert end time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # get month, weekday and hour from end time column to create new columns
    df['ET Month'] = df['End Time'].dt.month
    df['ET Day'] = df['End Time'].dt.weekday
    df['ET Hour'] = df['End Time'].dt.hour

    # modify months and days columns
    months_dic = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun'}
    days_dic = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

    df['ST Month'] = df['ST Month'].map(months_dic)
    df['ET Month'] = df['ET Month'].map(months_dic)
    df['ST Day'] = df['ST Day'].map(days_dic)
    df['ET Day'] = df['ET Day'].map(days_dic)

    # creat new column containing start station and end station
    df['Trip Combination'] = df['Start Station'] + ' --> ' + df['End Station']

    print('\nData was loaded successfully. Woah, this only took %.3f seconds!' % (time.time() - start_time))

    return df

#%% Function "Display Data"

def display_data(df):
    """
    Displays a window of a data frame.
    
    Args:
        df - data frame
    """
    
    print('\n' + '-'*88)
    while True:
        data_info = input('Do you want to see the data before the analysis starts? Enter yes or no: ').lower()
        if data_info in ('yes', 'no'):
            break
        else:
            print('\nD\'oh! Please enter yes or no. Let\'s go again!')
            
    i = 5
    if data_info == 'yes':
        while True:
            if i < len(df):
                print('\n')
                print(df.head(i))
            else:
                print('The entire data set has already been shown!')
                break
            while True:
                data_info = input('Do you want to see more data? Enter yes or no: ').lower()
                if data_info == 'yes':
                    i +=5
                    break
                elif data_info == 'no':
                    break
                else:
                    print('\nD\'oh! Please enter yes or no. Let\'s go again!')
            if data_info == 'no':
                break

#%% Function "Most Common"

def most_common(dfc, name):
    """
    Computes most common values of a data frame column.
    
    Args:
        dfc - data frame column
        (str) name - name of data frame column
    """

    dfc_mode = dfc.mode()
    dfc_mode_l = len(dfc_mode)
    dfc_mode_out = ''
    c = 0
    if  dfc_mode_l == 1:
        dfc_mode_out = dfc.mode()[0]
        print('The most common {} is '.format(name) + str(dfc_mode_out) + '.')
    else:
        for i in dfc_mode:
            c += 1
            if c == dfc_mode_l:
                dfc_mode_out = dfc_mode_out + str(i)
                print('The most common {}s are '.format(name) + dfc_mode_out + '.')
            else:
                dfc_mode_out = dfc_mode_out + str(i) + ', '

#%% Function "Time Statstics"

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n' + '-'*88 + '\n')
    print('The most frequent times of travel will be computed...\n')
    start_time = time.time()

    # display the most common month
    most_common(df['ST Month'], 'month')

    # display the most common day of week
    most_common(df['ST Day'], 'weekday')

    # display the most common start hour
    most_common(df['ST Hour'], 'hour')

    print('\nMost frequent times were computed. Woah, this only took %.3f seconds!' % (time.time() - start_time))

#%% Function "Travel Statstics I"

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\n' + '-'*88 + '\n')
    print('The most popular stations and trips will be computed...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common(df['Start Station'], 'start station')

    # display most commonly used end station
    most_common(df['End Station'], 'end station')

    # display most frequent combination of start station and end station trip
    most_common(df['Trip Combination'], 'trip')

    print('\nMost popular stations and trips were computed. Woah, this only took %.3f seconds!' % (time.time() - start_time))

#%% Function "Travel Statstics II"

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\n' + '-'*88 + '\n')
    print('Total and average trip duration will be computed...\n')
    start_time = time.time()

    # display total travel time
    print('Total trip duration:   %.2f' % df['Trip Duration'].sum())

    # display mean travel time
    print('Average trip duration: %.2f' % df['Trip Duration'].mean())

    print('\nTotal and average trip duration were computed. Woah, this only took %.3f seconds!' % (time.time() - start_time))

#%% Function "User Statstics"

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\n' + '-'*88 + '\n')
    print('User information will be computed...\n')
    start_time = time.time()

    # Display counts of user types
    print('User type inforamtion (normalized):\n')
    print(df['User Type'].value_counts(normalize=True).to_frame())

    # Display counts of gender
    print('\nUser gender information (normalized):\n')
    try:
        print(df['Gender'].value_counts(normalize=True).to_frame())
    except:
        print('No gender data available!')
    
    # Display earliest, most recent, and most common year of birth
    print('\nUser birth information:\n')
    try:
        print('Earliest birth:    %4.0f' % df['Birth Year'].min())
        print('Most recent birth: %4.0f' % df['Birth Year'].max())
        print('Most common birth: %4.0f' % df['Birth Year'].mode()[0])
    except:
        print('No birth data available!')

    print('\nUser inforamtion was computed. Woah, this only took %.3f seconds!' % (time.time() - start_time))
    print('\n' + '-'*88 + '\n')
    print('The entire analysis could be carried out successfully!')
    print('I hope you are satisfied with the result and have all the information you need.')
    print('See you next time!')
    print('\n' + '-'*88)
   
#%% Function "Main Program"

def main():
    while True:
        try:
            city, month, day = get_filters()
        except KeyboardInterrupt:
            print("\n\n\n#*! Interrupted by user!")
            break
        
        df = load_data(city, month, day)
        try:
            display_data(df)
        except KeyboardInterrupt:
            print("\n\n\n#*! Interrupted by user! Computation will be continued...")
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        try:
            restart = input('Do you want to restart? Enter yes or no: ')
        except KeyboardInterrupt:
            print("\n\n\n#*! Interrupted by user!")
            break
        if restart.lower() != 'yes':
            break

#%% Run program

if __name__ == "__main__":
	main()
        
#city, month, day = get_filters()
#df = load_data(city, month, day)

#time_stats(df)
#station_stats(df)
#trip_duration_stats(df)
#user_stats(df)
#display_data(df)