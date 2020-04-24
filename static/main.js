	$("#only_mobile").hide();
	var socket = io.connect("http://134.209.42.61:5001");
	socket.removeAllListeners();
	console.log('function in');
	socket.on('connect',function(){
		socket.emit('start_event',{
			
			data: window.location.href
		});
		console.log('connected.');
	
	});

if ($(window).width() > 600) {
	$('#reply_div').prop('disabled',true);
	socket.emit('greet_event',{
			
			data: ''
		});
}
else{
	$("footer").hide();
	$("#reply_div").hide();
	$("#right_bar").hide();
}

function start_socket(){ 
	$("#only_mobile").show();
	$("#right_bar").show();
	
	$("#reply_div").show();
	$("#reply_div").css("position","fixed");
	$("#left_bar").css("display","none");


	socket.emit('greet_event',{
			
			data: ''
		});
}


var input = document.getElementById("input");           //clicking enter on input clicks send button

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("button-addon2").click();
  }
});

$('#input').on('blur',function () { 
    		var blurEl = $(this); 
    		setTimeout(function() {
        	blurEl.focus()
    		}, 10);
		});


function add_chat(value='default'){
		if(value!='default'){
			console.log(value);
			socket.emit('send_answar',{
			data: value
			});
			text=`<div id='block_right'">
     					<div class='input-group mb-3' id="block_in_block_right">
      						<li style='margin-right:4px;display:table;border: solid 2px #205d77;background: rgba(234, 242, 246);color:#205d77;border-bottom-right-radius:25px; border-top-left-radius:5px;padding:15px;margin-top: 0px;margin-bottom:10px;max-width: 90%;'>`+value+`</li>
                  <div class="input-group-append" style="margin-right: 0px; padding: 0px;">
                    <img src="../static/images/user.png" class='img-responsive' id='block_image_right'>
                  </div>
    			</div>		
     				`
		}
		else{
			socket.emit('send_answar',{
				data: $('#input').val()

			});
			text=`<div id='block_right'">
     					<div class='input-group mb-3' id="block_in_block_right">
      						<li style='margin-right:4px;display:table;border: solid 2px #205d77;background: rgba(234, 242, 246);color:#205d77;border-bottom-right-radius:25px; border-top-left-radius:5px;padding:15px;margin-top: 0px;margin-bottom:10px; max-width:90%;'>`+$('#input').val()+`</li>
                  <div class="input-group-append" style="margin-right: 0px; padding: 0px;">
                    <img src="../static/images/user.png" class='img-responsive' id='block_image_right'>
                  </div>
    			</div>		
     				`
     	}

		$("#chatlist").append(text);

		var objDiv = document.getElementById("chatbox");
		objDiv.scrollTop = objDiv.scrollHeight;
		$('#input').val("");

		

		
	
}



socket.on('get_faculty',function(msg){
	//var Base64={_keyStr:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",encode:function(e){var t="";var n,r,i,s,o,u,a;var f=0;e=Base64._utf8_encode(e);while(f<e.length){n=e.charCodeAt(f++);r=e.charCodeAt(f++);i=e.charCodeAt(f++);s=n>>2;o=(n&3)<<4|r>>4;u=(r&15)<<2|i>>6;a=i&63;if(isNaN(r)){u=a=64}else if(isNaN(i)){a=64}t=t+this._keyStr.charAt(s)+this._keyStr.charAt(o)+this._keyStr.charAt(u)+this._keyStr.charAt(a)}return t},decode:function(e){var t="";var n,r,i;var s,o,u,a;var f=0;e = e.replace(/\\+\\+[++^A-Za-z0-9+/=]/g, "");while(f<e.length){s=this._keyStr.indexOf(e.charAt(f++));o=this._keyStr.indexOf(e.charAt(f++));u=this._keyStr.indexOf(e.charAt(f++));a=this._keyStr.indexOf(e.charAt(f++));n=s<<2|o>>4;r=(o&15)<<4|u>>2;i=(u&3)<<6|a;t=t+String.fromCharCode(n);if(u!=64){t=t+String.fromCharCode(r)}if(a!=64){t=t+String.fromCharCode(i)}}t=Base64._utf8_decode(t);return t},_utf8_encode:function(e){e=e.replace(/\r\n/g,"n");var t="";for(var n=0;n<e.length;n++){var r=e.charCodeAt(n);if(r<128){t+=String.fromCharCode(r)}else if(r>127&&r<2048){t+=String.fromCharCode(r>>6|192);t+=String.fromCharCode(r&63|128)}else{t+=String.fromCharCode(r>>12|224);t+=String.fromCharCode(r>>6&63|128);t+=String.fromCharCode(r&63|128)}}return t},_utf8_decode:function(e){var t="";var n=0;var r=c1=c2=0;while(n<e.length){r=e.charCodeAt(n);if(r<128){t+=String.fromCharCode(r);n++}else if(r>191&&r<224){c2=e.charCodeAt(n+1);t+=String.fromCharCode((r&31)<<6|c2&63);n+=2}else{c2=e.charCodeAt(n+1);c3=e.charCodeAt(n+2);t+=String.fromCharCode((r&15)<<12|(c2&63)<<6|c3&63);n+=3}}return t}}
	//var decodedString = Base64.decode(img_src);
	//form=document.getElementById('faculty_info');
	//image=new Image();
	//image.src=decodedString
	//console.log(image); 
	//form.append('image',image);
	fac_img=msg['image_data'];
	fac_name=msg['fac_name'];
	fac_dept=msg['fac_dept'];
	fac_desig=msg['fac_desig'];;
	fac_insti=msg['fac_insti'];
	if ($(window).width() < 600) {
    text=
	`<div id="faculty_heading"><h5><b>Faculty Information</b></h5></div>
        <img class="img-responsive" alt="faculty_image" src="`+fac_img+`" id="faculty_img">
        <div id="faculty_desc">
          <p>`+fac_name+`<br>`+fac_desig+`<br>`+fac_dept+`<br>Department</p>
          </div>
          <button class="btn btn-secondary" type="button" onclick="start_socket()" id="start_chat_btn">Start Chat</button>
          `
	}
	else{
	text=
	`<div id="faculty_heading"><h4><b>Faculty Information</b></h4></div>
        <img class="img-responsive" alt="faculty_image" src="`+fac_img+`" id="faculty_img">
        <div id="faculty_desc">
          <p>`+fac_name+`<br>`+fac_desig+`<br>`+fac_dept+`<br>Department<br>`+fac_insti+`<br></p>
        </div>`
	}
	$("#faculty_info").append(text);
});



socket.on('suggestions',function(msg){

	
	for (var i = 0; i < 5; i++) {
		text=`<button class="btn btn-secondary" type="button" onclick="add_chat('`+msg[i]+`')" id="`+msg[i]+`" value="`+msg[i]+`" style="vertical-align: middle;">`+msg[i]+`</button>`;
		$('#emoji').append(text);
	}
	
});


var txt=''	
var i=0;
var speed=30;
var count=0;






socket.on('get_question',function(msg){
	
	if(msg=="end"){
		$('#input').val("");
		
		
		socket.disconnect()
	}
	else{
		
		var data=msg;
		$("#spin").css("opacity","1");
		setTimeout( function(){

			
			$("#spin").css("opacity","0");
			text=`<div id="block_left">
     					<div class="input-group mb-3">
      						<div class="input-group-prepend">
        						<img src="../static/images/sara.png" class="img-responsive" id="block_image_left">
      						</div>
      						<li style='margin-right:5px;display:table;border: solid 1px #2E86AB;background: rgba(46,134,171);color:#ffffff;border-bottom-left-radius: 25px; border-top-right-radius:5px;padding:15px;margin-top: 10px;margin-bottom:10px;max-width: 83%;'><span id="animated_li`+count.toString(8)+`"></span><span id="cursor`+count.toString(8)+`" class='cursor'>_</span></li>
      					</div>
      				</div>`
			$("#chatlist").append(text);
			txt=data;
			typeWriter();
	    	
	    	
	    	var objDiv = document.getElementById("chatbox");
			objDiv.scrollTop = objDiv.scrollHeight;

	  		
	  		}, Math.floor(Math.random() * (2000 - 1000 + 1)) + 1000 );
		
		i=0;
		count++;
		
		}
});

function typeWriter() {

  if (i < txt.length) {
    document.getElementById("animated_li"+count.toString(8)).innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
  else{
  	setTimeout(function() {

  		document.getElementById("cursor"+count.toString(8)).innerHTML='';
  	}, 4);
  	
  }
  
  
}


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

@media only screen and (max-width: 383px) {

#block_image_left{
	
	height:20px;
	width: 20px; 
}

#block_image_right{
	
	height:20px;
	width: 20px; 
}

}




@import url('https://fonts.googleapis.com/css?family=Inconsolata');
li{
  font-family: 'Inconsolata', monospace;
  white-space: nowrap;
    overflow: hidden;
    width: inherit;
    background-color:#2E86AB; 
    margin: 10px 0;
    animation: typing 4s steps(60, end);
}

p:nth-child(2) {
    animation: typing-2 8s steps(60, end);
}

@keyframes typing {
    from {width: 0;}
}

@keyframes typing-2 {
    0% {width: 0;}
    50% {width: 0;}
    100% {width: 100;}
}
@keyframes blink {
    to {opacity: .0;}
}

.cursor {
    animation: blink 1s infinite;
}

*/