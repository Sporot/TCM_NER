from simi import utils as utils
from gensim.models.word2vec import Word2Vec
import numpy as np
import random
def calc_sim(dictionary_afterprocess, sentences, word_sp_dir,out_result_path):
    model=Word2Vec.load('TCM_corpus/model/w2v_TCM20-5-0.model')
    vocab=set(model.wv.vocab.keys())
    word_sp= utils.get_sp_char(word_sp_dir)
    sim_value1 = model.similarity('腹痛','黄连')
    sim_value2 = model.similarity('腹胀','腹痛')
    sim_value3 = model.similarity('腹胀','头痛')
    simi_list = []
    count=0
    print(sentences)
    sentences = utils.jiayan_cut_nostop(sentences,load_lm_dir='jiayan_models/jiayan.klm')
    print(sentences)
    word_list =sentences.strip().split()
    #计算相似度
    f_writer = open(out_result_path,'w',encoding='utf-8')

    for sample_word in word_list:
        if len(sample_word)>0:
            #print('样本集当前词语：'+''.join(sample_word))
            if sample_word in vocab:
                print('******在词表中********')
                simi_score=dict()
                sim_max = 0
                count=count+1
                with open (dictionary_afterprocess,'r',encoding='utf-8') as f_dictionary:
                    for dictionary_line in f_dictionary:
                        dictionary_line= utils.delete_r_n(dictionary_line)
                        dictionary_line_list=dictionary_line.split()
                        dictionary_line_list= utils.clear_char_from_vocab(dictionary_line_list, vocab)
                        #print(dictionary_line_list)
                        for dictionary_word in dictionary_line_list:
                            if len(dictionary_word)>0:
                                #print('词典中当前词:'+dictionary_word)
                                sim_value_list=[]
                                sim_value=model.similarity(sample_word, dictionary_word)
                                if sim_value==1:
                                    sim_value=0
                                sim_max=np.maximum(sim_max,sim_value)
                                #print(''.join(sample_word)+' 和 '+''.join(dictionary_word)+'相似度：'+str(sim_value))
                                    # if sim_value >sim_max:
                                    #     sim_max=sim_value
                                    #print('此时sim_max的值：'+str(sim_max))
                    print('************************************')
                    #print(sim_value_list)
                    #sim_max=max(sim_value_list)
                    print('最大相似度：'+str(sim_max))
                    #simi_score[sample_char]=sim_max
                    print(str(count)+'开始写入文档')
                    sim_max_2=round(sim_max,2)
                    if sim_max_2>=0.82:
                        sim_max_2=random.uniform(0.9,0.95)
                    elif 0.51<sim_max_2<0.82:
                        sim_max_2=0
                    else:
                        sim_max_2=0

                    for sample_char in sample_word:
                        #f_writer.write(str(sample_char)+' '+ str(str(sim_max_2)+'\n'))
                        f_writer.write(str(sample_char) + ' ' + str(sim_max_2)+'\n')
                        simi_list.append(sim_max_2)
                        f_writer.flush()

            elif sample_word in word_sp:
                print('******在特征词表中*********')
                for sample_char in sample_word:
                    #f_writer.write(str(sample_char) + ' ' + str(6) + '\n')
                    simi = random.uniform(0.6,0.65)
                    f_writer.write(str(sample_char) + ' ' + str(simi)+'\n')
                    simi_list.append(simi)
                    f_writer.flush()
            else:
                print('******均不在*********')
                for sample_char in sample_word:
                    simi = 0
                    f_writer.write(str(sample_char) + ' ' + str(0)+'\n')
                    simi_list.append(simi)
                    f_writer.flush()
    print (simi_list)
    f_writer.close()
    return simi_list



if __name__  =='__main__':
    calc_sim('../TCM_corpus/dictionary_smptom_afterprocess.txt','病身热足寒，颈项强急，恶寒，时头热面赤，目光脉赤，独头面摇，卒口噤，背反张者，痉病也。', '../TCM_corpus/word_sp.txt','../TCM_corpus/simi/simitest.txt')