import React, { useState } from 'react';
import '../../css/Login.css'; // Arquivo de estilos

const LoginPage = () => {
    const [email, setEmail] = useState('seguecomigo@email.com');
    const [password, setPassword] = useState('');
    const [rememberMe, setRememberMe] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        // Lógica de login aqui
        console.log({ email, password, rememberMe });
    };

    const handleForgotPassword = () => {
        // Lógica para recuperação de senha
        console.log('Forgot password clicked');
    };

    return (
        <div className="login-container">
            <div className="login-header">
                <h1>Segue Comigo</h1>
            </div>

            <div className="login-form-container">
                <h2>Login</h2>
                <p>Faça login para aceder à sua conta Segue Comigo</p>

                <form onSubmit={handleSubmit} className="login-form">
                    <div className="form-group">
                        <label htmlFor="email">Email</label>
                        <input
                            type="email"
                            id="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="Palavra palavra pass">Password</label>
                        <input
                            type="password"
                            id="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="........"
                            required
                        />
                    </div>

                    <div className="form-options">
                        <label className="checkbox-container">
                            <input
                                type="checkbox"
                                checked={rememberMe}
                                onChange={() => setRememberMe(!rememberMe)}
                            />
                            <span className="checkmark"></span>
                            Relembrar-me
                        </label>

                        <label className="checkbox-container forgot-password" onClick={handleForgotPassword}>
                            Esqueceu-se da palavra passe?
                        </label>
                    </div>

                    <button type="Submeter" className="login-button">Login</button>
                </form>

                <div className="login-divider">
                    <span>Ou</span>
                </div>

                {/* Aqui podem ser adicionados botões de login social */}
            </div>
        </div>
    );
};

export default LoginPage;