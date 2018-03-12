import sys;
import random;
totalList=["1","2","3","4","5","6","7","8","9"];
playerChoice=[];
player1List=[];
player2List=[];
winCombinationList=["123","456","789","147","258","369","159","357"];
answerList=[];
count=0;
flag=0;
value=0;
count1=0;
count2=0;
def createScreen(count,varTotalList):
		cross = 'X';
		zero = 'O';
		strg = "";
		newList=varTotalList;
		while (count < 10):
			if (count == 3 or count == 6 or count == 9) :
				print (strg + "\n--------------");
				strg="";
				if(count == 9):
					break;
			strg = strg +" | " +str(newList[count]);
			count = count + 1;
		count=0;
		return;






def checkWin(data,value,count1,count2):
		answer="";
		totalList.remove(data);
		if(value % 2 != 0):
			player1List.insert(count1,data);
			totalList.insert(int(data) - 1,playerChoice[0]);
			createScreen(count,totalList);
			count1 = count1 + 1;
		else:
			player2List.insert(count2,data);
			totalList.insert(int(data) - 1,playerChoice[1]);
			createScreen(count,totalList);
			count2 = count2 + 1;
		if(value > 4):
			answer = calculatePath();
		return answer;




def calculatePath():
		w="";
		k=0;
		temp=[];
		while(k<len(winCombinationList)):
			item = winCombinationList[k];
			for var in item:
				temp.append(var);
			if (totalList[int(temp[0])-1] == totalList[int(temp[1])-1] and totalList[int(temp[0])-1] == totalList[int(temp[2])-1]):
				if(totalList[int(temp[0])] == playerChoice[0]) :
						w="player 1 wins with path - ";
				else:
						w="player 2 wins with path - ";
				return w + item ;
			k=k+1;
			for var in item:
				temp.remove(var);
		return "";



print ("Tic - Tac - TOE \n\n");
print ("Enter your preference \n X or O\n");
try:
	compCount=0;
	ret = "";
	data = input();
	
	if(data == 'X'):
		playerChoice.insert(0,'X');
		playerChoice.insert(1,'O');
	else:
		if(data != 'O'):
			print ("Invalid entry ...Default values are set !!");
		playerChoice.insert(0,'O');
		playerChoice.insert(1,'X');

	print ("\nPlayer 1 = ",playerChoice[0]);
	print ("Player 2 = ",playerChoice[1]);
	print ("\n\n");
	
	createScreen(count,totalList);
	count=0;
	print ("\n\n Note : player should type numeric single digit values to enter there choice ...\n for example : \n 1 for 1st block              5 for center block and more..\n\n");
	while(value < 9) :
		if(value % 2 == 0) :
			print ("Player 1 turn - ");
			data = input();
		else :
			print ("Player 2 turn - ");
			comp = random.choice(totalList);
			print (comp);
			if (data !='X' and data!='O'):
				data=comp;
			else:
				continue;
		value = value + 1;
		if(int(data) >= 1  and int(data) <= 9) :
			ret = checkWin(data,value,count1,count2);
			if(ret != "") :
				break;
		else :
			print ("entry should be between 1 to 9 (single digit)...");
	print (ret);
except IOError:
	print ("\n\nError Reading value ... \n program terminated!!\nSorry!!\n :-(");


