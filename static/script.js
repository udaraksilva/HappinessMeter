
function login() {
  const empId = document.getElementById('employee-id').value;
  fetch('/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ employee_id: empId })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      document.querySelector('.login-container').style.display = 'none';
      document.getElementById('vote-section').classList.remove('hidden');
    } else {
      alert('Invalid Employee ID');
    }
  });
}

function submitVote(vote) {
  fetch('/api/vote', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ vote })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      window.location.href = 'thankyou.html';
    } else {
      alert('You have already voted. Try again in 24 hours.');
    }
  });
}
