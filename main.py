from document_read_write import doc_read,doc_write
from stemming import stem
from tf_idf_score import scoring
import re
import operator


all_sentence_list = []
stemmed_sentence_list = []



document = doc_read("input1.txt")
all_sentence_list = document.all_sentence



stm = stem()
for s in all_sentence_list:
    word_list = re.split('\s+',s)
    new_snt = ""
    for w in word_list:
        if new_snt == "":
            new_snt = new_snt + stm.stemmed(w)
        else:
            new_snt = new_snt + " " + stm.stemmed(w)

    stemmed_sentence_list.append(new_snt)



snt_scr = scoring(stemmed_sentence_list)
snt_scr.update()
snt_scr_list = snt_scr.sentence_score_list


score = list(zip(all_sentence_list,snt_scr_list))

score.sort(key=operator.itemgetter(1),reverse=True)
score = score[:(int)(len(score)/3)]

score = list(zip(*score))
score = score[0]


#print(score)

doc_write(score,"output.txt")


