import React, { useState } from 'react';
import '../css/Login.css'; // Import the CSS file
import '../css/NavBar.css';
import {Link} from "react-router-dom";

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loginSuccess, setLoginSuccess] = useState(false);
    const [rememberMe, setRememberMe] = useState(false);

    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    };

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleRememberMeChange = (event) => {
        setRememberMe(event.target.checked);
    };

    const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setLoginSuccess(false);

    if (!email.trim()) {
      setError('Email is required.');
      return;
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      setError('Invalid email format.');
      return;
    }

    if (!password) {
      setError('Password is required.');
      return;
    }

    // --- ADJUST THE URL HERE ---
    const loginUrl = 'http://localhost:8000/api/auth/login/'; // Replace with your actual Django login URL

    try {
      const response = await fetch(loginUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        setLoginSuccess(true);
        // Handle successful login (e.g., store token, redirect)
        console.log('Login successful:', data.message);
        // Example: Store a token in local storage
        // localStorage.setItem('authToken', data.token);
        // Example: Redirect to a dashboard page
        // window.location.href = '/dashboard';
      } else {
        setError(data.error || 'Login failed.');
      }
    } catch (error) {
      setError('Network error. Please try again.');
    }
    };

    return (
        <div className="login-container">
            <div className="login-card">
                <div className="login-image">
                    <img src="src/assets/images/login_images/mediumshothappywomencar.jpg" alt="Boleia com amigos" />
                </div>
                <div className="login-form">
                    <h2 className="login-title">Login</h2>
                    {error && <p className="error-message">{error}</p>}
                    {loginSuccess && <p className="success-message">Login successful!</p>}
                    <p className="login-subtitle">Faça Login para aceder à sua conta Segue Comigo</p>
                    <form onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="email">Email</label>
                            <input
                                type="email"
                                id="email"
                                className="form-control"
                                value={email}
                                onChange={handleEmailChange}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="password">Palavra-passe</label>
                            <div className="password-input-wrapper">
                                <input
                                    type="password"
                                    id="password"
                                    className="form-control"
                                    value={password}
                                    onChange={handlePasswordChange}
                                    required
                                />
                                {/* You might add a show/hide password icon here */}
                            </div>
                        </div>
                        <div className="form-group remember-forgot">
                            <label className="remember-me">
                                <input
                                    type="checkbox"
                                    checked={rememberMe}
                                    onChange={handleRememberMeChange}
                                />
                                Relembrar-me
                            </label>
                            <a href="#" className="forgot-password">
                                Esqueceu-se da Palavra-passe?
                            </a>
                        </div>
                        <button type="submit" className="login-button">
                            Login
                        </button>
                        <div className="login-separator">
                            <span>ou</span>
                        </div>
                        <div className="social-login">
                            <button className="social-button facebook">
                                <img src="src/assets/images/icons/facebook_icon.svg" alt="Facebook icon"/>
                            </button>
                            <button className="social-button apple">
                                <img src="src/assets/images/icons/Apple_icon.svg" alt="Apple icon"/>
                            </button>
                            <button className="social-button google">
                                <img src="src/assets/images/icons/Google.svg" alt="Google icon"/>
                            </button>
                        </div>
                        <p className="register-link">
                            Não tem conta na Segue Comigo? <Link to ="/register" ><a href="#">Registe-se!</a></Link>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Login;