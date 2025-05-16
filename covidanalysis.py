

import matplotlib.pyplot as plt
import pandas as pd


# Load the CSV file
df = pd.read_csv('owid-covid-data.csv')



print("Columns in the dataset:")
print(df.columns)


print("\nFirst 5 rows:")
print(df.head())


print("\nMissing values in each column:")
print(df.isnull().sum())




# Select countries to compare
selected_countries = ['United States', 'India', 'Brazil']



# Filter data for selected countries and non-null total_cases
df = df[df['location'].isin(selected_countries)]
df = df[['location', 'date', 'total_cases', 'total_deaths', 'new_cases']].dropna(subset=['total_cases'])


# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])


# --- 1. Plot Total Cases Over Time ---
plt.figure(figsize=(12, 6))
for country in selected_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# --- 2. Plot Total Deaths Over Time ---
plt.figure(figsize=(12, 6))
for country in selected_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# --- 3. Compare Daily New Cases ---
plt.figure(figsize=(12, 6))
for country in selected_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# --- 4. Calculate and Plot Death Rate ---
df['death_rate'] = df['total_deaths'] / df['total_cases']
avg_death_rate = df.groupby('location')['death_rate'].mean()

# Plot average death rate
avg_death_rate[selected_countries].plot(kind='bar', color='coral', figsize=(8, 5), title='Average Death Rate by Country')
plt.ylabel('Death Rate')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#Total Cases Over Time:

countries = ['United States', 'India', 'Brazil']
df = df[df['location'].isin(countries)]
df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


#Total Death over time

plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)

plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


#bar charts top 10 countries by Total Cases

# Get latest data for each country
latest = df.sort_values("date").groupby("location").tail(1)
top10 = latest.nlargest(10, 'total_cases')

plt.figure(figsize=(10, 6))
plt.barh(top10['location'], top10['total_cases'], color='skyblue')
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Total Cases")
plt.gca().invert_yaxis()  # Highest at top
plt.tight_layout()
plt.show()



# Plot
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title("Cumulative COVID-19 Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Compare % Vaccinated Population (Bar Chart)

# Get latest available data for each country
latest = df.sort_values('date').groupby('location').tail(1)

# Bar chart for people fully vaccinated per hundred
plt.figure(figsize=(8, 5))
vaccination_rates = latest.set_index('location').loc[countries]['people_fully_vaccinated_per_hundred']
vaccination_rates.plot(kind='bar', color='mediumseagreen')

plt.title("People Fully Vaccinated per 100 Population")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Pie Chart (Vaccinated vs. Unvaccinated)

# Get latest data for US
us = latest[latest['location'] == 'United States'].iloc[0]
vaccinated = us['people_fully_vaccinated_per_hundred']
unvaccinated = 100 - vaccinated

# Pie chart
plt.figure(figsize=(6, 6))
plt.pie([vaccinated, unvaccinated],
        labels=['Vaccinated', 'Unvaccinated'],
        autopct='%1.1f%%',
        colors=['green', 'lightgray'],
        startangle=90)

plt.title("United States: Vaccinated vs. Unvaccinated")
plt.axis('equal')
plt.tight_layout()
plt.show()




