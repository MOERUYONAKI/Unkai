import * as bootstrap from 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.esm.min.js';
// import * as popperjs from 'https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/esm/popper.min.js';

const actMode = document.getElementById('actMode')
const homeLink = document.getElementById('homeLink')
const serversLink = document.getElementById('serversLink')
const docsLink = document.getElementById('docsLink')

const modeTrigger = document.getElementById('modeTrigger');

const connectToast = document.getElementById('connectToast');
const connectToastTrigger = document.getElementById('connectToastTrigger');

if (modeTrigger) {
    modeTrigger.addEventListener('click', () => {
        if (actMode.getAttribute('data-bs-theme') == 'light') {
            actMode.setAttribute('data-bs-theme', 'dark');
            homeLink.setAttribute('href', 'index.php?dark');
            serversLink.setAttribute('href', 'servers/index.php?dark');
            docsLink.setAttribute('href', 'docs/index.php?dark');
        } else {
            actMode.setAttribute('data-bs-theme', 'light');
            homeLink.setAttribute('href', 'index.php?light');
            serversLink.setAttribute('href', 'servers/index.php?light');
            docsLink.setAttribute('href', 'docs/index.php?light');
        }
        console.log(1);
    })
}

if (connectToastTrigger) {
    const connectToastBootstrap = bootstrap.Toast.getOrCreateInstance(connectToast);

    connectToastTrigger.addEventListener('click', () => {
        connectToastBootstrap.show();
        console.log(1);
    })
}