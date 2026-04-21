import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# STEP 1 : LOAD CONFIRMED CASES DATA
# ---------------------------------

confirmed = pd.read_csv(
    "archive/CONVENIENT_global_confirmed_cases.csv",
    skiprows=[1]   # skip Province/State row
)

print("Preview of dataset:")
print(confirmed.head())


# ---------------------------------
# STEP 2 : CLEAN DATA
# ---------------------------------

confirmed = confirmed.fillna(0)


# ---------------------------------
# STEP 3 : TRANSPOSE DATA
# ---------------------------------

confirmed = confirmed.set_index("Country/Region").T
confirmed.index.name = "Date"

confirmed.reset_index(inplace=True)


# ---------------------------------
# STEP 4 : FIX DATE FORMAT
# ---------------------------------

confirmed["Date"] = pd.to_datetime(
    confirmed["Date"],
    format="%m/%d/%y",
    errors="coerce"
)


# ---------------------------------
# STEP 5 : SAVE CLEAN DATA
# ---------------------------------

confirmed.to_csv("cleaned_covid_data.csv", index=False)

print("Cleaned dataset saved!")


# ---------------------------------
# STEP 6 : DAILY GLOBAL TREND
# ---------------------------------

daily_cases = confirmed.iloc[:,1:].sum(axis=1)

plt.figure(figsize=(10,5))
plt.plot(confirmed["Date"], daily_cases)

plt.title("Daily Global COVID Cases Trend")
plt.xlabel("Date")
plt.ylabel("Total Cases")

plt.xticks(rotation=45)
plt.show()


# ---------------------------------
# STEP 7 : TOP 10 COUNTRIES
# ---------------------------------

latest = confirmed.iloc[-1,1:]

top_countries = latest.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind="bar")

plt.title("Top 10 Countries COVID Cases")
plt.xlabel("Country")
plt.ylabel("Cases")

plt.show()


# ---------------------------------
# STEP 8 : DEATH ANALYSIS
# ---------------------------------

deaths = pd.read_csv(
    "archive/CONVENIENT_global_deaths.csv",
    skiprows=[1]
)

deaths = deaths.fillna(0)

deaths = deaths.set_index("Country/Region").T
deaths.index.name = "Date"

deaths.reset_index(inplace=True)

deaths["Date"] = pd.to_datetime(
    deaths["Date"],
    format="%m/%d/%y",
    errors="coerce"
)

latest_deaths = deaths.iloc[-1,1:]

top_deaths = latest_deaths.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_deaths.plot(kind="bar")

plt.title("Top Countries by COVID Deaths")

plt.show()