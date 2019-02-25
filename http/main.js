	
	var socket = io.connect("http://127.0.0.1:5000");
	socket.removeAllListeners();
	console.log('function in');
	socket.on('connect',function(){
		socket.emit('start_event',{
			data: "user connected successfully."
			
		});
		console.log('connected.');
	});

$(document).ready(function(){
	socket.on('my_response',function(msg){
		$('#chatlist').append("<li style='display:table;border: solid 1px #272525;background: rgba(19,18,18,0.9);opacity: 20%;color:#dddddd;border-radius: 10px; padding:10px;margin-top: 10px;margin-bottom:10px;'>"+msg+"</li>");

		console.log('received message');
	});
});


function add_chat(){
	
		socket.emit('send_answar',{
			data: $('#input').val()

		});
		$("#chatlist").append("<li style='margin-right:0px;display:table;border: solid 1px #d2d0d0;background: rgba(210,208,208,0.9);opacity: 20%;color:#444444;border-radius: 10px; padding:10px;margin-top: 10px;margin-bottom:10px;'>"+$('#input').val()+"</li>");
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
		$("#chatlist").append("<li style='display:table;border: solid 1px #272525;background: rgba(19,18,18,0.9);opacity: 20%;color:#dddddd;border-radius: 10px; padding:10px;margin-top: 10px;margin-bottom:10px;'>"+data+"</li>");
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