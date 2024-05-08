const questions = [
    { question: "How old are you?", answers: ["Under 12 years", "13-19 years", "20-39 years", "40-59 years", "60 years and older"]},
    { question: "What is your sex?", answers: ["Male", "Female"]},
    { question: "Which type of build do you have?", answers: ["Ectomorph", "Mesomorph", "Endomorph"]},
    { question: "What are your workout goals?", answers: ["Weight loss", "Build Muscle", "Improve Mobility/Flexibility(reduce pain)", "Enhance Athletic Performance"]},
    { question: "What intensity level do you prefer for your workouts?", answers: ["Light", "Moderate", "Vigorous"]},
    { question: "How would you describe your current fitness level?", answers: ["Beginner", "Intermediate", "Advanced"]},
    { question: "How do you prefer to exercise?", answers: ["Bodyweight Workouts At Home", "I Have Some Basic Weights To Work With", "Full Gym"]},
    { question: "Do you have any injuries or health conditions that we should consider when designing your workout plan(multiple choice)?", answers: ["Knee problems (e.g., arthritis, past injuries)", "Shoulder issues (e.g., rotator cuff injuries)", "Hip discomfort (e.g., impingement, arthritis)",
     "Lower back pain (e.g., herniated disc, sciatica)", "Upper back/neck pain (e.g., cervical spondylosis)", "Muscle strains/sprains", "Tendonitis (e.g., Achilles, tennis elbow)",
     "Heart conditions (e.g., heart disease, post-surgery recovery)", "Osteoporosis", "Chronic pain conditions (e.g., fibromyalgia)", "Respiratory issues (e.g., asthma, COPD)", "Balance or coordination issues (e.g., from MS, Parkinson’s)"
    ], multiple: true},
    { question: "Which days of the week are you available to workout(multiple choice)?", answers: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], multiple: true},
    { question: "How much time can you dedicate to each workout session?", answers: ["Less than 30 minutes", "30-45 minutes", "45-60 minutes", "More than 60 minutes"]},
    { question: "Thats all for now! Please enter your email and we will send you a free workout plan(we will not send you any marketing or spam just this curated workout plan).", answers: [], email: true}
];

let currentQuestionIndex = 0;
let answers = {};

function showQuestion() {
    const question = questions[currentQuestionIndex];
    document.getElementById('question').textContent = question.question;
    const answerButtons = document.getElementById('answer-buttons');
    answerButtons.innerHTML = '';
    question.answers.forEach((answer, index) => {
        const button = document.createElement('li');
        button.textContent = answer;
        button.classList.add('btn');
        if (question.multiple) { // Check if the question allows multiple answers
            button.onclick = () => selectMultipleAnswers(answer);
        } else {
            button.onclick = () => selectSingleAnswer(answer);
        }
        answerButtons.appendChild(button);
    });

    document.getElementById('back-button').style.display = currentQuestionIndex > 0 ? 'block' : 'none';
    if (currentQuestionIndex === questions.length - 1) {
        document.getElementById('emailForm').style.display = 'block'; // Show the email form on the last question
        document.getElementById('next-button').style.display = 'none'; // Hide the Next button
    } else {
        document.getElementById('emailForm').style.display = 'none'; // Hide the email form
        document.getElementById('next-button').style.display = 'block'; // Show the Next button
    }
    
}

function selectSingleAnswer(answer) {
    answers[questions[currentQuestionIndex].question] = answer;
    const buttons = document.querySelectorAll('#answer-buttons .btn');
    buttons.forEach(btn => {
        btn.style.backgroundColor = btn.textContent === answer ? '#4CAF50' : '';
    });
}

function selectMultipleAnswers(answer) {
    let selectedAnswers = answers[questions[currentQuestionIndex].question] || [];
    if (selectedAnswers.includes(answer)) {
        selectedAnswers = selectedAnswers.filter(item => item !== answer);
    } else {
        selectedAnswers.push(answer);
    }
    answers[questions[currentQuestionIndex].question] = selectedAnswers;
    updateButtonStyles();
}

function updateButtonStyles() {
    const selectedAnswers = answers[questions[currentQuestionIndex].question] || [];
    const buttons = document.querySelectorAll('#answer-buttons .btn');
    buttons.forEach(btn => {
        btn.style.backgroundColor = selectedAnswers.includes(btn.textContent) ? '#4CAF50' : '';
    });
}

document.getElementById('next-button').addEventListener('click', () => {
    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        showQuestion();
    } else {
        document.getElementById('emailForm').style.display = 'block';
        document.getElementById('next-button').style.display = 'none';
    }
});

document.getElementById('back-button').addEventListener('click', () => {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        showQuestion();
    }
});    

document.getElementById('emailForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('emailInput').value;
    answers['Email'] = email;
    await fetch('/submit_answers', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(answers)
    });

    alert('Thank you! Your answers and email have been submitted.');
    window.location.href = '/'; // Redirect to homepage

});

window.onload = showQuestion;
