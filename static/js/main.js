	
	var socket = io.connect("http://127.0.0.1:5000");
	socket.removeAllListeners();
	console.log('function in');
	socket.on('connect',function(){
		socket.emit('start_event',{
			
			data: window.location.href
			
		});
		console.log('connected.');
	});

$(document).ready(function(){
	socket.on('my_response',function(msg){
		$('#chatlist').append("<li style='display:table;border: solid 1px #272525;background: rgba(19,18,18,0.9);opacity: 20%;color:#dddddd;border-radius: 10px; padding:10px;margin-top: 10px;margin-bottom:10px;'>"+msg+"</li>");

		var objDiv = document.getElementById("upper_section");
		objDiv.scrollTop = objDiv.scrollHeight;
		console.log('received message');
	});
});


var input = document.getElementById("input");           //clicking enter on input clicks send button

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("send_btn").click();
  }
});

$('#input').on('blur',function () { 
    		var blurEl = $(this); 
    		setTimeout(function() {
        	blurEl.focus()
    		}, 10);
		});


function add_chat(){
	
		socket.emit('send_answar',{
			data: $('#input').val()

		});
		$("#chatlist").append("<li style='margin-right:0px;display:table;border: solid 1px #d2d0d0;background: rgba(210,208,208,0.9);opacity: 20%;color:#444444;border-radius: 10px; padding:10px;margin-top: 10px;margin-bottom:10px;'>"+$('#input').val()+"</li>");
		var objDiv = document.getElementById("upper_section");
		objDiv.scrollTop = objDiv.scrollHeight;
		$('#input').val("");

		console.log('sent answar.');

		
	
}
	

socket.on('get_question',function(msg){
	
	if(msg=="end"){
		console.log("end");
		$('#input').val("");
		$( "#input" ).prop( "disabled", true );
	}
	else{
		var data=msg;
		$("#spin").css("opacity","1");
		setTimeout( function(){

			console.log("key up");
			$("#spin").css("opacity","0");

			
			$("#chatlist").append("<li style='display:table;border: solid 1px #272525;background: rgba(19,18,18,0.9);opacity: 20%;color:#dddddd;border-radius: 10px; padding:10px;margin-top: 10px;margin-bottom:10px;'>"+data+"</li>");
	    	console.log(data);
	    	var objDiv = document.getElementById("upper_section");
			objDiv.scrollTop = objDiv.scrollHeight;
	  		
	  		}, Math.floor(Math.random() * (2000 - 1000 + 1)) + 1000 );

		
		console.log(data);
		}
});
	




/*
que=1
ans=2
function add_chat(){


	socket.emit('send_answar',{
		data: $('#input').val()
	});
	console.log('sent answar.');
	
	socket.on('get_question',function(msg){
		if(msg=="end"){}
		else{
			cur_question=msg;
			console.log('question taken.');
		}
	});

	if(que>7){
		for (var i = 1; i <= 7; i++) {
			document.getElementById('p'+String(i)).innerText="";
		}
		ans=2;
		var x=document.getElementById('input').value;
		document.getElementById('p'+String(ans)).innerText=x;
		document.getElementById('p'+String(que)).innerText=cur_question;
		ans+=2;
		que+=2;
			
	}
	else{
	var x=document.getElementById('input').value;
	document.getElementById('p'+String(ans)).innerText=x;
	document.getElementById('p'+String(que)).innerText=cur_question;
	ans+=2;
	que+=2;
	}
	
}
*/