import sys;
import tkinter 
from tkinter import *;

class MainFrame:		
	def main(self):
			self.totalList=["1","2","3","4","5","6","7","8","9"];
			self.playerChoice=["X","O"];
			self.player1List=[];
			self.player2List=[];
			self.winCombinationList=["123","456","789","147","258","369","159","357"];
			self.answerList=[];
			self.count=0;
			self.flag=0;
			self.value=0;
			self.count1=0;
			self.count2=0;
			self.v=IntVar;
			self.win=Tk();
			self.root=Frame(self.win,bg='white');	
			self.reset=Button(self.root,text="Reset",bg='green',fg='white');
			self.start=Button(self.root,text="Start",bg='green',fg='white');
			self.status=Label(self.root,text="",bg='white');
			self.label1=Label(self.root,text="Welcome To Tic - Tac - TOE",bg='white',fg='green');
			self.player1box=Entry(self.root,fg='black');
			self.player1name=Label(self.root,bg='white' ,fg='red',text="Player 1 Name : ");
			self.player2box=Entry(self.root,fg='black');
			self.player2name=Label(self.root,bg='white' ,fg='blue',text="Player 2 Name : ");
			self.player1nameforgame=Label(self.root,bg='white',fg='red');
			self.player2nameforgame=Label(self.root,bg='white',fg='blue');
			self.playerChoiceIcon=Listbox(self.root,height=2,width=5,bg='white');
			self.label4=Label(self.root,bg='white',fg='green',text="choose a value");
			self.playerChoiceIcon.insert(END,"red");
			self.playerChoiceIcon.insert(END,"blue");
			self.label1.grid(row=0,column=0);
			self.player1name.grid(row=1,column=0)
			self.player1box.grid(row=1,column=1);
			self.label4.grid(row=2,column=0);
			self.playerChoiceIcon.grid(row=2,column=1);
			self.player2name.grid(row=3,column=0)
			self.player2box.grid(row=3,column=1);
			self.start.grid(row=4,column=0);
			self.reset.grid(row=4,column=1);
			self.button1=Button(self.root,text="1");
			self.button2=Button(self.root,text="2");
			self.button3=Button(self.root,text="3");
			self.button4=Button(self.root,text="4");
			self.button5=Button(self.root,text="5");
			self.button6=Button(self.root,text="6");
			self.button7=Button(self.root,text="7");
			self.button8=Button(self.root,text="8");
			self.button9=Button(self.root,text="9");
			self.button1.config(bg='white',height=3,width=5);
			self.button2.config(bg='white',height=3,width=5);
			self.button3.config(bg='white',height=3,width=5);
			self.button4.config(bg='white',height=3,width=5);
			self.button5.config(bg='white',height=3,width=5);
			self.button6.config(bg='white',height=3,width=5);
			self.button7.config(bg='white',height=3,width=5);
			self.button8.config(bg='white',height=3,width=5);
			self.button9.config(bg='white',height=3,width=5);
			self.button1.bind("<ButtonPress>",self.change);
			self.button2.bind("<ButtonPress>",self.change);
			self.button3.bind("<ButtonPress>",self.change);
			self.button4.bind("<ButtonPress>",self.change);
			self.button5.bind("<ButtonPress>",self.change);
			self.button6.bind("<ButtonPress>",self.change);
			self.button7.bind("<ButtonPress>",self.change);
			self.button8.bind("<ButtonPress>",self.change);
			self.button9.bind("<ButtonPress>",self.change);
						
			self.player1nameforgame.grid(row=5,column=0);
			self.player2nameforgame.grid(row=5,column=1);
			self.reset['state']="disable";	
			self.status.grid(row=5,column=0);
			self.start.bind("<ButtonPress>",self.change);
			self.reset.bind("<ButtonPress>",self.change);
			self.player1box.bind("<Key>",self.change);
			self.player2box.bind("<Key>",self.change);
			
			self.root.pack();
			self.win.mainloop();

	def change(self,event):
			
				
			
			if(event.widget==self.button1):
				if(self.value % 2 == 0):
					self.button1['bg']=self.player1nameforgame['fg'];
					self.button1['state']='disabled';
				else:
					self.button1['bg']=self.player2nameforgame['fg'];
					self.button1['state']='disabled';
				self.data="1";
				self.checkWin(self.data,self.value,self.count1,self.count2);
				self.value=self.value+1;

			if(event.widget==self.button2):
				if(self.value % 2 == 0):
					self.button2['bg']=self.player1nameforgame['fg'];
					self.button2['state']='disabled';
				else:
					self.button2['bg']=self.player2nameforgame['fg'];
					self.button2['state']='disabled';
				self.data="2";
				self.checkWin(self.data,self.value,self.count1,self.count2);
				self.value=self.value+1;

			if(event.widget==self.button3):
				if(self.value % 2 == 0):
					self.button3['bg']=self.player1nameforgame['fg'];
					self.button3['state']='disabled';
				else:
					self.button3['bg']=self.player2nameforgame['fg'];
					self.button3['state']='disabled';
				self.data="3";
				self.checkWin(self.data,self.value,self.count1,self.count2);
				self.value=self.value+1;

			if(event.widget==self.button4):
				if(self.value % 2 == 0):
					self.button4['bg']=self.player1nameforgame['fg'];
					self.button4['state']='disabled';
				else:
					self.button4['bg']=self.player2nameforgame['fg'];
					self.button4['state']='disabled';
				self.data="4";
				self.checkWin(self.data,self.value,self.count1,self.count2);
				self.value=self.value+1;


			if(event.widget==self.button5):
				if(self.value % 2 == 0):
					self.button5['bg']=self.player1nameforgame['fg'];
					self.button5['state']='disabled';
				else:
					self.button5['bg']=self.player2nameforgame['fg'];
					self.button5['state']='disabled';
				self.data="5";
				self.checkWin(self.data,self.value,self.count1,self.count2);
				self.value=self.value+1;

			if(event.widget==self.button6):
				if(self.value % 2 == 0):
					self.button6['bg']=self.player1nameforgame['fg'];
					self.button6['state']='disabled';
				else:
					self.button6['bg']=self.player2nameforgame['fg'];
					self.button6['state']='disabled';
				self.data="6";
				self.checkWin(self.data,self.value,self.count1,self.count2);
				self.value=self.value+1;

			if(event.widget==self.button7):
				if(self.value % 2 == 0):
					self.button7['bg']=self.player1nameforgame['fg'];
					self.button7['state']='disabled';
				else:
					self.button7['bg']=self.player2nameforgame['fg'];
					self.button7['state']='disabled';
				self.data="7";
				self.checkWin(self.data,self.value,self.count1,self.count2);
				self.value=self.value+1;


			if(event.widget==self.button8):
				if(self.value % 2 == 0):
					self.button8['bg']=self.player1nameforgame['fg'];
					self.button8['state']='disabled';
				else:
					self.button8['bg']=self.player2nameforgame['fg'];
					self.button8['state']='disabled';
				self.data="8";
				self.checkWin(self.data,self.value,self.count1,self.count2);
				self.value=self.value+1;

			if(event.widget==self.button9):
				if(self.value % 2 == 0):
					self.button9['bg']=self.player1nameforgame['fg'];
					self.button9['state']='disabled';
				else:
					self.button9['bg']=self.player2nameforgame['fg'];
					self.button9['state']='disabled';
				self.data="9";
				self.checkWin(self.data,self.value,self.count1,self.count2);
				self.value=self.value+1;



			if(event.widget==self.reset):
				self.player1nameforgame['text']="";
				self.player2nameforgame['text']="";
				self.player1box['state']="active";
				self.player2box['state']="active";
				self.player2box['text']="";
				self.player2box['text']="";
				self.start['state']='active';				



			if(event.widget==self.start):
				self.name1=self.player1box.get();
				if(self.name1!=""):
					self.name2=self.player2box.get();
					if(self.name2!=""):
						self.IconValue=self.playerChoiceIcon.curselection();
						if(len(self.IconValue)>0):
							self.player1nameforgame['text']=self.name1;
							self.player2nameforgame['text']=self.name2;
							self.player1box['state']="disabled";
							self.player2box['state']="disabled";
							self.button1['state']="active";
							self.button2['state']="active";
							self.button3['state']="active";
							self.button4['state']="active";
							self.button5['state']="active";
							self.button6['state']="active";
							self.button7['state']="active";
							self.button8['state']="active";
							self.button9['state']="active";
							self.reset['state']="active";
							self.start['state']="disable";
							self.playerChoiceIcon['state']="disabled";
							self.button1.grid(row=6,column=0);
							self.button2.grid(row=6,column=1);
							self.button3.grid(row=6,column=2);
							self.button4.grid(row=7,column=0);
							self.button5.grid(row=7,column=1);
							self.button6.grid(row=7,column=2);
							self.button7.grid(row=8,column=0);
							self.button8.grid(row=8,column=1);
							self.button9.grid(row=8,column=2);
							self.status.grid(row=9,column=0);
							self.status['text']="";
							self.status['bg']='white';
							self.status['fg']='green';
							if(self.IconValue[0] is 0):
								self.playerChoice.insert(0,'X');
								self.playerChoice.insert(1,'O');
								self.player1nameforgame['fg']='red';
								self.player2nameforgame['fg']='blue';	
							else:
								self.playerChoice.insert(0,'O');
								self.playerChoice.insert(1,'X');
								self.player1nameforgame['fg']='blue';
								self.player2nameforgame['fg']='red';
							
								
						else:
							self.status['text']="Choice is required..";
					else:
						self.status['text']="player 2 name required..";
				else:
					self.status['text']="player 1 name required..";
								

	def checkWin(self,data,value,count1,count2):
		self.answer="";
		self.totalList.remove(self.data);
		if(self.value % 2 != 0):
			self.player1List.insert(self.count1,self.data);
			self.totalList.insert(int(self.data) - 1,self.playerChoice[0]);
			self.count1 = self.count1 + 1;
		else:
			self.player2List.insert(self.count2,self.data);
			self.totalList.insert(int(self.data) - 1,self.playerChoice[1]);
			self.count2 = self.count2 + 1;
		if(self.value > 4):
			self.answer = self.calculatePath();
		return self.answer;




	def calculatePath(self):
		self.w="";
		self.k=0;
		self.temp=[];
		while(self.k<len(self.winCombinationList)):
			self.item = self.winCombinationList[self.k];
			for self.var in self.item:
				self.temp.append(self.var);
			if (self.totalList[int(self.temp[0])-1] == self.totalList[int(self.temp[1])-1] and self.totalList[int(self.temp[0])-1] == self.totalList[int(self.temp[2])-1]):
				if(self.totalList[int(self.temp[0])] == self.playerChoice[0]) :
						self.w="1";
				else:
						self.w="2";
				self.endgame(self.w,self.item);
				return self.w + self.item ;
			self.k=self.k+1;
			for self.var in self.item:
				self.temp.remove(self.var);
		return "";




	def endgame(self,w,item):
			self.winplayername=self.w;
			if(self.winplayername == "1"):
				self.wincolor=self.player1nameforgame['fg'];
			else:
				self.wincolor=self.player2nameforgame['fg'];
			self.button1['state']="disabled";
			self.button2['state']="disabled";
			self.button3['state']="disabled";
			self.button4['state']="disabled";
			self.button5['state']="disabled";
			self.button6['state']="disabled";
			self.button7['state']="disabled";
			self.button8['state']="disabled";
			self.button9['state']="disabled";
			self.button1['bg']="white";
			self.button2['bg']="white";
			self.button3['bg']="white";
			self.button4['bg']="white";
			self.button5['bg']="white";
			self.button6['bg']="white";
			self.button7['bg']="white";
			self.button8['bg']="white";
			self.button9['bg']="white";
			for self.var in self.item:
				if(self.button1['text'] == self.var):
					self.button1['bg']=self.wincolor;
				if(self.button2['text'] == self.var):
					self.button2['bg']=self.wincolor;
				if(self.button3['text'] == self.var):
					self.button4['bg']=self.wincolor;
				if(self.button4['text'] == self.var):
					self.button4['bg']=self.wincolor;
				if(self.button5['text'] == self.var):
					self.button5['bg']=self.wincolor;
				if(self.button6['text'] == self.var):
					self.button6['bg']=self.wincolor;
				if(self.button7['text'] == self.var):
					self.button7['bg']=self.wincolor;
				if(self.button8['text'] == self.var):
					self.button8['bg']=self.wincolor;
				if(self.button9['text'] == self.var):
					self.button9['bg']=self.wincolor;
			self.status['text']="player "+self.winplayername+"wins with path = "+self.item;

m=MainFrame();
m.main();


