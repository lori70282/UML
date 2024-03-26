import os
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.opc.exceptions import PackageNotFoundError

def modify_word_properties(doc_path, author, company):
    try:
        print(f"Attempting to modify: {doc_path}")
        doc = Document(doc_path)
        core_props = doc.core_properties
        core_props.author = author
        core_props.company = company
        doc.save(doc_path)
        print(f"Modified: {doc_path}")
    except PackageNotFoundError:
        print(f"Not a valid Word file: {doc_path}")
    except Exception as e:
        print(f"Error modifying {doc_path}: {e}")

def traverse_and_modify(directory, author, company):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.docx'):
                doc_path = os.path.join(root, file)
                modify_word_properties(doc_path, author, company)

if __name__ == '__main__':
    directory = r'E:\OneDrive\台灣資服\Systex\21.ISMS帳號管理盤點\帳號清查113.03.25\宜花東-正式環境 - 複製'
    author = 'Lory'
    company = 'TIST'
    traverse_and_modify(directory, author, company)
