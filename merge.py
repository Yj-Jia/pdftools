"""将单页PDF文件合并为新的PDF"""
import PyPDF2
import os


def str2int(slist):
    new_ilist = []
    for i in slist:
        new_ilist.append(int(i))
    return new_ilist


def int2str(ilist):
    new_slist = []
    for j in ilist:
        new_slist.append(str(j))
    return new_slist


def str_sort(list):
    list = str2int(list)
    list.sort()
    list = int2str(list)
    return list


def pdf_merge(new_file):
    pdffiles = []
    for f_nm in os.listdir('.'):
        if f_nm.endswith('.pdftemp'):
            fname = ''
            for char in f_nm:
                if char == '.':
                    break
                else:
                    fname += char
            pdffiles.append(fname)
    pdffiles = str_sort(pdffiles)
    new_pdf = open(new_file, 'wb')
    pdfWriter = PyPDF2.PdfFileWriter()
    objlist = []
    for f in pdffiles:
        f = f + '.pdftemp'
        pdf_obj = open(f, 'rb')
        objlist.append(pdf_obj)
        pdfReader = PyPDF2.PdfFileReader(pdf_obj)
        pdfWriter.addPage(pdfReader.getPage(0))
    pdfWriter.write(new_pdf)
    for obj in objlist:
        obj.close()
    new_pdf.close()
    print('Success !')
