import './css/App.css'
import {Routes, Route} from "react-router-dom";
import Home from './pages/Home.jsx';
import Login from './pages/Login.jsx';
import Favorites from "./pages/Favorites.jsx";
import Register from "./pages/Register.jsx";
import Admin from "./pages/Admin.jsx"
import NavBar from "./components/NavBar";
import RidesSearchResult from './pages/RidesSearchResult.jsx';

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
                </Routes>
            </main>
        </div>
  );
}

export default App;
