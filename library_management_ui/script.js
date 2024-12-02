document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
  
   
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;
  
    const userData = {
      name: name,
      email: email,
      password: password,
      role: role
    };
  
 
    fetch('http://127.0.0.1:8000/users/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('responseMessage').textContent = 'Registration successful!';
      document.getElementById('responseMessage').style.color = 'green';
    })
    .catch(error => {
      document.getElementById('responseMessage').textContent = 'Error: ' + error.message;
      document.getElementById('responseMessage').style.color = 'red';
    });
  });
  