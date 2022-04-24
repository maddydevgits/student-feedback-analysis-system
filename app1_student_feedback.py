import pickle
import streamlit as st

def app():
    model=pickle.load(open('model.pkl','rb'))
    st.title('Student Feedback Analysis System')
    feed=st.text_input('Enter Feedback')

    if st.button('Predict') and len(feed)>0:
        res=model.predict([feed])
        if(res[0]==1):
            st.success('Positive Feedback')
        elif(res[0]==0):
            st.warning('Neutral Feedback')
        elif(res[0]==-1):
            st.error('Negative Feedback')
    #st.write(res)