import pandas as pd
import os

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("2-demographic-data-analyzer/adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df.sex == "Male"].age.mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    num_people_with_bachelors = df.loc[df.education=="Bachelors"].shape[0]
    percentage_bachelors = num_people_with_bachelors/total_people *100
    percentage_bachelors = round(percentage_bachelors,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education =  df.loc[(df.education == "Masters") |(df.education == "Bachelors") | (df.education == "Doctorate")]
    lower_education = df.loc[(df.education != "Masters") & (df.education != "Bachelors") & (df.education != "Doctorate")]

    # percentage with salary >50K
    total_people_higher_education = higher_education.shape[0]
    num_people_with_higher_educationGT50K =  higher_education.loc[higher_education.salary == ">50K"].shape[0]
    higher_education_rich = num_people_with_higher_educationGT50K/total_people_higher_education * 100
    higher_education_rich = round(higher_education_rich,1)

    total_people_lower_education = lower_education.shape[0]
    num_people_with_lower_educationGT50K = lower_education.loc[lower_education.salary == ">50K"].shape[0]
    lower_education_rich = num_people_with_lower_educationGT50K / total_people_lower_education * 100
    lower_education_rich = round(lower_education_rich,1)
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].values.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hour_workers = df.loc[df["hours-per-week"] == min_work_hours]
    
    num_min_workers = min_hour_workers.shape[0]
    
    num_min_workersGT50K = min_hour_workers.loc[min_hour_workers["salary"] == ">50K"].shape[0]

    rich_percentage = num_min_workersGT50K/num_min_workers * 100


    # What country has the highest percentage of people that earn >50K?
    people_from_countryGT50K = df.loc[df.salary == ">50K"]["native-country"].value_counts()
    people_from_country = df["native-country"].value_counts()
    req = people_from_countryGT50K / people_from_country
    highest_earning_country = req.idxmax()
    highest_earning_country_percentage = round(req.max()*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    indian_data = df.loc[df["native-country"] == "India"].loc[df.salary == ">50K"]
    top_IN_occupation = indian_data.occupation.value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
