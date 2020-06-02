import time
import pandas as pd
import numpy as np

CITIES = {'chicago': 'chicago.csv',
          'new york city': 'new_york_city.csv',
          'washington': 'washington.csv'}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday',
        'sunday', 'all']

print('|-' + '-'*60 + '-|')
username = input('Hey! My name is Leonardo, what\'s yours?\n>')
print('\nNice to meet you, {}'.format(username.title() +
        '! Let\'s explore some US bikeshare data together.'))    


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # Goal: To get user input for one city (chicago, new york city or washington)
    cityname = ''
    while cityname.lower() not in CITIES:
        cityname = input('Which city would you like to know more about among:'
                         '\n\n- chicago \n- new york city \n- washington\n\n> ')
        if cityname.lower() in CITIES:
            city = CITIES[cityname.lower()]
        else:
            print('I found an error in your choice.'
                  '\nCan you make sure your selection was valid?\n> ')

    # Goal: To get user input for a specific month (all months, january, february, ... , june)
    monthname = ''
    while monthname.lower() not in MONTHS:
        monthname = input('Which months are you interested in? List them using ","'
                          '\n\n- january \n- february \n- march'
                          '\n- april \n- may \n- june \n- all'
                          ' (if you want to select all months)\n\n> ')

        if monthname.lower() in MONTHS:
            month = monthname.lower()
        else:
            print('I found an error in your choice.'
                  '\nCan you make sure your selection was valid?')

    # Goal: To get user input for weekdays (all days, monday, tuesday, ,,,ììì sunday)
    dayname = ''
    while dayname.lower() not in DAYS:
        dayname = input('\nAny particular weekday you want me to look at?'
                        '\n\n- monday \n- tuesday \n- wednesday'
                        '\n- thursday \n- friday \n- saturday \n- sunday'
                        '\n- all (if you want to select all days)\n\n> ')
        if dayname.lower() in DAYS:
            day = dayname.lower()
        else:
            print('I found an error in your choice.'
                  '\nCan you make sure your selection was valid?\n> ')
    print('|-' + '-'*60 + '-|')
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Goal: to load .csv into DF and manipulate/convert columns  
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour

    # Goal: to filter months/days if users wants to select a specific month/day

    if month != 'all':
        month = MONTHS.index(month)
        df = df.loc[df['month'] == month]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - DF containing city data filtered by month and day
    """

    print('\nThese are the statistics of the most frequent times of travel:\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print("- That's the most common month based on your selection: " +
          MONTHS[common_month].title())

    # Display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("- That's the most common weekday based on your selection: " +
          common_day_of_week)

    # Display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("- That's the most common start hour based on your selection: " +
          str(common_start_hour))

    print("\n>>> I calculated this in %s seconds." % round((time.time() - start_time)), 4)
    print('\n|-' + '-'*60 + '-|')


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - DF containing city data filtered by month and day
    """

    print('\nThese are the statistics of the most popular stations/trips:\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("- The most commonly used start station based on your selection is: " +
          common_start_station)

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("- The most commonly used end station based on your selection is: " 
        + common_end_station)

    # Display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] +
                            "||" + df['End Station']).mode()[0]
    print("- The most frequent combination of start station and end station trip is : " +
          str(frequent_combination.split("||")))

    print("\n>>> I calculated this in %s seconds." % round((time.time() - start_time)),2)
    print('\n|-' + '-'*60 + '-|')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nThese are the statistics related to the trips durations:\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\n- The total travel time based on your selection is: " +
          str(total_travel_time))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("- The mean travel time based on your selection is: " +
          str(mean_travel_time))

    print("\n>>> I calculated this in %s seconds." % round((time.time() - start_time)),4)
    print('\n|-' + '-'*60 + '-|')


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nThese are the main statistics related to users\'s gender and birth dates:\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types based on your selection is: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender based on your selection is: \n" + str(gender))
    
        # Display earliest year of birth 
        earliest_birth = df['Birth Year'].min()
        print('\n\n- The earliest year of birth based on your selection is: {}'.format(
            earliest_birth))

        # Display most recent year of birth
        most_recent_birth = df['Birth Year'].max()
        print('- The most recent year of birth based on your selection is: {}'.format(
            most_recent_birth))

        # Display most common year of birth 
        most_common_birth = df['Birth Year'].mode()[0]
        print('- The most common year of birth based on your selection is: {}'.format(
            most_common_birth))
    
        print("\n>>> I calculated this in %s seconds." % round((time.time() - start_time)),4)
        print('\n|-' + '-'*60 + '-|')


def display_raw_data(df):
    """Displays first 5 records of raw data if the user requests, incremented by 5 
       additional records at time
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input(
            '\nWould you like to view the next 5 records from the dataset? Enter yes or no.\n >')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # Display the latest 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input(
                '\nWould you like to view first 5 records from the dataset? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like me to restart? (yes or no).\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
