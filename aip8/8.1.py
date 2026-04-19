countries = {
    "Россия": "Москва",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Франция": "Париж",
    "Китай": "Пекин",
    "Япония": "Токио"
}

for key in countries:
    print(key, "-", countries[key])
print()

country = input("Введите любую страну из перечисленных: ")
capital = countries.get(country)
print(f"Для этой страны столица - {capital}")
print()

list_countries = list(countries.keys())
list_countries.sort()
print("Сортировка по алфавиту: ")
for i in list_countries:
    print(i, "-", countries[i])
