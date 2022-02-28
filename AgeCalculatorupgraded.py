#Source https://codingshiksha.com/python/python-tkinter-gui-script-to-make-a-simple-age-calculator-from-date-of-birth-dob-full-project-for-beginners/
# Age Calculator
from tkinter import * #this is a Gui tool kit
from datetime import date #data base for time and date

root = Tk() #instalizes the interpeter with the parameters
root.geometry("500x500") #parameters for the gui #changed the Dimensions to clean up the extra space
root.title("G's Age Calculator") # this function give a title the Gui
root.config(bg="black") # added this line of code to add color to the gui


def calculateAge(): # This is section of code that calculates the persons age
    today = date.today() # gets todays date
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get())) #takes the data inputed by the user
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))  #to get the difference in todays date and the day that person is born
    Label(text=f"{nameValue.get()} your age is {age} today").grid(row=6, column=1) #this displays the message of your age today using the lable function

Label(text="Name").grid(row=1, column=0, padx=90) # lines 16-19 are all labels for the gui with parameter on where to align them on the gui
Label(text="Year").grid(row=2, column=0)
Label(text="Month").grid(row=3, column=0)
Label(text="Day").grid(row=4, column=0)

nameValue = StringVar()  # lines 21-24helps manage the variables inputed by the user as string
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue) # lines 26-29creates the textbox entry for the gui for the user to input data
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)

nameEntry.grid(row=1, column=1, pady=10) # lines 31-34 this code is for the how the text boxes are aligned on the gui
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)
computeButton = Button(text="CalculateAge", command=calculateAge) #this code is to create a button to run the code to compute the age of the user
computeButton.grid(row=5, column=1, pady=10) #this code is for the positioning of the button
exitButton =Button(text="Exit Application!",command=exit)#added this code to close the the application
exitButton.grid(row=5, column=0, pady=10)
root.mainloop() #this code keeps applications running until the exit button is clicked




