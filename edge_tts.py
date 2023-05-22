import os

def edge_tts(file_path, voice='zh-CN-YunxiNeural', mp3_path=r'D:\new_file.mp3'):
    '''
    模块实现简单的文字转语音功能
    (tts命令参数补充
    [--rate=+-4% 语速加快/减慢]
    [--volume=+-4% 音量加减]
    [--list-voices 列出支持的声音]
    )
    :param file_path: 指定文本文件位置
    :param voice:指定音色
    :param mp3_path:指定生成的mp3文件位置
    :return:无
    '''
    cmd = f'edge-tts --voice {voice} -f "{file_path}" --write-media "{mp3_path}"'
    print(cmd)
    os.system(cmd)

# 音色help
'''
Name: zh-CN-XiaoxiaoNeural
Gender: Female

Name: zh-CN-XiaoyiNeural
Gender: Female

Name: zh-CN-YunjianNeural
Gender: Male

Name: zh-CN-YunxiNeural
Gender: Male

Name: zh-CN-YunxiaNeural
Gender: Male

Name: zh-CN-YunyangNeural
Gender: Male

Name: zh-CN-liaoning-XiaobeiNeural
Gender: Female

Name: zh-CN-shaanxi-XiaoniNeural
Gender: Female

Name: zh-HK-HiuGaaiNeural
Gender: Female

Name: zh-HK-HiuMaanNeural
Gender: Female

Name: zh-HK-WanLungNeural
Gender: Male

Name: zh-TW-HsiaoChenNeural
Gender: Female

Name: zh-TW-HsiaoYuNeural
Gender: Female

Name: zh-TW-YunJheNeural
Gender: Male
    '''
