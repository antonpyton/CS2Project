from tkinter import *
import csv


class GUI:
    def __init__(self, window):
        self.window = window
        window.title('Letter Grade Calculator')
        window.geometry('250x180')
        window.resizable(False, False)
        self.frame_name = Frame(self.window)
        self.nameLabel = Label(self.frame_name, text='Name')
        self.displayLabel = Label(self.frame_name, text='Enter name and number grade')
        self.gradeLabel = Label(self.frame_name, text='Grade')
        self.outputLabel = Label(self.frame_name, text='')
        self.nameEntry = Entry(self.frame_name)
        self.gradeEntry = Entry(self.frame_name)
        self.saveButton = Button(self.window, text='Get Grade', command=self.clicked)
        self.frame_name.pack(anchor='w', pady=10)
        self.saveButton.pack(side='right', padx=10)
# sets position of labels and entry boxes
        self.nameLabel.grid(row=0, column=0)
        self.nameEntry.grid(row=0, column=1)
        self.gradeLabel.grid(row=1, column=0)
        self.gradeEntry.grid(pady=5, row=1, column=1)
        self.displayLabel.grid(row=2, column=1)
        self.outputLabel.grid(row=3, column=1)

    def clicked(self):
        def export():
            # resets entry boxes and displays output + exports data to CSV
            self.displayLabel.configure(text='Success!')
            self.outputLabel.configure(text=f'{name}\'s grade of {grade} = {letter}')
            self.nameEntry.delete(0, 'end')
            self.gradeEntry.delete(0, 'end')
            with open('gradehistory.csv', 'a', newline='') as output:
                write = csv.writer(output)
                write.writerow([name, grade, letter])

        if self.nameEntry.get() == '' and self.gradeEntry.get() == '':
            # if both name and entry are empty, ask again for input
            self.displayLabel.configure(text=f'Enter Name and Grade')
            self.outputLabel.configure(text='')
        elif self.nameEntry.get() == '':
            # if only name is empty, ask again for name input, doesn't reset entered text
            self.displayLabel.configure(text=f'Enter Name')
            self.outputLabel.configure(text='')
        elif self.gradeEntry.get() == '':
            # if only grade is empty, ask again for grade input, doesn't reset entered text
            self.displayLabel.configure(text=f'Enter Grade')
            self.outputLabel.configure(text='')
        else:
            # if name and grade is provided, check if grade is integer
            grade = self.gradeEntry.get()
            name = self.nameEntry.get()
            try:
                grade = int(grade)
            except ValueError:
                # grade is not integer, reset grade entry box, display error
                self.displayLabel.configure(text=f'Error. Please enter integer grade.')
                self.gradeEntry.delete(0, 'end')
                self.outputLabel.configure(text='')
            else:
                # if grade is valid input, display output and reset entry boxes + export result to csv
                if 97 <= grade <= 100:
                    letter = 'A+'
                elif 93 <= grade < 97:
                    letter = 'A'
                elif 90 <= grade < 93:
                    letter = 'A-'
                elif 87 <= grade < 90:
                    letter = 'B+'
                elif 83 <= grade < 87:
                    letter = 'B'
                elif 80 <= grade < 83:
                    letter = 'B-'
                elif 77 <= grade < 80:
                    letter = 'C+'
                elif 73 <= grade < 77:
                    letter = 'C'
                elif 70 <= grade < 73:
                    letter = 'C-'
                elif 67 <= grade < 70:
                    letter = 'D+'
                elif 63 <= grade < 67:
                    letter = 'D'
                elif 60 <= grade < 63:
                    letter = 'D-'
                elif 0 <= grade < 60:
                    letter = 'F'
                else:
                    letter = 'Out of range'
                export()
