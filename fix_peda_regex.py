import os
import re

# 定义要处理的文件路径
file_paths = [
    '/root/peda/peda.py'
]

def process_file(file_path):
    """处理单个文件的正则表达式修复"""
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 替换 re.compile("pattern") 为 re.compile(r"pattern")
        pattern = re.compile(r're\.compile\("(.*?)"\)')
        content = pattern.sub(r're.compile(r"\1")', content)
        
        # 2. 仅对 peda.py 执行的特殊处理
        if file_path.endswith('peda.py'):
            # 匹配 re.match、re.search、re.findall 等函数调用中的正则表达式字符串
            pattern = re.compile(r'(re\.(match|search|findall|compile)\()(".*?")')
            def repl(m):
                if m.group(3).startswith('b'):
                    return f"{m.group(1)}b{r'{m.group(3)[2:-1]}'}"
                return f"{m.group(1)}r{m.group(3)}"
            
            content = pattern.sub(repl, content)
            
            # 修复特定行的问题
            content = content.replace('replace("\\ ",".*").replace("\\?",".*")', 
                                     'replace(r" ", ".*").replace(r"?", ".*")')
            content = content.replace('replace(b\' \', b\'\\ \')', 
                                     'replace(b\' \', b\' \')')
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"已成功处理文件: {file_path}")
        return True
    
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {str(e)}")
        return False

def main():
    """主函数，处理所有文件"""
    success_count = 0
    for file_path in file_paths:
        if process_file(file_path):
            success_count += 1
    
    print(f"处理完成，成功修复 {success_count}/{len(file_paths)} 个文件")

if __name__ == "__main__":
    main()