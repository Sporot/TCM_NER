import TCM_corpus.GlobalParament as GlobalParament
import TCM_corpus.utils as utils
from gensim.models import word2vec

#训练模型word2vec
def train_char(sentences, model_save_path):
    print("开始训练")
    model=word2vec.Word2Vec(sentences=sentences,size=GlobalParament.train_size,window=GlobalParament.train_window,sg=1,min_count=10)
    model.save(model_save_path)
    print("保存模型结束")


def train_bichar(sentences,model_save_path):
    print("开始训练")
    model=word2vec.Word2Vec(sentences=sentences,size=GlobalParament.train_size,window=GlobalParament.train_window,sg=1,min_count=10)
    model.save(model_save_path)
    print("保存模型结束")


if __name__ == '__main__':

    "*************************for bichar train*************************************************"
    # word='中风'
    # word1='大便'
    # word2='小便'
    # for i in range(0,1):
    #     #sentences=utils.process_text(GlobalParament.text_alldata,GlobalParament.text_afterprocess_alldata,GlobalParament.stop_words_dir)
    #     sentences=utils.load_traintext('data_all_after_bichar.txt')
    #     print(len(sentences))
    #     train_bichar(sentences,GlobalParament.model_bichar+str(GlobalParament.train_size)+'-'+str(GlobalParament.train_window)+'-'+str(i)+'.model')
    #     sim_list = []
    #     model=word2vec.Word2Vec.load(GlobalParament.model_bichar+str(GlobalParament.train_size)+'-'+str(GlobalParament.train_window)+'-'+str(i)+'.model')
    #     model.wv.save_word2vec_format(GlobalParament.model_bichar_vec+str(GlobalParament.train_size)+'.txt')
    #     vocab=list(model.wv.vocab.keys())
    #
    #     with open('test.txt', 'a', encoding=GlobalParament.encoding) as f_writer:
    #         f_writer.write("句子长度： " + str(len(sentences)) + '\n')
    #         f_writer.write("词表大小：" + str(len(vocab)) + '\n')
    #         f_writer.write('window: ' + str(GlobalParament.train_window) + '  size:' + str(GlobalParament.train_size )+ '\n')
    #         f_writer.write('与'+word+'相似的词是：'+'\n')
    #         for e in model.most_similar(positive=word, topn=10):
    #             f_writer.write(e[0]+'  '+str(e[1])+'\n')
    #
    #         sim_value = model.similarity(word1, word2)
    #         f_writer.write('比较词语：'+word+'\n')
    #         f_writer.write(str(sim_value))
    #         f_writer.write('\n***************'+str(i)+'*******bichar************\n')
    #         f_writer.flush()
    #     f_writer.close()


    # "************************************for char train****************************************************************"
    word = '头'
    word1 = '牙'
    word2 = '吐'
    for i in range(0, 1):
        # sentences=utils.process_text(GlobalParament.text_alldata,GlobalParament.text_afterprocess_alldata,GlobalParament.stop_words_dir)
        sentences = utils.load_traintext('data_all_after_char.txt')
        train_char(sentences, GlobalParament.model_char + str(GlobalParament.train_size) + '-' + str(
            GlobalParament.train_window) + '-' + str(i) + '.model')
        sim_list = []
        model = word2vec.Word2Vec.load(GlobalParament.model_char + str(GlobalParament.train_size) + '-' + str(
            GlobalParament.train_window) + '-' + str(i) + '.model')
        model.wv.save_word2vec_format(GlobalParament.model_char_vec + str(GlobalParament.train_size) + '.txt')
        vocab = list(model.wv.vocab.keys())

        with open('test.txt', 'a', encoding=GlobalParament.encoding) as f_writer:
            f_writer.write("句子长度： " + str(len(sentences)) + '\n')
            f_writer.write("词表大小：" + str(len(vocab)) + '\n')
            f_writer.write(
                'window: ' + str(GlobalParament.train_window) + '  size:' + str(GlobalParament.train_size) + '\n')
            for e in model.most_similar(positive=word, topn=10):
                f_writer.write(e[0] + '  ' + str(e[1]) + '\n')

            sim_value = model.similarity(word1, word2)
            f_writer.write('比较词语：' + word + '\n')
            f_writer.write(str(sim_value))
            f_writer.write('\n***************' + str(i) +'char'+ '*******************\n')
            f_writer.flush()
        f_writer.close()





 #************************** for word train ***************************************
    # word = '中风'
    # word1 = '大便'
    # word2 = '小便'
    # for i in range(0, 1):
    #     # sentences=utils.process_text(GlobalParament.text_alldata,GlobalParament.text_afterprocess_alldata,GlobalParament.stop_words_dir)
    #     sentences = utils.load_traintext('data_all_after_word.txt')
    #     print(len(sentences))
    #     train_bichar(sentences, GlobalParament.model_word + str(GlobalParament.train_size) + '-' + str(
    #         GlobalParament.train_window) + '-' + str(i) + '.model')
    #     sim_list = []
    #     model = word2vec.Word2Vec.load(GlobalParament.model_word + str(GlobalParament.train_size) + '-' + str(
    #         GlobalParament.train_window) + '-' + str(i) + '.model')
    #     model.wv.save_word2vec_format(GlobalParament.model_word_vec + str(GlobalParament.train_size) + '.txt')
    #     vocab = list(model.wv.vocab.keys())
    #
    #     with open('test.txt', 'a', encoding=GlobalParament.encoding) as f_writer:
    #         f_writer.write("句子长度： " + str(len(sentences)) + '\n')
    #         f_writer.write("词表大小：" + str(len(vocab)) + '\n')
    #         f_writer.write(
    #             'window: ' + str(GlobalParament.train_window) + '  size:' + str(GlobalParament.train_size) + '\n')
    #         f_writer.write('与' + word + '相似的词是：' + '\n')
    #         for e in model.most_similar(positive=word, topn=10):
    #             f_writer.write(e[0] + '  ' + str(e[1]) + '\n')
    #
    #         sim_value = model.similarity(word1, word2)
    #         f_writer.write('比较词语：' + word + '\n')
    #         f_writer.write(str(sim_value))
    #         f_writer.write('\n***************' + str(i) + '*******bichar************\n')
    #         f_writer.flush()
    #     f_writer.close()