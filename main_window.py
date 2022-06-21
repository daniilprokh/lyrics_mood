#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ui_main_window import Ui_MainWindow
from api_widget import ApiWidget
from api import Api


# In[2]:


import sys
from PySide2 import QtCore, QtGui, QtWidgets


# In[3]:


import mutagen


# In[4]:


import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius


# In[5]:


from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[6]:


import paralleldots


# In[7]:


import requests
import json


# In[8]:


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.m_ui = Ui_MainWindow()
        self.m_ui.setupUi(self)
        
        self.m_ui.a_audio_file.triggered.connect(self.chooseAudioFile)
        self.m_ui.a_txt.triggered.connect(self.saveLyricsAsTxt)
        self.m_ui.a_tag.triggered.connect(self.saveLyricsAsTag)
        
        self.m_ui.a_api.triggered.connect(self.chooseApi)
        
        self.m_ui.pb_load_lyrics.clicked.connect(self.loadLyrics)
        self.m_ui.pb_analyze_tone.clicked.connect(self.analyzeTone)
        
        self.m_ui.t_lyrics.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        
        self.api_widget = ApiWidget()
        
        self.file_filter = u'Аудиофайлы (*.mp3 *.flac)'
        
        self.tone_tranform = {
            'analytical' : 'Thoughtful',
            'anger': 'Angry', 'angry': 'Angry',
            'bored': 'Boring',
            'confident' : 'Confident',
            'disgust': 'Disgusting',
            'excited': 'Exciting', 'surprise': 'Exciting',
            'fear': 'Scary',
            'happy': 'Happy', 'joy': 'Happy',
            'sad' : 'Sad', 'sadness' : 'Sad',
            'tentative' : 'Doubtful',
        }
        
        self.genius = lg.Genius('',
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
        
        authenticator = IAMAuthenticator('')
        self.tone_analyzer = ToneAnalyzerV3(
            version='2017-09-21',
            authenticator=authenticator)
        self.tone_analyzer.set_service_url('https://api.au-syd.tone-analyzer.watson.cloud.ibm.com/instances/318b552b-ffe6-4b90-b0d2-50b68f2c2560')
        
        paralleldots.set_api_key('')
        
    @QtCore.Slot()
    def chooseAudioFile(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(parent=self,
            caption=u'Выбрать аудиофайл',
            filter=self.file_filter)[0]
        if file_name:
            audio_file = mutagen.File(file_name)
            audio_type = type(audio_file)
            artist_tag, title_tag, lyrics_tag = '', '', ''
            if audio_type == mutagen.mp3.MP3:
                artist_tag, title_tag, lyrics_tag = 'TPE2', 'TIT2', 'USLT::eng'
            elif audio_type == mutagen.flac.FLAC:
                artist_tag, title_tag, lyrics_tag = 'artist', 'title', 'lyrics'
            artist_list = audio_file.tags.get(artist_tag)
            title_list = audio_file.tags.get(title_tag)
            lyrics_list = audio_file.tags.get(lyrics_tag)
            if artist_list:
                self.m_ui.le_artist.setText(artist_list[0])
            if title_list:
                self.m_ui.le_title.setText(title_list[0])
            if lyrics_list:
                if(type(lyrics_list) == list):
                    self.m_ui.t_lyrics.setText(lyrics_list[0])
                else:
                    self.m_ui.t_lyrics.setText(str(lyrics_list))
    
    @QtCore.Slot()
    def saveLyricsAsTxt(self):
        lyrics = self.m_ui.t_lyrics.text()
        file_name = QtWidgets.QFileDialog.getSaveFileName(parent=self,
            caption=u'Сохранить текст песни',
            filter=u'Текстовый файл (*.txt)')[0]
        with open(file_name, mode='w', encoding='utf-8') as file:
            file.write(lyrics)
        
    @QtCore.Slot()
    def saveLyricsAsTag(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(parent=self,
            caption=u'Выбрать аудиофайл для сохранения текста',
            filter=self.file_filter)[0]
        if file_name:
            audio_file = mutagen.File(file_name)
            audio_type = type(audio_file)
            lyrics = self.m_ui.t_lyrics.text()
            if audio_type == mutagen.mp3.MP3:
                audio_file.tags.setall('USLT', [mutagen.id3.USLT(lang='eng',text=lyrics)])
            elif audio_type == mutagen.flac.FLAC:
                audio_file['lyrics'] = lyrics
            audio_file.save()
            
    @QtCore.Slot()
    def chooseApi(self):
        self.api_widget.show()
        self.api_widget.raise_()
    
    @QtCore.Slot()
    def loadLyrics(self):
        artist = self.m_ui.le_artist.text()
        title = self.m_ui.le_title.text()
        if artist and title:
            try:
                song = self.genius.search_song(title, artist)
                lyrics = song.lyrics
                # fix for extra text at last line of lyrics #215
                if lyrics.endswith('EmbedShare URLCopyEmbedCopy'):
                    lyrics = lyrics[:-27]
                    last_suf = ''
                    for i in range(lyrics.rfind('\n'), len(lyrics)):
                        if lyrics[i] >= '0' and lyrics[i] <= '9':
                            last_suf += lyrics[i]
                    lyrics = lyrics[:-1 * len(last_suf)]
                self.m_ui.t_lyrics.setText(lyrics)
            except:
                print(';(')
        else:
            print('(')
                
    @QtCore.Slot()
    def analyzeTone(self):
        lyrics = self.m_ui.t_lyrics.text()
        if lyrics:
            result = ''
            for api in self.api_widget.api_list:
                if api == Api.IBM_WATSON:
                    result += 'IBM Watson Tone Analyzer API:\n'
                    response = self.tone_analyzer.tone(lyrics, content_type='text/plain').get_result()
                    for tone in response['document_tone']['tones']:
                         result += '\t{0}: {1}%\n'.format(self.tone_tranform[tone['tone_name'].lower()],
                                                          int(round(tone['score'], 2) * 100))
                    result += '\n'
                elif api == Api.PARALLEL_DOTS:
                    result += 'ParallelDots Text Analysis API:\n'
                    response = paralleldots.emotion(lyrics)
                    for emotion in response['emotion'].keys():
                        score = response['emotion'][emotion]
                        result += '\t{0}: {1}%\n'.format(self.tone_tranform[emotion.lower()],
                                                         int(round(score, 2) * 100))
                    result += '\n'
                elif api == Api.TWINWORD:
                    result += 'Twinword Emotion Analysis API:\n'
                    response = requests.request('GET',
                        url='https://twinword-emotion-analysis-v1.p.rapidapi.com/analyze/',
                        headers={
                            'x-rapidapi-host': "twinword-emotion-analysis-v1.p.rapidapi.com",
                            'x-rapidapi-key': ""
                        },
                        params={'text' : lyrics})
                    response_dict = response.json()
                    for emotion in response_dict['emotions_detected']:
                        result += '\t{0}: {1}%\n'.format(self.tone_tranform[emotion.lower()],
                                                         int(round(response_dict['emotion_scores'][emotion], 2) * 100))
                    result += '\n'
                elif api == Api.PROMPT:
                    result += 'Prompt Text to Emotion API:\n'
                    payload = lyrics.encode('utf-8')
                    response = requests.request('POST',
                        url='https://api.promptapi.com/text_to_emotion',
                        headers={
                            'apikey': ''
                        },
                        data=payload)
                    for (emotion, score) in response.json().items():
                        result += '\t{0}: {1}%\n'.format(self.tone_tranform[emotion.lower()], int(score * 100))
                    result += '\n'
            self.m_ui.t_tone_analysis.setText(result)


# In[9]:


if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())


# In[ ]:





# In[ ]:





# In[ ]:




