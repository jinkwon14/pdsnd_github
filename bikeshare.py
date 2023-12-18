import time
import pandas as pd
import numpy as np
import calendar # pull in calendar months and corresponding numeric months
pd.set_option('max_columns', None)


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_NAMES_DICT = {calendar.month_name[i].lower():i for i in range(1, 13)}
WEEK_NAMES = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

# ref: https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/
def convert(time):
    """Given number of seconds, output number of days, hours, minutes, and seconds as a string.
    
    Returns:
        (str) output_str - number of seconds recomputed into number of days/hours/minutes/seconds
    """
    result_string = ''
    
    day = time // (24 * 3600)
    if day != 0: 
        result_string += f"{day} day(s)"
        
    time = time % (24 * 3600)
    hour = time // 3600
    if hour != 0: 
        result_string += f"{hour} hour(s)"
        
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = round(time)
    
    output_str = result_string + f" {minutes} minutes {seconds} seconds"
     
    return output_str


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day_of_week - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        # prompt to select a city
        city = input("Select a city (select from Chicago, New York City, and Washington): \n")
        
        # lowercase city for name check
        city_lower = city.lower()
        
        if city_lower == 'chicago' or city_lower == 'new york city' or city_lower == 'washington': 
            break 
        else: 
            print(f"{city} is not a valid selection.\n")
        
    
    # get user input for month (all, january, february, ... , june)
    while True: 
        month = input("Select a month (all, january, february, ... , june): \n")
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']: 
            break 
        else: 
            print(f"{month} is not a valid selection.\n")
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day_of_week = input("Select a day of week (all, monday, tuesday, ... sunday): \n")
        if len([el for el in WEEK_NAMES + ['all'] if el == day_of_week.lower()]) == 1: 
            break 
        else: 
            print(f"{day_of_week} is not a valid selection.\n")
    
    print('-'*40)
    return city.lower(), month.lower(), day_of_week.lower()




def load_data(city, month, day_of_week):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    DATA_PATH = CITY_DATA[city]
    city_df   = pd.read_csv(DATA_PATH)
    city_df['start_time'] = pd.to_datetime(city_df['Start Time'])
    city_df['end_time']   = pd.to_datetime(city_df['End Time'])
    
    if month != 'all': 
        # let's filter by month of the rental start time
        month_num = [val for key, val in MONTH_NAMES_DICT.items() if key == month][0]
        city_df = city_df[city_df['start_time'].dt.month == month_num]
        
    if day_of_week != 'all':
        city_df = city_df[city_df['start_time'].dt.day_name() == day_of_week.capitalize()]
    
    return city_df

def display_sample_data(df): 
    """Displays sampe data."""

    start_idx = 0
    is_display = 'yes'
    additional = ''
    
    while is_display != 'no':
        is_display = input(f"Would you like to display 5{additional} rows of the selected data (yes/no): \n")
        if is_display == 'yes': 
            print(df.iloc[start_idx: start_idx + 5])
            start_idx += 5
            additional = ' additional'
        else: 
            print(f"{is_display} is not a valid input.")
        


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\n\n' + '='*30)    
    print('Calculating The Most Frequent Times of Travel...')
    start_time = time.time()
    df['start_time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['start_month'] = df['start_time'].dt.month
    most_common_mo = df['start_month'].value_counts().idxmax()

    
    # display the most common day of week
    df['day_of_week'] = df['start_time'].dt.day_name()
    most_common_dow = df['day_of_week'].value_counts().idxmax()
    

    # display the most common start hour
    df['start_hr'] = df['start_time'].dt.hour
    most_common_hr = df['start_hr'].value_counts().idxmax()

    
    print(f"Most Popular Month is       {most_common_mo}")
    print(f"Most Popular Day of Week is {most_common_dow}")
    print(f"Most Popular Start Hour is  {most_common_hr}")
    print("\nThis took %s seconds." % round((time.time() - start_time), 5))
    print('='*30)    

    
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\n\n' + '='*30)    
    print('Calculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()

    # display most frequent combination of start station and end station trip
    most_common_hr = df.groupby(['Start Station', 'End Station']).size().reset_index(name="count")
    common_start_station_pair, common_end_station_pair, _ = list(most_common_hr.sort_values('count', ascending = False).values[:1])[0]
    

    print(f"Most Popular Start Station is {common_start_station}")
    print(f"Most Popular End Station is {common_end_station}")
    print(f"Most Popular Start - End Station Pair is {common_start_station_pair} - {common_end_station_pair}")
    
    print("\nThis took %s seconds." % round((time.time() - start_time), 5))
    print('='*30)  
    
    
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\n\n' + '='*30)    
    print('Calculating Trip Duration...')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    # summariz
    print(f"total   travel time is {convert(total_travel_time)}")
    print(f"average travel time is {convert(mean_travel_time)}")
    
    
    print("\nThis took %s seconds." % round((time.time() - start_time), 5))
    print('='*30)




def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\n\n' + '='*30)    
    print('Calculating User Stats...')
    start_time = time.time()

    # Display counts of user types
    user_count_summary = df['User Type'].value_counts().reset_index()
    user_count_summary.columns = ['User Type', 'Number of Records']
    print('- '*20)
    print("Summary on User Types:")
    print(user_count_summary)
    
    # Display counts of gender
    try: 
        gender_count_summary = df['Gender'].value_counts().reset_index()
        gender_count_summary.columns = ['Gender', 'Number of Records']
        print('- '*20)
        print("Summary on Gender:")
        print(gender_count_summary)
        print('- '*20)
    except KeyError: 
        print(f"{city} does not have Gender columns") 

        
    try: 
        # Display earliest, most recent, and most common year of birth
        df              = df[~df['Birth Year'].isna()]
        earliest_yob    = df['Birth Year'].max() 
        latest_yob      = df['Birth Year'].min() 
        most_common_yob = df['Birth Year'].value_counts().idxmax() 
        
        # summariz
        print('\n')
        print(f"Earliest      birth year in the data is {int(earliest_yob)}")
        print(f"Latest        birth year in the data is {int(latest_yob)}")
        print(f"Most frequent birth year in the data is {int(most_common_yob)}")        
    except KeyError: 
        print(f"{city} does not have Birth Year columns") 
        
    print("\nThis took %s seconds." % round((time.time() - start_time), 5))
    print('='*30)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_sample_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        while True: 
            restart = input('\nWould you like to restart? Enter yes(y) or no(n).\n')
            if restart.lower() == 'yes' or restart.lower() == 'y':
                break
            elif restart.lower() == 'no' or restart.lower() == 'n':
                return
            else: 
                print(f"{restart} is not a valid selection.")
                continue

                
if __name__ == "__main__":
	main()
