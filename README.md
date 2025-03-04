# fix_peda_regex
```bash
# python3 -V               
Python 3.13.2
# uname -a
Linux kali 6.6.9-amd64 #1 SMP PREEMPT_DYNAMIC Kali 6.6.9-1kali1 (2024-01-08) x86_64 GNU/Linux
```
最近在一台新的虚拟机里装 peda 的时候遇到了许多类似下面这样的报错
```
/root/peda/peda.py:1226: SyntaxWarning: invalid escape sequence '\s'
p = re.compile(".*?:\s.*\s(0x[^ ]*|\w+)")
```
解决方案
1. 手动修改文件
编辑出现警告的 Python 文件（如 `/root/peda/peda.py`  ），将正则表达式字符串修改为原始字符串，即在字符串前面加上`r`  。
例如，将：
`p = re.compile(".*?:\s.*\s(0x[^ ]*|\w+)")`  
修改为：
`p = re.compile(r".*?:\s.*\s(0x[^ ]*|\w+)")`  

由于量太多于是用 doubao 和 claude 写了个脚本，Take if needed。
