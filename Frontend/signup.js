const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

document.getElementById("signIn1").onclick = function () {
    location.href = "main.html";
};

document.getElementById("signUp1").onclick = function () {
    location.href = "main.html";
};