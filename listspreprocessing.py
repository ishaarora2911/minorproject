li5=['Roorkee 23 February 2023 Indian Institute of Technology IIT Roorkee an Institute of National Importance has announced to open application portal for SPARK program an institutefunded Summer Internships programmes for university students soonSome of the salient features of SPARK program includesStipend of Rs 2500weekOnline hasslefree application processStudents work on focussed projects advertised at the time of applicationRegular progress reviews and poster sessions with awards for best postersStarting from 2018 IIT Roorkee offers institutefunded with a stipend of Rs 2500week and projectfunded summer internships under the SPARK program The objective of this programme is to attract and nurture talented undergraduate students across the country Last year with 15000 applications 120 offers were madeEligibility Conditions\xa0 Students who are currently enrolled and have completed at least two semesters of the undergraduate degree BArchBEBTechMSc in a relevant discipline from any institute in IndiaFollowing minimum CGPA criterion will applyCGPA  75 for IITsIIScCGPA  80 for NITs IISERs NISERIIESTUMDAECBSCGPA  85 for students of other institutesFor further details about eligibility conditions how to apply and other details the candidates should refer the \xa0SPARK Page of IIT Roorkeehttpssparkiitracin', 'Hyderabad 04 March 2022 Indian Institute of Technology IIT Hyderabad has announced Summer Undergraduate Research Exposure SURE a Two Months Paid Internship Programs for students of other universitiesEligibility 2nd3rd Year BTech BDes 1st year\xa0 MScMAThe total number of internships are 150One can apply for 18 departments of IIT HyderabadFellowships \xa0The institute offers fellowships of Rs 15000 for two months Hostel accommodation is available on a sharing basisKey Dates \xa0Application opens from 03 February 2023The closing date for submission of application is 15 May 14 July 2023 2023\xa0For exact details about eligibility conditions how to apply and other details the candidates should refer the Admission Notification uploaded on the official website of\xa0 IIT HyderabadhttpsiithacinresearchSURE\nFacebookLinkedInWhatsAppTwitterTelegramMessengerSMS\n\n', 'Madras 20 February 2023 Indian Institute of Technology IIT Madras an Institute of National Importance has announced Summer Fellowship Programme 2023 The two months with stipend is designed to enhance awareness and interest in high quality academic research among young Engineering Management Sciences and Humanities students through a goal oriented summer miniproject undertaken at the Indian Institute of Technology MadrasEligibility Candidates pursuing 3rd year of BEBTechBSc Engg or 3rd or 4th year of Integrated MEMTech programme 1st year of MEMTechMScMA MBA with outstanding academic background in terms of high ranks in university examinations are encouraged to apply highlighting their academic performance and achievement including papers presented at seminars projects executed design contests participated scorerank in Mathematics Olympiad and any other awardsdistinctions obtained IIT students are not eligible to applyPeriod of the Project Duration of the programme may commence from 22 May 2023 to 21 July 2023 Schedule may be flexible to suit students convenienceParticipating DepartmentsEngineering DepartmentsAerospace EngineeringApplied MechanicsBio TechnologyChemical EngineeringCivil EngineeringComputer Science  EngineeringEngineeing DesignElectrical EngineeringMechanical EngineeringMetallurgical  Materials EngineeringOcean EngineeringScience DepartmentsPhysicsChemistryMathematicsHumanities  Social SciencesManagement StudiesStipend A sum of Rs6000 per month will be given as a stipend for a maximum period of 2 monthsKey DatesSite will be activated on  18 February 2023The Last date for Online Submission  31 March 2023 at 500 pmFor exact eligibility criteria how to apply and other details candidates should refer \xa0Summer Fellowship Programme of IIT Madrashttpssfpiitmacin', 'Gandhinagar 17 February 2023 Indian Institute of Technology IIT Gandhinagar an Institute of National Importance has announced Summer Research Internship Programme SRIP 2023 for university studentsStudents pursuing a bachelors or masters degree at an institution in India can apply for 8 weeks within summer break of IIT Gandhinagar Students in first second and third year of UG studies are encouraged to apply Students in their first year of PG studies can also apply\xa0In the present scenario SRIP 2023 will be conducted in the offline modeWeekly stipend of Rs 2000 will be paid after completion of the internship The stipend for faculty funded projects however may varyHostel accommodation will be provided to the summer interns and students are required to pay the applicable hostel chargesThe last date for receiving applications is 05 March \xa02023The students are expected to work on the project inperson and interact with the faculty mentor on a regular basis while staying on campus This mode is open to all the students Internal and External The interns will be entitled to receive a stipend and a certificate on successful completion of the internshipFor exact eligibility criteria how to apply and other details candidates should refer \xa0SRIP 2023 notification uploaded on the official website of IIT Gandhinagarhttpssripiitgnacininfosrip2023\nFacebookLinkedInWhatsAppTwitterTelegramMessengerSMS\n\n', 'Gandhinagar 18 February 2023 Indian Institute of Technology IIT Delhi an Institute of National Importance has announced Summer Faculty Research Fellow Programme SFRFP 2023IIT Delhi invites faculty fellows from various Engineering and Science Institutes and Colleges other than IIT Delhi to come and spend the summer MayJuly for pursuing research under the guidance of a faculty mentor of IIT Delhi The faculty fellow will get an opportunity to interact and work with the IITD faculty mentor and hisher research students and get exposure to the worldclass research matched by worldclass facilitiesThe SFRF programme works as a catalyst for those who are considering higher studies MastersPhD at IIT Delhi in the near futureThe SFRF programme duration ranges from 06 to 08 weeks during May July of 2023SupportThe selected applicants faculty fellows may avail of paid campus accommodation in hostels with basic facilities subject to availability during the period May 16 2023 Tuesday to July 14 2023 Friday only chargeable  Rs 750 per day including meal  bedding charges  Rs 50 per day ie Total approx Rs 800 per day Allotment will be on sharing basisThe faculty fellow should be a regular faculty member Preference will be given to those who are considering higher studies MastersPhD in the near futureKey DatesLast Date of Application  28 February 2023Results14th April 2023 TentativeEligibility Conditions \xa0The faculty fellow should be a regular faculty member Preference will be given to those who are considering higher studies MastersPhD in the near futureFor exact eligibility criteria how to apply and other details candidates should refer \xa0Summer Faculty Research Fellow Programme SFRFP 2023 of IIT Delhihttpshomeiitdacinshowphpid258in_sectionsNews\nFacebookLinkedInWhatsAppTwitterTelegramMessengerSMS\n\n']
li6=[]
import re
for string in li5:
    words = string.split()

    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    result = " ".join(unique_words)
 #   print(result)
    li6.append(result)
print(li6)

#pattern = r'\brs[.\d\s]+'
#pattern = r'\brs[.\d\s]+'

# iterate through each article and search for the pattern
# for sentence in li6:
#     matches = re.findall(pattern, sentence)
#     for match in matches:
#         print(match)

import nltk
# from nltk.stem import PorterStemmer
#
# # initialize the Porter stemmer
# stemmer = PorterStemmer()
#
# # define an example string to stem
#
# # split the string into words
# for i in li5:
#     words = i.split()
#
# # stem each word in the list
#     stemmed_words = []
#     for word in words:
#         stemmed_word = stemmer.stem(word)
#         stemmed_words.append(stemmed_word)
#
# # join the stemmed words back into a string
#     stemmed_string = " ".join(stemmed_words)
#     print(stemmed_string)  # "the quick brown fox jump over the lazi dog"

import re

# Define an example stipend string
for i in li6:


# Use regex to find all Rs values within the string
    rs_values = re.findall(r'Rs\s*([\d,]+(\.\d{1,2})?)', i)

# Convert the Rs values to float values
    stipend_values = [float(rs_value[0].replace(',', '')) for rs_value in rs_values]

# Get the maximum stipend value from the list
    max_stipend = max(stipend_values)

    print(max_stipend)  # Output: 25000.0
