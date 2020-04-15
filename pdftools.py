"""截取PDF"""
from split import pdf_split
from merge import pdf_merge
from remove import pdf_remove


def pdf_tools(pdf_ini, first_page, last_page, new_file):
    pdf_split(pdf_ini, first_page, last_page)
    print('split')
    pdf_merge(new_file)
    pdf_remove()


if __name__ == '__main__':
    pdf_tools()


