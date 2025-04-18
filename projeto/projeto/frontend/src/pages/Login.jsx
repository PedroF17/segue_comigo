import React, { useState } from 'react';
import '../css/Login.css'; // Import the CSS file
import '../css/NavBar.css';
import {Link} from "react-router-dom";

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
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

    const handleSubmit = (event) => {
        event.preventDefault();
        // Handle login logic here
        console.log('Login submitted:', { email, password, rememberMe });
    };

    return (
        <div className="login-container">
            <div className="login-card">
                <div className="login-image">
                    <img src="src/assets/images/login_images/mediumshothappywomencar.jpg" alt="Boleia com amigos" />
                </div>
                <div className="login-form">
                    <h2 className="login-title">Login</h2>
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