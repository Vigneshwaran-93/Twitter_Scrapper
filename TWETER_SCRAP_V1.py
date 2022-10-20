import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter

def TWT_USER_SCRAPE(us_name, no_of_twts):
    twts_list1 = []
    re='from:'+us_name #Username String
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(re).get_items()):
        if i>no_of_twts:
            break
        twts_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) #declare the attributes to be returned
    tweets_df1 = pd.DataFrame(twts_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    return tweets_df1  # return of DF for frontend



def TWT_SCRAPE(keyword, st_date, end_date, no_of_twts):
    twts_list2 = []
    main_st=keyword+" since:"+st_date+" until:"+end_date
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(main_st).get_items()):
        if i>no_of_twts:
            break
        twts_list2.append([tweet.date, tweet.content, tweet.user.username, tweet.user.location, tweet.replyCount    ])

    # Creating a dataframe from the tweets list above
    tweets_df2 = pd.DataFrame(twts_list2, columns=['Datetime',  'Text', 'Username','Locarion','Reply Count'])
    return tweets_df2 #return of DF for frontend


a="Diwali"
b="2022-10-19"
c="2022-10-20"
d=100
abc= TWT_SCRAPE(a,b,c,d)


# Write a page title
st.title('Twitter Scrapper | GUVI')
st.header("What would you like to do today?")

main_in1=st.checkbox("USER TWEET SEARCH", key="mainbt1", help="Select if you would like to scrape any user tweets")
main_in2=st.checkbox("KEYWORD TWEET SEARCH", key=None, help="Select if you would like to scrape BY keyword")

if main_in1==True :
    with st.form(key='my_form'):
        name = st.text_input(label='Enter a valid Username')
        number = st.number_input('Insert the number of tweets required')
        submit_button = st.form_submit_button(label='Submit')
    if name!="":
        abcd = TWT_USER_SCRAPE(name, number)
        st.write(" THE RESULTS ARE ")
        st.write(abcd)
        abcd.to_csv("TWEET_DATA.csv")
        st.download_button(
            label="Download data as CSV",
            data=abcd.to_csv(),
            file_name='TWEET_DATA.csv',
            mime='text/csv',
        )

if main_in2==True:
    with st.form(key='my_form'):
        keyword = st.text_input(label='Enter a Keyword to Search')
        number = st.number_input('Insert the number of tweets required')
        datest=str(st.date_input("FROM DATE"))
        dateend=str(st.date_input("End DATE"))
        submit_button = st.form_submit_button(label='Submit')

    if keyword != "":
        abcde = TWT_SCRAPE(keyword,datest,dateend,number)
        st.write(" THE RESULTS ARE ")
        st.write(abcde)
        abcde.to_csv("TWEET_DATA.csv")
        st.download_button(
            label="Download data as CSV",
            data=abcde.to_csv(),
            file_name='TWEET_DATA.csv',
            mime='text/csv',
        )



if st.button("EXIT"):
  st.warning('EXITING IN PROGRESS')
  st.stop()
  st.success('Thank you !')
  st.experimental_rerun()






