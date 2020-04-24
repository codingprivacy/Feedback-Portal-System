__author__ = 'Harsh Patel'
import pickle
from sklearn.feature_extraction.text import CountVectorizer
def sentiment_return(list):
    file=open("/var/www/FPSU/FPSU/backend_final/sentiment_analysis/reviews_train_clean","rb")
    reviews_train_clean=pickle.load(file)
    file.close()
    #print('start')
    cv = CountVectorizer(binary=True)
    cv.fit(reviews_train_clean)
    #print('fit')

    main_list=[]
    for i in list:
        #print(i)
        list=cv.transform(i)
        filename="/var/www/FPSU/FPSU/backend_final/sentiment_analysis/finalized_model.sav"
        final_model = pickle.load(open(filename, 'rb'))

        a=[str(i).replace('0','-1') for i in final_model.predict(list)]
        main_list.append(a)
    return main_list

