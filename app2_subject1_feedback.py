import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    model=pickle.load(open('model.pkl','rb'))
    st.title('Subject1 Feedback Analysis System')
    feed=st.file_uploader('Upload Class Feed',type=['.xlsx','.csv'])

    if feed is not None:
        file_details={}
        file_details['filename']=feed
        file_details['file type']=feed.type
        file_details['file size']=feed.size
        st.write(file_details)

        df = pd.DataFrame(pd.read_excel(feed))
        df.to_csv('uploads/subject1.csv')
    
    if st.button('Predict'):
        
        df=pd.read_csv('uploads/subject1.csv')
        data=df.iloc[:,-1].values
        positive_feedback=[]
        negative_feedback=[]
        neutral_feedback=[]
        for i in data:
            if(model.predict([i])[0]==-1):
                negative_feedback.append(i)
            elif(model.predict([i])[0]==1):
                positive_feedback.append(i)
            elif(model.predict([i])[0]==0):
                neutral_feedback.append(i)
        
        labels = 'Positive', 'Negative', 'Neutral'
        sizes = [len(positive_feedback), len(negative_feedback), len(neutral_feedback)]
        explode = (0.1, 0, 0)  
        fig1,ax1=plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)



