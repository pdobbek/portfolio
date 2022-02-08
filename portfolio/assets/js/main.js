const navMenu = document.getElementById('nav-menu')
const navToggle = document.getElementById('nav-toggle')
const navClose = document.getElementById('nav-close')

/* SHOW MENU */
/* Validate if constant exists */
if (navToggle) {
    navToggle.addEventListener('click', ()=>{
        navMenu.classList.add('show-menu')
    }
    )
}

/* HIDE MENU */
/* Validate if constant exists */
if (navClose) {
    navClose.addEventListener('click', ()=>{
        navMenu.classList.remove('show-menu')
    }
    )
}

/* REMOVE MENU ON MOBILE */
const navLink = document.querySelectorAll('.nav__link')  // get all nav links
function linkAction() {
    const navMenu = document.getElementById('nav-menu')
    // when we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))  // add listener to each nav link