import React, { useState } from 'react';
import '../css/Register.css'; // Import the CSS file
import '../css/NavBar.css';
import {Link} from "react-router-dom";

function RegisterForm() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [agreeTerms, setAgreeTerms] = useState(false);
    const [error, setError] = useState('');
    const [successMessage, setSuccessMessage] = useState('');

    const handleFirstNameChange = (event) => {
        setFirstName(event.target.value);
    };

    const handleLastNameChange = (event) => {
        setLastName(event.target.value);
    };

    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    };

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleConfirmPasswordChange = (event) => {
        setConfirmPassword(event.target.value);
    };

    const handleAgreeTermsChange = (event) => {
        setAgreeTerms(event.target.checked);
    };

const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setSuccessMessage('');

    if (!firstName.trim()) {
      setError('First name is required.');
      return;
    }

    if (!lastName.trim()) {
      setError('Last name is required.');
      return;
    }

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
    } else if (password.length < 6) {
      setError('Password must be at least 6 characters long.');
      return;
    }

    if (password !== confirmPassword) {
      setError('Passwords do not match.');
      return;
    }

    if (!agreeTerms) {
      setError('You must agree to the terms and conditions.');
      return;
    }

    const registrationUrl = 'http://localhost:8000/api/auth/register/'; // Replace with our actual Django registration URL
    try {
      const response = await fetch(registrationUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ firstName, lastName, email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        setSuccessMessage(data.message);
        // Optionally reset the form
        setFirstName('');
        setLastName('');
        setEmail('');
        setPassword('');
        setConfirmPassword('');
        setAgreeTerms(false);
      } else {
        setError(data.error || 'Registration failed.');
      }
    } catch (error) {
      setError('Network error. Please try again.');
    }

};

    return (
        <div className="register-container">
            <div className="register-card">
                <div className="register-image">
                    <img src="src/assets/images/login_images/mediumshothappywomencar.jpg" alt="Boleia com amigos" />
                </div>
                <div className="register-form">
                <form onSubmit={handleSubmit}>
                    <div className="name-fields">
                        <div className="form-group">
                            <h2 className="register-title">Registo</h2>
                            {error && <p className="error-message">{error}</p>}
                            {successMessage && <p className="success-message">{successMessage}</p>}
                            <label htmlFor="firstName">Primeiro Nome</label>
                            <input
                                type="text"
                                id="firstName"
                                className="form-control"
                                value={firstName}
                                onChange={handleFirstNameChange}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="lastName">Último Nome</label>
                            <input
                                type="text"
                                id="lastName"
                                className="form-control"
                                value={lastName}
                                onChange={handleLastNameChange}
                                required
                            />
                        </div>
                    </div>
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
                    <div className="form-group">
                        <label htmlFor="confirmPassword">Confirme a Palavra-Passe</label>
                        <div className="password-input-wrapper">
                            <input
                                type="password"
                                id="confirmPassword"
                                className="form-control"
                                value={confirmPassword}
                                onChange={handleConfirmPasswordChange}
                                required
                            />
                            {/* You might add a show/hide password icon here */}
                        </div>
                    </div>
                    <div className="form-group agree-terms">
                        <label>
                            <input
                                type="checkbox"
                                checked={agreeTerms}
                                onChange={handleAgreeTermsChange}
                                required
                            />
                            Concordo com todos os <a href="#">Termos e Políticas de Privacidade</a>
                        </label>
                    </div>
                    <button type="submit" className="register-button">
                        Registar
                    </button>
                    <p className='login-link'>
                        Já tem conta? <Link to ="/login" ><a href="#">Login</a></Link>
                    </p>
                    <div className="register-separator">
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
                </form>
                </div>
            </div>
        </div>
    );
}

export default RegisterForm;