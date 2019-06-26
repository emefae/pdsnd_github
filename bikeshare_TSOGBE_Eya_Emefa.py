import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#=========================================================================================================
#fonction  get_filters()
#the biggest's one !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Asks user to specify a city, month, and day to analyze    
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#============================================================================================================ 

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
print('*'*111)
time.sleep(2)
print('*'*111)
time.sleep(2)
print('*'*111)
time.sleep(2)
print('*'*111)
time.sleep(2)
print()
print('                         Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

print()
time.sleep(2)
print('                        Would you like to see data for Chicago, New York, or Washington?\n')
print()
print('*'*111)
print('*'*111)
print()
print('               =============>>>>>>> For Chicago enter 1\n')
print()
print('               =============>>>>>>> For New york enter 2\n')
print()
print('               =============>>>>>>> For Washington enter 3\n')
print()
print('                                    TO EXIT ENTER 0     \n')
print('*'*111)
print('*'*111)
time.sleep(2)
num_city = input("Please enter the number of the city you want to explore: \n")
a = 1
while a != 0 : 
   if num_city == '1':
    city = 'chicago'
    print('You have chose ',city,'\n')
    break
   elif num_city == '2':
    city = 'new york city'
    print('You have chose ',city,'\n')
    break
   elif num_city == '3':
    city = 'washington'
    print('You have chose ',city,'\n')
    break
   elif num_city == '0':      
    print('\n''    YOU HAVE CHOSE EXIT ','\n')
    print('\n''     #############','\n')
    print('\n''    BYE BYE, SEE YOU SOON !!!!' '\n')
    break
   else:
    print('INVALIDE INPUT !!!')
    num_city = input("Please enter the number of the city you want to explore: ")

    # get user input for month (all, january, february, ... , june)

time.sleep(3)
print('\n')
print('By Which month would you like to filter the data of ',city,'?\n')
print()
print('*'*111)
#print('*'*111)
print()
print('  * For January enter 1                           * For April enter 4\n')
print()
print('  * For February enter 2                          * For May enter 5\n')
print()
print('  * For March enter 3                             * For June enter 6\n')
print()
print('  * For none enter 7                             * TO EXIT ENTER 0\n')
print()
print('*'*111)
varmonth = input("Please enter the number of the month you want to explore: \n")
b = 1
while b != 0 : 
   if varmonth == '1':
    month = 'january'
    print('You have chose ',month,'\n')
    break
   elif varmonth == '2':
    month = 'february'
    print('You have chose ',month,'\n')
    break
   elif varmonth == '3':
    month = 'march'
    print('You have chose ',month,'\n')
    break
   elif varmonth == '4':
    month = 'april'
    print('You have chose ',month,'\n')
    break
   elif varmonth == '5':
    month = 'may'
    print('You have chose ',month,'\n')
    break
   elif varmonth == '6':
    month = 'june'
    print('You have chose ',month,'\n')
    break
   elif varmonth == '7':
    month = 'all'
    print('You have chose to not filter the data by month''\n')
    break
   elif varmonth == '0':      
    print('\n''    YOU HAVE CHOSE EXIT ','\n')
    print('\n''     #############','\n')
    print('\n''    BYE BYE, SEE YOU SOON !!!!' '\n')
    b = 0
    break
   else:
    print('INVALIDE INPUT !!!')
    varmonth = input("Please enter the number of the month you want to explore: \n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
#print('#'*111)
time.sleep(3)
print()
print()
print('By Which day of the week would you like to filter the data ?\n')
print()
print('*'*111)
print('*')
print('*                * For Sunday enter 1             * For Wednesday enter 4           * For Saturday enter 7   *')
print('*')
print('*                * For Monday enter 2             * For Thursday enter 5            * For none enter 8       *')
print('*')
print('*                * For Tuesday enter 3            * For Friday enter 6              * TO EXIT ENTER 0        *')
print('*')
print('*')
print('*')
print('*'*111)
varday = input("Please enter the number of the day of the week you want to explore: \n")
c = 1
while c != 0 : 
   if varday == '1':
    day = 'Sunday'
    print('You have chose ',day,'\n')
    print('Your choices : ',city,' ',month,'  ',day,'\n')    
    c = 0
    break
   elif varday == '2':
    day = 'Monday'
    print('You have chose ',day,'\n')
    print('Your choices : ',city,' ',month,'  ',day,'\n')    
    c = 0
    break
   elif varday == '3':
    day = 'Tuesday'
    print('You have chose ',day,'\n')
    print('Your choices : ',city,' ',month,'  ',day,'\n')
    c = 0
    break
   elif varday == '4':
    day = 'Wednesday'
    print('You have chose ',day,'\n')
    print('Your choices : ',city,' ',month,'  ',day,'\n')
    c = 0
    break
   elif varday == '5':
    day = 'Thursday'
    print('You have chose ',day,'\n')
    print('Your choices : ',city,' ',month,'  ',day,'\n')
    c = 0
    break
   elif varday == '6':
    day = 'Friday'
    print('You have chose ',day,'\n')
    print('Your choices : ',city,' ',month,'  ',day,'\n')
    c = 0
    break
   elif varday == '7':
    day = 'Saturday'
    print('You have chose ',day,'\n')
    print('Your choices : ',city,' ',month,'  ',day,'\n')
    c = 0
    break
   elif varday == '8':
    day = 'all'
    print('You have chose to not filter the data by day''\n')
    print('Your choices : ',city,' ',month,'  ',day,'\n')
    c = 0
    break
   elif varday == '0':      
    print('\n''    YOU HAVE CHOOSE EXIT ','\n')
    print('\n''     #############','\n')
    print('\n''    BYE BYE, SEE YOU SOON !!!!' '\n')
    c = 0
    break
   else:
    print('INVALIDE INPUT !!!')
    varday = input("Please enter the number of the day you want to explore: \n")

    print('-'*40)
    print('*'*111)
    print('\n Your choices : ',city,' ',month,'  ',day,'\n') 
# #   return city, month, day

#=========================================================================================================
#fonction  load_data(city, month, day) 
#Loads data for the specified city and filters by month and day if applicable.    
# 
#============================================================================================================ 


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
df['day_of_week'] = df['Start Time'].dt.weekday_name

# filter by month if applicable
if month != 'all':
   # use the index of the months list to get the corresponding int
   months = ['january', 'february', 'march', 'april', 'may', 'june']
   month = months.index(month) + 1

# filter by month to create the new dataframe
df = df[df['month'] == month]

# filter by day of week if applicable
if day != 'all':
   # filter by day of week to create the new dataframe
   df = df[df['day_of_week'] == day.title()]



###################    return df
#=========================================================================================================
#fonction  time_stats(df) 
#Displays statistics on the most frequent times of travel
# 
#============================================================================================================ 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()
# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name

    # display the most common month


# find the most popular month
popular_month = df['month'].mode()[0]

print('Most common start month:', popular_month)
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)



    # display the most common day of week

# find the most popular day_of_week
popular_day = df['day_of_week'].mode()[0]

print('Most common start day:', popular_day)
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

    # display the most common start hour

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

# find the most popular hour
popular_hour = df['hour'].mode()[0]

print('Most common start Hour:', popular_hour)
print("\nThis took %s seconds." % (time.time() - start_time))
time.sleep(3)
print('-'*40)
#=========================================================================================================
#fonction  station_stats(df) 
#Displays statistics on the most popular stations and trip
# display most commonly used start station,used end station
# combination of start station and end station trip
#============================================================================================================    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

print('\nCalculating The Most Popular Stations and Trip...\n')
start_time = time.time()
# extract month and day of week from Start Time to create new columns
df['Trip from start to end'] ='From '+df['Start Station']+' to '+df['End Station']

    # display most commonly used start station
# find the most commonly used start station
common_start_station = df['Start Station'].mode()[0]
print('Most commonly used start station:', common_start_station)

    # display most commonly used end station
# find the most commonly used end station
common_end_station = df['End Station'].mode()[0]
print('Most commonly used end station:', common_end_station)

    # display most frequent combination of start station and end station trip
common_trip_start_end_station = df['Trip from start to end'].mode()[0]
print('Most frequent combination of start station and end station:', common_trip_start_end_station)
print("\nThis took %s seconds to calculate the most popular stations and trip." % (time.time() - start_time))
time.sleep(3)
print('-'*40)

#=========================================================================================================
#fonction  trip_duration_stats(df) 
#Displays statistics on the total and average trip duration
# 
#============================================================================================================  


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

print('\nCalculating Trip Duration...\n')
start_time = time.time()

    # display total travel time
total_trip_duration = df['Trip Duration'].sum()
print('Total duration:', total_trip_duration)

    # display mean travel time
avg_trip_duration = df['Trip Duration'].mean()
print('The average duration:', avg_trip_duration)

print("\nThis took %s seconds to do statistics on the total and average trip duration." % (time.time() - start_time))
time.sleep(3)
print('-'*40)

#=========================================================================================================
#fonction  user_stats(df) 
#Display counts of user types, gender
# print value counts for each user type, for each gender
# # Display earliest, most recent, and most common year of birth
#============================================================================================================  

def user_stats(df):
    """Displays statistics on bikeshare users."""
if city!='washington':
    print('\nCalculating User Stats...\n')
    start_time = time.time()



    # Display counts of user types
# print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types)



    # Display counts of gender
# print value counts for each gender

    gender_types = df['Gender'].value_counts()
    print(gender_types)

    # Display earliest, most recent, and most common year of birth
# find the most popular year of birth
    common_year = df['Birth Year'].mode()[0]
# find the recent year of birth
    most_recent_year = max(df['Birth Year'])
# find the earliest year of birth
    most_earliest_year = min(df['Birth Year'])
# Display earliest, most recent, and most common year of birth
    print('Most common birth year:', int(common_year))
    print('Most recent birth year:', int(most_recent_year))
    print('Most earliest birth year:', int(most_earliest_year))

    print("\nThis took %s seconds to calculate User Stats." % (time.time() - start_time))
    time.sleep(3)
    print('-'*40)

#=========================================================================================================
# o is the file i will display
# it depend on the name of the city the user choose
# fonction show_me_city(o) display the city informations, statistiques
#============================================================================================================ 
def show_me_city(o):
     d = 5   
     while d != 0 :   
         df = pd.read_csv(o,nrows = d)
         print(df)
         d += 5
         print(d)
         var_continue = input('would you like to see more? Enter yes or no\n')
         if var_continue.lower() != 'yes':
             break
 #=========================================================================================================
      # the main program . here i can call fonctions and pass values to them
      # 
     #============================================================================================================ 

def main():
 while True:
      #city, month, day = 
      #•print('Hello! Let\'s explore some US bikeshare data!')
      get_filters()
      df = load_data(city, month, day)

      time_stats(df)
      time.sleep(3)
      station_stats(df)
#=========================================================================================================
      # city=='washington'.There is no gender data to share',There is no birth year data to share
      # so i don't want to run the fonction for washington
     #============================================================================================================      
      trip_duration_stats(df)
      if city!='washington':
          user_stats(df)
      else:
          print('There is no gender data to share','\n','There is no birth year data to share','\n')
            
          break
          print()
      
      #=========================================================================================================
      # o is the file i will display
      # it depend on the name of the city the user choose
     # fonction show_me_city(o) display the city informations, statistiques
     #============================================================================================================ 
      if city == 'washington':
           o= 'washington.csv'
      elif city == 'new york city':
           o= 'new_york_city.csv'
      elif city == 'chicago':
           o= 'chicago.csv'     
      else: 
            print('THERE IS NO CITY DATA TO SHARE ','\n','\n')

     
      show_me_city(o)
      print('*'*111)
      time.sleep(2)
      print('*'*111)
      time.sleep(2)
      print('*'*111)
      time.sleep(2)
      print('*'*111)
      time.sleep(2)
      restart = input('\nWould you like to restart? Enter yes or no.\n')
      if restart.lower() != 'yes':
            
          print('\n''    YOU HAVE CHOSE EXIT ','\n')
          print('\n''     #############','\n')
          print('\n''    BYE BYE, SEE YOU SOON !!!!' '\n')
          print('*'*111)
          time.sleep(2)
          print('*'*111)
          break


if __name__ == "__main__":
	main()
