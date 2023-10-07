from pytube import YouTube
import pytube
from pytube import Playlist
import PySimpleGUI as sg
import os

# Checks to see if download file exists, if it doesnt create it
if os.path.isdir(os.getcwd() + '\downloads') == False: 
    os.mkdir(os.getcwd() + '\downloads')


# Sets theme
sg.theme('Dark Grey 13')

# Sets layout for the window
layout = [[sg.Text('Youtube downloader')], 
          [sg.Text('Link:'), sg.Input()], 
          [sg.Frame('File type', [[sg.Radio('mp4', 'filetype', default=True, key = 'mp4'), sg.Radio('mp3', 'filetype', key = 'mp3')]])],
          [sg.Frame('Video quality', [[sg.Radio('Low', 'quality', key = 'lowQual'), sg.Radio('Medium', 'quality', default=True, key = 'medQual'), sg.Radio('High', 'quality', key = 'highQual')]])],
          [sg.Text('Download path: '), sg.Input(os.getcwd() + '\downloads', key = 'downPath'), sg.FolderBrowse()], 
          [sg.Button('Download')],
          [sg.Text('', key='status')]]

# Creates the window
window = sg.Window('Youtube downloader', layout)

# Function to change the bottom text on the window and update the window so it shows
def statusText(status):
    window['status'].update(status)
    sg.Window.refresh(window)

# Function to change a file's extention
def changeExt(file, ext):
    base = os.path.splitext(file)[0]
    os.rename(file, base + ext)

# Event loop
while True:
    success = True
    vidList = []
    event, values = window.read()

    # Breaks loop if window is closed
    if event == sg.WIN_CLOSED:
        break

    # For debugging
    # print(event)
    # print(values)

    # Tests to see if link is a playlist
    try:
        pl = Playlist(values[0])
        for i in pl.videos:
            vidList.append(i)

    except KeyError:
        # If its not tests to see if its a valid video
        try:
            vidList.append(YouTube(values[0]))

        # If its not a valid video link popup an error
        except pytube.exceptions.RegexMatchError:
            sg.popup_error('Invalid video/playlist URL')
            success = False

        # Extra exceptions
        except Exception as e:
            sg.popup_error(e)
            success = False

    # Extra exceptions
    except Exception as e:
        sg.popup_error(e)

    # For debugging
    # print(vidList)

    # Checks to see if the download path is valid
    downPath = values['downPath']
    if os.path.isdir(downPath) == True:
        pass
    
    else:
        # If its not popup an error
        sg.popup_error('Invalid download path')
        success = False

    # If everything went well, start the downloading of all the files
    if success == True:
        for yt in vidList:
            statusText('[{}/{}] Downloading: {}'.format(vidList.index(yt) + 1, len(vidList), yt.title))

            # Downloads files as mp4's
            if values['mp4'] == True:
                if values['lowQual'] == True:
                    stream = yt.streams.filter(progressive = True)
                    stream = stream[0]
                    downFile = stream.download(downPath)

                    
                elif values['medQual'] == True:
                    stream = yt.streams.filter(progressive = True)
                    stream = stream[int(len(stream) / 2)]
                    downFile = stream.download(downPath)

                elif values['highQual'] == True:
                    stream = yt.streams.filter(progressive = True)
                    stream = stream[-1]
                    downFile = stream.download(downPath)

                # Changes extention to mp4
                changeExt(downFile, '.mp4')

            # Downloads files as mp3's
            elif values['mp3'] == True:
                stream = yt.streams.filter(only_audio = True)
                stream = stream[-1]
                downFile = stream.download(downPath)

                changeExt(downFile, '.mp3')

            # Changes extention to mp3
            statusText('[{}/{}] Finished downloading: {}'.format(vidList.index(yt) + 1, len(vidList), yt.title))

        statusText('Finished downloading {} files.'.format(len(vidList)))