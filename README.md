# User Behavior Analysis

A Python project for analyzing user behavior data using Pandas.

## Overview

This project processes a CSV file with user data.
It filters users by age, categorizes them by spending level, calculates statistics, sorts the results, and exports the final dataset to a new CSV file.

## Features

* Load data from a CSV file
* Filter users older than 18
* Categorize users by spending level
* Calculate average spending
* Find maximum spending
* Sort users by spending
* Export processed data to a new CSV file

## Files

* `project5.py` — main Python script
* `users.csv` — input dataset
* `final_users.csv` — processed output dataset
* `README.md` — project documentation

## Technologies

* Python
* Pandas

## How it works

The script performs the following steps:

1. Reads user data from a CSV file
2. Filters users with age greater than 18
3. Creates a `category` column based on spending:

   * `VIP` for spending greater than or equal to 1500
   * `Medium` for spending greater than or equal to 800
   * `Low` for spending below 800
4. Calculates average spending
5. Finds maximum spending
6. Sorts users by spending in descending order
7. Saves the final result to a new CSV file

## Run the project

```python
py project5.py
```

## Example output

The output file contains:

* filtered users
* spending category for each user
* sorted spending data

## Purpose

This project demonstrates data filtering, conditional categorization, statistics, and CSV export using Python and Pandas.
