import pandas as pd
from googletrans import Translator

translator = Translator()
#translator = Translator(service_urls=['translate.googleapis.com'])

data=pd.read_csv('trans.csv')
jp_list=[]
for i in data['english']:
    try:
        dst = translator.translate(i, src='en', dest='ja')
        jp_list.append(dst.text)
    except Exception as e:
        translator = Translator()
        

data['jp']=jp_list
data.to_csv("result.csv",encoding='utf_8_sig' ,index=False)

