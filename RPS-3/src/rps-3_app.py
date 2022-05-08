from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from checklistcombobox import ChecklistCombobox
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class RPS:
  def __init__(self,root):
    self.root = root
    self.root.config(bg="white")
    self.root.geometry("653x610")
    self.root.title("Probability : Dissected")

    self.df = pd.DataFrame(data=[[0,0,0,0,0,0],[0,0,0,0,0,0]],columns=["No. of Wins","No. of Draws","Win Percentage","No. of Rocks","No. of Papers","No. of Scissors"])
    self.images = [ImageTk.PhotoImage(Image.open("rock.png").resize((100,100))),ImageTk.PhotoImage(Image.open("paper.png").resize((100,100))),ImageTk.PhotoImage(Image.open("scissors.png").resize((100,100)))]
    self.running = False

    # parameter frame
    self.paraframe = LabelFrame(self.root,bg="white",text="Parameters",labelanchor="n")
    self.paraframe.grid(row=0,column=0,padx=5,pady=5)

    # player 1 parameters
    self.play1para = LabelFrame(self.paraframe,bg="white",text="Player 1",labelanchor="n")
    self.play1para.grid(row=0,column=0,padx=5,pady=5)

    # player 1 - rock
    self.play1rlabel = Label(self.play1para,bg="white",text="Rock :")
    self.play1rlabel.grid(row=0,column=0,padx=5,pady=5)
    self.play1r = Spinbox(self.play1para,bg="white",from_=0.0,to=1.0,increment=0.01,width=5)
    self.play1r.grid(row=0,column=1,padx=5,pady=5)

    # player 1 - paper
    self.play1plabel = Label(self.play1para,bg="white",text="Paper :")
    self.play1plabel.grid(row=1,column=0,padx=5,pady=5)
    self.play1p = Spinbox(self.play1para,bg="white",from_=0.0,to=1.0,increment=0.01,width=5)
    self.play1p.grid(row=1,column=1,padx=5,pady=5)

    # player 1 - scissors
    self.play1slabel = Label(self.play1para,bg="white",text="Scissors :")
    self.play1slabel.grid(row=2,column=0,padx=5,pady=5)
    self.play1s = Spinbox(self.play1para,bg="white",from_=0.0,to=1.0,increment=0.01,width=5)
    self.play1s.grid(row=2,column=1,padx=5,pady=5)

    self.play1entry = [self.play1r,self.play1p,self.play1s]

    for i in self.play1entry:
      i.delete(0,END)
      i.insert(0,"0.33")
    
    # player 2 parameters
    self.play2para = LabelFrame(self.paraframe,bg="white",text="Player 2",labelanchor="n")
    self.play2para.grid(row=0,column=1,padx=5,pady=5)

    # player 2 - rock
    self.play2rlabel = Label(self.play2para,bg="white",text="Rock :")
    self.play2rlabel.grid(row=0,column=0,padx=5,pady=5)
    self.play2r = Spinbox(self.play2para,bg="white",from_=0.0,to=1.0,increment=0.01,width=5)
    self.play2r.grid(row=0,column=1,padx=5,pady=5)

    # player 2 - paper
    self.play2plabel = Label(self.play2para,bg="white",text="Paper :")
    self.play2plabel.grid(row=1,column=0,padx=5,pady=5)
    self.play2p = Spinbox(self.play2para,bg="white",from_=0,to=1,increment=0.01,width=5)
    self.play2p.grid(row=1,column=1,padx=5,pady=5)

    # player 2 - scissors
    self.play2slabel = Label(self.play2para,bg="white",text="Scissors :")
    self.play2slabel.grid(row=2,column=0,padx=5,pady=5)
    self.play2s = Spinbox(self.play2para,bg="white",from_=0.0,to=1.0,increment=0.01,width=5)
    self.play2s.grid(row=2,column=1,padx=5,pady=5)

    self.play2entry = [self.play2r,self.play2p,self.play2s]

    for i in self.play2entry:
      i.delete(0,END)
      i.insert(0,"0.33")

    # number of runs
    self.runlabel = Label(self.paraframe, bg="white",text="Number of Runs : ")
    self.runlabel.grid(row=1,column=0,padx=5,pady=5)
    self.runval = Spinbox(self.paraframe,bg="white",from_=1000,to=100000,increment=500,width=10)
    self.runval.grid(row=1,column=1,padx=5,pady=5)

    # graph option label
    self.graphoptlabel = Label(self.paraframe,bg="white",text="Graph Options :")
    self.graphoptlabel.grid(row=2,column=0,padx=5,pady=5)

    # graph options
    self.graphopttable = ChecklistCombobox(self.paraframe,values=("Pie Chart","Line Graph"))
    self.graphopttable.grid(row=2,column=1,padx=5,pady=5)

    # run button
    self.runbutton = Button(self.paraframe,bg="white",text="Run",width=15,font="helvetica 10",command=lambda: self.run(),relief=GROOVE)
    self.runbutton.grid(row=3,column=0,padx=5,pady=5)

    # pause button
    self.paused = False
    self.pausebutton = Button(self.paraframe,bg="white",text="Pause",width=15,font="helvetica 10",command=lambda: self.pause(),relief=GROOVE)
    self.pausebutton.grid(row=3,column=1,padx=5,pady=5)
    

    # simulation frame
    self.simframe = LabelFrame(self.root,bg="white",text="Simulation",labelanchor="n")
    self.simframe.grid(row=0,column=1,padx=5,pady=5)

    # player 1 canvas
    self.play1frame = LabelFrame(self.simframe,bg="white",text="Player 1",labelanchor="n")
    self.play1frame.grid(row=0,column=0,columnspan=2,padx=15,pady=15)
    self.play1canvas = Canvas(self.play1frame,width=100,height=100,bg="white")
    self.play1canvas.grid(row=0,column=0,padx=5,pady=5)

    # vs label
    self.vslabel = Label(self.simframe,bg="white",text="vs",font="helvetica 18 bold")
    self.vslabel.grid(row=0,column=2,columnspan=2,padx=5,pady=5)
    
    # player 2 canvas
    self.play2frame = LabelFrame(self.simframe,bg="white",text="Player 2",labelanchor="n")
    self.play2frame.grid(row=0,column=4,columnspan=2,padx=15,pady=15)
    self.play2canvas = Canvas(self.play2frame,width=100,height=100,bg="white")
    self.play2canvas.grid(row=0,column=1,padx=5,pady=5)

    # won label
    self.wonlabel = Label(self.simframe,bg="white",text="Player Won :",font="helvetica 10")
    self.wonlabel.grid(row=1,column=1,columnspan=2,pady=3)

    # won player label
    self.wonplayerlabel = Label(self.simframe,bg="white",text="",font="helvetica 10")
    self.wonplayerlabel.grid(row=1,column=3,columnspan=2,pady=3)

    # run label
    self.runslabel = Label(self.simframe,bg="white",text="Run Number :",font="helvetica 10")
    self.runslabel.grid(row=2,column=1,columnspan=2,pady=3)

    # run label
    self.runnumvar = StringVar()
    self.runnumlabel = Label(self.simframe,bg="white",textvariable=self.runnumvar,font="helvetica 10")
    self.runnumlabel.grid(row=2,column=3,columnspan=2,pady=3)


    # statistics frame
    self.statsframe = LabelFrame(self.root,bg="white",text="Statistics",labelanchor="n")
    self.statsframe.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

    # statistics table
    self.statstable = Treeview(self.statsframe,height=2,padding=5)
    self.statstable.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

    # table columns
    self.statstable["columns"] = ("","No. of Wins","No. of Draws","Win Percentage","No. of Rocks","No. of Papers","No. of Scissors")

    self.statstable.column("#0",width=0,stretch=NO)
    self.statstable.heading("#0",text="",anchor=CENTER)

    for i in self.statstable["columns"]:
      if i == "Win Percentage":
        self.statstable.column(i,anchor=CENTER,width=95)
      else:
        self.statstable.column(i,anchor=CENTER,width=87)

      self.statstable.heading(i,anchor=CENTER,text=i)

    # inserting values
    self.statstable.insert(parent="",index=END,iid=1,text="",values=("Player 1",0,0,"0%",0,0,0))
    self.statstable.insert(parent="",index=END,iid=2,text="",values=("Player 2",0,0,"0%",0,0,0))

    # graph frame
    self.graphframe = LabelFrame(self.statsframe,bg="white",text="Graph 1",labelanchor="n")
    self.graphframe.grid(row=1,column=0,padx=5,pady=5)

  def run(self):
    try:
      if not self.running:
        # get number of runs
        self.runnum = int(self.runval.get())
        self.runtemp = self.runnum 

        # resetting data
        self.df = pd.DataFrame(data=[[0,0,0,0,0,0],[0,0,0,0,0,0]],columns=["No. of Wins","No. of Draws","Win Percentage","No. of Rocks","No. of Papers","No. of Scissors"])
        self.statstable.item(item=1,values=("Player 1",0,0,"0%",0,0,0))
        self.statstable.item(item=2,values=("Player 2",0,0,"0%",0,0,0))

        if self.paused:
          self.paused = False
          self.pausebutton.config(text="Pause")

        # get all probabilities
        self.play1prob = [float(i.get()) for i in self.play1entry]
        self.play2prob = [float(i.get()) for i in self.play2entry]

        # check that probabilities add to 1
        if round(sum(self.play1prob)) == 1 and round(sum(self.play2prob)) == 1:
          # start loop
          self.running = True
          self.loop()
        else:
          showerror(title="Invalid Probability Inputs",message="Probability rates do not add up to 1")

    except ValueError:
      showerror(title="Invalid Run Number Input",message="The value you inputted was invalid.\nPlease enter a number.")

  def pause(self):
    self.paused = not self.paused
    self.running = not self.running
    self.loop()

    if self.paused:
      self.pausebutton.config(text="Unpause")
    else:
      self.pausebutton.config(text="Pause")

  def loop(self):
    if self.running and self.runnum >= 1:
      # display run number
      self.runnumvar.set(abs(self.runtemp-self.runnum+1))

      # choose player 1
      play1 = self.choose(self.play1prob,1)

      if play1 == 0:
        self.update(1,"No. of Rocks")
      elif play1 == 1:
        self.update(1,"No. of Papers")
      elif play1 == 2:
        self.update(1,"No. of Scissors")

      # choose player 2
      play2 = self.choose(self.play2prob,2)

      if play2 == 0:
        self.update(2,"No. of Rocks")
      elif play2 == 1:
        self.update(2,"No. of Papers")
      elif play2 == 2:
        self.update(2,"No. of Scissors")

      self.compare(play1,play2)

      if self.runnum == 1:
        self.running = False
        self.display()

      # run again 
      self.runnum -= 1
      self.root.after(1,lambda: self.loop())
        

  def choose(self,prob:list,player:int):
    # rock - 0, paper - 1, scissors - 2
    choice = (list(np.random.multinomial(1,prob))).index(1)

    if player == 1:
      self.play1canvas.delete("all")
      if choice == 0:
        self.play1canvas.create_image(0,0,anchor="nw",image=self.images[0])
      elif choice == 1:
        self.play1canvas.create_image(0,0,anchor="nw",image=self.images[1])
      elif choice == 2:
        self.play1canvas.create_image(0,0,anchor="nw",image=self.images[2])

    elif player == 2:
      self.play2canvas.delete("all")
      if choice == 0:
        self.play2canvas.create_image(0,0,anchor="nw",image=self.images[0])
      elif choice == 1:
        self.play2canvas.create_image(0,0,anchor="nw",image=self.images[1])
      elif choice == 2:
        self.play2canvas.create_image(0,0,anchor="nw",image=self.images[2])

    return choice
    
  def compare(self,p1:int,p2:int):
    if p1 == p2:
      # draw
      self.update(1,"No. of Draws")
      self.update(2,"No. of Draws")
      self.wonplayerlabel.config(text="Draw")
      
    elif (p1 == 0 and p2 == 1) or (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 0):
      # player 2 wins
      self.update(2,"No. of Wins")
      self.wonplayerlabel.config(text="Player 2")

    elif (p1 == 0 and p2 == 2) or (p1 == 1 and p2 == 0) or (p1 == 2 and p2 == 1):
      # player 1 wins      
      self.update(1,"No. of Wins")
      self.wonplayerlabel.config(text="Player 1")

  def update(self,player:int,col:str):
    if player == 1:
      # update df
      self.df.at[0,col] += 1

      # update stats
      temptuple = ()
      for i in range(self.df.loc[0].size):
        if i == 2:
          temptuple += (f'{round(((self.df.at[player-1,"No. of Wins"])/abs(self.runtemp-self.runnum+1))*100,2)}%',)
        else:
          temptuple += (int(list(self.df.loc[0])[i]),)

      self.statstable.item(item=1,values=("Player 1",)+temptuple)

    elif player == 2:
      # update df
      self.df.at[1,col] += 1

      # update stats
      temptuple = ()
      for i in range(self.df.loc[1].size):
        if i == 2:
          temptuple += (f'{round(((self.df.at[player-1,"No. of Wins"])/abs(self.runtemp-self.runnum+1))*100,2)}%',)
        else:
          temptuple += (int(list(self.df.loc[1])[i]),)

      self.statstable.item(item=2,values=("Player 2",)+temptuple)

    self.df.at[player-1,"Win Percentage"] = round(((self.df.at[player-1,"No. of Wins"])/abs(self.runtemp-self.runnum+1))*100,2)
    

  def display(self):
    graphs = [self.graphopttable.get()] if type(self.graphopttable.get()) != list else self.graphopttable.get()
    # print(graphs)
    


root = Tk()
RPSwin = RPS(root)

root.mainloop()