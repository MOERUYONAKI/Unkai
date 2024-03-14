import * as bootstrap from 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.esm.min.js';
// import * as popperjs from 'https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/esm/popper.min.js';

const lightMode = document.getElementById('light-mode');
const darkMode = document.getElementById('dark-mode');
const lightModeTrigger = document.getElementById('light-mode-trigger');
const darkModeTrigger = document.getElementById('dark-mode-trigger');

const lightToastTrigger = document.getElementById('lightToastTrigger');
const lightToast = document.getElementById('lightToast');
const darkToastTrigger = document.getElementById('darkToastTrigger');
const darkToast = document.getElementById('darkToast');

if (lightModeTrigger && darkModeTrigger) {
    lightModeTrigger.addEventListener('click', () => {
        lightMode.style.display = 'block';
        darkMode.style.display = 'none';
        console.log(1);
    })

    darkModeTrigger.addEventListener('click', () => {
        darkMode.style.display = 'block';
        lightMode.style.display = 'none';
        console.log(1);
    })
}

if (lightToastTrigger && darkToastTrigger) {
    const lightToastBootstrap = bootstrap.Toast.getOrCreateInstance(lightToast);
    const darkToastBootstrap = bootstrap.Toast.getOrCreateInstance(darkToast);

    lightToastTrigger.addEventListener('click', () => {
        lightToastBootstrap.show();
        console.log(1);
    })
    
    darkToastTrigger.addEventListener('click', () => {
        darkToastBootstrap.show();
        console.log(1);
    })
}