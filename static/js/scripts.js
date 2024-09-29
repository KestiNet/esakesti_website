// Add this to your script.js file

document.querySelector('.cta').addEventListener('click', function(e) {
    e.preventDefault();
    alert('More information coming soon!');
});

document.querySelector('.dropbtn').addEventListener('click', function(e) {
    e.preventDefault();
    this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';
});