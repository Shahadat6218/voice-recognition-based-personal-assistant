import speech_recognition as sr  # speech recognition api
import datetime                  #date and time api
import bangla                    #bangla calender api
import wikipediaapi              #wikipedia api
import webbrowser                #internet explorer browser api
import smtplib                   #email api
import os 
import requests                  #newspaper request
from opencage.geocoder import OpenCageGeocode  #opencage api(geo location)         
#Darksky api for weather information
from darksky import forecast
from datetime import date, timedelta
from gtts import gTTS 
import scholarly                      #google scholars#
from googletrans import Translator    #google translator
from apiclient.discovery import build #youtube
import operator                       #arethmetic

###########  opencage api key ###############

key = '44fe2fe0976d48d0a77e1e9d693ac650'

###########  opencage api key ###############


#speech recognition
############ greetings ############
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        print("শুভ সকাল!")

    elif hour>=12 and hour<18:
        print("শুভ সন্ধ্যা!")   

    else:
        print("শুভ রাত্রি")  

        print("আমি কিভাবে আপনাকে সাহায্য করতে পারি ")
############ greetings ############

############ speech recognition ############
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    
    mic = sr.Microphone()
    with mic as source:
        print("শুনছে...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("রিকগনাইজ করছে...")    
        query = r.recognize_google(audio, language='bn-BD')
        print(f" {query}\n")

    except Exception as e:
        # print(e)    
        print("আবার বলুন...")  
        return "None"
    return query
############ speech recognition ############

############ arethmetic ############
def getOperator(op):
    return{
        '+' : operator.add,
        '-' : operator.sub,
        'গুণ' : operator.mul,
        'গুন' : operator.mul,
        'ভাগ' : operator.__truediv__ ,
        'বাঘ' : operator.__truediv__ ,
        }[op]
def evalBinary(op1,oper, op2):
    op1,op2 = int (op1),int (op2)
    return getOperator(oper)(op1,op2)
def calculation():
    print(evalBinary(*(query.split())))
############ arethmetic ############

############ youtube ############
api_key='AIzaSyDRl--lB5l2bASGrYXHyct6lCiQel-iOlM'
youtube = build('youtube','v3',developerKey= api_key)
type(youtube)
#print(req.execute())
video= ['n1','n2','n3','n4','n5']
idd=['m1','m2','m3','m4','m5']
############ youtube ############

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shahadat6218@gmail.com', '202443@@@a')
    server.sendmail('shahadat6218@gmail.com', to, content)
    server.close()


def news():
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=associated-press&'
           'apiKey=2927a7118d1748bc805e4906126e0df8')
    response = requests.get(url)
    news_result=response.json()
    # print (response.json())
    for i in range(0,9,1):
        news1=news_result['articles'][i]['title']
        news2=news_result['articles'][i]['description']
        final_news= f" Title: {news1} \n Description: {news2} \n "
        # print('Headline: ',news1)
        # print('Description: ',news2)
        # print('')
        print (final_news)
    return final_news


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'উইকিপিডিয়া' in query:
            print('উইকিপিডিয়া খুজছে...')
            query = query.replace('উইকিপিডিয়া','')
            wiki_wiki = wikipediaapi.Wikipedia('bn')
            page_py = wiki_wiki.page(query)
            results=page_py.summary[0:2000]
            print(results)
            # text to speech
            language = 'bn'
            myobj = gTTS(text=results, lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3")                                  # Playing the converted file 

        elif 'আবহাওয়া বলুন' in query:
            geocoder = OpenCageGeocode(key)
            place = query.replace('আবহাওয়া বলুন','')
            result = geocoder.geocode(place)

            a = result[0]['geometry']['lat']
            b = result[0]['geometry']['lng']
            print('Lat:',a,'Lng:',b)
            # print(result[0])          

            Approximity= a,b
            weekday = date.today()
            with forecast('35eaf94a35d0825031e72d5fb524bf50', *Approximity) as area:
                temp = (((area.temperature)-32)/1.8)
                tempt="%.2f" % temp
                print('TimeZone:',area.timezone) 
                print('Temperature:',"%.2f" % temp,'Degree Celcius')
                print('Humidity',area.humidity) 
                print('Summary:',area.summary)
                print('Dewpoint:',area.dewPoint)
                print('WindSpeed:',area.windSpeed)
                print('Icon:',area.icon)    
            mytext= f"আমাদের আজকের তাপমাত্রা  {tempt} degree celcius"
            language = 'bn'
            myobj = gTTS(text=mytext, lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3")  

        elif 'আজকের সংবাদ গুলো কি কি' in query:
            newses= news()
            print (newses)
            mytext= f"আমাদের আজকের সংবাদগুলো  {newses}"
            language = 'bn'
            myobj = gTTS(text=mytext, lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3")
            
        elif 'গুগোল স্কলার' in query:
            print('searching google scholars...')
            query = query.replace('গুগোল স্কলার','')
            search_query = scholarly.search_author(query)
            author = next(search_query).fill()
            print(author)
            # Print the titles of the author's publications
            print([pub.bib['title'] for pub in author.publications])           
            # Take a closer look at the first publication
            pub = author.publications[0].fill()
            print(pub)           
            # Which papers cited that publication?
            print([citation.bib['title'] for citation in pub.            get_citedby()])

            translator = Translator()
            #textt='Condition monitoring of induction motors is important for their efficient and reliable operation.'
            #'english='en'
            bangla= 'bn'
            #'korean='ko'
            translations = translator.translate([author,pub], dest= bangla)
            for translation in translations:
                print(translation.text)

        elif 'ইউটিউব' in query:
            print('search result..')
            query= query.replace('youtube','')
            req = youtube.search().list(q= query ,part='snippet', type='video')
            reqs=req.execute()
            for i in range(0,4,1):
                video[i] = reqs['items'][i]['snippet']['title']
                idd[i] = reqs['items'][i]['id']['videoId']
                print(video[i])
                print(idd[i])
            while True:
                query = takeCommand()
                if 'প্রথম' in query:
                    webbrowser.open(f"www.youtube.com/watch?v={idd[0]}")
                elif 'দ্বিতীয়' in query:
                    webbrowser.open(f"www.youtube.com/watch?v={idd[1]}")
                elif 'তৃতীয়' in query:
                    webbrowser.open(f"www.youtube.com/watch?v={idd[2]}")
                elif 'চতুর্থ' in query:
                    webbrowser.open(f"www.youtube.com/watch?v={idd[3]}")
                elif 'বাহির হও' in query:
                    break

        
        elif 'সাধারণ গণনা করো' in query:
            print('কি গণনা করতে হবে?')        
            if True:
                query = takeCommand()
                try:
                    calculation()
                except:
                    print('আবার...')
            elif 'exit' in query:
                break


        elif 'ইউটিউব খুলুন' in query:
            webbrowser.open("www.youtube.com")
            mytext= 'ইউটিউব খুলছে'
            language = 'bn'
            myobj = gTTS(text=mytext, lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3")                                  # Playing the converted file 

        elif 'গুগল খুলুন' in query:
            webbrowser.open("www.google.com.bd")
            mytext= 'গুগল খুলছে'
            language = 'bn'
            myobj = gTTS(text=mytext, lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3")                                  # Playing the converted file 
        
        elif 'ইএসপিএন খুলুন' in query:
            webbrowser.open("www.espn.in")
            mytext= 'ইএসপিএন খুলছে'
            language = 'bn'
            myobj = gTTS(text=mytext, lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3")                                  # Playing the converted file

        elif 'প্রথম আলো খুলুন' in query:
            webbrowser.open("www.prothomalo.com")
            mytext= 'প্রথম আলো খুলছে'
            language = 'bn'
            myobj = gTTS(text=mytext, lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3")  

        elif 'ইস্ট ওয়েস্ট ইউনিভার্সিটি ওয়েবসাইট খুলুন' in query:
            webbrowser.open("www.ewubd.edu")
            mytext= 'ইস্ট ওয়েস্ট ইউনিভার্সিটি ওয়েবসাইট খুলছে'
            language = 'bn'
            myobj = gTTS(text=mytext, lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3") 


        elif 'বাংলা ক্যালেন্ডার খুলুন' in query:
            bangla_date = bangla.get_date()
            print(bangla_date)
            mytext= 'বাংলা ক্যালেন্ডার খুলছে'
            language = 'bn'
            myobj = gTTS(text=mytext, lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'গান শুনাও' in query:
            music_dir = 'D:'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'এখন কয়টা বাজে' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"এখন বাজে {strTime}")
            language = 'bn'
            myobj = gTTS(text=f"এখন বাজে {strTime}", lang=language, slow=False)           # Passing the text and language to the engine, 
            myobj.save("welcome.mp3")                                       # Saving the converted audio in a mp3 file named  'welcome' 
            os.system("start welcome.mp3")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            

   

        elif 'ইমেইল পাঠাও' in query:
            try:
                print("কি মেসেজ পাঠাব?")
                content = takeCommand()
                to = "shahadat6218@gmail.com"    
                sendEmail(to, content)
                print("ইমেইল পাঠান হয়েছে!")
            except Exception as e:
                print(e)
                print("দুঃখীত, মেইল টি পাঠানো যাচ্ছে না") 
