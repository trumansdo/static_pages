import os
import json

def convert_directory_to_json(root_dir, output_file='directory.json'):
    """
    将两级目录结构转换为有序JSON数据（路径使用正斜杠/）
    参数:
        root_dir: 根目录路径（如'figure'）
        output_file: 输出文件名（可选）
    """
    data = {}
    
    # 获取根目录下的所有子目录（保持原始顺序）
    subdirs = [d for d in os.listdir(root_dir) 
               if os.path.isdir(os.path.join(root_dir, d))]
    
    for subdir in subdirs:
        subdir_path = os.path.join(root_dir, subdir)
        image_files = []
        
        # 获取并排序图片文件（按文件名升序排列）
        files = sorted([
            f for f in os.listdir(subdir_path) 
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
        ])
        
        # 构建带标记的路径数组（强制替换反斜杠为正斜杠）
        for filename in files:
            relative_path = os.path.join(subdir, filename)
            # 替换反斜杠为正斜杠（适配Windows系统）[[3]]
            relative_path = relative_path.replace('\\', '/')
            image_files.append([relative_path, 1])  # 添加固定值1
        
        if image_files:
            data[subdir] = image_files
    
    # 生成有序JSON（Python 3.7+保证字典有序）
    json_output = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False)
    
    # 写入文件
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json_output)
    
    return json_output

# 使用示例
if __name__ == "__main__":
    result = convert_directory_to_json('D:/code_space/other/static_pages/figure')
    print(result)