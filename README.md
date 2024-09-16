[![Python 3.11.9](https://github.com/syedhumarahim/scaffold/actions/workflows/main.yml/badge.svg)](https://github.com/syedhumarahim/scaffold/actions/workflows/main.yml)

# Scaffold
This is the first Assignment for Data Engineering on Scaffolding.

# F1 Fastest Lap Analysis

## Project Overview

This project analyzes the fastest lap data from the 2024 Italian Grand Prix. The main focus is to determine the driver with the highest average speed for a given team. The project is implemented in Python, with a simple command-line interface and unit tests to verify the functionality.


## Code Description

### `main.py`

- **Functionality**:
  - **`get_driver_with_highest_avg_speed(car_name)`**: 
    - Takes the name of a car/team as input.
    - Filters the data to find the driver with the highest average speed for that team.
    - Returns the driver's name, the lap number, and the average speed.
  - **User Interaction**: The script prompts the user to enter a team name and displays the corresponding fastest lap details. For the CI/CD pipeline the input is hardcoded. However, it can be taken as an input from the user.

### `test_main.py`

- **Purpose**: Contains unit tests to verify the correctness of the `get_driver_with_highest_avg_speed` function.
- **Tests**:
  - **`test_mclaren_mercedes`**: Ensures that the function correctly identifies Norris as the fastest driver for McLaren Mercedes.
  - **`test_mercedes`**: Ensures that the function correctly identifies Hamilton as the fastest driver for Mercedes.
  - **`test_nonexistent_team`**: Checks the behavior of the function when a non-existent team is provided.

## Data

The data used in this project is stored in a CSV file located in the `data/` directory:

- **`italian_gp_2024_fastestlaps.csv`**: Contains lap time, driver, car, average speed, and other relevant details from the 2024 Italian Grand Prix.

