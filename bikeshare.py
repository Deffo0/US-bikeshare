import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) choice - type of filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("would you like to see the data for chicago, new york city or washington: ").lower()
    while (city != "chicago" and city != " new york city" and city != "washington"):
        print("it seems you enter a wrong city, please try again.")
        city = input("would you like to see the data for chicago, new york city or washington: ")

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    choice = input("would you like to filter data by \"month\", \"day\", \"both\" or \"not at all\": ").lower()
    while (choice != "day" and choice != "month" and choice != "both" and choice != "not at all"):

        print("it seems you enter a wrong answer, please try again.")
        choice = input("would you like to filter data by \"month\", \"day\", \"both\" or \"not at all\": ").lower()

    if choice == "month":

        day = "all"
        month = input("which month from the first six months?\n- ").lower()
        while(month not in months):

            print("it seems you enter a wrong answer, please try again.")
            month = input("which month from the first six months?\n- ")

    elif choice == "day":
        month = "all"
        day = input("which day?\n- ").lower()
        while(day not in days):

            print("it seems you enter a wrong answer, please try again.")
            day = input("which day?\n- ")

    elif choice == "both":
        month = input("which month from the first six months?\n- ").lower()
        while (month not in months):

            print("it seems you enter a wrong answer, please try again.")
            month = input("which month from the first six months?\n- ")

        day = input("which day?\n- ").lower()
        while (day not in days):
            print("it seems you enter a wrong answer, please try again.")
            day = input("which day?\n- ")

    elif choice == "not at all":
        day = "all"
        month = "all"

    print('-' * 40)
    return city, month, day, choice


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
    df = pd.read_csv(CITY_DATA[city],index_col= [0])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df["month"] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df, choice):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if (choice != "both"):

        if (choice != "month"):
            # TO DO: display the most common month
            month_mode = df.month.mode()[0]
            print("Most Frequent Month: {}    count: {}".format(month_mode, df["month"].value_counts()[month_mode]))

        if (choice != "day"):
            # TO DO: display the most common day of week
            day_mode = df.day_of_week.mode()[0]
            print("Most Frequent Day: {}    count: {}".format(day_mode, df["day_of_week"].value_counts()[day_mode]))

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    hour_mode = df['hour'].mode()[0]
    print('Most Frequent Start Hour: {}    count: {}'.format(hour_mode, df["hour"].value_counts()[hour_mode]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_mode = df["Start Station"].mode()[0]
    print("Most Frequent Start Station: {}    count: {}".format(start_station_mode,
                                                                df["Start Station"].value_counts()[start_station_mode]))

    # TO DO: display most commonly used end station
    end_station_mode = df["End Station"].mode()[0]
    print("Most Frequent End Station: {}    count: {}".format(end_station_mode,
                                                              df["End Station"].value_counts()[end_station_mode]))

    # TO DO: display most frequent combination of start station and end station trip
    df["trips"] = "From " + df["Start Station"] + " to " + df["End Station"]
    trip_mode = df["trips"].mode()[0]
    print("Most Frequent trip: {}    count: {}".format(trip_mode, df["trips"].value_counts()[trip_mode]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df["Trip Duration"].sum()
    tot_days = total / (3600 * 60)
    total /= (3600 * 60)
    tot_seconds = total

    print("Total Trip Duration: {}".format(datetime.timedelta(days=tot_days, seconds=tot_seconds)))

    # TO DO: display mean travel time
    average = df["Trip Duration"].mean()
    av_days = average / (3600 * 60)
    average /= (3600 * 60)
    av_seconds = total

    print("Average Trip Duration: {}".format(datetime.timedelta(days=av_days, seconds=av_seconds)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types:\n", df["User Type"].value_counts(), "\n")

    # handling a corner case in which our city is not washington
    if "Gender" not in df:
        print("gender and birth year stats can't be displayed because it didn't exist in the data of this city\n")
    else:
        # TO DO: Display counts of gender
        print("counts of gender:\n", df["Gender"].value_counts(), "\n")

        # TO DO: Display earliest, most recent, and most common year of birth
        print("The Oldest Person: {}".format(df["Birth Year"].min()), "\n")
        print("The Youngest Person: {}".format(df["Birth Year"].max()), "\n")
        print("The Most Frequent Year of Birth: {}".format(df["Birth Year"].mode()[0]), "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """Displays raw data upon request from the user"""
    start_time = time.time()

    view_data = input("would you like to see the first five row of the data? say 'yes' or 'no': ").lower()
    row_tracker = 0
    while (view_data == "yes"):
        # Display five rows from the data
        print(df.iloc[row_tracker:row_tracker + 5].to_dict())
        row_tracker += 5
        view_data = input("would you like to see the next five row of the data? say 'yes' or 'no': ").lower()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day, choice = get_filters()
        df = load_data(city, month, day)
        original_df = df.copy()
        time_stats(df, choice)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(original_df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
