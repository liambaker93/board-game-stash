let showButton = document.getElementById("showGameForm");
let formContainer = document.getElementById("addGameFormContainer");
let prepopulateGame = document.getElementById("gamePrepopulate");


showButton.addEventListener('click', function() {
    formContainer.classList.toggle('form-display');
    showButton.style.display = 'none';
    prepopulateGame.classList.toggle('form-display');
});