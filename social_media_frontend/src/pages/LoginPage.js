import React, { useState } from 'react';
import { useHistory } from 'react-router-dom'; // Import useHistory

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);
 // const history = useHistory(); // Initialize useHistory

  const handleLogin = (e) => {
    e.preventDefault();
    // Here you would typically make an API request to authenticate the user
    // For simplicity, let's just do a basic check here
    if (username === 'example_user' && password === 'password') {
      // Successful login logic (redirect, set authentication state, etc.)
  //    history.push('/home'); // Redirect to home page upon successful login
      console.log('Login successful');
    } else {
      setError('Invalid username or password');
    }
  };

  const handleRegister = (e) => {
    e.preventDefault();
    // Here you would typically make an API request to register the user
    console.log('User registration logic');
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
