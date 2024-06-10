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
python src/bikeshare.py
```

### Example Usage
When you run the script, you'll be prompted to select a city and apply filters by month or day. The script will then display various statistics based on your selection.

### Additional Information
- The script allows you to view individual trip data upon request.

- The script provides an option to restart the analysis with different filters.


