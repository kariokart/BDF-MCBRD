#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on September 30, 2020, at 13:55
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'BDF MCBRD'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Kari\\Downloads\\dynamic_selective_inspect-master (1)\\dynamic_selective_inspect-master\\BDF MCBRD_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='View picture stories by using your mouse to reveal detailed information in each image.\n\nUse the space bar to proceed to the next image.\n\n\nPress space to begin.',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
#import all libraries for experiment
from PIL import Image, ImageDraw
import win32api

#get window size
xwin, ywin = win.size

#find image location on screen
#(image is displayed at 1024x768 at the center
#of the screen, regardless of individual screen size)
#image dimensions start at the top left corner
imageStartX = (xwin / 2) - 512
imageStartY = (ywin / 2) - 384

#write participant's screen dimensions,
#the starting location of the 1024x768 BDF image,
#and column names at beginning of output file
#   note, if there is already content in this output file,
#   this code will begin writing after the previous content.
#   multiple runs can be viewed in the same file.
outfile = open('FixatedLocations.txt','a')
outfile.write('BEGIN EXPERIMENT')
outfile.write('\nWindow dimensions: ')
outfile.write('%s  %s\n' % (str(xwin),str(ywin)))
outfile.write('Image top left corner: ')
outfile.write('%s  %s\n' % (str(imageStartX),str(imageStartY)))
outfile.write('Begin mouse recording... \n')
#Column names:
#Img = image number
#OriX, OriY = original mouse position on the participant's screen
#   note, positions outside BDF edges displayed as the edge value,
#   as the nonblurred circle will not go past the image dimensions.
#ImgX, ImgY = mouse position relative to the 1024x768 dimensions
#   of the BDF image. Consider these dimensions standardized across
#   participants.
outfile.write('Img\tOriX\tOriY\tImgX\tImgY\n')
outfile.close()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
imageStimulus = visual.ImageStim(
    win=win,
    name='imageStimulus', units='norm', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
imageAperture = visual.ImageStim(
    win=win,
    name='imageAperture', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='All done! Thank you!',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text, mouse_2, key_resp_2]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ImageList.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [mouse, imageStimulus, imageAperture, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #get mouse position
        mousePos = win32api.GetCursorPos()
        xpixel = mousePos[0]
        ypixel = mousePos[1]
        
        #open output file
        outfile = open('FixatedLocations.txt','a')
        
        #limit mouse location reporting to image dimensions
        if xpixel < imageStartX:
            xpixel = imageStartX
        #    outfile.write('out of bounds')
        elif xpixel > (imageStartX + 1024):
            xpixel = (imageStartX + 1024)
        #    outfile.write('out of bounds')
        if ypixel < imageStartY:
            ypixel = imageStartY
        #    outfile.write('out of bounds')
        elif ypixel > (imageStartY + 768):
            ypixel = (imageStartY + 768)
        #    outfile.write('out of bounds')
        
        #write image number to output file
        imageNumber = OriginalImage.replace('images/','')
        imageNumber = imageNumber.replace('.bmp','')
        outfile.write(imageNumber)
        #write mouse location on participant's screen
        outfile.write('\t%s\t%s\t' % (str(xpixel),str(ypixel)))
        
        #open the input image as numpy array, convert to RGB
        img=Image.open(OriginalImage).convert("RGB")
        npImage=np.array(img)
        
        #create same size alpha layer with circle
        alpha = Image.new('L', img.size,0)
        draw = ImageDraw.Draw(alpha)
        
        #determine mouse location relative to image dimensions,
        #and use these to display nonblurred circle
        xpixelOnImage = xpixel- imageStartX
        ypixelOnImage = ypixel- imageStartY
        #output the values used to display nonblurred circle
        outfile.write('%s\t%s\n' % (str(xpixelOnImage),str(ypixelOnImage)))
        #draw circle on alpha layer, using pixel locations -/+ the radius
        #of the circle
        draw.pieslice([(xpixelOnImage - 50),(ypixelOnImage -50),(xpixelOnImage +50),(ypixelOnImage +50)],0,360,fill=255)
        #close output file
        outfile.close()
        
        #convert alpha Image to numpy array
        npAlpha=np.array(alpha)
        
        #add alpha layer to RGB
        npImage=np.dstack((npImage,npAlpha))
        
        #save with alpha
        Image.fromarray(npImage).save('images/result.png')
        # *mouse* updates
        if mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            x, y = mouse.getPos()
            mouse.x.append(x)
            mouse.y.append(y)
            buttons = mouse.getPressed()
            mouse.leftButton.append(buttons[0])
            mouse.midButton.append(buttons[1])
            mouse.rightButton.append(buttons[2])
            mouse.time.append(mouse.mouseClock.getTime())
        
        # *imageStimulus* updates
        if imageStimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageStimulus.frameNStart = frameN  # exact frame index
            imageStimulus.tStart = t  # local t and not account for scr refresh
            imageStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageStimulus, 'tStartRefresh')  # time at next scr refresh
            imageStimulus.setAutoDraw(True)
        if imageStimulus.status == STARTED:  # only update if drawing
            imageStimulus.setImage(BlurredImage, log=False)
        
        # *imageAperture* updates
        if imageAperture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageAperture.frameNStart = frameN  # exact frame index
            imageAperture.tStart = t  # local t and not account for scr refresh
            imageAperture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageAperture, 'tStartRefresh')  # time at next scr refresh
            imageAperture.setAutoDraw(True)
        if imageAperture.status == STARTED:  # only update if drawing
            imageAperture.setPos((0,0), log=False)
            imageAperture.setImage('images/result.png', log=False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    trials.addData('mouse.started', mouse.tStartRefresh)
    trials.addData('mouse.stopped', mouse.tStopRefresh)
    trials.addData('imageStimulus.started', imageStimulus.tStartRefresh)
    trials.addData('imageStimulus.stopped', imageStimulus.tStopRefresh)
    trials.addData('imageAperture.started', imageAperture.tStartRefresh)
    trials.addData('imageAperture.stopped', imageAperture.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
gotValidClick = False  # until a click is received
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
EndComponents = [text_2, mouse_3, key_resp_3]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    # *mouse_3* updates
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
