import pandas as pd
import numpy as np
import time


CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

months = ['January' , 'February' , 'March' , 'April' , 'May' , 'June']
days = ['Sunday' , 'Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday']
day = None
month = None
city = None

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    global month
    month = None
    global day
    day = None
    global city
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        try:
            city = str(input("Would you like to see data for Chicago, New York or Washington?\n "))
            if city.title() == "Washington" :
                break
            elif city.title() == "New York" :
                break
            elif city.title() == "Chicago" :
                break
            else :
                print("Please type a valid input!\n")

        except ValueError :
            print("Please type a valid input!\n")
    #use if to check for correct month name input
    while(True):
        try:
            filter = str(input('Would you like to filter the data by month, day, both, or not at all?\nType \"none" for no time filter:\n '))
            if filter == "month" :

                month = input("Which month? January, February, March, April, May, or June?\n ")
                if month.title() in months :
                    break
                else :
                    print("Please type a valid input!\n")

            #Checking fo day input
            elif filter =="day" :
                day = str(input("Which day? Please input full day name, etc Friday:\n "))
                if day.title() in days :
                    break
                else :
                    print("Please type a valid input!\n")

            elif filter == "both" :
                month = input("Which month? January, February, March, April, May, or June?\n ")
                day = input("Which day? Please input full day name, etc Friday:\n ")
                if (day.title() in days) and (month.title() in months):
                    break
                else :
                    print("Please type a valid input!\n")


            elif filter == "none" :
                break
            else :
                print("Please type a valid input!")

        except ValueError :
            print("Please type a valid input!")
    if month != None :
        month = month.title()
    if day != None :
        day = day.title()
    city = city.title()
    print('-'*40)
    return city , month , day

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != None:
        # use the index of the months list to get the corresponding int
        months = ['January' , 'February' , 'March' , 'April' , 'May' , 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != None:
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')


    # display the most common month
    if month == None :
        start_time = time.time()
        months = ['January' , 'February' , 'March' , 'April' , 'May' , 'June']
        common_month_index = df['month'].mode()[0]
        common_month = months[common_month_index-1]
        month_count = df['month'].value_counts().max()
        print("The most common month is {}. Counts: {}".format(common_month, month_count))
        print("\nThis took %s seconds.\n" % (time.time() - start_time))
    # display the most common day of week
    if day == None :
        start_time = time.time()
        common_day = df['day'].mode()[0]
        day_count = df['day'].value_counts().max()
        print("The most common day is {}. Counts: {}".format(common_day, day_count))
        print("\nThis took %s seconds.\n" % (time.time() - start_time))
    # display the most common start hour
    start_time = time.time()
    common_hour=df['hour'].mode()[0]
    hour_count = df['hour'].value_counts().max()
    print("The most common start hour is {}. Counts: {}".format(common_hour, hour_count))
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_common = df['Start Station'].mode()[0]
    start_count = df['Start Station'].value_counts().max()
    print("The most common start station is {}. Counts: {}".format(start_common, start_count))
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    # display most commonly used end station
    start_time = time.time()
    end_common = df['End Station'].mode()[0]
    end_count = df['End Station'].value_counts().max()
    print("The most common end station is {}. Counts: {}".format(end_common, end_count))
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    # display most frequent combination of start station and end station trip
    start_time = time.time()
    combination = df.groupby(['Start Station', 'End Station']).size().idxmax()

    comb_count = df.groupby(['Start Station', 'End Station']).size().max()
    print("Frequent combination of start and end Station is\n {}. Counts: {}".format(combination, comb_count))
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display t'otal travel time
    total = df["Trip Duration"].sum()
    day = total // (24 * 3600)
    total = total % (24 * 3600)
    hour = total // 3600
    total %= 3600
    minutes =total // 60
    total %= 60
    seconds = total
    print("Total travel time:")
    print("{} days %d:%d:%d".format(day) % (hour, minutes, seconds))
    # display mean travel time
    av = df["Trip Duration"].mean()
    h = av // 3600
    av %= 3600
    m = av // 60
    av %= 60
    s = av
    print("Average travel time: ")
    print(" %d:%d:%d" % (h, m, s))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df["User Type"].value_counts()
    print("Counts of user types:\n{}".format(user_count))
    print("\nThis took %s seconds.\n" % (time.time() - start_time))

    # Display counts of gender
    start_time = time.time()
    if city == "Washington" :
        print("No gender information available.\nNo birth year information available.")
    else :
        gender = df["Gender"].value_counts()
        print("Counts of gender:\n{}\n".format(gender))

    # Display earliest, most recent, and most common year of birth
        earliest = df["Birth Year"].min()
        recent = df["Birth Year"].max()
        com_birth = df["Birth Year"].mode()[0]
        print("The oldest: {}\nThe youngest: {}\nThe most common year of birth: {}".format(earliest, recent, com_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df) :
    pd.set_option('display.max_columns',200)
    response = input("\nWould you like to view individual trip data? Type 'yes' or 'no'.\n ")
    while response == 'yes' :
        print(df.sample(n=5))
        response = input("\nWould you like to view more individual trip data? Type 'yes' or 'no'.\n ")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
