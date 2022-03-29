function logInForm(state) {
	document.getElementById("login").style.display = state;
	document.getElementById("main-login").style.display = state;
}

function closeLogin(state) {
	document.getElementById("login").style.display = state;
	document.getElementById("main-login").style.display = state;
}

function signUpForm(state) {
	document.getElementById("signup").style.display = state;
}

function closeSignUp(state) {
	document.getElementById("signup").style.display = state;
}

function setWindow(state) {
	document.getElementById("settings-window").style.display = state;
	document.getElementById("labelForum").style.display = 'none';
}
//Slide
let sliderImage = document.querySelectorAll('.slide'),
	arrowLeft = document.querySelector('#arrow-left'),
	arrowRight = document.querySelector('#arrow-right'),
	current = 0;

function resetSlide(){
	for(let i=0; i<sliderImage.length; i++){
		sliderImage[i].style.display = 'none';
	}
}

function startSlide(){
	resetSlide();
	sliderImage[0].style.display = 'block';
}

function sliderLeft() {
	resetSlide();
	sliderImage[current - 1].style.display = 'block';
	current--;
}

function sliderRight(){
	resetSlide();
	sliderImage[current+1].style.display = 'block';
	current++;
}

arrowLeft.addEventListener('click', function(){
	if(current===0){
		current = sliderImage.length;
	}
	sliderLeft();
});

arrowRight.addEventListener('click', function(){
	if(current===sliderImage.length - 1){
		current = -1;
	}
	sliderRight();
});

startSlide();

//Time module
const time = document.getElementById('time');

function showTime(){
	let today = new Date(),
		hour = today.getHours(),
		min = today.getMinutes(),
		sec = today.getSeconds();
	const amPm = hour >= 12 ? 'PM' : 'AM';

//12hr format
	hour = hour % 12 || 12;

	time.innerHTML = `${hour}<span>:</span>${addZero(min)}<span>:</span>${addZero(sec)}`+ ' ' + amPm;
	setTimeout(showTime, 1000);
}

function addZero(n){
	return (parseInt(n,10) < 10 ? '0' : '')+n;
}

//Run
showTime();

//Upbutton
var smoothJumpUp = function(){
	if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0) {
		window.scrollBy(0,-50);
		setTimeout(smoothJumpUp, 12);
	}
}

window.onscroll = function(){
	var scrolled = window.pageYoffset || document.documentElement.scrollTop;
	if (scrolled > 100){
		document.getElementById('upbutton').style.display = 'block'
	} else{
		document.getElementById('upbutton').style.display = 'none';
	}
}
