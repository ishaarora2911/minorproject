import spacy
nlp = spacy.load("en_core_web_sm")
list_of_strings=['Roorkee23February2023IndianInstituteofTechnologyIITRoorkeeanInstituteofNationalImportancehasannouncedtoopenapplicationportalforSPARKprogramaninstitutefundedSummerInternshipsprogrammesforuniversitystudentssoon', 'SomeofthesalientfeaturesofSPARKprogramincludes', 'StipendofRs2500week', 'Onlinehasslefreeapplicationprocess', 'Studentsworkonfocussedprojectsadvertisedatthetimeofapplication', 'Regularprogressreviewsandpostersessionswithawardsforbestposters', 'Startingfrom2018IITRoorkeeoffersinstitutefundedwithastipendofRs2500weekandprojectfundedsummerinternshipsundertheSPARKprogramTheobjectiveofthisprogrammeistoattractandnurturetalentedundergraduatestudentsacrossthecountryLastyearwith15000applications120offersweremade', 'EligibilityConditionsStudentswhoarecurrentlyenrolledandhavecompletedatleasttwosemestersoftheundergraduatedegreeBArchBEBTechMScinarelevantdisciplinefromanyinstituteinIndia', 'FollowingminimumCGPAcriterionwillapply', 'CGPA75forIITsIISc', 'CGPA80forNITsIISERsNISERIIESTUMDAECBS', 'CGPA85forstudentsofotherinstitutes', 'ForfurtherdetailsabouteligibilityconditionshowtoapplyandotherdetailsthecandidatesshouldrefertheSPARKPageofIITRoorkee', 'httpssparkiitracin']


for string in list_of_strings:
    doc = nlp(string)
    for entity in doc.ents:
        if entity.label_ == "ORG":
            print(entity.text)
            """[[
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
                 'httpsiithacinresearchSURE', '\nFacebookLinkedInWhatsAppTwitterTelegramMessengerSMS\n\n'], [
                 'Madras 20 February 2023 Indian Institute of Technology IIT Madras an Institute of National Importance has announced Summer Fellowship Programme 2023 The two months with stipend is designed to enhance awareness and interest in high quality academic research among young Engineering Management Sciences and Humanities students through a goal oriented summer miniproject undertaken at the Indian Institute of Technology Madras',
                 'Eligibility Candidates pursuing 3rd year of BEBTechBSc Engg or 3rd or 4th year of Integrated MEMTech programme 1st year of MEMTechMScMA MBA with outstanding academic background in terms of high ranks in university examinations are encouraged to apply highlighting their academic performance and achievement including papers presented at seminars projects executed design contests participated scorerank in Mathematics Olympiad and any other awardsdistinctions obtained IIT students are not eligible to apply',
                 'Period of the Project Duration of the programme may commence from 22 May 2023 to 21 July 2023 Schedule may be flexible to suit students convenience',
                 'Participating Departments', 'Engineering Departments', 'Aerospace Engineering', 'Applied Mechanics',
                 'Bio Technology', 'Chemical Engineering', 'Civil Engineering', 'Computer Science  Engineering',
                 'Engineeing Design', 'Electrical Engineering', 'Mechanical Engineering',
                 'Metallurgical  Materials Engineering', 'Ocean Engineering', 'Science Departments', 'Physics',
                 'Chemistry', 'Mathematics', 'Humanities  Social Sciences', 'Management Studies',
                 'Stipend A sum of Rs6000 per month will be given as a stipend for a maximum period of 2 months',
                 'Key Dates', 'Site will be activated on  18 February 2023',
                 'The Last date for Online Submission  31 March 2023 at 500 pm',
                 'For exact eligibility criteria how to apply and other details candidates should refer \xa0Summer Fellowship Programme of IIT Madras',
                 'httpssfpiitmacin'], [
                 'Gandhinagar 17 February 2023 Indian Institute of Technology IIT Gandhinagar an Institute of National Importance has announced Summer Research Internship Programme SRIP 2023 for university students',
                 'Students pursuing a bachelors or masters degree at an institution in India can apply for 8 weeks within summer break of IIT Gandhinagar Students in first second and third year of UG studies are encouraged to apply Students in their first year of PG studies can also apply',
                 '\xa0In the present scenario SRIP 2023 will be conducted in the offline mode',
                 'Weekly stipend of Rs 2000 will be paid after completion of the internship The stipend for faculty funded projects however may vary',
                 'Hostel accommodation will be provided to the summer interns and students are required to pay the applicable hostel charges',
                 'The last date for receiving applications is 05 March \xa02023',
                 'The students are expected to work on the project inperson and interact with the faculty mentor on a regular basis while staying on campus This mode is open to all the students Internal and External The interns will be entitled to receive a stipend and a certificate on successful completion of the internship',
                 'For exact eligibility criteria how to apply and other details candidates should refer \xa0SRIP 2023 notification uploaded on the official website of IIT Gandhinagar',
                 'httpssripiitgnacininfosrip2023', '\nFacebookLinkedInWhatsAppTwitterTelegramMessengerSMS\n\n'], [
                 'Gandhinagar 18 February 2023 Indian Institute of Technology IIT Delhi an Institute of National Importance has announced Summer Faculty Research Fellow Programme SFRFP 2023',
                 'IIT Delhi invites faculty fellows from various Engineering and Science Institutes and Colleges other than IIT Delhi to come and spend the summer MayJuly for pursuing research under the guidance of a faculty mentor of IIT Delhi The faculty fellow will get an opportunity to interact and work with the IITD faculty mentor and hisher research students and get exposure to the worldclass research matched by worldclass facilities',
                 'The SFRF programme works as a catalyst for those who are considering higher studies MastersPhD at IIT Delhi in the near future',
                 'The SFRF programme duration ranges from 06 to 08 weeks during May July of 2023', 'Support',
                 'The selected applicants faculty fellows may avail of paid campus accommodation in hostels with basic facilities subject to availability during the period May 16 2023 Tuesday to July 14 2023 Friday only chargeable  Rs 750 per day including meal  bedding charges  Rs 50 per day ie Total approx Rs 800 per day Allotment will be on sharing basis',
                 'The faculty fellow should be a regular faculty member Preference will be given to those who are considering higher studies MastersPhD in the near future',
                 'Key Dates', 'Last Date of Application  28 February 2023', 'Results', '14th April 2023 Tentative',
                 'Eligibility Conditions \xa0The faculty fellow should be a regular faculty member Preference will be given to those who are considering higher studies MastersPhD in the near future',
                 'For exact eligibility criteria how to apply and other details candidates should refer \xa0Summer Faculty Research Fellow Programme SFRFP 2023 of IIT Delhi',
                 'httpshomeiitdacinshowphpid258in_sectionsNews',
                 '\nFacebookLinkedInWhatsAppTwitterTelegramMessengerSMS\n\n']]"""
