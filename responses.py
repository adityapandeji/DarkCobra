from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi"):
        return """
        Hello!
        """
    if user_message in ("pasc","pasc sig","pasc upcoming sig"):
        return """ Offline SIG on Artificial Intelligence and Machine Learning using Python for all FE and SE students 
Session 1:  🗓️ Date: June 15, 2022 (Wednesday)

Session 2:  🗓️ Date: June 16, 2022 (Thursday)

Time: 05:20 pm IST

Venue: Room no. - A1 212

For any queries feel free to contact:
Atharva Kumbhar - 8862036454
Shivani Yadav - 8530173361

     LAST UPDATED ON 13 JUNE 2022
        """

    if user_message in ("who are you","who are you?","what are you","what are you?"):
        return "I am PICTBOT ! Created by Ekajal, Jackfruit, Kobe, Brownmunda, Bunnyyaar"  

    if user_message in ("are you real","are you real?"):
        return "I am as REAL AS YOUR IMAGINARY GIRLFRIEND."  


    if user_message in ("debsoc"):
        return """Please append your names in the Excel sheet if you're interested in making the weekly quizzes for all DEBSOC members.
        The quiz can be on any topic of your choosing.

    EXCEL SHEET : https://docs.google.com/spreadsheets/d/1uC0LdIkMAVjb3PGrWZ2PqkOHNBNhViKIVHdiJOSTH5Q/edit?usp=sharing

    LAST UPDATED ON 13 JUNE 2022
        """

    if user_message in ("pisb"):
        return """ Python  Online Sig 
        Topic : OOPS Lecture no.02
        Date : 13/06/2022
        Time : 10 pm
        
        NOTE : LINK WILL BE SHARED ON WHATSAPP GROUPS AT 9 P.M

        LAST UPDATED ON 13 JUNE 2022 

        """

    if user_message in ("time","time?"):
        now= datetime.now()
        date_time = now.strftime(" %d/%m/%y, %H:%M:%S")

        return str(date_time)
    return "I DON'T UNDERSTAND WHAT YOU SAID"


