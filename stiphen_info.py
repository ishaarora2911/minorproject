import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
import re


articles=[ [
    'Roorkee 23 February 2023 Indian Institute of Technology IIT Roorkee an Institute of National Importance has announced to open application portal for SPARK program an institutefunded Summer Internships programmes for university students soon',
    'Some of the salient features of SPARK program includes', 'Stipend of Rs 2500week',
    'Online hasslefree application process',
    'Students work on focussed projects advertised at the time of application',
    'Regular progress reviews and poster sessions with awards for best posters',
    'Starting from 2018 IIT Roorkee offers institutefunded with a stipend of Rs 2500week and projectfunded summer internships under the SPARK program The objective of this programme is to attract and nurture talented undergraduate students across the country Last year with 15000 applications 120 offers were made',
    'Eligibility Conditions\xa0 Students who are currently enrolled and have completed at least two semesters of the undergraduate degree BArchBEBTechMSc in a relevant discipline from any institute in India',
    'Following minimum CGPA criterion will apply', 'CGPA  75 for IITsIISc',
    'CGPA  80 for NITs IISERs NISERIIESTUMDAECBS', 'CGPA  85 for students of other institutes',
    'For further details about eligibility conditions how to apply and other details the candidates should refer the \xa0SPARK Page of IIT Roorkee',
    'httpssparkiitracin'], [
                 'Hyderabad 04 March 2022 Indian Institute of Technology IIT Hyderabad has announced Summer Undergraduate Research Exposure SURE a Two Months Paid Internship Programs for students of other universities',
                 'Eligibility ', '2nd3rd Year BTech BDes 1st year\xa0 MScMA', 'The total number of internships are 150',
                 'One can apply for 18 departments of IIT Hyderabad',
                 'Fellowships \xa0The institute offers fellowships of Rs 15000 for two months ',
                 'Hostel accommodation is available on a sharing basis', 'Key Dates \xa0',
                 'Application opens from 03 February 2023',
                 'The closing date for submission of application is 15 May 14 July 2023 2023',
                 '\xa0For exact details about eligibility conditions how to apply and other details the candidates should refer the Admission Notification uploaded on the official website of\xa0 IIT Hyderabad',
                 'httpsiithacinresearchSURE', '\nFacebookLinkedInWhatsAppTwitterTelegramMessengerSMS\n\n']]
#Tokenization
li4=[]
li5=[]
for article in articles:
    for i in article:
        words=nltk.word_tokenize(i.lower())
        unique_words=set(words)
        clean_article=' '.join(unique_words)
     #   print(clean_article)
        li4.append(clean_article)
    li5.append(li4)
    li4=[]
print(li5)
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_stiphend(li5):
    stiphend_list = []
    for article in li5:
        doc = nlp(article)
        for ent in doc.ents:
            if ent.label_ == "MONEY":
                stiphend_list.append(ent.text)

    return stiphend_list

# for article in articles:
#     for i in article:
#         words=i.split()
#         unique_words=[]
#         for word in words:
#             if word not in unique_words:
#                 unique_words.append(word)
#         clean_article = " ".join(unique_words)
#         li4.append(clean_article)
#     li5.append(li4)
#     li4=[]
# print(li5)
# def remove_duplicates(li5):
#     for lst in li5:
#         seen = set()
#         new_lst = []
#         for word in lst:
#             if word not in seen:
#                 seen.add(word)
#                 new_lst.append(word)
#         lst[:] = new_lst
#         print(lst)






# regular expression pattern to match monetary values
#pattern = r"\$[\d,]+(?:\.\d+) Rs?"
pattern = r'\brs[.\d\s]+'

# iterate through each article and search for the pattern
for article in li5:
    for sentence in article:
        matches = re.findall(pattern, sentence)
        for match in matches:
            print(match)
#remove_duplicates(li5)
extract_stiphend(li5)