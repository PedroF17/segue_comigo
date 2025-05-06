import {Link} from "react-router-dom";

function NavBar() {

    return (
        <nav className="navbar">
            <div className="navbar-brand">
                <Link to ="/">
                    <div className='logo'> <img src="/logotipo_segue_comigo.png" alt="Segue Comigo Logo"/></div>
                </Link>
            </div>
            <div className="navbar-links">
                <Link to ="/" className="navbar-link">Home</Link>
                <Link to ="/favorites" className="navbar-link">Favoritos</Link>
                <Link to ="/login" className="navbar-link">Login</Link>
                <Link to ="/admin" className="navbar-link">Admin</Link>
                <Link to ="/os-meus-tickets" className="navbar-link">Meus Tickets</Link>
                <Link to ="/feedback-boleias" className="navbar-link">Feedback Boleias</Link>
            </div>
        </nav>
    )
}
export default NavBar;