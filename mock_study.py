#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Mon Jun 23 16:42:43 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'mock_study'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1280, 720]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/marcogiven/Desktop/PsychoPyProjects/mock_study_clean/mock_study.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_Continue') is None:
        # initialise key_Continue
        key_Continue = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_Continue',
        )
    if deviceManager.getDevice('key_NextScreen') is None:
        # initialise key_NextScreen
        key_NextScreen = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_NextScreen',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "WelcomeScreen" ---
    textWelcomeMessage = visual.TextStim(win=win, name='textWelcomeMessage',
        text="Welcome to the user study\n\nOn the following screen, you will see a query image on the left, and will choose from the images on the right which is the same. \n\nPress 'SPACE' to start",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_Continue = keyboard.Keyboard(deviceName='key_Continue')
    
    # --- Initialize components for Routine "trialColor" ---
    divider = visual.Rect(
        win=win, name='divider',units='height', 
        width=(0.001, 0.8)[0], height=(0.001, 0.8)[1],
        ori=0.0, pos=(-0.225, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=0.0, interpolate=True)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    imageQuery = visual.ImageStim(
        win=win,
        name='imageQuery', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.55, 0), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image1 = visual.ImageStim(
        win=win,
        name='image1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.35, -0.25), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image2 = visual.ImageStim(
        win=win,
        name='image2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0.25), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image3 = visual.ImageStim(
        win=win,
        name='image3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0.25), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    image4 = visual.ImageStim(
        win=win,
        name='image4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    image5 = visual.ImageStim(
        win=win,
        name='image5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    queryCaption = visual.TextStim(win=win, name='queryCaption',
        text='Query Image',
        font='Arial',
        pos=(-0.55, 0.2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "confidenceScreen" ---
    text_confidenceQuestion = visual.TextStim(win=win, name='text_confidenceQuestion',
        text='How confident do you feel your selected image was correct?',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(0.5, 0.05), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    buttonAdvance = visual.ButtonStim(win, 
        text='Submit', font='Arvo',
        pos=(0, -0.45),
        letterHeight=0.035,
        size=(0.2, 0.065), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='buttonAdvance',
        depth=-2
    )
    buttonAdvance.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "trialGrayscale" ---
    divider_2 = visual.Rect(
        win=win, name='divider_2',units='height', 
        width=(0.001, 0.8)[0], height=(0.001, 0.8)[1],
        ori=0.0, pos=(-0.225, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=0.0, interpolate=True)
    mouse_3 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_3.mouseClock = core.Clock()
    queryImage_2 = visual.ImageStim(
        win=win,
        name='queryImage_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.55, 0), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image1_3 = visual.ImageStim(
        win=win,
        name='image1_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.35, -0.25), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image2_3 = visual.ImageStim(
        win=win,
        name='image2_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0.25), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image3_3 = visual.ImageStim(
        win=win,
        name='image3_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0.25), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    image4_3 = visual.ImageStim(
        win=win,
        name='image4_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    image5_3 = visual.ImageStim(
        win=win,
        name='image5_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    queryCaption_gray = visual.TextStim(win=win, name='queryCaption_gray',
        text='Query Image',
        font='Arial',
        pos=(-0.55, 0.2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "confidenceScreen" ---
    text_confidenceQuestion = visual.TextStim(win=win, name='text_confidenceQuestion',
        text='How confident do you feel your selected image was correct?',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(0.5, 0.05), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    buttonAdvance = visual.ButtonStim(win, 
        text='Submit', font='Arvo',
        pos=(0, -0.45),
        letterHeight=0.035,
        size=(0.2, 0.065), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='buttonAdvance',
        depth=-2
    )
    buttonAdvance.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "NextScreen" ---
    textNextScreen = visual.TextStim(win=win, name='textNextScreen',
        text="\nUse the Button to change between color and grayscale\n\nPress 'SPACE' to continue",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_NextScreen = keyboard.Keyboard(deviceName='key_NextScreen')
    
    # --- Initialize components for Routine "trialColor_Gray" ---
    divider_3 = visual.Rect(
        win=win, name='divider_3',units='height', 
        width=(0.001, 0.8)[0], height=(0.001, 0.8)[1],
        ori=0.0, pos=(-0.225, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=0.0, interpolate=True)
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    imageQuery_2 = visual.ImageStim(
        win=win,
        name='imageQuery_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.55, 0), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image1_2 = visual.ImageStim(
        win=win,
        name='image1_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.35, -0.25), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image2_2 = visual.ImageStim(
        win=win,
        name='image2_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0.25), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image3_2 = visual.ImageStim(
        win=win,
        name='image3_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0.25), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    image4_2 = visual.ImageStim(
        win=win,
        name='image4_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    image5_2 = visual.ImageStim(
        win=win,
        name='image5_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0), draggable=False, size=(0.4984, 0.28),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    toggle_button = visual.ButtonStim(win, 
        text='Toggle Color/Grayscale', font='Arial',
        pos=(-0.55, -0.25),units='height',
        letterHeight=0.025,
        size=(0.45, 0.125), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[0.5, 0.5, 0.5], borderColor=[0.0000, 0.0000, 0.0000],
        color='white', colorSpace='rgb',
        opacity=1.0,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='toggle_button',
        depth=-9
    )
    toggle_button.buttonClock = core.Clock()
    queryCaption_GC = visual.TextStim(win=win, name='queryCaption_GC',
        text='Query Image',
        font='Arial',
        pos=(-0.55, 0.2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "confidenceScreen" ---
    text_confidenceQuestion = visual.TextStim(win=win, name='text_confidenceQuestion',
        text='How confident do you feel your selected image was correct?',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(0.5, 0.05), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    buttonAdvance = visual.ButtonStim(win, 
        text='Submit', font='Arvo',
        pos=(0, -0.45),
        letterHeight=0.035,
        size=(0.2, 0.065), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='buttonAdvance',
        depth=-2
    )
    buttonAdvance.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "EndScreen" ---
    textEndMessage = visual.TextStim(win=win, name='textEndMessage',
        text='Thank you for completing!\n\nPlease wait while we save your results...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "WelcomeScreen" ---
    # create an object to store info about Routine WelcomeScreen
    WelcomeScreen = data.Routine(
        name='WelcomeScreen',
        components=[textWelcomeMessage, key_Continue],
    )
    WelcomeScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_Continue
    key_Continue.keys = []
    key_Continue.rt = []
    _key_Continue_allKeys = []
    # store start times for WelcomeScreen
    WelcomeScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    WelcomeScreen.tStart = globalClock.getTime(format='float')
    WelcomeScreen.status = STARTED
    WelcomeScreen.maxDuration = None
    # keep track of which components have finished
    WelcomeScreenComponents = WelcomeScreen.components
    for thisComponent in WelcomeScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WelcomeScreen" ---
    WelcomeScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcomeMessage* updates
        
        # if textWelcomeMessage is starting this frame...
        if textWelcomeMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcomeMessage.frameNStart = frameN  # exact frame index
            textWelcomeMessage.tStart = t  # local t and not account for scr refresh
            textWelcomeMessage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcomeMessage, 'tStartRefresh')  # time at next scr refresh
            # update status
            textWelcomeMessage.status = STARTED
            textWelcomeMessage.setAutoDraw(True)
        
        # if textWelcomeMessage is active this frame...
        if textWelcomeMessage.status == STARTED:
            # update params
            pass
        
        # *key_Continue* updates
        
        # if key_Continue is starting this frame...
        if key_Continue.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_Continue.frameNStart = frameN  # exact frame index
            key_Continue.tStart = t  # local t and not account for scr refresh
            key_Continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_Continue, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_Continue.status = STARTED
            # keyboard checking is just starting
            key_Continue.clock.reset()  # now t=0
        if key_Continue.status == STARTED:
            theseKeys = key_Continue.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_Continue_allKeys.extend(theseKeys)
            if len(_key_Continue_allKeys):
                key_Continue.keys = _key_Continue_allKeys[-1].name  # just the last key pressed
                key_Continue.rt = _key_Continue_allKeys[-1].rt
                key_Continue.duration = _key_Continue_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=WelcomeScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            WelcomeScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WelcomeScreen" ---
    for thisComponent in WelcomeScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for WelcomeScreen
    WelcomeScreen.tStop = globalClock.getTime(format='float')
    WelcomeScreen.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsColor = data.TrialHandler2(
        name='trialsColor',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('resources/hotel_color.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trialsColor)  # add the loop to the experiment
    thisTrialsColor = trialsColor.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsColor.rgb)
    if thisTrialsColor != None:
        for paramName in thisTrialsColor:
            globals()[paramName] = thisTrialsColor[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrialsColor in trialsColor:
        trialsColor.status = STARTED
        if hasattr(thisTrialsColor, 'status'):
            thisTrialsColor.status = STARTED
        currentLoop = trialsColor
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsColor.rgb)
        if thisTrialsColor != None:
            for paramName in thisTrialsColor:
                globals()[paramName] = thisTrialsColor[paramName]
        
        # --- Prepare to start Routine "trialColor" ---
        # create an object to store info about Routine trialColor
        trialColor = data.Routine(
            name='trialColor',
            components=[divider, mouse, imageQuery, image1, image2, image3, image4, image5, queryCaption],
        )
        trialColor.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        mouse.mouseClock.reset()
        imageQuery.setImage(hotel_query)
        image1.setImage(choice1)
        image2.setImage(choice2)
        image3.setImage(choice3)
        image4.setImage(choice4)
        image5.setImage(choice5)
        # Run 'Begin Routine' code from colorCorrect
        clicked_img = None
        # store start times for trialColor
        trialColor.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trialColor.tStart = globalClock.getTime(format='float')
        trialColor.status = STARTED
        trialColor.maxDuration = None
        # keep track of which components have finished
        trialColorComponents = trialColor.components
        for thisComponent in trialColor.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialColor" ---
        trialColor.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrialsColor, 'status') and thisTrialsColor.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *divider* updates
            
            # if divider is starting this frame...
            if divider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                divider.frameNStart = frameN  # exact frame index
                divider.tStart = t  # local t and not account for scr refresh
                divider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(divider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'divider.started')
                # update status
                divider.status = STARTED
                divider.setAutoDraw(True)
            
            # if divider is active this frame...
            if divider.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse.status = STARTED
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([image1, image2, image3, image4, image5], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse.getPos()
                            mouse.x.append(x)
                            mouse.y.append(y)
                            buttons = mouse.getPressed()
                            mouse.leftButton.append(buttons[0])
                            mouse.midButton.append(buttons[1])
                            mouse.rightButton.append(buttons[2])
                            mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # *imageQuery* updates
            
            # if imageQuery is starting this frame...
            if imageQuery.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imageQuery.frameNStart = frameN  # exact frame index
                imageQuery.tStart = t  # local t and not account for scr refresh
                imageQuery.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageQuery, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageQuery.status = STARTED
                imageQuery.setAutoDraw(True)
            
            # if imageQuery is active this frame...
            if imageQuery.status == STARTED:
                # update params
                pass
            
            # *image1* updates
            
            # if image1 is starting this frame...
            if image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image1.frameNStart = frameN  # exact frame index
                image1.tStart = t  # local t and not account for scr refresh
                image1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
                # update status
                image1.status = STARTED
                image1.setAutoDraw(True)
            
            # if image1 is active this frame...
            if image1.status == STARTED:
                # update params
                pass
            
            # *image2* updates
            
            # if image2 is starting this frame...
            if image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image2.frameNStart = frameN  # exact frame index
                image2.tStart = t  # local t and not account for scr refresh
                image2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
                # update status
                image2.status = STARTED
                image2.setAutoDraw(True)
            
            # if image2 is active this frame...
            if image2.status == STARTED:
                # update params
                pass
            
            # *image3* updates
            
            # if image3 is starting this frame...
            if image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image3.frameNStart = frameN  # exact frame index
                image3.tStart = t  # local t and not account for scr refresh
                image3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image3, 'tStartRefresh')  # time at next scr refresh
                # update status
                image3.status = STARTED
                image3.setAutoDraw(True)
            
            # if image3 is active this frame...
            if image3.status == STARTED:
                # update params
                pass
            
            # *image4* updates
            
            # if image4 is starting this frame...
            if image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image4.frameNStart = frameN  # exact frame index
                image4.tStart = t  # local t and not account for scr refresh
                image4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image4, 'tStartRefresh')  # time at next scr refresh
                # update status
                image4.status = STARTED
                image4.setAutoDraw(True)
            
            # if image4 is active this frame...
            if image4.status == STARTED:
                # update params
                pass
            
            # *image5* updates
            
            # if image5 is starting this frame...
            if image5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image5.frameNStart = frameN  # exact frame index
                image5.tStart = t  # local t and not account for scr refresh
                image5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image5, 'tStartRefresh')  # time at next scr refresh
                # update status
                image5.status = STARTED
                image5.setAutoDraw(True)
            
            # if image5 is active this frame...
            if image5.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from colorCorrect
            clickable_objects = [image1, image2, image3, image4, image5]
            
            for obj in clickable_objects:
                if obj.contains(mouse) and mouse.getPressed()[0]:
                    clicked_img = obj.image  # This gives the filename like 'images/hotel2_sample4.png'
                    thisExp.addData("clicked_image", clicked_img)
                    thisExp.addData("correct_answer", correct_answer)
                    thisExp.addData("isCorrect", int(clicked_img == correct_answer))
                    continueRoutine = False
                    break
            
            
            # *queryCaption* updates
            
            # if queryCaption is starting this frame...
            if queryCaption.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                queryCaption.frameNStart = frameN  # exact frame index
                queryCaption.tStart = t  # local t and not account for scr refresh
                queryCaption.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(queryCaption, 'tStartRefresh')  # time at next scr refresh
                # update status
                queryCaption.status = STARTED
                queryCaption.setAutoDraw(True)
            
            # if queryCaption is active this frame...
            if queryCaption.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trialColor,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trialColor.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialColor.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialColor" ---
        for thisComponent in trialColor.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trialColor
        trialColor.tStop = globalClock.getTime(format='float')
        trialColor.tStopRefresh = tThisFlipGlobal
        # store data for trialsColor (TrialHandler)
        trialsColor.addData('mouse.x', mouse.x)
        trialsColor.addData('mouse.y', mouse.y)
        trialsColor.addData('mouse.leftButton', mouse.leftButton)
        trialsColor.addData('mouse.midButton', mouse.midButton)
        trialsColor.addData('mouse.rightButton', mouse.rightButton)
        trialsColor.addData('mouse.time', mouse.time)
        trialsColor.addData('mouse.clicked_name', mouse.clicked_name)
        # the Routine "trialColor" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[text],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrialsColor, 'status') and thisTrialsColor.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blank500,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisTrialsColor as finished
        if hasattr(thisTrialsColor, 'status'):
            thisTrialsColor.status = FINISHED
        # if awaiting a pause, pause now
        if trialsColor.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trialsColor.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialsColor'
    trialsColor.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "confidenceScreen" ---
    # create an object to store info about Routine confidenceScreen
    confidenceScreen = data.Routine(
        name='confidenceScreen',
        components=[text_confidenceQuestion, slider, buttonAdvance],
    )
    confidenceScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    slider.reset()
    # reset buttonAdvance to account for continued clicks & clear times on/off
    buttonAdvance.reset()
    # store start times for confidenceScreen
    confidenceScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    confidenceScreen.tStart = globalClock.getTime(format='float')
    confidenceScreen.status = STARTED
    confidenceScreen.maxDuration = None
    # keep track of which components have finished
    confidenceScreenComponents = confidenceScreen.components
    for thisComponent in confidenceScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "confidenceScreen" ---
    confidenceScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_confidenceQuestion* updates
        
        # if text_confidenceQuestion is starting this frame...
        if text_confidenceQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_confidenceQuestion.frameNStart = frameN  # exact frame index
            text_confidenceQuestion.tStart = t  # local t and not account for scr refresh
            text_confidenceQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_confidenceQuestion, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_confidenceQuestion.status = STARTED
            text_confidenceQuestion.setAutoDraw(True)
        
        # if text_confidenceQuestion is active this frame...
        if text_confidenceQuestion.status == STARTED:
            # update params
            pass
        
        # *slider* updates
        
        # if slider is starting this frame...
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # update status
            slider.status = STARTED
            slider.setAutoDraw(True)
        
        # if slider is active this frame...
        if slider.status == STARTED:
            # update params
            pass
        # *buttonAdvance* updates
        
        # if buttonAdvance is starting this frame...
        if buttonAdvance.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            buttonAdvance.frameNStart = frameN  # exact frame index
            buttonAdvance.tStart = t  # local t and not account for scr refresh
            buttonAdvance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonAdvance, 'tStartRefresh')  # time at next scr refresh
            # update status
            buttonAdvance.status = STARTED
            win.callOnFlip(buttonAdvance.buttonClock.reset)
            buttonAdvance.setAutoDraw(True)
        
        # if buttonAdvance is active this frame...
        if buttonAdvance.status == STARTED:
            # update params
            pass
            # check whether buttonAdvance has been pressed
            if buttonAdvance.isClicked:
                if not buttonAdvance.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    buttonAdvance.timesOn.append(routineTimer.getTime())
                    buttonAdvance.timesOff.append(routineTimer.getTime())
                elif len(buttonAdvance.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    buttonAdvance.timesOff[-1] = routineTimer.getTime()
                if not buttonAdvance.wasClicked:
                    # end routine when buttonAdvance is clicked
                    continueRoutine = False
                if not buttonAdvance.wasClicked:
                    # run callback code when buttonAdvance is clicked
                    pass
        # take note of whether buttonAdvance was clicked, so that next frame we know if clicks are new
        buttonAdvance.wasClicked = buttonAdvance.isClicked and buttonAdvance.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=confidenceScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            confidenceScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidenceScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "confidenceScreen" ---
    for thisComponent in confidenceScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for confidenceScreen
    confidenceScreen.tStop = globalClock.getTime(format='float')
    confidenceScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('slider.response', slider.getRating())
    thisExp.addData('slider.rt', slider.getRT())
    thisExp.addData('slider.history', slider.getHistory())
    thisExp.nextEntry()
    # the Routine "confidenceScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsGray = data.TrialHandler2(
        name='trialsGray',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('resources/hotel_color.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trialsGray)  # add the loop to the experiment
    thisTrialsGray = trialsGray.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsGray.rgb)
    if thisTrialsGray != None:
        for paramName in thisTrialsGray:
            globals()[paramName] = thisTrialsGray[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrialsGray in trialsGray:
        trialsGray.status = STARTED
        if hasattr(thisTrialsGray, 'status'):
            thisTrialsGray.status = STARTED
        currentLoop = trialsGray
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsGray.rgb)
        if thisTrialsGray != None:
            for paramName in thisTrialsGray:
                globals()[paramName] = thisTrialsGray[paramName]
        
        # --- Prepare to start Routine "trialGrayscale" ---
        # create an object to store info about Routine trialGrayscale
        trialGrayscale = data.Routine(
            name='trialGrayscale',
            components=[divider_2, mouse_3, queryImage_2, image1_3, image2_3, image3_3, image4_3, image5_3, queryCaption_gray],
        )
        trialGrayscale.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_3
        mouse_3.x = []
        mouse_3.y = []
        mouse_3.leftButton = []
        mouse_3.midButton = []
        mouse_3.rightButton = []
        mouse_3.time = []
        mouse_3.clicked_name = []
        gotValidClick = False  # until a click is received
        mouse_3.mouseClock.reset()
        queryImage_2.setImage(hotel_query)
        image1_3.setImage(gray1)
        image2_3.setImage(gray2)
        image3_3.setImage(gray3)
        image4_3.setImage(gray4)
        image5_3.setImage(gray5)
        # store start times for trialGrayscale
        trialGrayscale.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trialGrayscale.tStart = globalClock.getTime(format='float')
        trialGrayscale.status = STARTED
        trialGrayscale.maxDuration = None
        # keep track of which components have finished
        trialGrayscaleComponents = trialGrayscale.components
        for thisComponent in trialGrayscale.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialGrayscale" ---
        trialGrayscale.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrialsGray, 'status') and thisTrialsGray.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *divider_2* updates
            
            # if divider_2 is starting this frame...
            if divider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                divider_2.frameNStart = frameN  # exact frame index
                divider_2.tStart = t  # local t and not account for scr refresh
                divider_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(divider_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'divider_2.started')
                # update status
                divider_2.status = STARTED
                divider_2.setAutoDraw(True)
            
            # if divider_2 is active this frame...
            if divider_2.status == STARTED:
                # update params
                pass
            # *mouse_3* updates
            
            # if mouse_3 is starting this frame...
            if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_3.frameNStart = frameN  # exact frame index
                mouse_3.tStart = t  # local t and not account for scr refresh
                mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_3.status = STARTED
                prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
            if mouse_3.status == STARTED:  # only update if started and not finished!
                buttons = mouse_3.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([image1, image2, image3, image4, image5], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_3):
                                gotValidClick = True
                                mouse_3.clicked_name.append(obj.name)
                                mouse_3.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse_3.getPos()
                            mouse_3.x.append(x)
                            mouse_3.y.append(y)
                            buttons = mouse_3.getPressed()
                            mouse_3.leftButton.append(buttons[0])
                            mouse_3.midButton.append(buttons[1])
                            mouse_3.rightButton.append(buttons[2])
                            mouse_3.time.append(mouse_3.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # *queryImage_2* updates
            
            # if queryImage_2 is starting this frame...
            if queryImage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                queryImage_2.frameNStart = frameN  # exact frame index
                queryImage_2.tStart = t  # local t and not account for scr refresh
                queryImage_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(queryImage_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                queryImage_2.status = STARTED
                queryImage_2.setAutoDraw(True)
            
            # if queryImage_2 is active this frame...
            if queryImage_2.status == STARTED:
                # update params
                pass
            
            # *image1_3* updates
            
            # if image1_3 is starting this frame...
            if image1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image1_3.frameNStart = frameN  # exact frame index
                image1_3.tStart = t  # local t and not account for scr refresh
                image1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image1_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                image1_3.status = STARTED
                image1_3.setAutoDraw(True)
            
            # if image1_3 is active this frame...
            if image1_3.status == STARTED:
                # update params
                pass
            
            # *image2_3* updates
            
            # if image2_3 is starting this frame...
            if image2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image2_3.frameNStart = frameN  # exact frame index
                image2_3.tStart = t  # local t and not account for scr refresh
                image2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image2_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                image2_3.status = STARTED
                image2_3.setAutoDraw(True)
            
            # if image2_3 is active this frame...
            if image2_3.status == STARTED:
                # update params
                pass
            
            # *image3_3* updates
            
            # if image3_3 is starting this frame...
            if image3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image3_3.frameNStart = frameN  # exact frame index
                image3_3.tStart = t  # local t and not account for scr refresh
                image3_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image3_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image3_3.started')
                # update status
                image3_3.status = STARTED
                image3_3.setAutoDraw(True)
            
            # if image3_3 is active this frame...
            if image3_3.status == STARTED:
                # update params
                pass
            
            # *image4_3* updates
            
            # if image4_3 is starting this frame...
            if image4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image4_3.frameNStart = frameN  # exact frame index
                image4_3.tStart = t  # local t and not account for scr refresh
                image4_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image4_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                image4_3.status = STARTED
                image4_3.setAutoDraw(True)
            
            # if image4_3 is active this frame...
            if image4_3.status == STARTED:
                # update params
                pass
            
            # *image5_3* updates
            
            # if image5_3 is starting this frame...
            if image5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image5_3.frameNStart = frameN  # exact frame index
                image5_3.tStart = t  # local t and not account for scr refresh
                image5_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image5_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                image5_3.status = STARTED
                image5_3.setAutoDraw(True)
            
            # if image5_3 is active this frame...
            if image5_3.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from grayCorrect
            clickable_objects = [image1_3, image2_3, image3_3, image4_3, image5_3]
            
            for obj in clickable_objects:
                if obj.contains(mouse) and mouse.getPressed()[0]:
                    clicked_img = obj.image  # This gives the filename like 'images/hotel2_sample4.png'
                    thisExp.addData("clicked_image", clicked_img)
                    thisExp.addData("correct_answer", correct_answer)
                    thisExp.addData("isCorrect", int(clicked_img == correct_answer))
                    continueRoutine = False
                    break
            
            
            # *queryCaption_gray* updates
            
            # if queryCaption_gray is starting this frame...
            if queryCaption_gray.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                queryCaption_gray.frameNStart = frameN  # exact frame index
                queryCaption_gray.tStart = t  # local t and not account for scr refresh
                queryCaption_gray.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(queryCaption_gray, 'tStartRefresh')  # time at next scr refresh
                # update status
                queryCaption_gray.status = STARTED
                queryCaption_gray.setAutoDraw(True)
            
            # if queryCaption_gray is active this frame...
            if queryCaption_gray.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trialGrayscale,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trialGrayscale.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialGrayscale.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialGrayscale" ---
        for thisComponent in trialGrayscale.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trialGrayscale
        trialGrayscale.tStop = globalClock.getTime(format='float')
        trialGrayscale.tStopRefresh = tThisFlipGlobal
        # store data for trialsGray (TrialHandler)
        trialsGray.addData('mouse_3.x', mouse_3.x)
        trialsGray.addData('mouse_3.y', mouse_3.y)
        trialsGray.addData('mouse_3.leftButton', mouse_3.leftButton)
        trialsGray.addData('mouse_3.midButton', mouse_3.midButton)
        trialsGray.addData('mouse_3.rightButton', mouse_3.rightButton)
        trialsGray.addData('mouse_3.time', mouse_3.time)
        trialsGray.addData('mouse_3.clicked_name', mouse_3.clicked_name)
        # the Routine "trialGrayscale" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[text],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrialsGray, 'status') and thisTrialsGray.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blank500,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisTrialsGray as finished
        if hasattr(thisTrialsGray, 'status'):
            thisTrialsGray.status = FINISHED
        # if awaiting a pause, pause now
        if trialsGray.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trialsGray.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialsGray'
    trialsGray.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "confidenceScreen" ---
    # create an object to store info about Routine confidenceScreen
    confidenceScreen = data.Routine(
        name='confidenceScreen',
        components=[text_confidenceQuestion, slider, buttonAdvance],
    )
    confidenceScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    slider.reset()
    # reset buttonAdvance to account for continued clicks & clear times on/off
    buttonAdvance.reset()
    # store start times for confidenceScreen
    confidenceScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    confidenceScreen.tStart = globalClock.getTime(format='float')
    confidenceScreen.status = STARTED
    confidenceScreen.maxDuration = None
    # keep track of which components have finished
    confidenceScreenComponents = confidenceScreen.components
    for thisComponent in confidenceScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "confidenceScreen" ---
    confidenceScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_confidenceQuestion* updates
        
        # if text_confidenceQuestion is starting this frame...
        if text_confidenceQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_confidenceQuestion.frameNStart = frameN  # exact frame index
            text_confidenceQuestion.tStart = t  # local t and not account for scr refresh
            text_confidenceQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_confidenceQuestion, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_confidenceQuestion.status = STARTED
            text_confidenceQuestion.setAutoDraw(True)
        
        # if text_confidenceQuestion is active this frame...
        if text_confidenceQuestion.status == STARTED:
            # update params
            pass
        
        # *slider* updates
        
        # if slider is starting this frame...
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # update status
            slider.status = STARTED
            slider.setAutoDraw(True)
        
        # if slider is active this frame...
        if slider.status == STARTED:
            # update params
            pass
        # *buttonAdvance* updates
        
        # if buttonAdvance is starting this frame...
        if buttonAdvance.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            buttonAdvance.frameNStart = frameN  # exact frame index
            buttonAdvance.tStart = t  # local t and not account for scr refresh
            buttonAdvance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonAdvance, 'tStartRefresh')  # time at next scr refresh
            # update status
            buttonAdvance.status = STARTED
            win.callOnFlip(buttonAdvance.buttonClock.reset)
            buttonAdvance.setAutoDraw(True)
        
        # if buttonAdvance is active this frame...
        if buttonAdvance.status == STARTED:
            # update params
            pass
            # check whether buttonAdvance has been pressed
            if buttonAdvance.isClicked:
                if not buttonAdvance.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    buttonAdvance.timesOn.append(routineTimer.getTime())
                    buttonAdvance.timesOff.append(routineTimer.getTime())
                elif len(buttonAdvance.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    buttonAdvance.timesOff[-1] = routineTimer.getTime()
                if not buttonAdvance.wasClicked:
                    # end routine when buttonAdvance is clicked
                    continueRoutine = False
                if not buttonAdvance.wasClicked:
                    # run callback code when buttonAdvance is clicked
                    pass
        # take note of whether buttonAdvance was clicked, so that next frame we know if clicks are new
        buttonAdvance.wasClicked = buttonAdvance.isClicked and buttonAdvance.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=confidenceScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            confidenceScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidenceScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "confidenceScreen" ---
    for thisComponent in confidenceScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for confidenceScreen
    confidenceScreen.tStop = globalClock.getTime(format='float')
    confidenceScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('slider.response', slider.getRating())
    thisExp.addData('slider.rt', slider.getRT())
    thisExp.addData('slider.history', slider.getHistory())
    thisExp.nextEntry()
    # the Routine "confidenceScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "NextScreen" ---
    # create an object to store info about Routine NextScreen
    NextScreen = data.Routine(
        name='NextScreen',
        components=[textNextScreen, key_NextScreen],
    )
    NextScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_NextScreen
    key_NextScreen.keys = []
    key_NextScreen.rt = []
    _key_NextScreen_allKeys = []
    # store start times for NextScreen
    NextScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    NextScreen.tStart = globalClock.getTime(format='float')
    NextScreen.status = STARTED
    NextScreen.maxDuration = None
    # keep track of which components have finished
    NextScreenComponents = NextScreen.components
    for thisComponent in NextScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NextScreen" ---
    NextScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textNextScreen* updates
        
        # if textNextScreen is starting this frame...
        if textNextScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textNextScreen.frameNStart = frameN  # exact frame index
            textNextScreen.tStart = t  # local t and not account for scr refresh
            textNextScreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textNextScreen, 'tStartRefresh')  # time at next scr refresh
            # update status
            textNextScreen.status = STARTED
            textNextScreen.setAutoDraw(True)
        
        # if textNextScreen is active this frame...
        if textNextScreen.status == STARTED:
            # update params
            pass
        
        # *key_NextScreen* updates
        
        # if key_NextScreen is starting this frame...
        if key_NextScreen.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_NextScreen.frameNStart = frameN  # exact frame index
            key_NextScreen.tStart = t  # local t and not account for scr refresh
            key_NextScreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_NextScreen, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_NextScreen.status = STARTED
            # keyboard checking is just starting
            key_NextScreen.clock.reset()  # now t=0
        if key_NextScreen.status == STARTED:
            theseKeys = key_NextScreen.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_NextScreen_allKeys.extend(theseKeys)
            if len(_key_NextScreen_allKeys):
                key_NextScreen.keys = _key_NextScreen_allKeys[-1].name  # just the last key pressed
                key_NextScreen.rt = _key_NextScreen_allKeys[-1].rt
                key_NextScreen.duration = _key_NextScreen_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=NextScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            NextScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NextScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NextScreen" ---
    for thisComponent in NextScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for NextScreen
    NextScreen.tStop = globalClock.getTime(format='float')
    NextScreen.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "NextScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsGray_Color = data.TrialHandler2(
        name='trialsGray_Color',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('resources/hotel_color.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trialsGray_Color)  # add the loop to the experiment
    thisTrialsGray_Color = trialsGray_Color.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsGray_Color.rgb)
    if thisTrialsGray_Color != None:
        for paramName in thisTrialsGray_Color:
            globals()[paramName] = thisTrialsGray_Color[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrialsGray_Color in trialsGray_Color:
        trialsGray_Color.status = STARTED
        if hasattr(thisTrialsGray_Color, 'status'):
            thisTrialsGray_Color.status = STARTED
        currentLoop = trialsGray_Color
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsGray_Color.rgb)
        if thisTrialsGray_Color != None:
            for paramName in thisTrialsGray_Color:
                globals()[paramName] = thisTrialsGray_Color[paramName]
        
        # --- Prepare to start Routine "trialColor_Gray" ---
        # create an object to store info about Routine trialColor_Gray
        trialColor_Gray = data.Routine(
            name='trialColor_Gray',
            components=[divider_3, mouse_2, imageQuery_2, image1_2, image2_2, image3_2, image4_2, image5_2, toggle_button, queryCaption_GC],
        )
        trialColor_Gray.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_2
        mouse_2.x = []
        mouse_2.y = []
        mouse_2.leftButton = []
        mouse_2.midButton = []
        mouse_2.rightButton = []
        mouse_2.time = []
        mouse_2.clicked_name = []
        gotValidClick = False  # until a click is received
        mouse_2.mouseClock.reset()
        imageQuery_2.setImage(hotel_query)
        image1_2.setImage(choice1)
        image2_2.setImage(choice2)
        image3_2.setImage(choice3)
        image4_2.setImage(choice4)
        image5_2.setImage(choice5)
        # Run 'Begin Routine' code from toggleGray
        
        color_paths = [choice1, choice2, choice3, choice4, choice5]
        grayscale_paths = [gray1, gray2, gray3, gray4, gray5]
        
        toggle_button.toggleGray = False  # Set the toggle state ON the button object
        
        image1_2.setImage(color_paths[0])
        image2_2.setImage(color_paths[1])
        image3_2.setImage(color_paths[2])
        image4_2.setImage(color_paths[3])
        image5_2.setImage(color_paths[4])
        
        
        
        # reset toggle_button to account for continued clicks & clear times on/off
        toggle_button.reset()
        # store start times for trialColor_Gray
        trialColor_Gray.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trialColor_Gray.tStart = globalClock.getTime(format='float')
        trialColor_Gray.status = STARTED
        trialColor_Gray.maxDuration = None
        # keep track of which components have finished
        trialColor_GrayComponents = trialColor_Gray.components
        for thisComponent in trialColor_Gray.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialColor_Gray" ---
        trialColor_Gray.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrialsGray_Color, 'status') and thisTrialsGray_Color.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *divider_3* updates
            
            # if divider_3 is starting this frame...
            if divider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                divider_3.frameNStart = frameN  # exact frame index
                divider_3.tStart = t  # local t and not account for scr refresh
                divider_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(divider_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'divider_3.started')
                # update status
                divider_3.status = STARTED
                divider_3.setAutoDraw(True)
            
            # if divider_3 is active this frame...
            if divider_3.status == STARTED:
                # update params
                pass
            # *mouse_2* updates
            
            # if mouse_2 is starting this frame...
            if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_2.frameNStart = frameN  # exact frame index
                mouse_2.tStart = t  # local t and not account for scr refresh
                mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_2.status = STARTED
                prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([image1, image2, image3, image4, image5,], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_2):
                                gotValidClick = True
                                mouse_2.clicked_name.append(obj.name)
                                mouse_2.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse_2.getPos()
                            mouse_2.x.append(x)
                            mouse_2.y.append(y)
                            buttons = mouse_2.getPressed()
                            mouse_2.leftButton.append(buttons[0])
                            mouse_2.midButton.append(buttons[1])
                            mouse_2.rightButton.append(buttons[2])
                            mouse_2.time.append(mouse_2.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # *imageQuery_2* updates
            
            # if imageQuery_2 is starting this frame...
            if imageQuery_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imageQuery_2.frameNStart = frameN  # exact frame index
                imageQuery_2.tStart = t  # local t and not account for scr refresh
                imageQuery_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageQuery_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                imageQuery_2.status = STARTED
                imageQuery_2.setAutoDraw(True)
            
            # if imageQuery_2 is active this frame...
            if imageQuery_2.status == STARTED:
                # update params
                pass
            
            # *image1_2* updates
            
            # if image1_2 is starting this frame...
            if image1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image1_2.frameNStart = frameN  # exact frame index
                image1_2.tStart = t  # local t and not account for scr refresh
                image1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image1_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                image1_2.status = STARTED
                image1_2.setAutoDraw(True)
            
            # if image1_2 is active this frame...
            if image1_2.status == STARTED:
                # update params
                pass
            
            # *image2_2* updates
            
            # if image2_2 is starting this frame...
            if image2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image2_2.frameNStart = frameN  # exact frame index
                image2_2.tStart = t  # local t and not account for scr refresh
                image2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image2_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                image2_2.status = STARTED
                image2_2.setAutoDraw(True)
            
            # if image2_2 is active this frame...
            if image2_2.status == STARTED:
                # update params
                pass
            
            # *image3_2* updates
            
            # if image3_2 is starting this frame...
            if image3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image3_2.frameNStart = frameN  # exact frame index
                image3_2.tStart = t  # local t and not account for scr refresh
                image3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image3_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                image3_2.status = STARTED
                image3_2.setAutoDraw(True)
            
            # if image3_2 is active this frame...
            if image3_2.status == STARTED:
                # update params
                pass
            
            # *image4_2* updates
            
            # if image4_2 is starting this frame...
            if image4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image4_2.frameNStart = frameN  # exact frame index
                image4_2.tStart = t  # local t and not account for scr refresh
                image4_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image4_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                image4_2.status = STARTED
                image4_2.setAutoDraw(True)
            
            # if image4_2 is active this frame...
            if image4_2.status == STARTED:
                # update params
                pass
            
            # *image5_2* updates
            
            # if image5_2 is starting this frame...
            if image5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image5_2.frameNStart = frameN  # exact frame index
                image5_2.tStart = t  # local t and not account for scr refresh
                image5_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image5_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                image5_2.status = STARTED
                image5_2.setAutoDraw(True)
            
            # if image5_2 is active this frame...
            if image5_2.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from toggleGray
            
            clickable_objects = [image1_2, image2_2, image3_2, image4_2, image5_2]
            
            for obj in clickable_objects:
                if obj.contains(mouse) and mouse.getPressed()[0]:
                    clicked_img = obj.image  # This gives the filename like 'images/hotel2_sample4.png'
                    thisExp.addData("clicked_image", clicked_img)
                    thisExp.addData("correct_answer", correct_answer)
                    thisExp.addData("isCorrect", int(clicked_img == correct_answer))
                    continueRoutine = False
                    break
            
            # *toggle_button* updates
            
            # if toggle_button is starting this frame...
            if toggle_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                toggle_button.frameNStart = frameN  # exact frame index
                toggle_button.tStart = t  # local t and not account for scr refresh
                toggle_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(toggle_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                toggle_button.status = STARTED
                win.callOnFlip(toggle_button.buttonClock.reset)
                toggle_button.setAutoDraw(True)
            
            # if toggle_button is active this frame...
            if toggle_button.status == STARTED:
                # update params
                pass
                # check whether toggle_button has been pressed
                if toggle_button.isClicked:
                    if not toggle_button.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        toggle_button.timesOn.append(routineTimer.getTime())
                        toggle_button.timesOff.append(routineTimer.getTime())
                    elif len(toggle_button.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        toggle_button.timesOff[-1] = routineTimer.getTime()
                    if not toggle_button.wasClicked:
                        # run callback code when toggle_button is clicked
                        
                        toggle_button.toggleGray = not toggle_button.toggleGray
                        
                        if toggle_button.toggleGray:
                            image1_2.setImage(grayscale_paths[0])
                            image2_2.setImage(grayscale_paths[1])
                            image3_2.setImage(grayscale_paths[2])
                            image4_2.setImage(grayscale_paths[3])
                            image5_2.setImage(grayscale_paths[4])
                        
                             # Change button background color to darker to indicate grayscale
                            toggle_button.color = [0.5, 0.5, 0.5]  # RGB in 0–1 range (gray)
                        
                        else:
                            image1_2.setImage(color_paths[0])
                            image2_2.setImage(color_paths[1])
                            image3_2.setImage(color_paths[2])
                            image4_2.setImage(color_paths[3])
                            image5_2.setImage(color_paths[4])
                            
                           # Change button background back to lighter
                            toggle_button.color = [0.8, 0.8, 0.8]  # light gray
                            
            # take note of whether toggle_button was clicked, so that next frame we know if clicks are new
            toggle_button.wasClicked = toggle_button.isClicked and toggle_button.status == STARTED
            
            # *queryCaption_GC* updates
            
            # if queryCaption_GC is starting this frame...
            if queryCaption_GC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                queryCaption_GC.frameNStart = frameN  # exact frame index
                queryCaption_GC.tStart = t  # local t and not account for scr refresh
                queryCaption_GC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(queryCaption_GC, 'tStartRefresh')  # time at next scr refresh
                # update status
                queryCaption_GC.status = STARTED
                queryCaption_GC.setAutoDraw(True)
            
            # if queryCaption_GC is active this frame...
            if queryCaption_GC.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trialColor_Gray,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trialColor_Gray.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialColor_Gray.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialColor_Gray" ---
        for thisComponent in trialColor_Gray.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trialColor_Gray
        trialColor_Gray.tStop = globalClock.getTime(format='float')
        trialColor_Gray.tStopRefresh = tThisFlipGlobal
        # store data for trialsGray_Color (TrialHandler)
        trialsGray_Color.addData('mouse_2.x', mouse_2.x)
        trialsGray_Color.addData('mouse_2.y', mouse_2.y)
        trialsGray_Color.addData('mouse_2.leftButton', mouse_2.leftButton)
        trialsGray_Color.addData('mouse_2.midButton', mouse_2.midButton)
        trialsGray_Color.addData('mouse_2.rightButton', mouse_2.rightButton)
        trialsGray_Color.addData('mouse_2.time', mouse_2.time)
        trialsGray_Color.addData('mouse_2.clicked_name', mouse_2.clicked_name)
        trialsGray_Color.addData('toggle_button.numClicks', toggle_button.numClicks)
        if toggle_button.numClicks:
           trialsGray_Color.addData('toggle_button.timesOn', toggle_button.timesOn)
           trialsGray_Color.addData('toggle_button.timesOff', toggle_button.timesOff)
        else:
           trialsGray_Color.addData('toggle_button.timesOn', "")
           trialsGray_Color.addData('toggle_button.timesOff', "")
        # the Routine "trialColor_Gray" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[text],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrialsGray_Color, 'status') and thisTrialsGray_Color.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blank500,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisTrialsGray_Color as finished
        if hasattr(thisTrialsGray_Color, 'status'):
            thisTrialsGray_Color.status = FINISHED
        # if awaiting a pause, pause now
        if trialsGray_Color.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trialsGray_Color.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialsGray_Color'
    trialsGray_Color.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "confidenceScreen" ---
    # create an object to store info about Routine confidenceScreen
    confidenceScreen = data.Routine(
        name='confidenceScreen',
        components=[text_confidenceQuestion, slider, buttonAdvance],
    )
    confidenceScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    slider.reset()
    # reset buttonAdvance to account for continued clicks & clear times on/off
    buttonAdvance.reset()
    # store start times for confidenceScreen
    confidenceScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    confidenceScreen.tStart = globalClock.getTime(format='float')
    confidenceScreen.status = STARTED
    confidenceScreen.maxDuration = None
    # keep track of which components have finished
    confidenceScreenComponents = confidenceScreen.components
    for thisComponent in confidenceScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "confidenceScreen" ---
    confidenceScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_confidenceQuestion* updates
        
        # if text_confidenceQuestion is starting this frame...
        if text_confidenceQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_confidenceQuestion.frameNStart = frameN  # exact frame index
            text_confidenceQuestion.tStart = t  # local t and not account for scr refresh
            text_confidenceQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_confidenceQuestion, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_confidenceQuestion.status = STARTED
            text_confidenceQuestion.setAutoDraw(True)
        
        # if text_confidenceQuestion is active this frame...
        if text_confidenceQuestion.status == STARTED:
            # update params
            pass
        
        # *slider* updates
        
        # if slider is starting this frame...
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # update status
            slider.status = STARTED
            slider.setAutoDraw(True)
        
        # if slider is active this frame...
        if slider.status == STARTED:
            # update params
            pass
        # *buttonAdvance* updates
        
        # if buttonAdvance is starting this frame...
        if buttonAdvance.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            buttonAdvance.frameNStart = frameN  # exact frame index
            buttonAdvance.tStart = t  # local t and not account for scr refresh
            buttonAdvance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonAdvance, 'tStartRefresh')  # time at next scr refresh
            # update status
            buttonAdvance.status = STARTED
            win.callOnFlip(buttonAdvance.buttonClock.reset)
            buttonAdvance.setAutoDraw(True)
        
        # if buttonAdvance is active this frame...
        if buttonAdvance.status == STARTED:
            # update params
            pass
            # check whether buttonAdvance has been pressed
            if buttonAdvance.isClicked:
                if not buttonAdvance.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    buttonAdvance.timesOn.append(routineTimer.getTime())
                    buttonAdvance.timesOff.append(routineTimer.getTime())
                elif len(buttonAdvance.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    buttonAdvance.timesOff[-1] = routineTimer.getTime()
                if not buttonAdvance.wasClicked:
                    # end routine when buttonAdvance is clicked
                    continueRoutine = False
                if not buttonAdvance.wasClicked:
                    # run callback code when buttonAdvance is clicked
                    pass
        # take note of whether buttonAdvance was clicked, so that next frame we know if clicks are new
        buttonAdvance.wasClicked = buttonAdvance.isClicked and buttonAdvance.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=confidenceScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            confidenceScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidenceScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "confidenceScreen" ---
    for thisComponent in confidenceScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for confidenceScreen
    confidenceScreen.tStop = globalClock.getTime(format='float')
    confidenceScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('slider.response', slider.getRating())
    thisExp.addData('slider.rt', slider.getRT())
    thisExp.addData('slider.history', slider.getHistory())
    thisExp.nextEntry()
    # the Routine "confidenceScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EndScreen" ---
    # create an object to store info about Routine EndScreen
    EndScreen = data.Routine(
        name='EndScreen',
        components=[textEndMessage],
    )
    EndScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for EndScreen
    EndScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EndScreen.tStart = globalClock.getTime(format='float')
    EndScreen.status = STARTED
    EndScreen.maxDuration = None
    # keep track of which components have finished
    EndScreenComponents = EndScreen.components
    for thisComponent in EndScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndScreen" ---
    EndScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textEndMessage* updates
        
        # if textEndMessage is starting this frame...
        if textEndMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEndMessage.frameNStart = frameN  # exact frame index
            textEndMessage.tStart = t  # local t and not account for scr refresh
            textEndMessage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEndMessage, 'tStartRefresh')  # time at next scr refresh
            # update status
            textEndMessage.status = STARTED
            textEndMessage.setAutoDraw(True)
        
        # if textEndMessage is active this frame...
        if textEndMessage.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=EndScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EndScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndScreen" ---
    for thisComponent in EndScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EndScreen
    EndScreen.tStop = globalClock.getTime(format='float')
    EndScreen.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
