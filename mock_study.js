/******************* 
 * Mock_Study *
 *******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2025.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'mock_study';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeScreenRoutineBegin());
flowScheduler.add(WelcomeScreenRoutineEachFrame());
flowScheduler.add(WelcomeScreenRoutineEnd());
const trialsColorLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsColorLoopBegin(trialsColorLoopScheduler));
flowScheduler.add(trialsColorLoopScheduler);
flowScheduler.add(trialsColorLoopEnd);



flowScheduler.add(confidenceScreenRoutineBegin());
flowScheduler.add(confidenceScreenRoutineEachFrame());
flowScheduler.add(confidenceScreenRoutineEnd());
flowScheduler.add(NextScreenRoutineBegin());
flowScheduler.add(NextScreenRoutineEachFrame());
flowScheduler.add(NextScreenRoutineEnd());
const trialsGrayscaleLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsGrayscaleLoopBegin(trialsGrayscaleLoopScheduler));
flowScheduler.add(trialsGrayscaleLoopScheduler);
flowScheduler.add(trialsGrayscaleLoopEnd);



flowScheduler.add(confidenceScreenRoutineBegin());
flowScheduler.add(confidenceScreenRoutineEachFrame());
flowScheduler.add(confidenceScreenRoutineEnd());
flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'queryImages.xlsx', 'path': 'queryImages.xlsx'},
    {'name': 'images/grape.png', 'path': 'images/grape.png'},
    {'name': 'images/kiwi.png', 'path': 'images/kiwi.png'},
    {'name': 'images/orange.png', 'path': 'images/orange.png'},
    {'name': 'images/banana.png', 'path': 'images/banana.png'},
    {'name': 'images/apple.png', 'path': 'images/apple.png'},
    {'name': 'images/kiwi_gray.png', 'path': 'images/kiwi_gray.png'},
    {'name': 'images/orange_gray.png', 'path': 'images/orange_gray.png'},
    {'name': 'images/grape_gray.png', 'path': 'images/grape_gray.png'},
    {'name': 'images/banana_gray.png', 'path': 'images/banana_gray.png'},
    {'name': 'images/apple_gray.png', 'path': 'images/apple_gray.png'},
    {'name': 'queryImages.xlsx', 'path': 'queryImages.xlsx'},
    {'name': 'images/grape.png', 'path': 'images/grape.png'},
    {'name': 'images/kiwi.png', 'path': 'images/kiwi.png'},
    {'name': 'images/orange.png', 'path': 'images/orange.png'},
    {'name': 'images/banana.png', 'path': 'images/banana.png'},
    {'name': 'images/apple.png', 'path': 'images/apple.png'},
    {'name': 'images/kiwi_gray.png', 'path': 'images/kiwi_gray.png'},
    {'name': 'images/orange_gray.png', 'path': 'images/orange_gray.png'},
    {'name': 'images/grape_gray.png', 'path': 'images/grape_gray.png'},
    {'name': 'images/banana_gray.png', 'path': 'images/banana_gray.png'},
    {'name': 'images/apple_gray.png', 'path': 'images/apple_gray.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DATA);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var WelcomeScreenClock;
var textWelcomeMessage;
var key_Continue;
var trialColorClock;
var mouse;
var imageQuery;
var image1;
var image2;
var image3;
var image4;
var image5;
var blank500Clock;
var text;
var confidenceScreenClock;
var text_confidenceQuestion;
var slider;
var NextScreenClock;
var textNextScreen;
var key_NextScreen;
var trialGrayscaleClock;
var mouse_2;
var imageQuery_2;
var image1_2;
var image2_2;
var image3_2;
var image4_2;
var image5_2;
var toggle_button;
var EndScreenClock;
var textEndMessage;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  textWelcomeMessage = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcomeMessage',
    text: "Welcome to the user study\n\nOn the following screen, you will see a query image on the left, and will choose from the images on the right which is the same. \n\nPress 'SPACE' to start",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_Continue = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trialColor"
  trialColorClock = new util.Clock();
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  imageQuery = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageQuery', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.5), 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0.2], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  image2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, 0.2], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  image3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.6, 0.2], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  image4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  image5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image5', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, (- 0.2)], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  // Initialize components for Routine "blank500"
  blank500Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "confidenceScreen"
  confidenceScreenClock = new util.Clock();
  text_confidenceQuestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_confidenceQuestion',
    text: 'Any text\n\nincluding line breaks',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: psychoJS.window.units,
    labels: [1, 2, 3, 4, 5], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Noto Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "NextScreen"
  NextScreenClock = new util.Clock();
  textNextScreen = new visual.TextStim({
    win: psychoJS.window,
    name: 'textNextScreen',
    text: "Next Set of Images\n\nUse the Button to change between color and grayscale\n\nPress 'SPACE' to continue",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_NextScreen = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trialGrayscale"
  trialGrayscaleClock = new util.Clock();
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  imageQuery_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageQuery_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.5), 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image1_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0.2], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  image2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image2_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, 0.2], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  image3_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image3_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.6, 0.2], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  image4_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image4_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  image5_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image5_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, (- 0.2)], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  toggle_button = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'toggle_button',
    text: 'Toggle Color/Grayscale',
    font: 'Arvo',
    pos: [(- 0.5), (- 0.4)],
    size: [0.25, 0.125],
    padding: null,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: 'white',
    fillColor: 'darkgrey',
    borderColor: [0.9608, 0.8431, 0.6863],
    colorSpace: 'rgb',
    borderWidth: 0.5,
    opacity: null,
    depth: -8,
    letterHeight: 0.025,
    bold: true,
    italic: false,
  });
  toggle_button.clock = new util.Clock();
  
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  textEndMessage = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEndMessage',
    text: 'Thank you for completing!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var WelcomeScreenMaxDurationReached;
var _key_Continue_allKeys;
var WelcomeScreenMaxDuration;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'WelcomeScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    WelcomeScreenClock.reset();
    routineTimer.reset();
    WelcomeScreenMaxDurationReached = false;
    // update component parameters for each repeat
    key_Continue.keys = undefined;
    key_Continue.rt = undefined;
    _key_Continue_allKeys = [];
    psychoJS.experiment.addData('WelcomeScreen.started', globalClock.getTime());
    WelcomeScreenMaxDuration = null
    // keep track of which components have finished
    WelcomeScreenComponents = [];
    WelcomeScreenComponents.push(textWelcomeMessage);
    WelcomeScreenComponents.push(key_Continue);
    
    for (const thisComponent of WelcomeScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function WelcomeScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WelcomeScreen' ---
    // get current time
    t = WelcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcomeMessage* updates
    if (t >= 0.0 && textWelcomeMessage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcomeMessage.tStart = t;  // (not accounting for frame time here)
      textWelcomeMessage.frameNStart = frameN;  // exact frame index
      
      textWelcomeMessage.setAutoDraw(true);
    }
    
    
    // if textWelcomeMessage is active this frame...
    if (textWelcomeMessage.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_Continue* updates
    if (t >= 0.0 && key_Continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_Continue.tStart = t;  // (not accounting for frame time here)
      key_Continue.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_Continue.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_Continue.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_Continue.clearEvents(); });
    }
    
    // if key_Continue is active this frame...
    if (key_Continue.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_Continue.getKeys({keyList: 'space', waitRelease: false});
      _key_Continue_allKeys = _key_Continue_allKeys.concat(theseKeys);
      if (_key_Continue_allKeys.length > 0) {
        key_Continue.keys = _key_Continue_allKeys[_key_Continue_allKeys.length - 1].name;  // just the last key pressed
        key_Continue.rt = _key_Continue_allKeys[_key_Continue_allKeys.length - 1].rt;
        key_Continue.duration = _key_Continue_allKeys[_key_Continue_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WelcomeScreen' ---
    for (const thisComponent of WelcomeScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('WelcomeScreen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_Continue.corr, level);
    }
    psychoJS.experiment.addData('key_Continue.keys', key_Continue.keys);
    if (typeof key_Continue.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_Continue.rt', key_Continue.rt);
        psychoJS.experiment.addData('key_Continue.duration', key_Continue.duration);
        routineTimer.reset();
        }
    
    key_Continue.stop();
    // the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialsColor;
function trialsColorLoopBegin(trialsColorLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsColor = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'queryImages.xlsx',
      seed: undefined, name: 'trialsColor'
    });
    psychoJS.experiment.addLoop(trialsColor); // add the loop to the experiment
    currentLoop = trialsColor;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsColor of trialsColor) {
      snapshot = trialsColor.getSnapshot();
      trialsColorLoopScheduler.add(importConditions(snapshot));
      trialsColorLoopScheduler.add(trialColorRoutineBegin(snapshot));
      trialsColorLoopScheduler.add(trialColorRoutineEachFrame());
      trialsColorLoopScheduler.add(trialColorRoutineEnd(snapshot));
      trialsColorLoopScheduler.add(blank500RoutineBegin(snapshot));
      trialsColorLoopScheduler.add(blank500RoutineEachFrame());
      trialsColorLoopScheduler.add(blank500RoutineEnd(snapshot));
      trialsColorLoopScheduler.add(trialsColorLoopEndIteration(trialsColorLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsColorLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsColor);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsColorLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialsGrayscale;
function trialsGrayscaleLoopBegin(trialsGrayscaleLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsGrayscale = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'queryImages.xlsx',
      seed: undefined, name: 'trialsGrayscale'
    });
    psychoJS.experiment.addLoop(trialsGrayscale); // add the loop to the experiment
    currentLoop = trialsGrayscale;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsGrayscale of trialsGrayscale) {
      snapshot = trialsGrayscale.getSnapshot();
      trialsGrayscaleLoopScheduler.add(importConditions(snapshot));
      trialsGrayscaleLoopScheduler.add(trialGrayscaleRoutineBegin(snapshot));
      trialsGrayscaleLoopScheduler.add(trialGrayscaleRoutineEachFrame());
      trialsGrayscaleLoopScheduler.add(trialGrayscaleRoutineEnd(snapshot));
      trialsGrayscaleLoopScheduler.add(blank500RoutineBegin(snapshot));
      trialsGrayscaleLoopScheduler.add(blank500RoutineEachFrame());
      trialsGrayscaleLoopScheduler.add(blank500RoutineEnd(snapshot));
      trialsGrayscaleLoopScheduler.add(trialsGrayscaleLoopEndIteration(trialsGrayscaleLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsGrayscaleLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsGrayscale);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsGrayscaleLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialColorMaxDurationReached;
var gotValidClick;
var trialColorMaxDuration;
var trialColorComponents;
function trialColorRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trialColor' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialColorClock.reset();
    routineTimer.reset();
    trialColorMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.corr = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    imageQuery.setImage(query_image);
    image1.setImage(choice1);
    image2.setImage(choice2);
    image3.setImage(choice3);
    image4.setImage(choice4);
    image5.setImage(choice5);
    psychoJS.experiment.addData('trialColor.started', globalClock.getTime());
    trialColorMaxDuration = null
    // keep track of which components have finished
    trialColorComponents = [];
    trialColorComponents.push(mouse);
    trialColorComponents.push(imageQuery);
    trialColorComponents.push(image1);
    trialColorComponents.push(image2);
    trialColorComponents.push(image3);
    trialColorComponents.push(image4);
    trialColorComponents.push(image5);
    
    for (const thisComponent of trialColorComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var corr;
var corrAns;
var _mouseXYs;
function trialColorRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trialColor' ---
    // get current time
    t = trialColorClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if mouse is active this frame...
    if (mouse.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse.clickableObjects = eval([image1, image2, image3, image4, image5])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse.clickableObjects)) {
              mouse.clickableObjects = [mouse.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse.clickableObjects) {
              if (obj.contains(mouse)) {
                  gotValidClick = true;
                  mouse.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse.clicked_name.push(null);
          }
          // check whether click was in correct object
          if (gotValidClick) {
              corr = 0;
              corrAns = eval( correct_answer);
              for (let obj of [corrAns]) {
                  if (obj.contains(mouse)) {
                      corr = 1;
                  };
              };
              mouse.corr.push(corr);
          };
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *imageQuery* updates
    if (t >= 0.0 && imageQuery.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageQuery.tStart = t;  // (not accounting for frame time here)
      imageQuery.frameNStart = frameN;  // exact frame index
      
      imageQuery.setAutoDraw(true);
    }
    
    
    // if imageQuery is active this frame...
    if (imageQuery.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image1* updates
    if (t >= 0.0 && image1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image1.tStart = t;  // (not accounting for frame time here)
      image1.frameNStart = frameN;  // exact frame index
      
      image1.setAutoDraw(true);
    }
    
    
    // if image1 is active this frame...
    if (image1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image2* updates
    if (t >= 0.0 && image2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image2.tStart = t;  // (not accounting for frame time here)
      image2.frameNStart = frameN;  // exact frame index
      
      image2.setAutoDraw(true);
    }
    
    
    // if image2 is active this frame...
    if (image2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image3* updates
    if (t >= 0.0 && image3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image3.tStart = t;  // (not accounting for frame time here)
      image3.frameNStart = frameN;  // exact frame index
      
      image3.setAutoDraw(true);
    }
    
    
    // if image3 is active this frame...
    if (image3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image4* updates
    if (t >= 0.0 && image4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image4.tStart = t;  // (not accounting for frame time here)
      image4.frameNStart = frameN;  // exact frame index
      
      image4.setAutoDraw(true);
    }
    
    
    // if image4 is active this frame...
    if (image4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image5* updates
    if (t >= 0.0 && image5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image5.tStart = t;  // (not accounting for frame time here)
      image5.frameNStart = frameN;  // exact frame index
      
      image5.setAutoDraw(true);
    }
    
    
    // if image5 is active this frame...
    if (image5.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialColorComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialColorRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trialColor' ---
    for (const thisComponent of trialColorComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trialColor.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.corr', mouse.corr);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    
    // the Routine "trialColor" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blank500MaxDurationReached;
var blank500MaxDuration;
var blank500Components;
function blank500RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blank500' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    blank500Clock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    blank500MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('blank500.started', globalClock.getTime());
    blank500MaxDuration = null
    // keep track of which components have finished
    blank500Components = [];
    blank500Components.push(text);
    
    for (const thisComponent of blank500Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function blank500RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank500' ---
    // get current time
    t = blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text.tStop = t;  // not accounting for scr refresh
      text.frameNStop = frameN;  // exact frame index
      // update status
      text.status = PsychoJS.Status.FINISHED;
      text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blank500Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blank500RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank500' ---
    for (const thisComponent of blank500Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('blank500.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (blank500MaxDurationReached) {
        blank500Clock.add(blank500MaxDuration);
    } else {
        blank500Clock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var confidenceScreenMaxDurationReached;
var confidenceScreenMaxDuration;
var confidenceScreenComponents;
function confidenceScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'confidenceScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    confidenceScreenClock.reset();
    routineTimer.reset();
    confidenceScreenMaxDurationReached = false;
    // update component parameters for each repeat
    slider.reset()
    psychoJS.experiment.addData('confidenceScreen.started', globalClock.getTime());
    confidenceScreenMaxDuration = null
    // keep track of which components have finished
    confidenceScreenComponents = [];
    confidenceScreenComponents.push(text_confidenceQuestion);
    confidenceScreenComponents.push(slider);
    
    for (const thisComponent of confidenceScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function confidenceScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'confidenceScreen' ---
    // get current time
    t = confidenceScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_confidenceQuestion* updates
    if (t >= 0.0 && text_confidenceQuestion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_confidenceQuestion.tStart = t;  // (not accounting for frame time here)
      text_confidenceQuestion.frameNStart = frameN;  // exact frame index
      
      text_confidenceQuestion.setAutoDraw(true);
    }
    
    
    // if text_confidenceQuestion is active this frame...
    if (text_confidenceQuestion.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }
    
    
    // if slider is active this frame...
    if (slider.status === PsychoJS.Status.STARTED) {
    }
    
    
    // Check slider for response to end Routine
    if (slider.getRating() !== undefined && slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of confidenceScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function confidenceScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'confidenceScreen' ---
    for (const thisComponent of confidenceScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('confidenceScreen.stopped', globalClock.getTime());
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    // the Routine "confidenceScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var NextScreenMaxDurationReached;
var _key_NextScreen_allKeys;
var NextScreenMaxDuration;
var NextScreenComponents;
function NextScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'NextScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    NextScreenClock.reset();
    routineTimer.reset();
    NextScreenMaxDurationReached = false;
    // update component parameters for each repeat
    key_NextScreen.keys = undefined;
    key_NextScreen.rt = undefined;
    _key_NextScreen_allKeys = [];
    psychoJS.experiment.addData('NextScreen.started', globalClock.getTime());
    NextScreenMaxDuration = null
    // keep track of which components have finished
    NextScreenComponents = [];
    NextScreenComponents.push(textNextScreen);
    NextScreenComponents.push(key_NextScreen);
    
    for (const thisComponent of NextScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function NextScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'NextScreen' ---
    // get current time
    t = NextScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textNextScreen* updates
    if (t >= 0.0 && textNextScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textNextScreen.tStart = t;  // (not accounting for frame time here)
      textNextScreen.frameNStart = frameN;  // exact frame index
      
      textNextScreen.setAutoDraw(true);
    }
    
    
    // if textNextScreen is active this frame...
    if (textNextScreen.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_NextScreen* updates
    if (t >= 0.0 && key_NextScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_NextScreen.tStart = t;  // (not accounting for frame time here)
      key_NextScreen.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_NextScreen.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_NextScreen.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_NextScreen.clearEvents(); });
    }
    
    // if key_NextScreen is active this frame...
    if (key_NextScreen.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_NextScreen.getKeys({keyList: 'space', waitRelease: false});
      _key_NextScreen_allKeys = _key_NextScreen_allKeys.concat(theseKeys);
      if (_key_NextScreen_allKeys.length > 0) {
        key_NextScreen.keys = _key_NextScreen_allKeys[_key_NextScreen_allKeys.length - 1].name;  // just the last key pressed
        key_NextScreen.rt = _key_NextScreen_allKeys[_key_NextScreen_allKeys.length - 1].rt;
        key_NextScreen.duration = _key_NextScreen_allKeys[_key_NextScreen_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NextScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NextScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'NextScreen' ---
    for (const thisComponent of NextScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('NextScreen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_NextScreen.corr, level);
    }
    psychoJS.experiment.addData('key_NextScreen.keys', key_NextScreen.keys);
    if (typeof key_NextScreen.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_NextScreen.rt', key_NextScreen.rt);
        psychoJS.experiment.addData('key_NextScreen.duration', key_NextScreen.duration);
        routineTimer.reset();
        }
    
    key_NextScreen.stop();
    // the Routine "NextScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialGrayscaleMaxDurationReached;
var color_paths;
var grayscale_paths;
var trialGrayscaleMaxDuration;
var trialGrayscaleComponents;
function trialGrayscaleRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trialGrayscale' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialGrayscaleClock.reset();
    routineTimer.reset();
    trialGrayscaleMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_2
    // current position of the mouse:
    mouse_2.x = [];
    mouse_2.y = [];
    mouse_2.leftButton = [];
    mouse_2.midButton = [];
    mouse_2.rightButton = [];
    mouse_2.time = [];
    mouse_2.corr = [];
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    imageQuery_2.setImage(query_image);
    image1_2.setImage(choice1);
    image2_2.setImage(choice2);
    image3_2.setImage(choice3);
    image4_2.setImage(choice4);
    image5_2.setImage(choice5);
    // Run 'Begin Routine' code from code
    color_paths = [choice1, choice2, choice3, choice4, choice5];
    grayscale_paths = [gray1, gray2, gray3, gray4, gray5];
    toggle_button.toggleGray = false;
    image1_2.setImage(color_paths[0]);
    image2_2.setImage(color_paths[1]);
    image3_2.setImage(color_paths[2]);
    image4_2.setImage(color_paths[3]);
    image5_2.setImage(color_paths[4]);
    
    // reset toggle_button to account for continued clicks & clear times on/off
    toggle_button.reset()
    psychoJS.experiment.addData('trialGrayscale.started', globalClock.getTime());
    trialGrayscaleMaxDuration = null
    // keep track of which components have finished
    trialGrayscaleComponents = [];
    trialGrayscaleComponents.push(mouse_2);
    trialGrayscaleComponents.push(imageQuery_2);
    trialGrayscaleComponents.push(image1_2);
    trialGrayscaleComponents.push(image2_2);
    trialGrayscaleComponents.push(image3_2);
    trialGrayscaleComponents.push(image4_2);
    trialGrayscaleComponents.push(image5_2);
    trialGrayscaleComponents.push(toggle_button);
    
    for (const thisComponent of trialGrayscaleComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialGrayscaleRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trialGrayscale' ---
    // get current time
    t = trialGrayscaleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if mouse_2 is active this frame...
    if (mouse_2.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_2.clickableObjects = eval([image1, image2, image3, image4, image5])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_2.clickableObjects)) {
              mouse_2.clickableObjects = [mouse_2.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_2.clickableObjects) {
              if (obj.contains(mouse_2)) {
                  gotValidClick = true;
                  mouse_2.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse_2.clicked_name.push(null);
          }
          // check whether click was in correct object
          if (gotValidClick) {
              corr = 0;
              corrAns = eval( correct_answer);
              for (let obj of [corrAns]) {
                  if (obj.contains(mouse_2)) {
                      corr = 1;
                  };
              };
              mouse_2.corr.push(corr);
          };
          _mouseXYs = mouse_2.getPos();
          mouse_2.x.push(_mouseXYs[0]);
          mouse_2.y.push(_mouseXYs[1]);
          mouse_2.leftButton.push(_mouseButtons[0]);
          mouse_2.midButton.push(_mouseButtons[1]);
          mouse_2.rightButton.push(_mouseButtons[2]);
          mouse_2.time.push(mouse_2.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *imageQuery_2* updates
    if (t >= 0.0 && imageQuery_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageQuery_2.tStart = t;  // (not accounting for frame time here)
      imageQuery_2.frameNStart = frameN;  // exact frame index
      
      imageQuery_2.setAutoDraw(true);
    }
    
    
    // if imageQuery_2 is active this frame...
    if (imageQuery_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image1_2* updates
    if (t >= 0.0 && image1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image1_2.tStart = t;  // (not accounting for frame time here)
      image1_2.frameNStart = frameN;  // exact frame index
      
      image1_2.setAutoDraw(true);
    }
    
    
    // if image1_2 is active this frame...
    if (image1_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image2_2* updates
    if (t >= 0.0 && image2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image2_2.tStart = t;  // (not accounting for frame time here)
      image2_2.frameNStart = frameN;  // exact frame index
      
      image2_2.setAutoDraw(true);
    }
    
    
    // if image2_2 is active this frame...
    if (image2_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image3_2* updates
    if (t >= 0.0 && image3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image3_2.tStart = t;  // (not accounting for frame time here)
      image3_2.frameNStart = frameN;  // exact frame index
      
      image3_2.setAutoDraw(true);
    }
    
    
    // if image3_2 is active this frame...
    if (image3_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image4_2* updates
    if (t >= 0.0 && image4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image4_2.tStart = t;  // (not accounting for frame time here)
      image4_2.frameNStart = frameN;  // exact frame index
      
      image4_2.setAutoDraw(true);
    }
    
    
    // if image4_2 is active this frame...
    if (image4_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image5_2* updates
    if (t >= 0.0 && image5_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image5_2.tStart = t;  // (not accounting for frame time here)
      image5_2.frameNStart = frameN;  // exact frame index
      
      image5_2.setAutoDraw(true);
    }
    
    
    // if image5_2 is active this frame...
    if (image5_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *toggle_button* updates
    if (t >= 0 && toggle_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      toggle_button.tStart = t;  // (not accounting for frame time here)
      toggle_button.frameNStart = frameN;  // exact frame index
      
      toggle_button.setAutoDraw(true);
    }
    
    
    // if toggle_button is active this frame...
    if (toggle_button.status === PsychoJS.Status.STARTED) {
    }
    
    if (toggle_button.status === PsychoJS.Status.STARTED) {
      // check whether toggle_button has been pressed
      if (toggle_button.isClicked) {
        if (!toggle_button.wasClicked) {
          // store time of first click
          toggle_button.timesOn.push(toggle_button.clock.getTime());
          // store time clicked until
          toggle_button.timesOff.push(toggle_button.clock.getTime());
        } else {
          // update time clicked until;
          toggle_button.timesOff[toggle_button.timesOff.length - 1] = toggle_button.clock.getTime();
        }
        if (!toggle_button.wasClicked) {
          console.log("Button clicked.");
          toggle_button.toggleGray = (! toggle_button.toggleGray);
          console.log("Grayscale is now:", toggle_button.toggleGray);
          if (toggle_button.toggleGray) {
              image1_2.setImage(grayscale_paths[0]);
              image2_2.setImage(grayscale_paths[1]);
              image3_2.setImage(grayscale_paths[2]);
              image4_2.setImage(grayscale_paths[3]);
              image5_2.setImage(grayscale_paths[4]);
          } else {
              image1_2.setImage(color_paths[0]);
              image2_2.setImage(color_paths[1]);
              image3_2.setImage(color_paths[2]);
              image4_2.setImage(color_paths[3]);
              image5_2.setImage(color_paths[4]);
          }
        }
        // if toggle_button is still clicked next frame, it is not a new click
        toggle_button.wasClicked = true;
      } else {
        // if toggle_button is clicked next frame, it is a new click
        toggle_button.wasClicked = false;
      }
    } else {
      // keep clock at 0 if toggle_button hasn't started / has finished
      toggle_button.clock.reset();
      // if toggle_button is clicked next frame, it is a new click
      toggle_button.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialGrayscaleComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialGrayscaleRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trialGrayscale' ---
    for (const thisComponent of trialGrayscaleComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trialGrayscale.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_2.x', mouse_2.x);
    psychoJS.experiment.addData('mouse_2.y', mouse_2.y);
    psychoJS.experiment.addData('mouse_2.leftButton', mouse_2.leftButton);
    psychoJS.experiment.addData('mouse_2.midButton', mouse_2.midButton);
    psychoJS.experiment.addData('mouse_2.rightButton', mouse_2.rightButton);
    psychoJS.experiment.addData('mouse_2.time', mouse_2.time);
    psychoJS.experiment.addData('mouse_2.corr', mouse_2.corr);
    psychoJS.experiment.addData('mouse_2.clicked_name', mouse_2.clicked_name);
    
    psychoJS.experiment.addData('toggle_button.numClicks', toggle_button.numClicks);
    psychoJS.experiment.addData('toggle_button.timesOn', toggle_button.timesOn);
    psychoJS.experiment.addData('toggle_button.timesOff', toggle_button.timesOff);
    // the Routine "trialGrayscale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EndScreenMaxDurationReached;
var EndScreenMaxDuration;
var EndScreenComponents;
function EndScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    EndScreenClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    EndScreenMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('EndScreen.started', globalClock.getTime());
    EndScreenMaxDuration = null
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(textEndMessage);
    
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndScreen' ---
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textEndMessage* updates
    if (t >= 0.0 && textEndMessage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEndMessage.tStart = t;  // (not accounting for frame time here)
      textEndMessage.frameNStart = frameN;  // exact frame index
      
      textEndMessage.setAutoDraw(true);
    }
    
    
    // if textEndMessage is active this frame...
    if (textEndMessage.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textEndMessage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      textEndMessage.tStop = t;  // not accounting for scr refresh
      textEndMessage.frameNStop = frameN;  // exact frame index
      // update status
      textEndMessage.status = PsychoJS.Status.FINISHED;
      textEndMessage.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndScreen' ---
    for (const thisComponent of EndScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EndScreen.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (EndScreenMaxDurationReached) {
        EndScreenClock.add(EndScreenMaxDuration);
    } else {
        EndScreenClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
