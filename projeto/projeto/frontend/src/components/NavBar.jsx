import { Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { checkAdmin, checkCondutor, checkPassageiro } from '../services/auth.js'; // Importe as funções para verificar o tipo de utilizador

function NavBar() {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [isAdmin, setIsAdmin] = useState(false);
    const [isCondutor, setIsCondutor] = useState(false);
    const [isPassageiro, setIsPassageiro] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem('accessToken');
        setIsAuthenticated(!!token);
        if (token) {
            // Verifica o tipo de utilizador
            checkAdmin().then(setIsAdmin);
            checkCondutor().then(setIsCondutor);
            checkPassageiro().then(setIsPassageiro);
        }
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        setIsAuthenticated(false);
        navigate('/');
        window.location.reload(); // força recarregamento
    };

    return (
        <nav className="navbar">
            <div className="navbar-brand">
                <Link to="/">
                    <div className="logo">
                        <img src="/logotipo_segue_comigo.png" alt="Segue Comigo Logo" />
                    </div>
                </Link>
            </div>
            <div className="navbar-links">
                <Link to="/" className="navbar-link">Home</Link>
                {isAdmin && (
                    <Link to="/admin" className="navbar-link">Admin</Link> // Este link será mostrado apenas se o utilizador for Admin
                )}
                {(isCondutor || isPassageiro) && (
                    <Link to="/os-meus-tickets" className="navbar-link">Meus Tickets</Link>
                )}
                {(isCondutor || isPassageiro) && (
                    <Link to="/feedback-boleias" className="navbar-link">Feedback Boleias</Link>
                )}
                {!isAuthenticated ? (
                    <Link to="/login" className="navbar-link">Login</Link>
                ) : (
                    <Link to="#" onClick={handleLogout} className="navbar-link">Logout</Link>
                )}
            </div>
        </nav>
    );
}

export default NavBar;
