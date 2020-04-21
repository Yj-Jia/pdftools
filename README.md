# pdftools
## 项目简介
从PDF文件中拆分指定范围页面并生成新PDF文件。

##  实现
gui.py实现图形界面，调用pdftools库，其中pdf_split 函数将原PDF指定部分拆为单页PDF，pdf_merge函数按页码顺序将其合为新文件，remove函数移除临时文件。

## 使用

```
python gui.py
```

![image]( https://github.com/yjjia/pdftools/blob/master/IMG/gui.jpg )

## 依赖环境
Python 3.7 ，主要功能使用PyPDF2库。
