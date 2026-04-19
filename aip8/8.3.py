students = {
    "Петров": ["английский", "немецкий", "китайский"],
    "Иванов": ["английский", "французский"],
    "Сидоров": ["китайский", "испанский"],
    "Волков": ["немецкий", "английский", "французский"],
    "Романов": ["китайский", "японский", "испанский"]
}
all_langs = set()
for name in students:
    for lang in students[name]:
        all_langs.add(lang)
print("Студенты знают эти языки: ", sorted(all_langs))
print()

count_chinese = 0
for name in students:
    for lang in students[name]:
        if lang == "китайский":
            count_chinese += 1
print(f"Студентов, знающих китайский язык: {count_chinese}")
