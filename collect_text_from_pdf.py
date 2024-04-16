import string
from pypdf import PdfReader

LETTERS = string.ascii_lowercase + string.digits + \
    'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '

reader = PdfReader("data/interview_questions.pdf")

try:
    for page in reader.pages:
        page_content = page.extract_text()

        i = 0
        while page_content[i:i+1] != '\n':
            page_header_for_filename = str(page_content[:i])
            i += 1

        page_header_for_filename = "".join(
            [ch for ch in page_header_for_filename.lower() if ch in LETTERS])

        file_name = f"data/questions/{page_header_for_filename}.txt"
        with open(file=file_name, mode="w", encoding="utf-8") as file:
            file.write(page_content)

except Exception as err:
    print(f'ALARM!!!! {err}')
