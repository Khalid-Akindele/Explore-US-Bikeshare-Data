import time
import pandas as pd
# import calendar module for full month and weekday names
import calendar as cal

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTHS = ["all", "january", "february", "march", "april", "may", "june"]
DAYS = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    def get_valid_input(prompt, valid_options):
        while True:
            user_input = input(prompt).strip().lower()
            if user_input in valid_options:
                return user_input
            else:
                print(f"Invalid input. Please enter one of {valid_options}.")

    city = get_valid_input("Please enter a city (Chicago, New York City, Washington): ", CITY_DATA.keys())
    month = get_valid_input("Please select a month (all, january, february, ... june): ", MONTHS)
    day = get_valid_input("Please select a day (all, monday, tuesday, ... sunday): ", DAYS)

    print('-' * 40)
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
    file_name = CITY_DATA[city]
    if file_name:
        df = pd.read_csv(file_name)

        # Converting the start time colum to a date time format
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # Extracting the month and day of the week from the Start Time column
        df["Month"] = df['Start Time'].dt.month
        df["Day_of_Week"] = df['Start Time'].dt.weekday

        # Applying month filter if month is not all
        if month != 'all':
            months = ["january", "february", "march", "april", "may", "june"]
            month = months.index(month) + 1
            df = df[df["Month"] == month]

        # Applying day filter if day is not all
        if day != 'all':
            days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            day = days.index(day)
            df = df[df['Day_of_Week'] == day]

        return df
    else:
        print("City data file not found.")
        return None

def calculate_most_common(column):
    return column.mode()[0]

def time_stats(df, month, day, city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = calculate_most_common(df['Month'])
    
    # to print name of the most common month
    if month != 'all':
        print('You have selected', month.title(), ', so, the most common month for travel in ', 
              city.title(), 'is definitely', cal.month_name[common_month], '.\n\n')
    else:
        print("The most common month for travel in ", city.title(), "is:", cal.month_name[common_month], ".\n\n")

    # display the most common day of week
    list(cal.day_name)
    common_day = calculate_most_common(df['Day_of_Week'])
    
    # to print name of the most common day of the week
    if day != 'all':
        print('You have selected ', day.title(), ', so, the most common day for travel in',
              city.title(), 'is definitely', cal.day_name[common_day], '.\n')
    else:
        print("The most common day of the week for travel in ", city.title(), 
              "is:", cal.day_name[common_day], ".\n")

    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_start_hour = calculate_most_common(df['Start Hour'])
    print(f'The most common start hour for travel for your selection is: {common_start_hour} o\'clock.\n\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print(f"The most commonly used start station for your selection is: {common_start_station}")

    # display most commonly used end station
    common_end_station = df['End Station'].mode()
    print(f"The most commonly used end station for your selection is: {common_end_station}")

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()
    print(f"The most frequent combination of start station and end station trip is: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    # to convert total travel time to hours
    total_time_hr = round(total_travel_time / 60 / 60, 2)
    
    print(f"Total travel time for your selection is: {total_time_hr} hours.\n")

    # display mean travel time (secs)
    mean_travel_time = df['Trip Duration'].mean()
    
    # to convert mean travel time to minutes
    mean_time_min = round(mean_travel_time / 60, 0)
    
    # display mean travel time either in minutes if below one hour, or in hours if above
    if mean_time_min < 60:
        print('The average travel time for your selection is ', mean_time_min, 'minutes.\n\n')
    else:
        mean_time_hr = round(mean_time_min / 60, 2)
        print('The average travel time for your selection is ', mean_time_hr, 'hours.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Counts of User Types: {user_types}")

    # Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print(f"\nCounts of Gender: {gender_count}")
    else:
        print("\nGender information is not available for this dataset.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]

        print("\nBirth Year Statistics: ")
        print(f"Earliest Birth Year: {earliest_birth_year:.0f}")
        print(f"Most Recent Birth Year: {most_recent_birth_year:.0f}")
        print(f"Most Common Birth Year: {common_birth_year:.0f}")
    else:
        print("\nBirth year information is not available for this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# new function for raw data display    
def raw_data(df):
    """ Displays 5 lines of raw data at a time when yes is selected."""
    # define index i, start at line 1
    i = 1
    while True:
        rawdata = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if rawdata.lower() == 'yes':
            # print current 5 lines
            print(df[i:i+5])
            
            # increase index i by 5 to print next 5 lines in new execution
            i = i+5        
        else:
            # break when 'no' is selected
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        if df is not None:            
            # adapted arguments to make the code run smoothly
            time_stats(df, month, day, city)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            
            # to call funtion to display raw data
            raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

    
