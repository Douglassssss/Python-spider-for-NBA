# 代码用于批量修改文本文件的编码格式，这里是将默认的以utf-8编码的文件用ANSI编码
from os import listdir

fns = (fn for fn in listdir() if fn.endswith('.txt'))
for fn in fns:
    with open(fn, 'rb+') as fp:
        content = fp.read()
        content = content.decode('utf-8').encode('ANSI')
        fp.seek(0)
        fp.write(content)
