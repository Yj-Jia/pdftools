"""移除临时文件"""
import os


def pdf_remove():
    rm_temp = []
    for f in os.listdir('.'):
        if f.endswith('.pdftemp'):
            rm_temp.append(f)

    for fnm in rm_temp:
        os.remove(fnm)
