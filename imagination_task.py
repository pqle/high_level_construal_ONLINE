#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on March 31, 2021, at 14:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'imagination_task'  # from the Builder filename that created this script
expInfo = {'workerId': '', 'assignmentId': '', 'hitId': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['workerId'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Phuong\\OneDrive - The Ohio State University\\Fujita Lab\\Experiments\\Berkman smoking pilot SU19\\Scanner task pilot SP21\\Pilot Github Materials\\high_level_construal\\imagination_task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
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

# Initialize components for Routine "setup"
setupClock = core.Clock()
conditions_file_name = os.path.join('conditions', 'choose_condition.csv')
#is_first = False

#if is_first:
#    start_text_str = 'Calibrating scanner'
start_text_duration = 120
#    end_text_str = 'The task has ended. The next task will start in a few seconds.'
end_text_duration = 10
#else:
#    start_text_str = ''
#    start_text_duration = 0.1
#    end_text_str = 'The task has ended. Waiting for researcher to start next task.'
#    end_text_duration = 120

# session 0 is a practice session
#if expInfo['session'] == '0':
#    conditions_file_name = os.path.join('conditions', 'choose_condition_practice.csv')
#    scenario_trials_selection = [0]
#    action_trials_selection = [0, 1, 2]
#    start_text_str = 'Practice for construal level task'

rating_keys = ['5', '6', '7', '8', '9']

def convert_key_to_rating(key):
    rating = None
    if key in rating_keys:
        rating = int(key)
        rating = rating - 4

    return rating

import random
MturkNUMCODE = random.randint(0, 999999999)
MturkCODE = "Your Mturk completion code is: " + str(MturkNUMCODE) + ". Please press the space bar to ensure your survey response is recorded. Thank you!"

expInfo['MturkCODE'] = MturkNUMCODE

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text='IMPORTANT: You should respond to questions through out this task by pressing the "5, 6, 7, 8, 9" buttons.\n\nWhen you are ready, press the space bar to continue.',
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "block_setup"
block_setupClock = core.Clock()

# Initialize components for Routine "cue"
cueClock = core.Clock()
cue_str = visual.TextStim(win=win, name='cue_str',
    text='',
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "action"
actionClock = core.Clock()
action_text = visual.TextStim(win=win, name='action_text',
    text='',
    font='Helvetica',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
attention_check = visual.TextStim(win=win, name='attention_check',
    text='',
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
attention_check_rating = visual.Slider(win=win, name='attention_check_rating',
    size=(1.0, 0.025), pos=(0, -0.3), units=None,
    labels=['not at all\noften', 'somewhat\noften', 'moderately\noften', 'very\noften', 'extremely\noften'], ticks=(1, 2, 3, 4, 5), granularity=0,
    style='rating', styleTweaks=('triangleMarker',), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Helvetica', labelHeight=0.03,
    flip=False, depth=-3, readOnly=False)
attention_check_keyboard = keyboard.Keyboard()

# Initialize components for Routine "scenario_cue"
scenario_cueClock = core.Clock()
scenario_cue_text = visual.TextStim(win=win, name='scenario_cue_text',
    text='',
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "scenario1"
scenario1Clock = core.Clock()
block1_text = visual.TextStim(win=win, name='block1_text',
    text='',
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
block1_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='block1_sound')
block1_sound.setVolume(1)

# Initialize components for Routine "scenario2"
scenario2Clock = core.Clock()
block2_text = visual.TextStim(win=win, name='block2_text',
    text='',
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
block2_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='block2_sound')
block2_sound.setVolume(1)

# Initialize components for Routine "scenario3"
scenario3Clock = core.Clock()
block3_text = visual.TextStim(win=win, name='block3_text',
    text='',
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
block3_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='block3_sound')
block3_sound.setVolume(1)

# Initialize components for Routine "quitting_intention"
quitting_intentionClock = core.Clock()
quitting_intention_text = visual.TextStim(win=win, name='quitting_intention_text',
    text='',
    font='Helvetica',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
quitting_intention_rating = visual.Slider(win=win, name='quitting_intention_rating',
    size=(1.0, 0.025), pos=(0, -0.3), units=None,
    labels=['encourage\na great deal','encourage\na little','neither encourage\nnor discourage','discourage\na little','discourage\na great deal'], ticks=(1, 2, 3, 4, 5), granularity=0,
    style='rating', styleTweaks=('triangleMarker',), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Helvetica', labelHeight=0.03,
    flip=False, depth=-2, readOnly=False)
quitting_intention_keyboard = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
debrief_text1 = visual.TextStim(win=win, name='debrief_text1',
    text='The next pages provide information about the purpose of this survey. After reviewing this information to your satisfaction, you will receive a code to submit your survey response. Thank you!\n\nPress the space bar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_key_resp = keyboard.Keyboard()

# Initialize components for Routine "end2"
end2Clock = core.Clock()
debrief_text1_2 = visual.TextStim(win=win, name='debrief_text1_2',
    text='Thank you for your participation! We are examining the influence of mental representations on how people behave in situations requiring self-control.  For example, in previous experiments in our lab, we found that mental representations that cause people to think more globally and "big picture" (high-level construals) lead to greater self-control as compared to representations that cause thinking in a more local, "seeing the trees instead of the forest" manner (low-level construals).\n\nPress the space bar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "end3"
end3Clock = core.Clock()
debrief_text1_3 = visual.TextStim(win=win, name='debrief_text1_3',
    text='In this study, you completed tasks designed to evoke either a high-level or low-level mindset. You then answered a variety of questions about your behavioral description preferences. We expect that the condition you were assigned to may have impacted some of the answers you provided. \n\nPress the space bar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "end4"
end4Clock = core.Clock()
debrief_text1_4 = visual.TextStim(win=win, name='debrief_text1_4',
    text='Your data will remain confidential. Data are kept in locked areas. Your de-identified information may be used or shared with other researchers without your additional informed consent. If you have any questions about this study, please contact Kentaro Fujita (fujita.5@osu.edu).  If you have questions or concerns about your rights as a research participant, contact Sandra Meadows at The Office of Responsible Research Practices, 1-800-678-6251 or 1-614-688-4792 (see also their website at http://www.orrp.osu.edu/).\n\nPress the space bar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Mturk_Completion_Code"
Mturk_Completion_CodeClock = core.Clock()
complete_code = visual.TextStim(win=win, name='complete_code',
    text=MturkCODE,
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_key_resp_5 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instruction, key_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    if instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instruction.tStartRefresh + start_text_duration-frameTolerance:
            # keep track of stop time/frame for later
            instruction.tStop = t  # not accounting for scr refresh
            instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instruction, 'tStopRefresh')  # time at next scr refresh
            instruction.setAutoDraw(False)
    
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
    if key_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp.tStartRefresh + start_text_duration-frameTolerance:
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
            key_resp.status = FINISHED
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(conditions_file_name),
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block_setup"-------
    continueRoutine = True
    # update component parameters for each repeat
    scenario_trials_selection = randint(low=0,high=15,size=1)
    action_trials_selection = randint(low=0,high=47,size=3)
    # keep track of which components have finished
    block_setupComponents = []
    for thisComponent in block_setupComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_setup"-------
    while continueRoutine:
        # get current time
        t = block_setupClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_setupClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_setupComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_setup"-------
    for thisComponent in block_setupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "block_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    scenario_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(scenario_file, selection=scenario_trials_selection),
        seed=None, name='scenario_trials')
    thisExp.addLoop(scenario_trials)  # add the loop to the experiment
    thisScenario_trial = scenario_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisScenario_trial.rgb)
    if thisScenario_trial != None:
        for paramName in thisScenario_trial:
            exec('{} = thisScenario_trial[paramName]'.format(paramName))
    
    for thisScenario_trial in scenario_trials:
        currentLoop = scenario_trials
        # abbreviate parameter names if possible (e.g. rgb = thisScenario_trial.rgb)
        if thisScenario_trial != None:
            for paramName in thisScenario_trial:
                exec('{} = thisScenario_trial[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        action_trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions/action_conditions.csv', selection=action_trials_selection),
            seed=None, name='action_trials')
        thisExp.addLoop(action_trials)  # add the loop to the experiment
        thisAction_trial = action_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAction_trial.rgb)
        if thisAction_trial != None:
            for paramName in thisAction_trial:
                exec('{} = thisAction_trial[paramName]'.format(paramName))
        
        for thisAction_trial in action_trials:
            currentLoop = action_trials
            # abbreviate parameter names if possible (e.g. rgb = thisAction_trial.rgb)
            if thisAction_trial != None:
                for paramName in thisAction_trial:
                    exec('{} = thisAction_trial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "cue"-------
            continueRoutine = True
            routineTimer.add(4.000000)
            # update component parameters for each repeat
            cue_str.setText("Please imagine the next events occurring " + cue_text)
            # keep track of which components have finished
            cueComponents = [cue_str]
            for thisComponent in cueComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "cue"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cueClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=cueClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cue_str* updates
                if cue_str.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cue_str.frameNStart = frameN  # exact frame index
                    cue_str.tStart = t  # local t and not account for scr refresh
                    cue_str.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cue_str, 'tStartRefresh')  # time at next scr refresh
                    cue_str.setAutoDraw(True)
                if cue_str.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cue_str.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        cue_str.tStop = t  # not accounting for scr refresh
                        cue_str.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(cue_str, 'tStopRefresh')  # time at next scr refresh
                        cue_str.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cueComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "cue"-------
            for thisComponent in cueComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            action_trials.addData('cue_str.started', cue_str.tStartRefresh)
            action_trials.addData('cue_str.stopped', cue_str.tStopRefresh)
            
            # ------Prepare to start Routine "action"-------
            continueRoutine = True
            routineTimer.add(5.000000)
            # update component parameters for each repeat
            if condition_type == 'present':
                attention_check_text = 'How often do you currently engage in this action?'
            else:
                attention_check_text = 'How likely would you engage in this action five years from now?'
            action_text.setText(action)
            attention_check.setText(attention_check_text)
            attention_check_rating.reset()
            attention_check_keyboard.keys = []
            attention_check_keyboard.rt = []
            _attention_check_keyboard_allKeys = []
            # keep track of which components have finished
            actionComponents = [action_text, attention_check, attention_check_rating, attention_check_keyboard]
            for thisComponent in actionComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            actionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "action"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = actionClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=actionClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Update marker position and slider rating
                # when there are keypresses of the rating buttons
                r = convert_key_to_rating(attention_check_keyboard.keys)
                attention_check_rating.markerPos = r
                # confirm rating by setting to current markerPos
                attention_check_rating.rating = r
                
                
                # *action_text* updates
                if action_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    action_text.frameNStart = frameN  # exact frame index
                    action_text.tStart = t  # local t and not account for scr refresh
                    action_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(action_text, 'tStartRefresh')  # time at next scr refresh
                    action_text.setAutoDraw(True)
                if action_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > action_text.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        action_text.tStop = t  # not accounting for scr refresh
                        action_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(action_text, 'tStopRefresh')  # time at next scr refresh
                        action_text.setAutoDraw(False)
                
                # *attention_check* updates
                if attention_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    attention_check.frameNStart = frameN  # exact frame index
                    attention_check.tStart = t  # local t and not account for scr refresh
                    attention_check.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(attention_check, 'tStartRefresh')  # time at next scr refresh
                    attention_check.setAutoDraw(True)
                if attention_check.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > attention_check.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        attention_check.tStop = t  # not accounting for scr refresh
                        attention_check.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(attention_check, 'tStopRefresh')  # time at next scr refresh
                        attention_check.setAutoDraw(False)
                
                # *attention_check_rating* updates
                if attention_check_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    attention_check_rating.frameNStart = frameN  # exact frame index
                    attention_check_rating.tStart = t  # local t and not account for scr refresh
                    attention_check_rating.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(attention_check_rating, 'tStartRefresh')  # time at next scr refresh
                    attention_check_rating.setAutoDraw(True)
                if attention_check_rating.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > attention_check_rating.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        attention_check_rating.tStop = t  # not accounting for scr refresh
                        attention_check_rating.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(attention_check_rating, 'tStopRefresh')  # time at next scr refresh
                        attention_check_rating.setAutoDraw(False)
                
                # *attention_check_keyboard* updates
                waitOnFlip = False
                if attention_check_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    attention_check_keyboard.frameNStart = frameN  # exact frame index
                    attention_check_keyboard.tStart = t  # local t and not account for scr refresh
                    attention_check_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(attention_check_keyboard, 'tStartRefresh')  # time at next scr refresh
                    attention_check_keyboard.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(attention_check_keyboard.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(attention_check_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if attention_check_keyboard.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > attention_check_keyboard.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        attention_check_keyboard.tStop = t  # not accounting for scr refresh
                        attention_check_keyboard.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(attention_check_keyboard, 'tStopRefresh')  # time at next scr refresh
                        attention_check_keyboard.status = FINISHED
                if attention_check_keyboard.status == STARTED and not waitOnFlip:
                    theseKeys = attention_check_keyboard.getKeys(keyList=['5', '6', '7', '8', '9'], waitRelease=False)
                    _attention_check_keyboard_allKeys.extend(theseKeys)
                    if len(_attention_check_keyboard_allKeys):
                        attention_check_keyboard.keys = _attention_check_keyboard_allKeys[-1].name  # just the last key pressed
                        attention_check_keyboard.rt = _attention_check_keyboard_allKeys[-1].rt
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in actionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "action"-------
            for thisComponent in actionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            action_trials.addData('attention_check_rating.response', attention_check_rating.getRating())
            action_trials.addData('attention_check_rating.rt', attention_check_rating.getRT())
            action_trials.addData('attention_check_rating.started', attention_check_rating.tStartRefresh)
            action_trials.addData('attention_check_rating.stopped', attention_check_rating.tStopRefresh)
            # check responses
            if attention_check_keyboard.keys in ['', [], None]:  # No response was made
                attention_check_keyboard.keys = None
            action_trials.addData('attention_check_keyboard.keys',attention_check_keyboard.keys)
            if attention_check_keyboard.keys != None:  # we had a response
                action_trials.addData('attention_check_keyboard.rt', attention_check_keyboard.rt)
            action_trials.addData('attention_check_keyboard.started', attention_check_keyboard.tStartRefresh)
            action_trials.addData('attention_check_keyboard.stopped', attention_check_keyboard.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'action_trials'
        
        # get names of stimulus parameters
        if action_trials.trialList in ([], [None], None):
            params = []
        else:
            params = action_trials.trialList[0].keys()
        # save data for this loop
        action_trials.saveAsExcel(filename + '.xlsx', sheetName='action_trials',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "scenario_cue"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        scenario_cue_text.setText("Please imagine the next events occurring " + cue_text)
        # keep track of which components have finished
        scenario_cueComponents = [scenario_cue_text]
        for thisComponent in scenario_cueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        scenario_cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "scenario_cue"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = scenario_cueClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=scenario_cueClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *scenario_cue_text* updates
            if scenario_cue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                scenario_cue_text.frameNStart = frameN  # exact frame index
                scenario_cue_text.tStart = t  # local t and not account for scr refresh
                scenario_cue_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(scenario_cue_text, 'tStartRefresh')  # time at next scr refresh
                scenario_cue_text.setAutoDraw(True)
            if scenario_cue_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > scenario_cue_text.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    scenario_cue_text.tStop = t  # not accounting for scr refresh
                    scenario_cue_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(scenario_cue_text, 'tStopRefresh')  # time at next scr refresh
                    scenario_cue_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in scenario_cueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "scenario_cue"-------
        for thisComponent in scenario_cueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "scenario1"-------
        continueRoutine = True
        # update component parameters for each repeat
        block1_text.setText(block1)
        block1_sound.setSound(block1_audio, hamming=True)
        block1_sound.setVolume(1, log=False)
        # keep track of which components have finished
        scenario1Components = [block1_text, block1_sound]
        for thisComponent in scenario1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        scenario1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "scenario1"-------
        while continueRoutine:
            # get current time
            t = scenario1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=scenario1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *block1_text* updates
            if block1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block1_text.frameNStart = frameN  # exact frame index
                block1_text.tStart = t  # local t and not account for scr refresh
                block1_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block1_text, 'tStartRefresh')  # time at next scr refresh
                block1_text.setAutoDraw(True)
            if block1_text.status == STARTED:
                if bool(block1_sound.status==FINISHED):
                    # keep track of stop time/frame for later
                    block1_text.tStop = t  # not accounting for scr refresh
                    block1_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block1_text, 'tStopRefresh')  # time at next scr refresh
                    block1_text.setAutoDraw(False)
            # start/stop block1_sound
            if block1_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block1_sound.frameNStart = frameN  # exact frame index
                block1_sound.tStart = t  # local t and not account for scr refresh
                block1_sound.tStartRefresh = tThisFlipGlobal  # on global time
                block1_sound.play(when=win)  # sync with win flip
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in scenario1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "scenario1"-------
        for thisComponent in scenario1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1_sound.stop()  # ensure sound has stopped at end of routine
        scenario_trials.addData('block1_sound.started', block1_sound.tStartRefresh)
        scenario_trials.addData('block1_sound.stopped', block1_sound.tStopRefresh)
        # the Routine "scenario1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "scenario2"-------
        continueRoutine = True
        # update component parameters for each repeat
        block2_text.setText(block2)
        block2_sound.setSound(block2_audio, hamming=True)
        block2_sound.setVolume(1, log=False)
        # keep track of which components have finished
        scenario2Components = [block2_text, block2_sound]
        for thisComponent in scenario2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        scenario2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "scenario2"-------
        while continueRoutine:
            # get current time
            t = scenario2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=scenario2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *block2_text* updates
            if block2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block2_text.frameNStart = frameN  # exact frame index
                block2_text.tStart = t  # local t and not account for scr refresh
                block2_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block2_text, 'tStartRefresh')  # time at next scr refresh
                block2_text.setAutoDraw(True)
            if block2_text.status == STARTED:
                if bool(block2_sound.status==FINISHED):
                    # keep track of stop time/frame for later
                    block2_text.tStop = t  # not accounting for scr refresh
                    block2_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block2_text, 'tStopRefresh')  # time at next scr refresh
                    block2_text.setAutoDraw(False)
            # start/stop block2_sound
            if block2_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block2_sound.frameNStart = frameN  # exact frame index
                block2_sound.tStart = t  # local t and not account for scr refresh
                block2_sound.tStartRefresh = tThisFlipGlobal  # on global time
                block2_sound.play(when=win)  # sync with win flip
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in scenario2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "scenario2"-------
        for thisComponent in scenario2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2_sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "scenario2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "scenario3"-------
        continueRoutine = True
        # update component parameters for each repeat
        block3_text.setText(block3)
        block3_sound.setSound(block3_audio, hamming=True)
        block3_sound.setVolume(1, log=False)
        # keep track of which components have finished
        scenario3Components = [block3_text, block3_sound]
        for thisComponent in scenario3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        scenario3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "scenario3"-------
        while continueRoutine:
            # get current time
            t = scenario3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=scenario3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *block3_text* updates
            if block3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block3_text.frameNStart = frameN  # exact frame index
                block3_text.tStart = t  # local t and not account for scr refresh
                block3_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block3_text, 'tStartRefresh')  # time at next scr refresh
                block3_text.setAutoDraw(True)
            if block3_text.status == STARTED:
                if bool(block3_sound.status==FINISHED):
                    # keep track of stop time/frame for later
                    block3_text.tStop = t  # not accounting for scr refresh
                    block3_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(block3_text, 'tStopRefresh')  # time at next scr refresh
                    block3_text.setAutoDraw(False)
            # start/stop block3_sound
            if block3_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block3_sound.frameNStart = frameN  # exact frame index
                block3_sound.tStart = t  # local t and not account for scr refresh
                block3_sound.tStartRefresh = tThisFlipGlobal  # on global time
                block3_sound.play(when=win)  # sync with win flip
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in scenario3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "scenario3"-------
        for thisComponent in scenario3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        scenario_trials.addData('block3_text.started', block3_text.tStartRefresh)
        scenario_trials.addData('block3_text.stopped', block3_text.tStopRefresh)
        block3_sound.stop()  # ensure sound has stopped at end of routine
        scenario_trials.addData('block3_sound.started', block3_sound.tStartRefresh)
        scenario_trials.addData('block3_sound.stopped', block3_sound.tStopRefresh)
        # the Routine "scenario3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "quitting_intention"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        if condition_type == 'present':
            quitting_intention_str = 'Consider the thoughts that would go through your mind if you were in this situation right now.\n\nTo what extent do these thoughts encourage or discourage you to smoke?'
        else:
            quitting_intention_str = 'Consider the thoughts that would go through your mind if you are in this situation five years from now.\n\nTo what extent do these thoughts encourage or discourage you to smoke?'
        quitting_intention_text.setText(quitting_intention_str)
        quitting_intention_rating.reset()
        quitting_intention_keyboard.keys = []
        quitting_intention_keyboard.rt = []
        _quitting_intention_keyboard_allKeys = []
        # keep track of which components have finished
        quitting_intentionComponents = [quitting_intention_text, quitting_intention_rating, quitting_intention_keyboard]
        for thisComponent in quitting_intentionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        quitting_intentionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "quitting_intention"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = quitting_intentionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=quitting_intentionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Update marker position and slider rating
            # when there are keypresses of the rating buttons
            r = convert_key_to_rating(quitting_intention_keyboard.keys)
            quitting_intention_rating.markerPos = r
            # confirm rating by setting to current markerPos
            quitting_intention_rating.rating = r
            
            
            # *quitting_intention_text* updates
            if quitting_intention_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                quitting_intention_text.frameNStart = frameN  # exact frame index
                quitting_intention_text.tStart = t  # local t and not account for scr refresh
                quitting_intention_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(quitting_intention_text, 'tStartRefresh')  # time at next scr refresh
                quitting_intention_text.setAutoDraw(True)
            if quitting_intention_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > quitting_intention_text.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    quitting_intention_text.tStop = t  # not accounting for scr refresh
                    quitting_intention_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(quitting_intention_text, 'tStopRefresh')  # time at next scr refresh
                    quitting_intention_text.setAutoDraw(False)
            
            # *quitting_intention_rating* updates
            if quitting_intention_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                quitting_intention_rating.frameNStart = frameN  # exact frame index
                quitting_intention_rating.tStart = t  # local t and not account for scr refresh
                quitting_intention_rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(quitting_intention_rating, 'tStartRefresh')  # time at next scr refresh
                quitting_intention_rating.setAutoDraw(True)
            if quitting_intention_rating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > quitting_intention_rating.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    quitting_intention_rating.tStop = t  # not accounting for scr refresh
                    quitting_intention_rating.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(quitting_intention_rating, 'tStopRefresh')  # time at next scr refresh
                    quitting_intention_rating.setAutoDraw(False)
            
            # *quitting_intention_keyboard* updates
            waitOnFlip = False
            if quitting_intention_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                quitting_intention_keyboard.frameNStart = frameN  # exact frame index
                quitting_intention_keyboard.tStart = t  # local t and not account for scr refresh
                quitting_intention_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(quitting_intention_keyboard, 'tStartRefresh')  # time at next scr refresh
                quitting_intention_keyboard.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(quitting_intention_keyboard.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(quitting_intention_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if quitting_intention_keyboard.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > quitting_intention_keyboard.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    quitting_intention_keyboard.tStop = t  # not accounting for scr refresh
                    quitting_intention_keyboard.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(quitting_intention_keyboard, 'tStopRefresh')  # time at next scr refresh
                    quitting_intention_keyboard.status = FINISHED
            if quitting_intention_keyboard.status == STARTED and not waitOnFlip:
                theseKeys = quitting_intention_keyboard.getKeys(keyList=['5', '6', '7', '8', '9'], waitRelease=False)
                _quitting_intention_keyboard_allKeys.extend(theseKeys)
                if len(_quitting_intention_keyboard_allKeys):
                    quitting_intention_keyboard.keys = _quitting_intention_keyboard_allKeys[-1].name  # just the last key pressed
                    quitting_intention_keyboard.rt = _quitting_intention_keyboard_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in quitting_intentionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "quitting_intention"-------
        for thisComponent in quitting_intentionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        scenario_trials.addData('quitting_intention_rating.response', quitting_intention_rating.getRating())
        scenario_trials.addData('quitting_intention_rating.rt', quitting_intention_rating.getRT())
        scenario_trials.addData('quitting_intention_rating.started', quitting_intention_rating.tStartRefresh)
        scenario_trials.addData('quitting_intention_rating.stopped', quitting_intention_rating.tStopRefresh)
        # check responses
        if quitting_intention_keyboard.keys in ['', [], None]:  # No response was made
            quitting_intention_keyboard.keys = None
        scenario_trials.addData('quitting_intention_keyboard.keys',quitting_intention_keyboard.keys)
        if quitting_intention_keyboard.keys != None:  # we had a response
            scenario_trials.addData('quitting_intention_keyboard.rt', quitting_intention_keyboard.rt)
        scenario_trials.addData('quitting_intention_keyboard.started', quitting_intention_keyboard.tStartRefresh)
        scenario_trials.addData('quitting_intention_keyboard.stopped', quitting_intention_keyboard.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'scenario_trials'
    
    # get names of stimulus parameters
    if scenario_trials.trialList in ([], [None], None):
        params = []
    else:
        params = scenario_trials.trialList[0].keys()
    # save data for this loop
    scenario_trials.saveAsExcel(filename + '.xlsx', sheetName='scenario_trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'block'

# get names of stimulus parameters
if block.trialList in ([], [None], None):
    params = []
else:
    params = block.trialList[0].keys()
# save data for this loop
block.saveAsExcel(filename + '.xlsx', sheetName='block',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
end_key_resp.keys = []
end_key_resp.rt = []
_end_key_resp_allKeys = []
# keep track of which components have finished
endComponents = [debrief_text1, end_key_resp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debrief_text1* updates
    if debrief_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief_text1.frameNStart = frameN  # exact frame index
        debrief_text1.tStart = t  # local t and not account for scr refresh
        debrief_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief_text1, 'tStartRefresh')  # time at next scr refresh
        debrief_text1.setAutoDraw(True)
    if debrief_text1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > debrief_text1.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            debrief_text1.tStop = t  # not accounting for scr refresh
            debrief_text1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(debrief_text1, 'tStopRefresh')  # time at next scr refresh
            debrief_text1.setAutoDraw(False)
    
    # *end_key_resp* updates
    waitOnFlip = False
    if end_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key_resp.frameNStart = frameN  # exact frame index
        end_key_resp.tStart = t  # local t and not account for scr refresh
        end_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key_resp, 'tStartRefresh')  # time at next scr refresh
        end_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_key_resp.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            end_key_resp.tStop = t  # not accounting for scr refresh
            end_key_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_key_resp, 'tStopRefresh')  # time at next scr refresh
            end_key_resp.status = FINISHED
    if end_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _end_key_resp_allKeys.extend(theseKeys)
        if len(_end_key_resp_allKeys):
            end_key_resp.keys = _end_key_resp_allKeys[-1].name  # just the last key pressed
            end_key_resp.rt = _end_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debrief_text1.started', debrief_text1.tStartRefresh)
thisExp.addData('debrief_text1.stopped', debrief_text1.tStopRefresh)
# check responses
if end_key_resp.keys in ['', [], None]:  # No response was made
    end_key_resp.keys = None
thisExp.addData('end_key_resp.keys',end_key_resp.keys)
if end_key_resp.keys != None:  # we had a response
    thisExp.addData('end_key_resp.rt', end_key_resp.rt)
thisExp.addData('end_key_resp.started', end_key_resp.tStartRefresh)
thisExp.addData('end_key_resp.stopped', end_key_resp.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "end2"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
end_key_resp_2.keys = []
end_key_resp_2.rt = []
_end_key_resp_2_allKeys = []
# keep track of which components have finished
end2Components = [debrief_text1_2, end_key_resp_2]
for thisComponent in end2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debrief_text1_2* updates
    if debrief_text1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief_text1_2.frameNStart = frameN  # exact frame index
        debrief_text1_2.tStart = t  # local t and not account for scr refresh
        debrief_text1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief_text1_2, 'tStartRefresh')  # time at next scr refresh
        debrief_text1_2.setAutoDraw(True)
    if debrief_text1_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > debrief_text1_2.tStartRefresh + 30.0-frameTolerance:
            # keep track of stop time/frame for later
            debrief_text1_2.tStop = t  # not accounting for scr refresh
            debrief_text1_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(debrief_text1_2, 'tStopRefresh')  # time at next scr refresh
            debrief_text1_2.setAutoDraw(False)
    
    # *end_key_resp_2* updates
    waitOnFlip = False
    if end_key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key_resp_2.frameNStart = frameN  # exact frame index
        end_key_resp_2.tStart = t  # local t and not account for scr refresh
        end_key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key_resp_2, 'tStartRefresh')  # time at next scr refresh
        end_key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key_resp_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_key_resp_2.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            end_key_resp_2.tStop = t  # not accounting for scr refresh
            end_key_resp_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_key_resp_2, 'tStopRefresh')  # time at next scr refresh
            end_key_resp_2.status = FINISHED
    if end_key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = end_key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _end_key_resp_2_allKeys.extend(theseKeys)
        if len(_end_key_resp_2_allKeys):
            end_key_resp_2.keys = _end_key_resp_2_allKeys[-1].name  # just the last key pressed
            end_key_resp_2.rt = _end_key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end2"-------
for thisComponent in end2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debrief_text1_2.started', debrief_text1_2.tStartRefresh)
thisExp.addData('debrief_text1_2.stopped', debrief_text1_2.tStopRefresh)
# check responses
if end_key_resp_2.keys in ['', [], None]:  # No response was made
    end_key_resp_2.keys = None
thisExp.addData('end_key_resp_2.keys',end_key_resp_2.keys)
if end_key_resp_2.keys != None:  # we had a response
    thisExp.addData('end_key_resp_2.rt', end_key_resp_2.rt)
thisExp.addData('end_key_resp_2.started', end_key_resp_2.tStartRefresh)
thisExp.addData('end_key_resp_2.stopped', end_key_resp_2.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "end3"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
end_key_resp_3.keys = []
end_key_resp_3.rt = []
_end_key_resp_3_allKeys = []
# keep track of which components have finished
end3Components = [debrief_text1_3, end_key_resp_3]
for thisComponent in end3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debrief_text1_3* updates
    if debrief_text1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief_text1_3.frameNStart = frameN  # exact frame index
        debrief_text1_3.tStart = t  # local t and not account for scr refresh
        debrief_text1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief_text1_3, 'tStartRefresh')  # time at next scr refresh
        debrief_text1_3.setAutoDraw(True)
    if debrief_text1_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > debrief_text1_3.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            debrief_text1_3.tStop = t  # not accounting for scr refresh
            debrief_text1_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(debrief_text1_3, 'tStopRefresh')  # time at next scr refresh
            debrief_text1_3.setAutoDraw(False)
    
    # *end_key_resp_3* updates
    waitOnFlip = False
    if end_key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key_resp_3.frameNStart = frameN  # exact frame index
        end_key_resp_3.tStart = t  # local t and not account for scr refresh
        end_key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key_resp_3, 'tStartRefresh')  # time at next scr refresh
        end_key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key_resp_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_key_resp_3.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            end_key_resp_3.tStop = t  # not accounting for scr refresh
            end_key_resp_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_key_resp_3, 'tStopRefresh')  # time at next scr refresh
            end_key_resp_3.status = FINISHED
    if end_key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = end_key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _end_key_resp_3_allKeys.extend(theseKeys)
        if len(_end_key_resp_3_allKeys):
            end_key_resp_3.keys = _end_key_resp_3_allKeys[-1].name  # just the last key pressed
            end_key_resp_3.rt = _end_key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end3"-------
for thisComponent in end3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debrief_text1_3.started', debrief_text1_3.tStartRefresh)
thisExp.addData('debrief_text1_3.stopped', debrief_text1_3.tStopRefresh)
# check responses
if end_key_resp_3.keys in ['', [], None]:  # No response was made
    end_key_resp_3.keys = None
thisExp.addData('end_key_resp_3.keys',end_key_resp_3.keys)
if end_key_resp_3.keys != None:  # we had a response
    thisExp.addData('end_key_resp_3.rt', end_key_resp_3.rt)
thisExp.addData('end_key_resp_3.started', end_key_resp_3.tStartRefresh)
thisExp.addData('end_key_resp_3.stopped', end_key_resp_3.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "end4"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
end_key_resp_4.keys = []
end_key_resp_4.rt = []
_end_key_resp_4_allKeys = []
# keep track of which components have finished
end4Components = [debrief_text1_4, end_key_resp_4]
for thisComponent in end4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debrief_text1_4* updates
    if debrief_text1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief_text1_4.frameNStart = frameN  # exact frame index
        debrief_text1_4.tStart = t  # local t and not account for scr refresh
        debrief_text1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief_text1_4, 'tStartRefresh')  # time at next scr refresh
        debrief_text1_4.setAutoDraw(True)
    if debrief_text1_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > debrief_text1_4.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            debrief_text1_4.tStop = t  # not accounting for scr refresh
            debrief_text1_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(debrief_text1_4, 'tStopRefresh')  # time at next scr refresh
            debrief_text1_4.setAutoDraw(False)
    
    # *end_key_resp_4* updates
    waitOnFlip = False
    if end_key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key_resp_4.frameNStart = frameN  # exact frame index
        end_key_resp_4.tStart = t  # local t and not account for scr refresh
        end_key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key_resp_4, 'tStartRefresh')  # time at next scr refresh
        end_key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key_resp_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_key_resp_4.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            end_key_resp_4.tStop = t  # not accounting for scr refresh
            end_key_resp_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_key_resp_4, 'tStopRefresh')  # time at next scr refresh
            end_key_resp_4.status = FINISHED
    if end_key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = end_key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _end_key_resp_4_allKeys.extend(theseKeys)
        if len(_end_key_resp_4_allKeys):
            end_key_resp_4.keys = _end_key_resp_4_allKeys[-1].name  # just the last key pressed
            end_key_resp_4.rt = _end_key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end4"-------
for thisComponent in end4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debrief_text1_4.started', debrief_text1_4.tStartRefresh)
thisExp.addData('debrief_text1_4.stopped', debrief_text1_4.tStopRefresh)
# check responses
if end_key_resp_4.keys in ['', [], None]:  # No response was made
    end_key_resp_4.keys = None
thisExp.addData('end_key_resp_4.keys',end_key_resp_4.keys)
if end_key_resp_4.keys != None:  # we had a response
    thisExp.addData('end_key_resp_4.rt', end_key_resp_4.rt)
thisExp.addData('end_key_resp_4.started', end_key_resp_4.tStartRefresh)
thisExp.addData('end_key_resp_4.stopped', end_key_resp_4.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "Mturk_Completion_Code"-------
continueRoutine = True
routineTimer.add(700.000000)
# update component parameters for each repeat
end_key_resp_5.keys = []
end_key_resp_5.rt = []
_end_key_resp_5_allKeys = []
# keep track of which components have finished
Mturk_Completion_CodeComponents = [complete_code, end_key_resp_5]
for thisComponent in Mturk_Completion_CodeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Mturk_Completion_CodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Mturk_Completion_Code"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Mturk_Completion_CodeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Mturk_Completion_CodeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *complete_code* updates
    if complete_code.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        complete_code.frameNStart = frameN  # exact frame index
        complete_code.tStart = t  # local t and not account for scr refresh
        complete_code.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(complete_code, 'tStartRefresh')  # time at next scr refresh
        complete_code.setAutoDraw(True)
    if complete_code.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > complete_code.tStartRefresh + 700.0-frameTolerance:
            # keep track of stop time/frame for later
            complete_code.tStop = t  # not accounting for scr refresh
            complete_code.frameNStop = frameN  # exact frame index
            win.timeOnFlip(complete_code, 'tStopRefresh')  # time at next scr refresh
            complete_code.setAutoDraw(False)
    
    # *end_key_resp_5* updates
    waitOnFlip = False
    if end_key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key_resp_5.frameNStart = frameN  # exact frame index
        end_key_resp_5.tStart = t  # local t and not account for scr refresh
        end_key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key_resp_5, 'tStartRefresh')  # time at next scr refresh
        end_key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key_resp_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_key_resp_5.tStartRefresh + 700.0-frameTolerance:
            # keep track of stop time/frame for later
            end_key_resp_5.tStop = t  # not accounting for scr refresh
            end_key_resp_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_key_resp_5, 'tStopRefresh')  # time at next scr refresh
            end_key_resp_5.status = FINISHED
    if end_key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = end_key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _end_key_resp_5_allKeys.extend(theseKeys)
        if len(_end_key_resp_5_allKeys):
            end_key_resp_5.keys = _end_key_resp_5_allKeys[-1].name  # just the last key pressed
            end_key_resp_5.rt = _end_key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Mturk_Completion_CodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Mturk_Completion_Code"-------
for thisComponent in Mturk_Completion_CodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('complete_code.started', complete_code.tStartRefresh)
thisExp.addData('complete_code.stopped', complete_code.tStopRefresh)
# check responses
if end_key_resp_5.keys in ['', [], None]:  # No response was made
    end_key_resp_5.keys = None
thisExp.addData('end_key_resp_5.keys',end_key_resp_5.keys)
if end_key_resp_5.keys != None:  # we had a response
    thisExp.addData('end_key_resp_5.rt', end_key_resp_5.rt)
thisExp.addData('end_key_resp_5.started', end_key_resp_5.tStartRefresh)
thisExp.addData('end_key_resp_5.stopped', end_key_resp_5.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
