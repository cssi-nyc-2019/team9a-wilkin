
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
$ = jQuery;
var maxHealth = 500,
  curHealth = maxHealth;
$('.total').html(maxHealth + "/" + maxHealth);
$(".health-bar-text").html("100%");
$(".health-bar").css({
  "width": "100%"
});
$(".add-damage").click(function() {
  if (curHealth == 0) {
    $('.message-box').html("Is this the end??");
  } else {
    var damage = 100;
    $(".health-bar-red, .health-bar").stop();
    curHealth = curHealth - damage;
    if (curHealth < 0) {
      curHealth = 0;
      restart();
    } else {
      $('.message-box').html("You took " + damage + " points of damage!");
    }
    applyChange(curHealth);
  }
});
$(".add-heal").click(function() {
  if (curHealth == maxHealth) {
    $('.message-box').html("You are already at full health");
  } else {
    var heal = 0;
    $(".health-bar-red, .health-bar-blue, .health-bar").stop();
    curHealth = curHealth + heal;
    if (curHealth > maxHealth) {
      curHealth = maxHealth;
      $('.message-box').html("You're at full health");
    } else if (curHealth == 0) {
      $('.message-box').html("Miraculously! You regained your health by " + heal + " points and get back on to your feet!");
    } else {
      $('.message-box').html("You regained your health by " + heal + " points!");
    }
    applyChange(curHealth);
  }
});

function applyChange(curHealth) {
  var a = curHealth * (100 / maxHealth);
  $(".health-bar-text").html(Math.round(a) + "%");
  $(".health-bar-red").animate({
    'width': a + "%"
  }, 700);
  $(".health-bar").animate({
    'width': a + "%"
  }, 500);
  $(".health-bar-blue").animate({
    'width': a + "%"
  }, 300);
  $('.total').html(curHealth + "/" + maxHealth);
}

function restart() {
  //Was going to have a game over/restart function here. 
  $('.health-bar-red, .health-bar');
  $('.message-box').html("You've been knocked down! Thing's are looking bad.");
}