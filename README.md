# CharRNN
----------
文本自动生成项目Char-RNN

# 语言
----------
[![](https://img.shields.io/badge/Python-3.5-blue.svg)](https://www.python.org/)<br>

# 项目简介
---------
最近刚刚学习完RNN和LSTM、GRU，对LSTM结构不是很理解，所以上网查看资料，刚好看到一位大神写的一篇[博客](https://zhuanlan.zhihu.com/p/28196873 "悬停显示"),
顿时觉得茅塞顿开，看到最后，建议立刻上手一个简单的项目加深自己的理解。马不停蹄，我也立刻尝试了他推荐的文本生成项目，
所以此项目也主要是参照该位大神的[项目](https://github.com/hzy46/Char-RNN-TensorFlow)，
在其中加入了部分的个人理解和修改，在此表示感谢！

__*项目实现：*__ 五字唐诗和周杰伦歌词的生成，有相关训练集的还可以进行小说的生成。

# 项目结构
----------
主要分为[model](./model.py)，[train](./train.py)和[sample](./sample.py)模块。<br>
model部分主要包含了模型的主要结构，train部分主要是导入模型结构，训练模型以及保存模型，sample部分就是直接导入最后的模型，然后根据用户输入的初始文本，
开始作诗或者写歌。

# 示例
----------
![](/pics/sample1.png)<br>
![](/pics/sample2.png)
