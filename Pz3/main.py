import markovify

try:
    with open('dataset.txt', 'r', encoding='utf-8') as file:
        corpus = file.read()
except FileNotFoundError:
    print("Помилка: Файл 'dataset.txt' не знайдено.")
    exit(1)
except Exception as e:
    print(f"Помилка при читанні файлу: {e}")
    exit(1)

if not corpus.strip():
    print("Помилка: Файл 'dataset.txt' порожній.")
    exit(1)

text_model = markovify.Text(corpus, state_size=1)

for i in range(3):
    generated_report = text_model.make_short_sentence(140, tries=100)
    if generated_report is None:
        generated_report = "Не вдалося згенерувати звіт через обмеження."
    print(f"Звіт {i+1}: {generated_report}")
