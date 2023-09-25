import os
import glob
import pandas as pd
import numpy as np
class SSHRCAnalysis:
# 35 Functions
    def APTimePointSorter(directory:str):
        file_list = os.listdir(directory)
        for file in file_list:
            df_temp = pd.read_csv(directory+file,sep=';',skiprows=15, na_values=['N/A'],header=0)
            #Reads the 5th to 7th characters in the file name to identify if it is BL PI or FU
            if file[4:6] == "BL":
                #Sort to BL folder if BL
                df_temp.to_csv(os.path.join("timepoints/BL/", os.path.basename(file)), na_rep='N/A', index=False)
            elif (str(file[4:6]) == "PI"):
                #Sort to PI folder if PI
                df_temp.to_csv(os.path.join("timepoints/PI/", os.path.basename(file)), na_rep='N/A', index=False)
            elif (str(file[4:6]) == "FU"):
                #Sort to FU folder if FU
                df_temp.to_csv(os.path.join("timepoints/FU/", os.path.basename(file)), na_rep='N/A', index=False)
            else:
                print(f"error on {file}")

    # Sort **Sleep Survey CSV files** based on participant timepoint entries\
    # 1. *Calculated sleep duration* = Time delta between Bedtime to Wake up
    # 2. *Weighted Average* = WD*(5/7)+WE(2/7)
    def surveydatasorter(array):
        seen = 0 # create an empty set
        bl= []
        blid = []
        pi= [] 
        piid = []
        fu= []
        fuid = []
        try:
            for entry in array:
                seen += 1
                if entry[7] in blid :
                    if entry[7] in piid:
                        if entry[7] in fuid:
                            print(f"Extra Participant ID#: {entry} index #:{seen} ")
                        else:
                            fu += [entry]
                            fuid += [(entry[7])] # add entry to the set

                    else:
                        pi += [entry]
                        piid += [(entry[7])] # add entry to the set

                else:
                    bl += [entry] # add entry to the set
                    blid += [(entry[7])] # add entry to the set

                    # do something with entry
            print("----------------------------")
            print(f'Total: {len(bl+pi+fu)} Baseline: {len(bl)} PostIntervention: {len(pi)} FollowUp: {len(fu)}')
            print("----------------------------")
        except:
            print("error")
        return bl,pi,fu
    def sleepdataprocessor(sleepdf1):
        sleepentry=[]
        for entry in sleepdf1:
            sleepdf = entry
            weekday_wake = sleepdf[11]
            weekday_sleep =sleepdf[12]
            weekend_wake = sleepdf[13]
            weekend_sleep = sleepdf[14]
            weekday_sleep_duration =  pd.Timedelta((pd.to_datetime(sleepdf[12])-(pd.to_datetime(sleepdf[11])))).seconds/60
            weekend_sleep_duration = pd.Timedelta((pd.to_datetime(sleepdf[14])-(pd.to_datetime(sleepdf[13])))).seconds/60
            avg_sleep_duration = (((pd.Timedelta((pd.to_datetime(sleepdf[12])-(pd.to_datetime(sleepdf[11])))).seconds/60)*(5/7))+((pd.Timedelta((pd.to_datetime(sleepdf[14])-(pd.to_datetime(sleepdf[13])))).seconds/60)*(2/7)))
            sleepentry += [[sleepdf[7],avg_sleep_duration,weekday_sleep_duration,weekend_sleep_duration]]
        return sleepentry  
    def valuetohours(value):
        newvalue=0
        match value:
            case 1:
                newvalue = 0
            case 2:
                newvalue = 0.25
            case 3:
                newvalue = 0.5
            case 4:
                newvalue = 1
            case 5:
                newvalue = 2
            case 6:
                newvalue = 3
            case 7:
                newvalue = 4
            case 8:
                newvalue = 5
            case 9:
                newvalue = 6
            case 10:
                newvalue = 7
            case 11:
                newvalue = 8   
            case 12:
                newvalue = 9       
            case -9:
                newvalue = -9
        return newvalue
    def valuestominutes(value):

        match value:
            case 1: #None
                newvalue = 0
            case 2:# 1 - 15 min
                newvalue = 0.25
            case 3:# 15 - 30 min
                newvalue = 0.5
            case 4:# 30 - 1 hour
                newvalue = 1
            case 5:# 1 - 2 hours
                newvalue = 2
            case 6:# 2 - 3 hours
                newvalue = 3
            case 7:# 3 - 4 hours
                newvalue = 4
            case 8:# 4 - 5 hours
                newvalue = 5
            case 9:# 5 - 6 hours
                newvalue = 6
            case 10:# 6 - 7 hours
                newvalue = 7
            case 11:# More than 7 hours
                newvalue = 8
            case -9:# Not answered
                newvalue = -9
            case _:
                print(f"No match found {value}")
        return newvalue
    def durationvaluetominutes(value):
        newvalue = 0
        match value:
            case 1: #None
                newvalue = 0
            case 2:# Less than 30 sec
                newvalue = 0.5
            case 3:# 30 sec to 1min
                newvalue = 1
            case 4:# 1-2min
                newvalue = 2
            case 5:# 2-3min
                newvalue = 3
            case 6:# 3-4min
                newvalue = 4
            case 7:# 4-5min
                newvalue = 5
            case 8:# 5-10min
                newvalue = 10
            case 9:# 10-15min
                newvalue = 15
            case 10:# 15-30min
                newvalue = 30
            case 11:# 30+min
                newvalue = 99
            case -9:# Not answered
                newvalue = -9

        return newvalue
    def freqvaluestohours(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 0.5
            case 2:# 30-45
                newvalue = 0.75
            case 3:# 45 - 1hr
                newvalue = 1
            case 4:# 1-1.5hr
                newvalue = 1.5
            case 5:#1.5-2hr
                newvalue = 2
            case 6:#2-3hr
                newvalue = 3
            case 7:#3-4hr
                newvalue = 4
            case 8:#4-5hr
                newvalue = 5
            case 9:#5-6hr
                newvalue = 6
            case 10:#No Interruption
                newvalue = 10
            case 11: # Did not sit
                newvalue = 0
            case -9:# Not Answered
                newvalue = -9
        return newvalue
    def convert_ShortHours(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 0
            case 2:# 30-45
                newvalue = 1/6
            case 3:# 45 - 1hr
                newvalue = 1/3
            case 4:# 1-1.5hr
                newvalue = 1/2
            case 5:#1.5-2hr
                newvalue = 3/4
            case 6:#2-3hr
                newvalue = 1
            case 7:#3-4hr
                newvalue = 2

            case -9:# Not Answered
                newvalue = -9
        return newvalue
    def convert_Nap(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 0
            case 2:# 30-45
                newvalue = 1/4
            case 3:# 45 - 1hr
                newvalue = 1/2
            case 4:# 1-1.5hr
                newvalue = 3/4
            case 5:#1.5-2hr
                newvalue = 1
            case 6:#2-3hr
                newvalue = 2
            case -9:# Not Answered
                newvalue = np.NaN 
        return newvalue
    def convert_COMP(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 1
            case 2:# 30-45
                newvalue = 2
            case 3:# 45 - 1hr
                newvalue = 3
            case 4:# 1-1.5hr
                newvalue = 4
            case 5:#1.5-2hr
                newvalue = 5
            case -9:# Not Answered
                newvalue = -9
        return newvalue
    def convert_1to4scale(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 1
            case 2:# 30-45
                newvalue = 2
            case 3:# 45 - 1hr
                newvalue = 3
            case 4:# 1-1.5hr
                newvalue = 4
            case -9:# Not Answered
                newvalue = -9
        return newvalue
    def convert_OCCUTime(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 0
            case 2:# 30-45
                newvalue = 1/4
            case 3:# 45 - 1hr
                newvalue = 1/2
            case 4:# 1-1.5hr
                newvalue = 3/4
            case 5:#1.5-2hr
                newvalue = 1
            case 6:# <30min
                newvalue = 1.5
            case 7:# 30-45
                newvalue = 2
            case 8:# 45 - 1hr
                newvalue = 2.5
            case 9:# 1-1.5hr
                newvalue = 3
            case 10:#1.5-2hr
                newvalue = 4
            case 11:# <30min
                newvalue = 5
            case 12:# 30-4
                newvalue = 6
            case 13:# 45 - 1hr
                newvalue = 7
            case 14:# 1-1.5hr
                newvalue = 8
            case -9:# Not Answered
                newvalue = -9
        return newvalue
    def convert_OCCUDAYsTime(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 1
            case 2:# 30-45
                newvalue = 2
            case 3:# 45 - 1hr
                newvalue = 3
            case 4:# 1-1.5hr
                newvalue = 4
            case 5:#1.5-2hr
                newvalue = 5
            case 6:# <30min
                newvalue = 6
            case 7:# 30-45
                newvalue = 7
            case -9:# Not Answered
                newvalue = -9
        return newvalue
    def convert_OCC_FREQ(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 0.5
            case 2:# 30-45
                newvalue = 0.75
            case 3:# 45 - 1hr
                newvalue = 1
            case 4:# 1-1.5hr
                newvalue = 1.5
            case 5:#1.5-2hr
                newvalue = 2
            case 6:#2-3hr
                newvalue = 3
            case 7:#3-4hr
                newvalue = 4
            case 8:#4-5hr
                newvalue = 5
            case 9:#5-6hr
                newvalue = 6
            case 10:#No Interruption
                newvalue = 10
            case 11: # Did not sit
                newvalue = 11
            case -9:# Not Answered
                newvalue = -9
        return newvalue
    def convert_OCC_YN(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 1
            case 2:# 30-45
                newvalue = 2

            case -9:# Not Answered
                newvalue = -9
        return newvalue
    def convert_OCC_TYPE(value):
        newvalue=0
        match value:
            case 1:# <30min
                newvalue = 1
            case 2:# 30-45
                newvalue = 2
            case 3:
                newvalue = 3
            case -9:# Not Answered
                newvalue = -9
        return newvalue
    def noconversion(value):
        return value     
    def sitcompdata(x):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        array = SSHRC_NP[1:,x]
        totalblsitcomp = ["Total Baseline Sit Comparison"]
        totalpisitcomp = ["Total Post-Int Sit Comparison"]
        totalfusitcomp = ["Total Follow-Up Sit Comparison"]
        for s in SSHRC_NP[1:,bl]:
            totalblsitcomp += [convert_COMP(s)]
        for s in SSHRC_NP[1:,pi]:
            totalpisitcomp += [convert_COMP(s)]
        for s in SSHRC_NP[1:,fu]:
            totalfusitcomp += [convert_COMP(s)]
        returndata += [totalblsitcomp]
        returndata += [totalpisitcomp]
        returndata += [totalfusitcomp]
        return returndata
    def brkfrqcompdata(x):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        array = SSHRC_NP[1:,x]
        totalblsitcomp = ["Total Baseline Break Freq Comparison"]
        totalpisitcomp = ["Total Post-Int Break Freq Comparison"]
        totalfusitcomp = ["Total Follow-Up Break Freq Comparison"]
        for s in SSHRC_NP[1:,bl]:
            totalblsitcomp += [convert_COMP(s)]
        for s in SSHRC_NP[1:,pi]:
            totalpisitcomp += [convert_COMP(s)]
        for s in SSHRC_NP[1:,fu]:
            totalfusitcomp += [convert_COMP(s)]
        returndata += [totalblsitcomp]
        returndata += [totalpisitcomp]
        returndata += [totalfusitcomp]
        return returndata
    def brkduracompdata(x):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        array = SSHRC_NP[1:,x]
        totalblsitcomp = ["Total Baseline Break Duration Comparison"]
        totalpisitcomp = ["Total Post-Int Break Duration Comparison"]
        totalfusitcomp = ["Total Follow-Up Break Duration Comparison"]
        for s in SSHRC_NP[1:,bl]:
            totalblsitcomp += [convert_COMP(s)]
        for s in SSHRC_NP[1:,pi]:
            totalpisitcomp += [convert_COMP(s)]
        for s in SSHRC_NP[1:,fu]:
            totalfusitcomp += [convert_COMP(s)]
        returndata += [totalblsitcomp]
        returndata += [totalpisitcomp]
        returndata += [totalfusitcomp]
        return returndata
    def totalnapdata(x):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = ["Total Baseline Nap Time"]
        totalpinap = ["Total Post-Int Nap Time"]
        totalfunap = ["Total Follow-Up Nap Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round(convert_Nap(SSHRC_NP[S,bl])+convert_Nap(SSHRC_NP[S,(bl+3)]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):

            totalpinap += [round(convert_Nap(SSHRC_NP[S,pi])+convert_Nap(SSHRC_NP[S,(pi+3)]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):

            totalfunap += [round(convert_Nap(SSHRC_NP[S,fu])+convert_Nap(SSHRC_NP[S,(fu+3)]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totaloccdata(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round(convert_OCCUTime(SSHRC_NP[S,bl])+convert_OCCUTime(SSHRC_NP[S,(bl+3)])+convert_OCCUTime(SSHRC_NP[S,(bl+6)]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):
            totalpinap += [round(convert_OCCUTime(SSHRC_NP[S,pi])+convert_OCCUTime(SSHRC_NP[S,(pi+3)])+convert_OCCUTime(SSHRC_NP[S,(pi+6)]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):
            totalfunap += [round(convert_OCCUTime(SSHRC_NP[S,fu])+convert_OCCUTime(SSHRC_NP[S,(fu+3)])+convert_OCCUTime(SSHRC_NP[S,(fu+6)]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totaloccdaysdata(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round(convert_OCCUDAYsTime(SSHRC_NP[S,bl])+convert_OCCUDAYsTime(SSHRC_NP[S,(bl+27)])+convert_OCCUDAYsTime(SSHRC_NP[S,(bl+54)]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):
            totalpinap += [round(convert_OCCUDAYsTime(SSHRC_NP[S,pi])+convert_OCCUDAYsTime(SSHRC_NP[S,(pi+27)])+convert_OCCUDAYsTime(SSHRC_NP[S,(pi+54)]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):
            totalfunap += [round(convert_OCCUDAYsTime(SSHRC_NP[S,fu])+convert_OCCUDAYsTime(SSHRC_NP[S,(fu+27)])+convert_OCCUDAYsTime(SSHRC_NP[S,(fu+54)]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totaloccafdata(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round(convert_OCCUTime(SSHRC_NP[S,bl])*convert_OCCUTime(SSHRC_NP[S,(bl+3)]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):
            totalpinap += [round(convert_OCCUTime(SSHRC_NP[S,pi])*convert_OCCUTime(SSHRC_NP[S,(pi+3)]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):
            totalfunap += [round(convert_OCCUTime(SSHRC_NP[S,fu])*convert_OCCUTime(SSHRC_NP[S,(fu+3)]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totalocctypedata(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [[convert_OCC_TYPE(SSHRC_NP[S,bl]),convert_OCC_TYPE(SSHRC_NP[S,(bl+27)]),convert_OCC_TYPE(SSHRC_NP[S,(bl+54)])]]
        for S in range (1,len(SSHRC_NP[:,pi])):
            totalpinap += [[convert_OCC_TYPE(SSHRC_NP[S,pi]),convert_OCC_TYPE(SSHRC_NP[S,(pi+27)]),convert_OCC_TYPE(SSHRC_NP[S,(pi+54)])]]
        for S in range (1,len(SSHRC_NP[:,fu])):
            totalfunap += [[convert_OCC_TYPE(SSHRC_NP[S,fu]),convert_OCC_TYPE(SSHRC_NP[S,(fu+27)]),convert_OCC_TYPE(SSHRC_NP[S,(fu+54)])]]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totaloccbrkduradata(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round(convert_DUR(SSHRC_NP[S,bl])+convert_DUR(SSHRC_NP[S,(bl+27)])+convert_DUR(SSHRC_NP[S,(bl+54)]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):
            totalpinap += [round(convert_DUR(SSHRC_NP[S,pi])+convert_DUR(SSHRC_NP[S,(pi+27)])+convert_DUR(SSHRC_NP[S,(pi+54)]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):
            totalfunap += [round(convert_DUR(SSHRC_NP[S,fu])+convert_DUR(SSHRC_NP[S,(fu+27)])+convert_DUR(SSHRC_NP[S,(fu+54)]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totaloccbrkfreqdata(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round(convert_FREQ(SSHRC_NP[S,bl])+convert_FREQ(SSHRC_NP[S,(bl+27)])+convert_FREQ(SSHRC_NP[S,(bl+54)]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):
            totalpinap += [round(convert_FREQ(SSHRC_NP[S,pi])+convert_FREQ(SSHRC_NP[S,(pi+27)])+convert_FREQ(SSHRC_NP[S,(pi+54)]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):
            totalfunap += [round(convert_FREQ(SSHRC_NP[S,fu])+convert_FREQ(SSHRC_NP[S,(fu+27)])+convert_FREQ(SSHRC_NP[S,(fu+54)]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totaloccsitdata(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round(convert_sit_hr(SSHRC_NP[S,bl])+convert_sit_hr(SSHRC_NP[S,(bl+27)])+convert_sit_hr(SSHRC_NP[S,(bl+54)]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):
            totalpinap += [round(convert_sit_hr(SSHRC_NP[S,pi])+convert_sit_hr(SSHRC_NP[S,(pi+27)])+convert_sit_hr(SSHRC_NP[S,(pi+54)]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):
            totalfunap += [round(convert_sit_hr(SSHRC_NP[S,fu])+convert_sit_hr(SSHRC_NP[S,(fu+27)])+convert_sit_hr(SSHRC_NP[S,(fu+54)]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totaloccYNdata(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round((SSHRC_NP[S,bl]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):
            totalpinap += [round((SSHRC_NP[S,pi]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):
            totalfunap += [round((SSHRC_NP[S,fu]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totaloccCLASSHRSdata(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round((SSHRC_NP[S,bl])+(SSHRC_NP[S,bl+30])+(SSHRC_NP[S,(bl+60)]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):
            totalpinap += [round((SSHRC_NP[S,pi])+(SSHRC_NP[S,pi+30])+(SSHRC_NP[S,(pi+60)]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):
            totalfunap += [round((SSHRC_NP[S,fu])+(SSHRC_NP[S,fu+30])+(SSHRC_NP[S,(fu+60)]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def mealdata(x,Meal):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblmeal = [f"Total Baseline {Meal} Time"]
        totalpimeal = [f"Total Post-Int {Meal} Time"]
        totalfumeal = [f"Total Follow-Up {Meal} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblmeal += [[convert_1HR(SSHRC_NP[S,bl]),convert_1HR(SSHRC_NP[S,(bl+9)])]]
        for S in range (1,len(SSHRC_NP[:,pi])):

            totalpimeal += [[convert_1HR(SSHRC_NP[S,pi]),convert_1HR(SSHRC_NP[S,(pi+9)])]]
        for S in range (1,len(SSHRC_NP[:,fu])):

            totalfumeal += [[convert_1HR(SSHRC_NP[S,fu]),convert_1HR(SSHRC_NP[S,(fu+9)])]]
        returndata += [totalblmeal]
        returndata += [totalpimeal]
        returndata += [totalfumeal]
        return returndata
    def toaldatacalc(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [convert_min(SSHRC_NP[S,bl])]
        for S in range (1,len(SSHRC_NP[:,pi])):

            totalpinap += [convert_min(SSHRC_NP[S,pi])]
        for S in range (1,len(SSHRC_NP[:,fu])):

            totalfunap += [convert_min(SSHRC_NP[S,fu])]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totaldurationdatacalc(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [convert_DUR(SSHRC_NP[S,bl])]
        for S in range (1,len(SSHRC_NP[:,pi])):

            totalpinap += [convert_DUR(SSHRC_NP[S,pi])]
        for S in range (1,len(SSHRC_NP[:,fu])):

            totalfunap += [convert_DUR(SSHRC_NP[S,fu])]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totalfreqdatacalc(x,string):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = [f"Total Baseline {string} Time"]
        totalpinap = [f"Total Post-Int {string} Time"]
        totalfunap = [f"Total Follow-Up {string} Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [convert_FREQ(SSHRC_NP[S,bl])]
        for S in range (1,len(SSHRC_NP[:,pi])):

            totalpinap += [convert_FREQ(SSHRC_NP[S,pi])]
        for S in range (1,len(SSHRC_NP[:,fu])):

            totalfunap += [convert_FREQ(SSHRC_NP[S,fu])]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata
    def totalmiscdata(x):
        bl=x
        pi=x+1
        fu=x+2
        returndata = []
        totalblnap = ["Total Baseline MISC Time"]
        totalpinap = ["Total Post-Int MISC Time"]
        totalfunap = ["Total Follow-Up MISC Time"]
        for S in range (1,len(SSHRC_NP[:,bl])):
            totalblnap += [round(convert_min(SSHRC_NP[S,bl])+convert_min(SSHRC_NP[S,(bl+18)]),2)]
        for S in range (1,len(SSHRC_NP[:,pi])):

            totalpinap += [round(convert_min(SSHRC_NP[S,pi])+convert_min(SSHRC_NP[S,(pi+18)]),2)]
        for S in range (1,len(SSHRC_NP[:,fu])):

            totalfunap += [round(convert_min(SSHRC_NP[S,fu])+convert_min(SSHRC_NP[S,(fu+18)]),2)]
        returndata += [totalblnap]
        returndata += [totalpinap]
        returndata += [totalfunap]
        return returndata