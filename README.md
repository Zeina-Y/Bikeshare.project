# Bike Share Data Analysis
This project explores data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. The project aims to provide insights into bike share usage patterns by computing descriptive statistics.

## Project Overview
In this project, Python is used to analyze bike share data provided by Motivate, a bike share system provider. The analysis includes the following statistics:

1. **Popular times of travel**:
    - Most common month
      
    - Most common day of week
      
    - Most common hour of day

2. **Popular stations and trips**:
    - Most common start station
      
    - Most common end station
      
    - Most common trip from start to end

3. **Trip duration**:
    - Total travel time
      
    - Average travel time  

4. **User info**:
    - Counts of each user type
      
    - Counts of each gender (only available for NYC and Chicago)
  
    - Earliest, most recent, and most common year of birth (only available for NYC and Chicago)

## Datasets
The datasets used in this project are provided in the `data` directory. The data files are as follows:

- `chicago.csv`
  
- `new_york_city.csv`
  
- `washington.csv`

## Getting Started

### Prerequisites

- Python 3.6+
  
- Pandas library

### Running the Analysis
The analysis is performed using the script `bikeshare.py` located in the `src` directory. To run the script, use the following command:
```bash
python bikeshare.py
```

### Example Usage
When you run the script, you'll be prompted to select a city and apply filters by month or day. The script will then display various statistics based on your selection.

### Additional Information
- The script allows you to view individual trip data upon request.

- The script provides an option to restart the analysis with different filters.

## Examples
### Example 1: Analyzing Chicago Data for January
**Input:**
- City: Chicago
- Month: January
- Day: None

**Expected Output:** 
```
----------------------------------------
The most common month is January. Counts: 3245

This took 0.02 seconds.

The most common day is Wednesday. Counts: 645

This took 0.01 seconds.

The most common start hour is 17. Counts: 231

This took 0.01 seconds.
----------------------------------------
The most common start station is Clinton St & Washington Blvd. Counts: 99

This took 0.01 seconds.

The most common end station is Lake Shore Dr & Monroe St. Counts: 85

This took 0.01 seconds.

Frequent combination of start and end Station is ('Clinton St & Washington Blvd', 'Lake Shore Dr & Monroe St'). Counts: 21

This took 0.02 seconds.
----------------------------------------
Total travel time:
4 days 12:30:45

Average travel time:
0:14:32

This took 0.01 seconds.
----------------------------------------
Counts of user types:
Subscriber    3000
Customer      245
Name: User Type, dtype: int64

This took 0.01 seconds.

Counts of gender:
Male      2000
Female    1245
Name: Gender, dtype: int64

Earliest birth year: 1940
Most recent birth year: 1999
Most common birth year: 1985

This took 0.02 seconds.
----------------------------------------
Would you like to view individual trip data? Type 'yes' or 'no'.
```
## Dataset 
https://www.kaggle.com/datasets/marwandiab/bike-share-data-udacity





