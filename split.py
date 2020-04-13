"""拆分PDF为单页文件"""
import PyPDF2


def pdf_split(path, first_page, last_page):
    pdf_ini = PyPDF2.PdfFileReader(path)
    page = int(first_page) - 1
    pages = []
    while page <= (int(last_page) - 1):
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf_ini.getPage(page))
        temp_file = str(page + 1) + '.pdftemp'
        with open(temp_file, 'wb') as f_obj:
            pdf_writer.write(f_obj)
        pages.append(page)
        page += 1

    print(pages)
