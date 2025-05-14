import './css/App.css'
import {Routes, Route} from "react-router-dom";
import Home from './pages/Home.jsx';
import Login from './pages/Login.jsx';
import Favorites from "./pages/Favorites.jsx";
import Register from "./pages/Register.jsx";
import Admin from "./pages/Admin.jsx"
import NavBar from "./components/NavBar";
import RidesSearchResult from './pages/RidesSearchResult.jsx';
import RideTicketsPage from "./pages/RideTicketsPage.jsx";
import RateRidesPage from "./pages/RateRidesPage.jsx";
import CondutorTicketsPage from './pages/CondutorTicketsPage.jsx';
import Alerts from './pages/Alerts.jsx';
import Profile from './pages/Profile.jsx';

function App() {

    return (
        <div>
            <NavBar />
            <main className="main_content">
                <Routes>
                    <Route path="/" element={<Home/>}/>
                    <Route path="/login" element={<Login/>}/>
                    <Route path="/register" element={<Register/>}/>
                    <Route path="/favorites" element={<Favorites/>}/>
                    <Route path="/admin" element={<Admin/>}/>
                    <Route path="/resultados" element={<RidesSearchResult />} />
                    <Route path="/os-meus-tickets" element={<RideTicketsPage />} />
                    <Route path="/condutor-tickets" element={<CondutorTicketsPage />} />
                    <Route path="/feedback-boleias" element={<RateRidesPage />} />
                    <Route path="/alerts" element={<Alerts />} />
                    <Route path="/profile" element={<Profile />} />
                </Routes>
            </main>
        </div>
  );
}

export default App;
