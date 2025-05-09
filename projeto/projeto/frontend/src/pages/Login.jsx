// src/pages/Login.jsx
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../services/auth';
import '../css/NavBar.css';

import '../css/Login.css';

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [rememberMe, setRememberMe] = useState(false);
    const navigate = useNavigate();

    // Se o usuário já estiver autenticado, redireciona e faz refresh
    useEffect(() => {
        const token = localStorage.getItem('accessToken');
        if (token) {
            navigate('/');
            window.location.reload(); // força recarregamento para refletir o estado autenticado
        }
    }, [navigate]);

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError('');

        if (!email.trim()) {
            setError('Email é obrigatório.');
            return;
        } else if (!/\S+@\S+\.\S+/.test(email)) {
            setError('Formato de email inválido.');
            return;
        }

        if (!password) {
            setError('Senha é obrigatória.');
            return;
        }

        try {
            const response = await loginUser(email, password);

            if (response.access && response.refresh) {
                localStorage.setItem('accessToken', response.access);
                localStorage.setItem('refreshToken', response.refresh);

                navigate('/');
                window.location.reload(); // força recarregamento após login
            } else {
                setError('Login inválido. Verifique as credenciais.');
            }
        } catch (err) {
            setError(err.message || 'Erro na conexão. Tente novamente.');
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
                    <p className="login-subtitle">Faça login para aceder à sua conta Segue Comigo</p>
                    <form onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="email">Email</label>
                            <input
                                type="email"
                                id="email"
                                className="form-control"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="password">Palavra-passe</label>
                            <input
                                type="password"
                                id="password"
                                className="form-control"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                        </div>
                        <div className="form-group remember-forgot">
                            <label className="remember-me">
                                <input
                                    type="checkbox"
                                    checked={rememberMe}
                                    onChange={(e) => setRememberMe(e.target.checked)}
                                />
                                Relembrar-me
                            </label>
                            <a href="#" className="forgot-password">Esqueceu-se da Palavra-passe?</a>
                        </div>
                        <button type="submit" className="login-button">Login</button>
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
                            Não tem conta na Segue Comigo? <a href="/register">Registe-se!</a>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Login;
