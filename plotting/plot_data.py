import pandas as pd
import matplotlib.pyplot as plt


def age_plot():
    data = pd.read_csv("name_sex_age.csv")

    print(data)
    names = data.Name
    ages = data.Age

    print(ages)
    print(names)

    plt.bar(names, ages, color='g', width=0.72, label="Age")
    plt.xlabel('Names')
    plt.ylabel('Ages')
    plt.title('Ages of different persons')
    plt.legend()
    plt.show()


def weather_plot(year: int, city: str):
    data = pd.read_csv("temperature.csv")
    data2 = data.query(f'City == "{city}" & year == {year+10}').sort_values(by="month")
    data = data.query(f'City == "{city}" & year == {year}').sort_values(by="month")

    y = [(item - 32) * (5 / 9) for item in data.AverageTemperatureFahr]
    while len(y) < 12:
        y.append(0)
    x = [i for i in range(1,13)]
    print(y)
    print(x)
    plt.plot(x, y, color='r', linestyle='dashed',
             marker='o', label="Weather Data")
    y2 = [(item - 32) * (5 / 9) for item in data2.AverageTemperatureFahr]
    print(y2)
    plt.plot(x, y2, color='g', linestyle='dashed', marker='*')
    plt.xlabel("Month")
    plt.ylabel("Temperature(C)")
    plt.legend()
    plt.show()


def oscars():
    pd.set_option('display.max_rows', 999)
    pd.set_option('display.max_columns', 999)
    pd.set_option('display.width', 999)
    data_male = pd.read_csv("oscar_age_male.csv")
    data_female = pd.read_csv("oscar_age_female.csv")

    data = pd.concat([data_male, data_female])

    age = list(set(data.Age))
    print(age)
    number_of_oscars = []
    for item in age:
        number_of_oscars.append(data.Age.value_counts()[item])
    print(number_of_oscars)

    plt.bar(age, number_of_oscars, color='g', width=0.72, label="Age")
    plt.xlabel('Age')
    plt.ylabel('Number of oscars')
    plt.title('Number of oscars by actors age')
    plt.legend()
    plt.show()


def pie():
    score = [85, 65, 70, 80, 60]
    subjects = ["Math", "Science", "History", "Economics", "Physics"]

    plt.pie(score, labels=subjects, autopct='%.2f%%')
    plt.show()



pie()
