import os
import re
from fpdf import FPDF

# 步驟1: 撈取Java程式碼中的所有文件
def get_java_files(path):
    java_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
    return java_files

# 步驟2: 分析文件以找出特定的程式碼片段
def extract_code_snippets(java_files):
    code_snippets = []
    snippet_pattern = re.compile(r'/\* START \*/(.*?)/\* END \*/', re.DOTALL)
    for file_path in java_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = snippet_pattern.findall(content)
            code_snippets.extend(matches)
    return code_snippets

# 步驟3: 將找到的程式碼片段寫入一個文本文件
def write_to_text_file(code_snippets, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for snippet in code_snippets:
            file.write(snippet + '\n\n')

# 步驟4: 將文本文件轉換成PDF檔
def convert_to_pdf(text_file_path, pdf_file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    with open(text_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            pdf.cell(0, 10, line.strip(), ln=True)
    pdf.output(pdf_file_path)

if __name__ == '__main__':
    java_files = get_java_files('E:\code\mgov')
    code_snippets = extract_code_snippets(java_files)
    text_file_path = 'code_snippets.txt'
    write_to_text_file(code_snippets, text_file_path)
    pdf_file_path = 'code_snippets.pdf'
    convert_to_pdf(text_file_path, pdf_file_path)
    print(f'程式碼片段已經保存在 {pdf_file_path}')
