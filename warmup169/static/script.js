function show_message(msg) {
	var width = $(window).width();
	$('#modal-strip-message').text(msg);
	$('#modal-strip').css({'-webkit-transform': 'translate3d(-'+width+'px, 0, 0)'});
	$('#modal').show('fade', 300);
	setTimeout(function(){
		$('#modal-strip').show();
		setTimeout(function(){
			$('#modal-strip').css({'-webkit-transform': 'translate3d(0, 0, 0)'});
		}, 0);
	}, 300);
}

function hide_message() {
	var width = $(window).width();
	$('#modal-strip').css({'-webkit-transform': 'translate3d(-'+width+'px, 0, 0)'});
	setTimeout(function(){
		$('#modal-strip').hide();
		$('#modal-strip-message').text('');
		$('#modal').hide('fade', 300);
	}, 500);
}

$(document).ready(function(){
	
	$('#login-box-signin').click(function(){
		
		$('.login-box-progress-bar').addClass('login-box-progress-bar-active');
		
		setTimeout(function(){
			var user = $('#login-input-username').val();
			var pass = $('#login-input-password').val();
			
			$.post('users/login', {'user': user, 'password': pass}, function(data){
				var data = data.split(";");
				if (data[0] == 1) {
					
					window.location.href ='/welcome';
					
					// REDIRECT TO WELCOME PAGE
					// WELCOME PAGE SHOULD RECEIVE LOGCOUNT AS A PARAMETER
					// WELCOME PAGE SHOULD REDIRECT THE USER BACK TO THE LOGIN PAGE IF THE USER IS NOT LOGGED IN.
					
				} else {
					if (data[0] == -1) {
						show_message("Invalid username and password combination. Please try again.");
					} else if (data[0] == -2) {
						show_message("This user name already exists. Please try again.");
					} else if (data[0] == -3) {
						show_message("The user name should be non-empty and at most 128 characters long. Please try again.");
					} else if (data[0] == -4) {
						show_message("The password should be at most 128 characters long. Please try again.");
					}
				}
			});
		}, 900);
		
	});
	
	$('#login-box-signup').click(function(){
		
		$('.login-box-progress-bar').addClass('login-box-progress-bar-active');
		
		setTimeout(function(){
			var user = $('#login-input-username').val();
			var pass = $('#login-input-password').val();
			
			$.post('users/add', {'user': user, 'password': pass}, function(data){
				if (data[0] == 1) {
					
					window.location.href ='/welcome';
					
					// REDIRECT TO WELCOME PAGE
					// WELCOME PAGE SHOULD RECEIVE LOGCOUNT AS A PARAMETER
					// WELCOME PAGE SHOULD REDIRECT THE USER BACK TO THE LOGIN PAGE IF THE USER IS NOT LOGGED IN.
					
				} else {
					if (data[0] == "-1") {
						$('#login-message').text("Invalid username and password combination. Please try again.");
					} else if (data[0] == "-2") {
						$('#login-message').text("This user name already exists. Please try again.");
					} else if (data[0] == "-3") {
						$('#login-message').text("The user name should be non-empty and at most 128 characters long. Please try again.");
					} else if (data[0] == "-4") {
						$('#login-message').text("The password should be at most 128 characters long. Please try again.");
					}
				}
			});
		}, 900);
		
	});
	
	$('#login-box-logout').click(function(){
		window.location.href = '/';
	});
	
	$('#login-input-username').focus(function(){
		$(this).parent().parent().addClass('login-box-input-active');
	});
	
	$('#login-input-username').blur(function(){
		$(this).parent().parent().removeClass('login-box-input-active');
	});
	
	$('#login-input-password').focus(function(){
		$(this).parent().parent().addClass('login-box-input-active');
	});
	
	$('#login-input-password').blur(function(){
		$(this).parent().parent().removeClass('login-box-input-active');
	});
	
	$('#modal-strip-button').click(function(){
		var width = $(window).width();
		$('#modal-strip').css({'-webkit-transform': 'translate3d(-'+width+'px, 0, 0)'});
		setTimeout(function(){
			$('#modal-strip').hide();
			$('#modal').hide('fade', 300);
		}, 500);
	});
	
});