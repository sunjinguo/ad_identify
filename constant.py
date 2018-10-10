#coding=utf-8
import re
import os


# word2vec model 路径
MODEL_PATH='/data0/nfs_data/nlp/word2vec/word2vec_128.bin'

# word2vec 词向量维度
EMBEDDING_SIZE=128

# 相似度阈值
SIMILAR_THRESHOLD=0.96

# 广告段落最短长度
AD_MINI_LENGTH=6

# 需要过滤的作者文件路径
AUTHOR_FILTER_FILE='/data0/home/jinguo3/projects/simba/trunk/src/content_analysis/scripts/user/jinguo3/code/ad_clusters/config/author_filter.txt'

# 广告聚类中心路径
AD_CLUSTER_CENTER_FILE='/data0/nfs_data/nlp/ad_clusters/ad_result/AD_clusCenter_result.json'

# 过滤URL正则
RE_HTTP=re.compile(ur'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# 过滤符号
RE_SIGN=re.compile(ur'[@#*&$,.:：，。’“”\'"\[\]【】（）()《》<>\\?？/ 、;；~\-|]+')

# 过滤数字
RE_NUMBER=re.compile(u'[a-zA-Z0-9一二三四五六七八九十]')

# 文本分段模式
RE_PATTERN=re.compile(u'\n')


