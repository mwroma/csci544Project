pip3 install jieba
pip3 install hanziconv

word bag 在 bags 文件夹，song id 为文件名，用pickle 封装一个dictionary
{
    “word_bag”: list,
    "label1": list
}
example;
{
    “word_bag”: [3, 0, 0, 0, 1, ...],
    "label1": [1, 0, 0, 0]
}
