from os import listdir
from os.path import isfile, isdir, join, exists
import re
import json 
import uuid

hash = lambda : uuid.uuid4().hex
files = listdir('.')
for file in files:
    if isdir(file):
        print(file)
        
        # .item
        content = """{
   "AnimationRetargetingConfig" : {
      "enabled" : true,
      "mappings" : null
   },
   "AnimationStandard" : "Live2D_4_0",
   "Attachments" : null,
   "CameraSettings" : {
      "CameraBone" : "Camera",
      "FOV" : 60,
      "LookAtBone" : "BipHead",
      "OffsetPos" : [ 0.0, 0.0, 3.0 ],
      "OffsetRot" : [ -0.0, 0.0, -0.0 ],
      "ResetType" : 1
   },
   "CubismTextureHeight" : 2048,
   "CubismTextureWidth" : 2048,
   "CubismTextureWrap" : "Clamp",
   "CustomizationName" : "",
   "CustomizationOptions" : null,
   "Description" : "<ID>",
   "FriendlyName" : "<ID>",
   "IsPersona" : false,
   "ItemName" : "<ID>",
   "LeapMotionBonesRemapping" : null,
   "LeapMotionEnabled" : true,
   "LeapMotionHiddenOffset" : [ 0.0, 0.0, 0.0 ],
   "Live2DAnimazeVersion" : 1,
   "Live2DPosition" : [ 0.0, 0.0 ],
   "Live2DScale" : [ 1.0, 1.0 ],
   "LoadCustomizations" : false,
   "ModelPath" : "<ID>.model3.json",
   "PerceptionNeuronRetargetingConfig" : {
      "enabled" : true,
      "mappings" : null
   },
   "Position" : [ 0.0, 0.0, 0.0 ],
   "PropTags" : [ "MISSING_TAG" ],
   "RetargetingOverrides" : null,
   "Rotation" : [ -0.0, 0.0, -0.0 ],
   "Scale" : [ 1.0, 1.0, 1.0 ],
   "SourceFileMetaInfo" : null,
   "Type" : "Avatar2D"
}
"""
        content = re.sub(r"<ID>", file, content)
        with open(f'{file}/{file}.item', 'w') as f:
            f.write(content)
            
        # .vtube.json
        motions = [
            'login',
            'main_1',
            'main_2',
            'main_3',
            'complete',
            'effect',
            'home',
            'mission',
            'mission_complete',
            'wedding',
        ]
        hotkeys = []
        for index, motion in enumerate(motions):
            hotkeys.append({
                "HotkeyID": hash(),
                "Name": motion,
                "Action": "TriggerAnimation",
                "File": f"{motion}.motion3.json",
                "Position": {
                    "X": 0.0,
                    "Y": 0.0,
                    "Z": 0.0,
                    "Rotation": 0.0
                },
                "ColorOverlay": {
                    "On": False,
                    "Display": -1,
                    "WindowName": "",
                    "IncludeLeft": False,
                    "IncludeMid": False,
                    "IncludeRight": False,
                    "BaseValue": 0,
                    "OverlayValue": 0,
                    "Smoothing": 0,
                    "IncludeItems": False
                },
                "HandGestureSettings": {
                    "GestureLeft": "",
                    "GestureRight": "",
                    "GestureCombinator": "AND",
                    "AllowMirroredGesture": False,
                    "DeactivateExpWhenGestureNotDetected": False,
                    "SecondsUntilDetection": 0.5,
                    "SecondsDetected": 0.0,
                    "PercentDetected": 0.0
                },
                "Triggers": {
                    "Trigger1": "RightControl",
                    "Trigger2": f"Numpad{index}",
                    "ScreenButton": -1
                },
                "IsGlobal": True,
                "IsActive": True,
                "Minimized": False,
                "StopsOnLastFrame": False,
                "DeactivateAfterKeyUp": False,
                "DeactivateAfterSeconds": False,
                "DeactivateAfterSecondsAmount": 10.0,
                "FadeSecondsAmount": 0.5,
                "OnScreenHotkeyColor": {
                    "r": 1.0,
                    "g": 1.0,
                    "b": 1.0,
                    "a": 1.0
                }
            })
        content = {
            "Version": 1,
            "Name": file,
            "ModelID": hash(),
            "FileReferences": {
                "Icon": f"icon_{file}.png",
                "Model": f"{file}.model3.json",
                "IdleAnimation": "",
                "IdleAnimationWhenTrackingLost": "idle.motion3.json"
            },
            "ModelSaveMetadata": {
                "LastSavedVTubeStudioVersion": "1.17.0",
                "LastSavedPlatform": "Steam",
                "LastSavedDateUTC": "Wednesday, 23 February 2022, 15:23:51",
                "LastSavedDateLocalTime": "Wednesday, 23 February 2022, 23:23:51",
                "LastSavedDateUnixMillisecondTimestamp": "1645629831909"
            },
            "SavedModelPosition": {
                "Position": {
                    "x": 0.0,
                    "y": 0.0,
                    "z": 0.0
                },
                "Rotation": {
                    "x": 0.0,
                    "y": 0.0,
                    "z": 0.0,
                    "w": 1.0
                },
                "Scale": {
                    "x": 0.1,
                    "y": 0.1,
                    "z": 1.0
                }
            },
            "ModelPositionMovement": {
                "Use": True,
                "X": 6,
                "Y": 8,
                "Z": 11,
                "SmoothingX": 10,
                "SmoothingY": 10,
                "SmoothingZ": 10
            },
            "PhysicsSettings": {
                "Use": True,
                "UseLegacyPhysics": False,
                "Live2DPhysicsFPS": 3,
                "PhysicsStrength": 50,
                "WindStrength": 0
            },
            "GeneralSettings": {
                "TimeUntilTrackingLostIdleAnimation": 0.0
            },
            "ParameterSettings": [],
            "Hotkeys": hotkeys,
            "HotkeySettings": {
                "UseOnScreenHotkeys": False,
                "UseKeyboardHotkeys": True,
                "SendOnScreenHotkeysToPC": True,
                "OnScreenHotkeyAlpha": 75
            },
            "ArtMeshDetails": {
                "ArtMeshesExcludedFromPinning": [],
                "ArtMeshesThatDeleteItemsOnDrop": [],
                "ArtMeshSceneLightingMultipliers": []
            },
            "PhysicsCustomizationSettings": {
                "PhysicsMultipliersPerPhysicsGroup": [],
                "WindMultipliersPerPhysicsGroup": []
            }
        }
        with open(f'{file}/{file}.vtube.json', 'w') as f:
            json.dump(content, f, indent=2)

        # motions
        motionFiles = listdir(f'{file}/motions')
        for motionFile in motionFiles:
            with open(f'{file}/motions/{motionFile}', 'r') as fm:
                data = json.loads(fm.read())
                
                totalPointCount = 0
                totalSegmentCount = 0

                for curve in data['Curves']:
                    segmentPosition = 0
                    while segmentPosition < len(curve['Segments']):
                        if (segmentPosition == 0):
                            totalPointCount += 1
                            segmentPosition += 2

                        segment = curve['Segments'][segmentPosition]
                        if segment == 0:
                            totalPointCount += 1
                            segmentPosition += 3
                        elif segment == 1:
                            totalPointCount += 3
                            segmentPosition += 7
                        elif segment == 2:
                            totalPointCount += 1
                            segmentPosition += 3
                        elif segment == 3:
                            totalPointCount += 1
                            segmentPosition += 3
                        else:
                            raise Exception(f"Unknown segment type of the curve: {segment}")

                        totalSegmentCount += 1

                data['Meta']['TotalSegmentCount'] = totalSegmentCount
                data['Meta']['TotalPointCount'] = totalPointCount
                with open(f'{file}/motions/{motionFile}', 'w') as fw:
                    json.dump(data, fw, indent=2)
                
                
   
    