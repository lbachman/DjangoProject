import React, { useState } from 'react';
import { useHistory } from 'react-router-dom'; // Import useHistory

const LoginPage = () => 
{
const [username, setUsername] = useState('');
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const [error, setError] = useState('');
const [isRegistering, setIsRegistering] = useState(false);
// const history = useHistory(); // Initialize useHistory

const handleLogin = (e) => 
{
	
    e.preventDefault();

    // Here you would typically make an API request to authenticate the user



    // For simplicity, let's just do a basic check here
    if (username === 'logan' && password === 'password') 
    {
    	// Successful login logic (redirect, set authentication state, etc.)
    	//history.push('/home'); // Redirect to home page upon successful login
    	console.log('Login successful');
    } 
    else 
    {
    	setError('Invalid username or password');
    }




};

const handleRegister = (e) => 
{
    e.preventDefault();



    // Here you would typically make an API request to register the user
    fetch('http://127.0.0.1:8000/api/users/', 
    {
		method: 'POST',
		headers: {
		'Content-Type': 'application/json',
  		},
  		body: JSON.stringify({
    	username: username,
    	email: email,
    	password: password,
  		}),
	})
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('Success:', data);
  })
  .catch(error => {
    console.error('Errorr:', error);
  });

  };

  return (
    <div>
      <h2>{isRegistering ? 'Register' : 'Login'}</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={isRegistering ? handleRegister : handleLogin}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        {/* <div>
          <label>Email:</label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div> */}
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">{isRegistering ? 'Register' : 'Login'}</button>
      </form>
      <p>
        {isRegistering
          ? 'Already have an account?'
          : 'Don\'t have an account?'}
        <button onClick={() => setIsRegistering(!isRegistering)}>
          {isRegistering ? 'Login' : 'Register'}
        </button>
      </p>
    </div>
  );
};

export default LoginPage;
