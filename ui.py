from tkinter import *  # Imports all classes and functions from tkinter for GUI building
from quiz_brain import QuizBrain  # Imports the quiz logic class to interact with the GUI

THEME_COLOR = "#375362"     # Sets a custom color for consistent styling (dark blue-gray)

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain      # Stores the QuizBrain instance for logic access

        #Setup main window
        self.window = Tk()  # Creates the main application window
        self.window.title("Quizzler")  # Sets the title of the window
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)  # Adds padding and background color

        #Score system
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)      # Places the label in the top right
        
        self.canvas = Canvas(width=300, height=250, bg="white")     # Creates a canvas (a drawable area) with a white background to display questions.

        self.question_text = self.canvas.create_text(
            150, 125, width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)    # Places the canvas across 2 columns in row 1 with vertical padding.

        #True Button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
     

        #False Button 
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()    # Load the first question
        self.window.mainloop()      # Start the GUI event loop

    def get_next_question(self):
        self.canvas.config(bg="white")  # Reset canvas color
        if self.quiz.still_has_questions():  # Checks if questions remain
            self.score_label.config(text=f"Score: {self.quiz.score}")  # Update score label
            q_text = self.quiz.next_question()  # Fetch next question
            self.canvas.itemconfig(self.question_text, text=q_text)  # Update canvas text
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")  # Disable True button
            self.false_button.config(state="disabled")  # Disable False button
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self): 
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")  # Show green if correct
        else:
            self.canvas.config(bg="red")  # Show red if wrong
        self.window.after(1000, self.get_next_question)     # Waits 1 second before loading the next question







