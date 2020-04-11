"""截取PDF"""
from split import pdf_splitter
from merge import pdf_merge
from remove import pdf_remove



def pdf_tools():
    print('示例：测试.pdf')
    pdf_ini = input('请按示例格式输入待处理PDF文件名:')
    start_page = input('截取起始页（包含该页）：')
    stop_page = input('截取终止页（包含该页）：')
    new_file = input('请按示例格式输入新PDF文件名：')
    pdf_splitter(pdf_ini, start_page, stop_page)
    pdf_merge(new_file)
    pdf_remove()


if __name__ == '__main__':
    pdf_tools()


