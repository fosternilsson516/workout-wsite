document.getElementById('homeBtn').addEventListener('click', function() {
    document.getElementById('homeSection').style.display = 'block';
    document.getElementById('aboutSection').style.display = 'none';
    setActiveButton(this);
});

document.getElementById('aboutBtn').addEventListener('click', function() {
    document.getElementById('homeSection').style.display = 'none';
    document.getElementById('aboutSection').style.display = 'block';
    setActiveButton(this);
});

function setActiveButton(activeBtn) {
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    activeBtn.classList.add('active');
}
