#Created by Fernando Echavarria 20 May 2020
#to create an executable file go to command window and at the directory type
#pyinstaller --onefile -w [filename.py]

from Tkinter import * #adding GUI module
import random   #adding random module

window = Tk()

## setting window size

window.title("FEZUL Mastermind") #Screen name
window.geometry('1280x800') #Screen dimensions



#Initiatizing list and variables

#Master list of Colours and Items added to the dropdown box
coloursList =[
    "black",
    "blue",
    "green",
    "orange",
    "pink",
    "red",
    "white",
    "yellow"
]

hidenColoursList = random.sample(coloursList, 5)#list of randowm hiden colours

mySelectedColoursList = ["gray","gray","gray","gray","gray"] #List of start colours

##Creating 4 frames
frame_buttons = Frame(window,highlightbackground="black", highlightthickness=3, borderwidth = 5, padx=2, pady=2)
frame_colours = Frame(window, highlightbackground="black", highlightthickness=3, borderwidth = 5, padx=2, pady=2)
frame_hiden_colours = Frame(window, highlightbackground="black", highlightthickness=3, borderwidth = 5, padx=2, pady=2)
frame_tips = Frame(window,highlightbackground="black", highlightthickness=3, borderwidth = 5, padx=2, pady=2)
frame_text = Frame(window,highlightbackground="black", highlightthickness=3, borderwidth = 5, padx=2, pady=2)
frame_select = Frame(window,highlightbackground="red", highlightthickness=3, borderwidth = 5, padx=2, pady=2)
frame_help = Frame(window,highlightbackground="black", highlightthickness=3, borderwidth = 5, padx=2, pady=2)
frame_logo = Frame(window,highlightbackground="black", highlightthickness=3, borderwidth = 5, padx=2, pady=2)

##Placing 4 frames within the window
frame_hiden_colours.grid(row = 0 , column = 1,padx=2, pady=2, sticky=W+E+N+S)

frame_buttons.grid(row = 1, column = 0, padx=2, pady=2, sticky=W+E+N+S)
#frame_buttons.grid_propagate(False)

frame_colours.grid(row = 1, column = 1,padx=2, pady=2,sticky=W+E+N+S)

frame_tips.grid(row = 1, column = 2,padx=2, pady=2,sticky=W+E+N+S)

frame_text.grid(row = 0, column = 2,padx=2, pady=2, sticky=W+E+N+S)
frame_text.grid_propagate(False)

frame_select.grid(row = 2, columnspan = 2,padx=2, pady=2,sticky=W+E+N+S)

frame_help.grid(row = 2, column = 2, padx=2, pady=2, sticky=W+E+N+S)
frame_logo.grid(row = 0, column = 0, padx=2, pady=2, sticky=W+E+N+S)


#Adding Fezul Logo
fezul_logo_label = Label(frame_logo, text= "FEZUL Mastermind",fg = "black", font= 'Arial 12 bold', anchor="center")
fezul_logo_label.grid(row=0, column=0)

#Placing checkboxes for manual help

track_label = Label(frame_help, text="TRACK", fg = "black", font= 'Arial 10 bold')
track_label.grid(row = 0, column = 0, padx=3, pady=1) 

black_help = Checkbutton(frame_help, text="Black")
black_help.grid(row = 0, column = 1, padx=1, pady=1)

blue_help = Checkbutton(frame_help, text="Blue ")
blue_help.grid(row = 1, column = 1, padx=1, pady=1)

green_help = Checkbutton(frame_help, text="Green ")
green_help.grid(row = 0, column = 2, padx=1, pady=1)

orange_help = Checkbutton(frame_help, text="Orange")
orange_help.grid(row = 1, column = 2, padx=1, pady=1)

pink_help = Checkbutton(frame_help, text="Pink")
pink_help.grid(row = 0, column = 3, padx=1, pady=1)

red_help = Checkbutton(frame_help, text="Red")
red_help.grid(row = 1, column = 3, padx=1, pady=1)

white_help = Checkbutton(frame_help, text="White")
white_help.grid(row = 0, column = 4, padx=1, pady=1)

yellow_help = Checkbutton(frame_help, text="Yellow")
yellow_help.grid(row = 1, column = 4, padx=1, pady=1)

#Adding labels to report colours results

commonColoursNumber = int()
numberRightColours = int()

myColoursLabel= Label(frame_select, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
myColoursLabel.grid(row=0, column=7, padx=5, pady=5)

myRigthColoursLabel= Label(frame_select, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)

myRigthColoursLabel.grid(row=0, column=8, padx=5, pady=5)


##Creating widgets for frame_buttons

#Adding buttons

#New command

def newFunction():

    #reset Radiobutton

    global line_selected
    global r
    
    line_selected = 1
    
    r.set(1)

    #reset colours tips values

    #global commonColoursNumber
    #global numberRightColours
    
    commonColoursNumber = 0
    numberRightColours = 0

      

    global mySelectedColoursList
    global hidenColoursList
    
    mySelectedColoursList = ["gray","gray","gray","gray","gray"] #reset List of start coloursmy
    hidenColoursList = random.sample(coloursList, 5)#reset list of randowm hiden colours

    #reset select colours list
    firstColour["bg"]="gray"
    secondColour["bg"]="gray"
    thirdColour["bg"]="gray"
    fourthColour["bg"]="gray"
    fifthColour["bg"]="gray"

    #reset hiden colours display
    firstHidenColour["bg"]= "gray"
    secondHidenColour["bg"]= "gray"
    thirdHidenColour["bg"]= "gray"
    fourthHidenColour["bg"]= "gray"
    fifthHidenColour["bg"]= "gray"

     #Clear first column

    row0Color1["bg"] = "gray"
    row1Color1["bg"] = "gray"
    row2Color1["bg"] = "gray"
    row3Color1["bg"] = "gray"
    row4Color1["bg"] = "gray"
    row5Color1["bg"] = "gray"    
    row6Color1["bg"] = "gray"
    row7Color1["bg"] = "gray"
    row8Color1["bg"] = "gray"
    row9Color1["bg"] = "gray"
    row10Color1["bg"] = "gray"
    row11Color1["bg"] = "gray"

    #Clear second column

    row0Color2["bg"] = "gray"
    row1Color2["bg"] = "gray"
    row2Color2["bg"] = "gray"
    row3Color2["bg"] = "gray"
    row4Color2["bg"] = "gray"
    row5Color2["bg"] = "gray"    
    row6Color2["bg"] = "gray"
    row7Color2["bg"] = "gray"
    row8Color2["bg"] = "gray"
    row9Color2["bg"] = "gray"
    row10Color2["bg"] = "gray"
    row11Color2["bg"] = "gray"

    #Clear third column

    row0Color3["bg"] = "gray"
    row1Color3["bg"] = "gray"
    row2Color3["bg"] = "gray"
    row3Color3["bg"] = "gray"
    row4Color3["bg"] = "gray"
    row5Color3["bg"] = "gray"    
    row6Color3["bg"] = "gray"
    row7Color3["bg"] = "gray"
    row8Color3["bg"] = "gray"
    row9Color3["bg"] = "gray"
    row10Color3["bg"] = "gray"
    row11Color3["bg"] = "gray"

    #Clear fourth column

    row0Color4["bg"] = "gray"
    row1Color4["bg"] = "gray"
    row2Color4["bg"] = "gray"
    row3Color4["bg"] = "gray"
    row4Color4["bg"] = "gray"
    row5Color4["bg"] = "gray"    
    row6Color4["bg"] = "gray"
    row7Color4["bg"] = "gray"
    row8Color4["bg"] = "gray"
    row9Color4["bg"] = "gray"
    row10Color4["bg"] = "gray"
    row11Color4["bg"] = "gray"

    #Clear fifth column

    row0Color5["bg"] = "gray"
    row1Color5["bg"] = "gray"
    row2Color5["bg"] = "gray"
    row3Color5["bg"] = "gray"
    row4Color5["bg"] = "gray"
    row5Color5["bg"] = "gray"    
    row6Color5["bg"] = "gray"
    row7Color5["bg"] = "gray"
    row8Color5["bg"] = "gray"
    row9Color5["bg"] = "gray"
    row10Color5["bg"] = "gray"
    row11Color5["bg"] = "gray"

    #Activate buttons

    button_evaluate['state'] = ACTIVE
    button_show['state'] = ACTIVE
    button_clear['state'] = ACTIVE
    firstColour['state'] = ACTIVE
    secondColour['state'] = ACTIVE
    thirdColour['state'] = ACTIVE
    fourthColour['state'] = ACTIVE
    fifthColour['state'] = ACTIVE

    #clear message

    messageLabel1 = Label(frame_text, text= "                                             ")
    messageLabel1.grid(row=0, column=0, sticky=E+W+N+S)

    myColoursLabel = Label(frame_select, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    myColoursLabel.grid(row=0, column=7, padx=5, pady=5)

    myRigthColoursLabel = Label(frame_select, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    myRigthColoursLabel.grid(row=0, column=8, padx=5, pady=5)

     
    row0_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row0_colour_tip.grid(row=0, column=0, padx=5, pady=5)

           
    row0_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row0_Rigth_tip.grid(row=0, column=1, padx=5, pady=5)

        
    row1_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row1_colour_tip.grid(row=1, column=0, padx=5, pady=5)

    
    row1_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row1_Rigth_tip.grid(row=1, column=1, padx=5, pady=5)

    row2_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row2_colour_tip.grid(row=2, column=0, padx=5, pady=5)

    row2_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row2_Rigth_tip.grid(row=2, column=1, padx=5, pady=5)

               
    row3_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row3_colour_tip.grid(row=3, column=0, padx=5, pady=5)

         
    row3_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row3_Rigth_tip.grid(row=3, column=1, padx=5, pady=5)

                    
    row4_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row4_colour_tip.grid(row=4, column=0, padx=5, pady=5)

      
    row4_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row4_Rigth_tip.grid(row=4, column=1, padx=5, pady=5)

         
    row5_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row5_colour_tip.grid(row=5, column=0, padx=5, pady=5)

            
    row5_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row5_Rigth_tip.grid(row=5, column=1, padx=5, pady=5)

    row6_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row6_colour_tip.grid(row=6, column=0, padx=5, pady=5)

         
    row6_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row6_Rigth_tip.grid(row=6, column=1, padx=5, pady=5)

    row7_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row7_colour_tip.grid(row=7, column=0, padx=5, pady=5)

      
    row7_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row7_Rigth_tip.grid(row=7, column=1, padx=5, pady=5)

    row8_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row8_colour_tip.grid(row=8, column=0, padx=5, pady=5)

    row8_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row8_Rigth_tip.grid(row=8, column=1, padx=5, pady=5)

    row9_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row9_colour_tip.grid(row=9, column=0, padx=5, pady=5)

    row9_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row9_Rigth_tip.grid(row=9, column=1, padx=5, pady=5)

    row10_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row10_colour_tip.grid(row=10, column=0, padx=5, pady=5)

    row10_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row10_Rigth_tip.grid(row=10, column=1, padx=5, pady=5)

    row11_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row11_colour_tip.grid(row=11, column=0, padx=5, pady=5)

    row11_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row11_Rigth_tip.grid(row=11, column=1, padx=5, pady=5)



    #=========================================================
    
    

button_new = Button(frame_buttons, text="NEW",bg = "gray", fg = "black", command=newFunction, padx=30, pady=5)
button_new.grid(row=0, column=0, padx=10, pady=10,ipadx=10, sticky="ew")


#Evaluate Command                                                      

def evaluateFunction():

    #Convert list to a set
    global hidenColoursList
    global mySelectedColoursList
    global messageLabel1
    global messageLabel2
    global messageLabel3
    global myColoursLabel
    global myRigthColoursLabel
    global myseta
    global mysetb
    global commonColours
    global commonColoursNumber
    global commonColoursList
    global rightColoursList
    global numberRightColours
    global line_selected

    #Verify that there is not missing colours selected

    global count_gray
    count_gray = 0
    for i in mySelectedColoursList:
        if i == "gray":
            count_gray = count_gray + 1
        
    if count_gray > 0:
        
        messageLabel1 = Label(frame_text, text= "                                        ")
        messageLabel1.grid(row=0, column=0)

        messageLabel2 = Label(frame_text, text = "                                       ")
        messageLabel2.grid(row=0, column=0)

        messageLabel3 = Label(frame_text, text= "                                        ")
        messageLabel3.grid(row=0, column=0)

        messageLabel1 = Label(frame_text, text= "Missing Colours ??", fg = "red", font= 'Arial 10 bold')
        messageLabel1.grid(row=0, column=0, sticky=N+E+W+S)

    else:
                 
        myseta = set(hidenColoursList) #create a set for hiden colours
        mysetb = set(mySelectedColoursList) #create a set for selected colours

        #Compute the number of common colours - Set Interception

        commonColours = myseta & mysetb

        commonColoursNumber = len(commonColours)
        
        #Iterating through the set to print commun colours

        commonColoursList = [] #List of commun colours

        for colours in commonColours:
            #print(colours) #Print commun colours
            commonColoursList.append(colours) #Append comun colours to list

        #Determine the number of colours in the right position - list comprehension

        rightColoursList = [] #List of right colours
        rightColoursList = [i for i, j in zip(hidenColoursList,mySelectedColoursList) if i==j]

        numberRightColours = len(rightColoursList)
        
             
        if numberRightColours == 5:

            #showFunction()
            #print "Well done!"
            messageLabel1 = Label(frame_text, text= "                                        ")
            messageLabel1.grid(row=0, column=0)

            messageLabel2 = Label(frame_text, text = "                                       ")
            messageLabel2.grid(row=0, column=0)

            messageLabel3 = Label(frame_text, text= "                                        ")
            messageLabel3.grid(row=0, column=0)

            messageLabel1 = Label(frame_text, text= "Excellent Job! \nYou have selected \nthe right colours!")
            messageLabel1.grid(row=0, column=0)

            #Show hidden colours

            showFunction()
                    
        elif numberRightColours == 4:
            #print "Almost there!"
            messageLabel1 = Label(frame_text, text= "                                        ")
            messageLabel1.grid(row=0, column=0)

            messageLabel2 = Label(frame_text, text = "                                       ")
            messageLabel2.grid(row=0, column=0)

            messageLabel3 = Label(frame_text, text= "                                        ")
            messageLabel3.grid(row=0, column=0)

            
            messageLabel2 = Label(frame_text, text = "Great Job! \nAlmost there! \nTry it again!")
            messageLabel2.grid(row=0, column=0)
            
        else:
            #print "it's not enough!. Please try it again"
            messageLabel1 = Label(frame_text, text= "                                         ")
            messageLabel1.grid(row=0, column=0)

            messageLabel2 = Label(frame_text, text = "                                        ")
            messageLabel2.grid(row=0, column=0)

            messageLabel3 = Label(frame_text, text= "                                         ")
            messageLabel3.grid(row=0, column=0)

            messageLabel3 = Label(frame_text, text= "Good Job!, \nbut it's still not enough! \nTry it again!")
            messageLabel3.grid(row=0, column=0)
               
        #Adjust label for number of colours
        myColoursLabel = Label(frame_select, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
        myColoursLabel.grid(row=0, column=7, padx=5, pady=5)

        #Adjust label for number of right colours
        myRigthColoursLabel = Label(frame_select, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
        myRigthColoursLabel.grid(row=0, column=8, padx=5, pady=5)

        #Display tip for each line

        global line_selected
        global r
           
        if line_selected == 1:
            #Adjust label for number of colours
            
            row0_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row0_colour_tip.grid(row=0, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row0_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row0_Rigth_tip.grid(row=0, column=1, padx=5, pady=5)

            line_selected = 2
            
            r.set(2)

        elif line_selected == 2:

            #Adjust label for number of colours
            
            row1_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row1_colour_tip.grid(row=1, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row1_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row1_Rigth_tip.grid(row=1, column=1, padx=5, pady=5)

            line_selected = 3
            
            r.set(3)
                    
        elif line_selected == 3:

            row2_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row2_colour_tip.grid(row=2, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row2_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row2_Rigth_tip.grid(row=2, column=1, padx=5, pady=5)

            line_selected = 4
            
            r.set(4)
            
        elif line_selected == 4:

            row3_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row3_colour_tip.grid(row=3, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row3_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row3_Rigth_tip.grid(row=3, column=1, padx=5, pady=5)

            line_selected = 5
            
            r.set(5)
                   
        elif line_selected == 5:

            row4_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row4_colour_tip.grid(row=4, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row4_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row4_Rigth_tip.grid(row=4, column=1, padx=5, pady=5)

            line_selected = 6
            
            r.set(6)
            
        elif line_selected == 6:

            row5_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row5_colour_tip.grid(row=5, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row5_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row5_Rigth_tip.grid(row=5, column=1, padx=5, pady=5)

            line_selected = 7
            
            r.set(7)
               
        elif line_selected == 7:

            row6_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row6_colour_tip.grid(row=6, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row6_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row6_Rigth_tip.grid(row=6, column=1, padx=5, pady=5)

            line_selected = 8
            
            r.set(8)
            
        elif line_selected == 8:

            row7_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row7_colour_tip.grid(row=7, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row7_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row7_Rigth_tip.grid(row=7, column=1, padx=5, pady=5)

            line_selected = 9
            
            r.set(9)
            
        elif line_selected == 9:

            row8_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row8_colour_tip.grid(row=8, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row8_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row8_Rigth_tip.grid(row=8, column=1, padx=5, pady=5)

            line_selected = 10
            
            r.set(10)
            
        elif line_selected == 10:

            row9_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row9_colour_tip.grid(row=9, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row9_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row9_Rigth_tip.grid(row=9, column=1, padx=5, pady=5)

            line_selected = 11
            
            r.set(11)
            
        elif line_selected == 11:

            row10_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row10_colour_tip.grid(row=10, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row10_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row10_Rigth_tip.grid(row=10, column=1, padx=5, pady=5)

            line_selected = 12
            
            r.set(12)
            
        else:
            
            row11_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row11_colour_tip.grid(row=11, column=0, padx=5, pady=5)

            #Adjust label for number of right colours
          
            row11_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
            row11_Rigth_tip.grid(row=11, column=1, padx=5, pady=5)

            #Show hidden values

            showFunction()

            #Display Game Over

            if numberRightColours == 5:

                messageLabel1 = Label(frame_text, text= "                                        ",justify=LEFT)
                messageLabel1.grid(row=0, column=0)

                messageLabel2 = Label(frame_text, text = "                                       ",justify=LEFT)
                messageLabel2.grid(row=0, column=0)

                messageLabel3 = Label(frame_text, text= "                                        ",justify=LEFT)
                messageLabel3.grid(row=0, column=0)

                messageLabel1 = Label(frame_text, text= "Excellent Job! \nYou have selected \nthe right colours!")
                messageLabel1.grid(row=0, column=0)

            else:
                messageLabel1 = Label(frame_text, text= "                                        ",justify=LEFT )
                messageLabel1.grid(row=0, column=0)

                messageLabel2 = Label(frame_text, text = "                                       ",justify=LEFT)
                messageLabel2.grid(row=0, column=0)

                messageLabel3 = Label(frame_text, text= "                                        ",justify=LEFT)
                messageLabel3.grid(row=0, column=0)

                messageLabel1 = Label(frame_text, text= "Sorry! \nGame Over. \nPlay it again!")
                messageLabel1.grid(row=0, column=0)
       
        #reset select colours list
        firstColour["bg"]="gray"
        secondColour["bg"]="gray"
        thirdColour["bg"]="gray"
        fourthColour["bg"]="gray"
        fifthColour["bg"]="gray"

        #Clear my selectedColoursList
        
        mySelectedColoursList = ["gray","gray","gray","gray","gray"] #reset List of start coloursmy

        
# adding the evaluate colours button

button_evaluate = Button(frame_buttons, text="EVALUATE",bg = "gray", fg = "black", state= DISABLED, command = evaluateFunction ,padx=30, pady=5)
button_evaluate.grid(row=2, column=0, padx=10, pady=10, ipadx=10, sticky="ew")

#Show Command

def showFunction():
    global hidenColoursList
    firstHidenColour["bg"]= hidenColoursList[0]
    secondHidenColour["bg"]= hidenColoursList[1]
    thirdHidenColour["bg"]= hidenColoursList[2]
    fourthHidenColour["bg"]= hidenColoursList[3]
    fifthHidenColour["bg"]= hidenColoursList[4]

    #Disabled buttons to start new game
    global button_evaluate
    global button_clear
    global firstColour
    global secondColour
    global thirdColour
    global fourthColour
    global fifthColour

    button_evaluate['state'] = DISABLED
    button_clear['state'] = DISABLED
    button_show['state'] = DISABLED
    firstColour['state'] = DISABLED
    secondColour['state'] = DISABLED
    thirdColour['state'] = DISABLED
    fourthColour['state'] = DISABLED
    fifthColour['state'] = DISABLED
    

#button show 
      
button_show = Button(frame_buttons, text="SHOW",bg = "gray", state= DISABLED, command= showFunction, fg = "black", padx=30, pady=5)
button_show.grid(row=3, column=0, padx=10, pady=10, ipadx=10, sticky="ew")

#Clear Command

def clearFunction():
    
    global mySelectedColoursList
    global line_selected
    global r
    
    
    mySelectedColoursList = ["gray","gray","gray","gray","gray"]

    #reset Radiobutton

    line_selected = 1
    
    r.set(1)

    #reset colours tips values

      
    commonColoursNumber = 0
    numberRightColours = 0

    myColoursLabel = Label(frame_select, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    myColoursLabel.grid(row=0, column=7, padx=5, pady=5)

    myRigthColoursLabel = Label(frame_select, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    myRigthColoursLabel.grid(row=0, column=8, padx=5, pady=5)

     
    row0_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row0_colour_tip.grid(row=0, column=0, padx=5, pady=5)

           
    row0_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row0_Rigth_tip.grid(row=0, column=1, padx=5, pady=5)

        
    row1_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row1_colour_tip.grid(row=1, column=0, padx=5, pady=5)

    
    row1_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row1_Rigth_tip.grid(row=1, column=1, padx=5, pady=5)

    row2_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row2_colour_tip.grid(row=2, column=0, padx=5, pady=5)

    row2_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row2_Rigth_tip.grid(row=2, column=1, padx=5, pady=5)

               
    row3_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row3_colour_tip.grid(row=3, column=0, padx=5, pady=5)

         
    row3_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row3_Rigth_tip.grid(row=3, column=1, padx=5, pady=5)

                    
    row4_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row4_colour_tip.grid(row=4, column=0, padx=5, pady=5)

      
    row4_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row4_Rigth_tip.grid(row=4, column=1, padx=5, pady=5)

         
    row5_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row5_colour_tip.grid(row=5, column=0, padx=5, pady=5)

            
    row5_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row5_Rigth_tip.grid(row=5, column=1, padx=5, pady=5)

    row6_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row6_colour_tip.grid(row=6, column=0, padx=5, pady=5)

         
    row6_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row6_Rigth_tip.grid(row=6, column=1, padx=5, pady=5)

    row7_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row7_colour_tip.grid(row=7, column=0, padx=5, pady=5)

      
    row7_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row7_Rigth_tip.grid(row=7, column=1, padx=5, pady=5)

    row8_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row8_colour_tip.grid(row=8, column=0, padx=5, pady=5)

    row8_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row8_Rigth_tip.grid(row=8, column=1, padx=5, pady=5)

    row9_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row9_colour_tip.grid(row=9, column=0, padx=5, pady=5)

    row9_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row9_Rigth_tip.grid(row=9, column=1, padx=5, pady=5)

    row10_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row10_colour_tip.grid(row=10, column=0, padx=5, pady=5)

    row10_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row10_Rigth_tip.grid(row=10, column=1, padx=5, pady=5)

    row11_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row11_colour_tip.grid(row=11, column=0, padx=5, pady=5)

    row11_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid", padx=5, pady=5)
    row11_Rigth_tip.grid(row=11, column=1, padx=5, pady=5)

    #Clear SelectedColours

    firstColour["bg"]="gray"
    secondColour["bg"]="gray"
    thirdColour["bg"]="gray"
    fourthColour["bg"]="gray"
    fifthColour["bg"]="gray"

    #Clear HidenColours
    
    firstHidenColour["bg"]= "gray"
    secondHidenColour["bg"]= "gray"
    thirdHidenColour["bg"]= "gray"
    fourthHidenColour["bg"]= "gray"
    fifthHidenColour["bg"]= "gray"

    #Clear first column

    row0Color1["bg"] = "gray"
    row1Color1["bg"] = "gray"
    row2Color1["bg"] = "gray"
    row3Color1["bg"] = "gray"
    row4Color1["bg"] = "gray"
    row5Color1["bg"] = "gray"    
    row6Color1["bg"] = "gray"
    row7Color1["bg"] = "gray"
    row8Color1["bg"] = "gray"
    row9Color1["bg"] = "gray"
    row10Color1["bg"] = "gray"
    row11Color1["bg"] = "gray"

    #Clear second column

    row0Color2["bg"] = "gray"
    row1Color2["bg"] = "gray"
    row2Color2["bg"] = "gray"
    row3Color2["bg"] = "gray"
    row4Color2["bg"] = "gray"
    row5Color2["bg"] = "gray"    
    row6Color2["bg"] = "gray"
    row7Color2["bg"] = "gray"
    row8Color2["bg"] = "gray"
    row9Color2["bg"] = "gray"
    row10Color2["bg"] = "gray"
    row11Color2["bg"] = "gray"

    #Clear third column

    row0Color3["bg"] = "gray"
    row1Color3["bg"] = "gray"
    row2Color3["bg"] = "gray"
    row3Color3["bg"] = "gray"
    row4Color3["bg"] = "gray"
    row5Color3["bg"] = "gray"    
    row6Color3["bg"] = "gray"
    row7Color3["bg"] = "gray"
    row8Color3["bg"] = "gray"
    row9Color3["bg"] = "gray"
    row10Color3["bg"] = "gray"
    row11Color3["bg"] = "gray"

    #Clear fourth column

    row0Color4["bg"] = "gray"
    row1Color4["bg"] = "gray"
    row2Color4["bg"] = "gray"
    row3Color4["bg"] = "gray"
    row4Color4["bg"] = "gray"
    row5Color4["bg"] = "gray"    
    row6Color4["bg"] = "gray"
    row7Color4["bg"] = "gray"
    row8Color4["bg"] = "gray"
    row9Color4["bg"] = "gray"
    row10Color4["bg"] = "gray"
    row11Color4["bg"] = "gray"

    #Clear fifth column

    row0Color5["bg"] = "gray"
    row1Color5["bg"] = "gray"
    row2Color5["bg"] = "gray"
    row3Color5["bg"] = "gray"
    row4Color5["bg"] = "gray"
    row5Color5["bg"] = "gray"    
    row6Color5["bg"] = "gray"
    row7Color5["bg"] = "gray"
    row8Color5["bg"] = "gray"
    row9Color5["bg"] = "gray"
    row10Color5["bg"] = "gray"
    row11Color5["bg"] = "gray"

    #Clear message box
    
    messageLabel1 = Label(frame_text, text= "")
    messageLabel1.grid(row=0, column=0, sticky=E+W+N+S)

    #Add message label back

    start_message_label = Label(frame_text, text= "MESSAGE:",fg = "black", font= 'Arial 10 bold', justify=CENTER)
    start_message_label.grid(row=0, column=0)

  
button_clear = Button(frame_buttons, text="CLEAR",bg = "gray", fg = "black", state= DISABLED, command = clearFunction, padx=30, pady=5)
button_clear.grid(row=4, column=0, padx=10, pady=10, ipadx=10, sticky="ew")

#Quit Commmand

button_quit = Button(frame_buttons, text="QUIT",bg = "gray", fg = "black", command=window.destroy, padx=30, pady=5).grid(row=5, column=0, padx=10, pady=10, ipadx=10, sticky="ew")

###Creating widgets for frame_colours

##Creating colours table within the frame_colours

#Creating radiobuttons to pick line to be evaluated

#Variable to pass the value select by radiobutton
r=IntVar()

r.set("1") #Set initial radiobutton value

line_selected = r.get()

def radioclicked(value):
    global line_selected
    line_selected=value
    
#Creating Radiobutton
    
Radiobutton(frame_colours, text= "Line 1", variable=r, value = 1, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=0, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 2", variable=r, value = 2, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=1, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 3", variable=r, value = 3, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=2, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 4", variable=r, value = 4, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=3, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 5", variable=r, value = 5, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=4, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 6", variable=r, value = 6, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=5, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 7", variable=r, value = 7, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=6, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 8", variable=r, value = 8, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=7, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 9", variable=r, value = 9, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=8, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 10", variable=r, value = 10, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=9, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 11", variable=r, value = 11, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=10, column=5,padx=5, pady=5)
Radiobutton(frame_colours, text= "Line 12", variable=r, value = 12, command=lambda:radioclicked(r.get()),padx=5, pady=5).grid(row=11, column=5,padx=5, pady=5)

#creating colours matrix 5x12

row0Color1 = Button(frame_colours, text="", bg = "gray", fg = "black", padx=30, pady=5)
row0Color1.grid(row=0, column=0,padx=5, pady=5)

row0Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row0Color2.grid(row=0, column=1,padx=5, pady=5)

row0Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row0Color3.grid(row=0, column=2,padx=5, pady=5)

row0Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row0Color4 .grid(row=0, column=3,padx=5, pady=5)

row0Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row0Color5.grid(row=0, column=4,padx=5, pady=5)

row1Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row1Color1.grid(row=1, column=0,padx=5, pady=5)

row1Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row1Color2.grid(row=1, column=1,padx=5, pady=5)

row1Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row1Color3.grid(row=1, column=2,padx=5, pady=5)

row1Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row1Color4.grid(row=1, column=3,padx=5, pady=5)

row1Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row1Color5.grid(row=1, column=4,padx=5, pady=5)

row2Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row2Color1.grid(row=2, column=0,padx=5, pady=5)

row2Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row2Color2.grid(row=2, column=1,padx=5, pady=5)

row2Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row2Color3.grid(row=2, column=2,padx=5, pady=5)

row2Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row2Color4.grid(row=2, column=3,padx=5, pady=5)

row2Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row2Color5.grid(row=2, column=4,padx=5, pady=5)

row3Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row3Color1.grid(row=3, column=0,padx=5, pady=5)

row3Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row3Color2.grid(row=3, column=1,padx=5, pady=5)

row3Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row3Color3.grid(row=3, column=2,padx=5, pady=5)

row3Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row3Color4.grid(row=3, column=3,padx=5, pady=5)

row3Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row3Color5.grid(row=3, column=4,padx=5, pady=5)

row4Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row4Color1.grid(row=4, column=0,padx=5, pady=5)

row4Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row4Color2.grid(row=4, column=1,padx=5, pady=5)

row4Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row4Color3.grid(row=4, column=2,padx=5, pady=5)

row4Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row4Color4.grid(row=4, column=3,padx=5, pady=5)

row4Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row4Color5.grid(row=4, column=4,padx=5, pady=5)

row5Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row5Color1.grid(row=5, column=0,padx=5, pady=5)

row5Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row5Color2.grid(row=5, column=1,padx=5, pady=5)

row5Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row5Color3.grid(row=5, column=2,padx=5, pady=5)

row5Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row5Color4.grid(row=5, column=3,padx=5, pady=5)

row5Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row5Color5.grid(row=5, column=4,padx=5, pady=5)

row6Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row6Color1.grid(row=6, column=0,padx=5, pady=5)

row6Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row6Color2.grid(row=6, column=1,padx=5, pady=5)

row6Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row6Color3.grid(row=6, column=2,padx=5, pady=5)

row6Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row6Color4.grid(row=6, column=3,padx=5, pady=5)

row6Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row6Color5.grid(row=6, column=4,padx=5, pady=5)

row7Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row7Color1.grid(row=7, column=0,padx=5, pady=5)

row7Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row7Color2.grid(row=7, column=1,padx=5, pady=5)

row7Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row7Color3.grid(row=7, column=2,padx=5, pady=5)

row7Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row7Color4.grid(row=7, column=3,padx=5, pady=5)

row7Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row7Color5.grid(row=7, column=4,padx=5, pady=5)

row8Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row8Color1.grid(row=8, column=0,padx=5, pady=5)

row8Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row8Color2.grid(row=8, column=1,padx=5, pady=5)

row8Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row8Color3.grid(row=8, column=2,padx=5, pady=5)

row8Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row8Color4.grid(row=8, column=3,padx=5, pady=5)

row8Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row8Color5.grid(row=8, column=4,padx=5, pady=5)

row9Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row9Color1.grid(row=9, column=0,padx=5, pady=5)

row9Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row9Color2.grid(row=9, column=1,padx=5, pady=5)

row9Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row9Color3.grid(row=9, column=2,padx=5, pady=5)

row9Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row9Color4.grid(row=9, column=3,padx=5, pady=5)

row9Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row9Color5.grid(row=9, column=4,padx=5, pady=5)

row10Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row10Color1.grid(row=10, column=0,padx=5, pady=5)

row10Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row10Color2.grid(row=10, column=1,padx=5, pady=5)

row10Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row10Color3.grid(row=10, column=2,padx=5, pady=5)

row10Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row10Color4.grid(row=10, column=3,padx=5, pady=5)

row10Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row10Color5.grid(row=10, column=4,padx=5, pady=5)

row11Color1 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row11Color1.grid(row=11, column=0,padx=5, pady=5)

row11Color2 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row11Color2.grid(row=11, column=1,padx=5, pady=5)

row11Color3 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row11Color3.grid(row=11, column=2,padx=5, pady=5)

row11Color4 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row11Color4.grid(row=11, column=3,padx=5, pady=5)

row11Color5 = Button(frame_colours, text="",bg = "gray", fg = "black", padx=30, pady=5)
row11Color5.grid(row=11, column=4,padx=5, pady=5)

##Creating hiden colours row within the frame_hide_colours

##Adding colours dropdown and select label

#Adding Select Colours label
selectLabel= Label(frame_select, text = "SELECT",fg = "black", font= 'Arial 10 bold',padx=5, pady=5)
selectLabel.grid(row=0, column=0, padx=5, pady=5)

#Variable to pass item selected into selectedColoursList
clicked = StringVar()
clicked.set(coloursList[0]) #default value

#adding a dropdown menu
colourDrop = OptionMenu(frame_select, clicked, *coloursList)
colourDrop.grid(row=0, column=1, padx=5, pady=5)
colourDrop.config(width=8) #Prevent from resizing

# adding first Hiden colour Button
firstHidenColour = Button(frame_hiden_colours, text = "", bg = "gray", state = "disabled" , fg= "black", padx=30, pady=5)
firstHidenColour.grid(row = 2, column = 0,padx=5, pady=5)

# adding second Hiden colour Button
secondHidenColour = Button(frame_hiden_colours, text = "", bg = "gray", state = "disabled", fg= "black", padx=30, pady=5)
secondHidenColour.grid(row = 2, column = 1,padx=5, pady=5)

# adding third Hided colour Button
thirdHidenColour = Button(frame_hiden_colours, text = "", bg = "gray", state = "disabled", fg= "black", padx=30, pady=5)
thirdHidenColour.grid(row = 2, column = 2,padx=5, pady=5)

# adding fourth Hided colour Button
fourthHidenColour = Button(frame_hiden_colours, text = "", bg = "gray", state = "disabled", fg= "black", padx=30, pady=5)
fourthHidenColour.grid(row = 2, column = 3,padx=5, pady=5)

# adding fifth Hided colour Button
fifthHidenColour = Button(frame_hiden_colours, text = "", bg = "gray", state= "disabled", fg= "black", padx=30, pady=5)
fifthHidenColour.grid(row = 2, column = 4,padx=5, pady=5)

#placing Colours key into hidden colours frame

colour_key_label = Label(frame_hiden_colours, text= "COLOURS KEY", fg = "black", font= 'Arial 10 bold', padx=1, pady=1)
colour_key_label.grid(row=2, column=5, padx=1, pady=1)

##adding Picked colour Buttons

def changeFirstColour():
    global line_selected
    global mySelectedColoursList
    firstColour["bg"] = clicked.get()
    if line_selected == 1:
        row0Color1["bg"] = clicked.get()
    elif line_selected == 2:
        row1Color1["bg"] = clicked.get()
    elif line_selected == 3:
        row2Color1["bg"] = clicked.get()
    elif line_selected == 4:
        row3Color1["bg"] = clicked.get()
    elif line_selected == 5:
        row4Color1["bg"] = clicked.get()
    elif line_selected == 6:
        row5Color1["bg"] = clicked.get()    
    elif line_selected == 7:
        row6Color1["bg"] = clicked.get()
    elif line_selected == 8:
        row7Color1["bg"] = clicked.get()
    elif line_selected == 9:
        row8Color1["bg"] = clicked.get()
    elif line_selected == 10:
        row9Color1["bg"] = clicked.get()
    elif line_selected == 11:
        row10Color1["bg"] = clicked.get()
    else:
        row11Color1["bg"] = clicked.get()
     
    mySelectedColoursList.insert(0, clicked.get()) #add new item to the colour list
    mySelectedColoursList.pop(1) #remove next item (n+1) to the colour list
  
# adding first colour
firstColour = Button(frame_select, text = "", bg = "gray", fg= "black", state= DISABLED, command = changeFirstColour, padx=30, pady=5)
firstColour.grid(row = 0, column = 2,padx=5, pady=5)

def changeSecondColour():  
    global line_selected
    global mySelectedColoursList
    
    secondColour["bg"] = clicked.get()
    if line_selected == 1:
        row0Color2["bg"] = clicked.get()
    elif line_selected == 2:
        row1Color2["bg"] = clicked.get()
    elif line_selected == 3:
        row2Color2["bg"] = clicked.get()
    elif line_selected == 4:
        row3Color2["bg"] = clicked.get()
    elif line_selected == 5:
        row4Color2["bg"] = clicked.get()
    elif line_selected == 6:
        row5Color2["bg"] = clicked.get()    
    elif line_selected == 7:
        row6Color2["bg"] = clicked.get()
    elif line_selected == 8:
        row7Color2["bg"] = clicked.get()
    elif line_selected == 9:
        row8Color2["bg"] = clicked.get()
    elif line_selected == 10:
        row9Color2["bg"] = clicked.get()
    elif line_selected == 11:
        row10Color2["bg"] = clicked.get()
    else:
        row11Color2["bg"] = clicked.get()

    mySelectedColoursList.insert(1, clicked.get())
    mySelectedColoursList.pop(2) #remove next item (n+1) to the colour list

# adding second colour
secondColour = Button(frame_select, text = "", bg = "gray", fg= "black", state= DISABLED, command = changeSecondColour, padx=30, pady=5)
secondColour.grid(row = 0, column = 3,padx=5, pady=5)

def changeThirdColour():  
    global mySelectedColoursList
    global line_selected

    thirdColour["bg"] = clicked.get()
    if line_selected == 1:
        row0Color3["bg"] = clicked.get()
    elif line_selected == 2:
        row1Color3["bg"] = clicked.get()
    elif line_selected == 3:
        row2Color3["bg"] = clicked.get()
    elif line_selected == 4:
        row3Color3["bg"] = clicked.get()
    elif line_selected == 5:
        row4Color3["bg"] = clicked.get()
    elif line_selected == 6:
        row5Color3["bg"] = clicked.get()    
    elif line_selected == 7:
        row6Color3["bg"] = clicked.get()
    elif line_selected == 8:
        row7Color3["bg"] = clicked.get()
    elif line_selected == 9:
        row8Color3["bg"] = clicked.get()
    elif line_selected == 10:
        row9Color3["bg"] = clicked.get()
    elif line_selected == 11:
        row10Color3["bg"] = clicked.get()
    else:
        row11Color3["bg"] = clicked.get()

    mySelectedColoursList.insert(2, clicked.get())
    mySelectedColoursList.pop(3) #remove next item (n+1) to the colour list

# adding third colour
thirdColour = Button(frame_select, text = "", bg = "gray", fg= "black", state= DISABLED, command = changeThirdColour, padx=30, pady=5)
thirdColour.grid(row = 0, column = 4,padx=5, pady=5)

def changeFourthColour():  
    global mySelectedColoursList
    global line_selected

    fourthColour["bg"] = clicked.get()
    if line_selected == 1:
        row0Color4["bg"] = clicked.get()
    elif line_selected == 2:
        row1Color4["bg"] = clicked.get()
    elif line_selected == 3:
        row2Color4["bg"] = clicked.get()
    elif line_selected == 4:
        row3Color4["bg"] = clicked.get()
    elif line_selected == 5:
        row4Color4["bg"] = clicked.get()
    elif line_selected == 6:
        row5Color4["bg"] = clicked.get()    
    elif line_selected == 7:
        row6Color4["bg"] = clicked.get()
    elif line_selected == 8:
        row7Color4["bg"] = clicked.get()
    elif line_selected == 9:
        row8Color4["bg"] = clicked.get()
    elif line_selected == 10:
        row9Color4["bg"] = clicked.get()
    elif line_selected == 11:
        row10Color4["bg"] = clicked.get()
    else:
        row11Color4["bg"] = clicked.get()

    mySelectedColoursList.insert(3, clicked.get())
    mySelectedColoursList.pop(4) #remove next item (n+1) to the colour list

# adding fourth colour
fourthColour = Button(frame_select, text = "", bg = "gray", fg= "black", state= DISABLED, command = changeFourthColour, padx=30, pady=5)
fourthColour.grid(row = 0, column = 5,padx=5, pady=5)

def changeFifthColour():  

    global line_selected
    global mySelectedColoursList

    fifthColour["bg"] = clicked.get()
    if line_selected == 1:
        row0Color5["bg"] = clicked.get()
    elif line_selected == 2:
        row1Color5["bg"] = clicked.get()
    elif line_selected == 3:
        row2Color5["bg"] = clicked.get()
    elif line_selected == 4:
        row3Color5["bg"] = clicked.get()
    elif line_selected == 5:
        row4Color5["bg"] = clicked.get()
    elif line_selected == 6:
        row5Color5["bg"] = clicked.get()    
    elif line_selected == 7:
        row6Color5["bg"] = clicked.get()
    elif line_selected == 8:
        row7Color5["bg"] = clicked.get()
    elif line_selected == 9:
        row8Color5["bg"] = clicked.get()
    elif line_selected == 10:
        row9Color5["bg"] = clicked.get()
    elif line_selected == 11:
        row10Color5["bg"] = clicked.get()
    else:
        row11Color5["bg"] = clicked.get()

    mySelectedColoursList.insert(4, clicked.get())
    mySelectedColoursList.pop(5) #remove next item (n+1) to the colour list

# adding fifth colour
fifthColour = Button(frame_select, text = "", bg = "gray", fg= "black", state= DISABLED, command = changeFifthColour, padx=30, pady=5)
fifthColour.grid(row = 0, column = 6,padx=5, pady=5)

##Creating widgets for frame_tips

commonColoursNumber = int()
numberRightColours = int()

#Creating colours tip labels

row0_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=0, column=0,padx=5, pady=7.5)

row1_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=1, column=0,padx=5, pady=7.5)

row2_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=2, column=0,padx=5, pady=7.5)

row3_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=3, column=0,padx=5, pady=7.5)

row4_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=4, column=0,padx=5, pady=7.5)

row5_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=5, column=0,padx=5, pady=7.5)

row6_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=6, column=0,padx=5, pady=7.5)

row7_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=7, column=0,padx=5, pady=7.5)

row8_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=8, column=0,padx=5, pady=7.5)

row9_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=9, column=0,padx=5, pady=7.5)

row10_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=10, column=0,padx=5, pady=7.5)

row11_colour_tip = Label(frame_tips, text = ("Colours: " + str(commonColoursNumber)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=11, column=0,padx=5, pady=7.5)

#Creating right colours tip labels

row0_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=0, column=1,padx=5, pady=7.5)

row1_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=1, column=1,padx=5, pady=7.5)

row2_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=2, column=1,padx=5, pady=7.5)

row3_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=3, column=1,padx=5, pady=7.5)

row4_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=4, column=1,padx=5, pady=7.5)

row5_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=5, column=1,padx=5, pady=7.5)

row6_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=6, column=1,padx=5, pady=7.5)

row7_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=7, column=1,padx=5, pady=7.5)

row8_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=8, column=1,padx=5, pady=7.5)

row9_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=9, column=1,padx=5, pady=7.5)

row10_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=10, column=1,padx=5, pady=7.5)

row11_Rigth_tip = Label(frame_tips, text = ("Right: "+ str(numberRightColours)), borderwidth=2, relief = "solid",padx=5, pady=5).grid(row=11, column=1,padx=5, pady=7.5)

window.mainloop()
