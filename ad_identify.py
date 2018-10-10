#coding=utf-8
from __future__ import division
import json
import math
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from util import util
from constant import *
import numpy as np
from collections import defaultdict
from bs4 import BeautifulSoup as BS


class AdIdentify(object):
    '''
         基于聚类中心的广告识别
    '''

    def __init__(self):
        '''
            初始化各参数
        '''
        # word2vec模型
        self.word2vec_model=util.load_model(MODEL_PATH)
        
        # 以作者为单位的广告聚类中心列表
        self.cluster_centers=self.load_cluster_centers(AD_CLUSTER_CENTER_FILE)
        # 需过滤的作者列表
        self.authors_filter=self.load_filter_authors(AUTHOR_FILTER_FILE)

    def load_cluster_centers(self,path):
        '''
            加载广告聚类中心
        '''
        author_cluscenters=defaultdict(list)
        with open(path,'r')as f:
            for line in f:
                msg=json.loads(line.strip())
                author_cluscenters[msg.get('author','')]=msg.get('vec_center',[])
        return author_cluscenters

    def load_filter_authors(self,path):
        '''
            加载需过滤的作者
        '''
        authors_filter_dic=defaultdict(int)
        with open(path,'r')as f:
            for line in f:
                author=line.strip()
                if not isinstance(author,unicode):author=author.decode('utf-8')
                authors_filter_dic[author]=1
        return authors_filter_dic
    
    def get_text_len(self,text):
        '''
            获取文本有效长度
        '''
        if not text:
            return 0
        if not isinstance(text,unicode):text=text.decode('utf-8')
        content=re.sub(RE_HTTP,'',text)
        content=re.sub(RE_NUMBER,'',content)
        content=re.sub(RE_SIGN,'',content)
        return len(content)


    def get_sens(self,text):
        '''
        将文本切分为段落
        '''
        text=text.strip()
        if not isinstance(text,unicode):text=text.decode('utf-8')
        sentences=[]
        if text.startswith('<'):
            try:
                soup=BS(text)
            except:
                return []
            p_list=soup.find_all('p')
            for p in p_list:
                sen=p.get_text()
                if not sen.strip():continue
                sentences.append(sen.replace(' ','').lower())
        else:
            sens=RE_PATTERN.split(text)
            for sen in sens:
                if not sen.strip():continue
                sentences.append(sen.replace(' ','').lower())
        return sentences

    def get_text_vector(self,text):
        '''
            文本段落 word2vec 词向量平均
        '''
        word_num=0
        vec=np.zeros(EMBEDDING_SIZE)
        for word in util.get_tokens(text):
            word_num+=1
            if word in self.word2vec_model:
                vec+=self.word2vec_model[word]
            else:
                continue
        try:
            vec=vec/word_num
        except ZeroDivisionError as err:
            pass
        return vec

    def get_similar_score(self,vec1,vec2):
        '''
            计算两向量相似度得分
        '''
        if isinstance(vec1,list):
            vec1=np.array(vec1)
        if isinstance(vec2,list):
            vec2=np.array(vec2)
        if not any(vec2):
            return 0
        return vec1.dot(vec2)/(math.sqrt((vec1**2).sum())*math.sqrt((vec2**2).sum()))
    
    def get_adlist(self,msg):
        '''
            获取广告列表
        '''
        ad_list=[]
        author=msg.get('author')
        if not author:return []
        if author in self.authors_filter:return []
        if author not in self.cluster_centers:return []
        content=msg.get('content')
        if not content:return []
        sens=self.get_sens(content)
        url=msg.get('url')
        for sen in sens:
            if self.get_text_len(sen)<AD_MINI_LENGTH:continue
            vec=self.get_text_vector(sen)
            score_list=[self.get_similar_score(vec,vec_center)for vec_center in self.cluster_centers.get(author)]
            if max(score_list)<SIMILAR_THRESHOLD:continue
            ad_list.append({'author':author,'max_score':max(score_list),'ad_sen':sen,'url':url})
        return ad_list
                
