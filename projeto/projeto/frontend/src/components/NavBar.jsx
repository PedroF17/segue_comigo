import { Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { checkAdmin, checkCondutor, checkPassageiro } from '../services/auth.js'; // Verifica tipo de utilizador

function NavBar() {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [isAdmin, setIsAdmin] = useState(false);
    const [isCondutor, setIsCondutor] = useState(false);
    const [isPassageiro, setIsPassageiro] = useState(false);
    const [alertCount, setAlertCount] = useState(0);
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem('accessToken');
        setIsAuthenticated(!!token);
        if (token) {
            checkAdmin().then(setIsAdmin);
            checkCondutor().then(setIsCondutor);
            checkPassageiro().then(setIsPassageiro);
            fetchAlertCount(token);
        }
    }, []);

    const fetchAlertCount = async (token) => {
        try {
            const response = await fetch("http://127.0.0.1:8000/comunicacao/utilizador_alerta/count/", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            if (!response.ok) throw new Error("Erro ao buscar contagem de alertas.");

            const data = await response.json();
            const count = typeof data === 'object' ? Object.values(data)[0] : 0;
            setAlertCount(count);
        } catch (error) {
            console.error("Erro ao buscar contagem de alertas:", error);
        }
    };

    const handleLogout = () => {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        setIsAuthenticated(false);
        navigate('/');
        window.location.reload();
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
                    <Link to="/admin" className="navbar-link">Admin</Link>
                )}
                {isPassageiro && (
                    <Link to="/os-meus-tickets" className="navbar-link">Meus Tickets</Link>
                )}
                {isCondutor && (
                    <Link to="/condutor-tickets" className="navbar-link">Painel Condutor</Link>
                )}
                {(isCondutor || isPassageiro) && (
                    <Link to="/feedback-boleias" className="navbar-link">Feedback Boleias</Link>
                )}
                {isAuthenticated && (
                    <Link to="/profile" className="navbar-link">Perfil</Link>
                )}
                {isAuthenticated && (
                    <Link to="/alerts" className="navbar-link alert-icon">
                        🔔 
                        {alertCount > 0 && <span className="alert-count">{alertCount}</span>}
                    </Link>
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
