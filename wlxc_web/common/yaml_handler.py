import yaml

def read_yaml(file):
    """读取文件"""
    with open(file,encoding="utf8") as f:
        conf = yaml.load(f,Loader=yaml.SafeLoader)
    return conf

def write_yaml(file,data):
    """编写文件"""
    with open(file,'w',encoding='utf8') as f:
        yaml.dump(data,f)