$(document).ready(function(){
//Function to run automatically display the first question on the back of the card
   

//The array for the questions 
	let questions = [
    {
        question1: 'A boolean is something that stores true or false values',
        answer: 'True'
    },

    {
       	question : 'The command to print a something to the terminal in python is "console.log()"',
        answer: 'False'
           
    },

    {
        
        question: "The $ establishes that you're coding in jQuery",
        answer: 'True'
            
        
    },

    {
        
        question : "In python 2.7 the code line to get user input is 'raw_input()'",
        answer: 'True'
    },
    {
        
        question : "The logical operator && will evaluate a statement as true only if both expressions are true",
        answer: 'True'
         
    },
    {
        
        question : " The equation (3*5)++ will evaluate to 18",
        answer: 'False'
    },
    {
       
        question : "=! is used in JavaScript for something not true ",
        answer: 'False'
    },
    {
        
        question: "Three equal signs are used for a strict evaluate",
        answer: 'True'
    },
    {
       
        question : "Companies like Facebook, Google, and Youtube use Python",
        answer: 'True'
    },
    {
        question : " 7 % 2 would evaluate as 3.5",
        answer: 'False'
            
    },
]

$("#question").text(questions[0].question1); 


});

