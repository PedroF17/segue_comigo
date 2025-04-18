import Rides from '../components/rides/Rides.jsx'
import {useState} from 'react'

function Home() {
    const [searchQuery, setSearchQuery] = useState('');

    const rides = [
        {
            id: 1,
            title: "Mario",
            origin: "Barcelos",
            destiny: "Braga",
            departure: '12:00',
            arrive: "13:00",
            description: "Por Martim"
        },
        {
            id: 2,
            title: "Maria",
            origin: "Barcelos",
            destiny: "Famalicão",
            departure: '11:00',
            arrive: "12:00",
            description: "Por Nine"
        },
        {
            id: 3,
            title: "Paulo",
            origin: "Famalicão",
            destiny: "Barcelos",
            departure: '16:00',
            arrive: "17:00",
            description: "Por Via Todos"
        },
        {
            id: 4,
            title: "Paula",
            origin: "Braga",
            destiny: "Barcelos",
            departure: '14:00',
            arrive: "15:00",
            description: "Por Prado"
        },
    ];

    const handleSearch = (e) => {
        e.preventDefault();
        alert(searchQuery);
        setSearchQuery("");
    }

    return (
        <div className="home">
            <form onSubmit={handleSearch} className="search_form">
                <input type="text"
                       placeholder = "Procura por boleias"
                       className="search_input"
                       value = {searchQuery}
                       onChange={(e) => setSearchQuery(e.target.value)}
                />
                <button type="submit" className="search_button"> Pesquisar </button>
            </form>
            <div className="ride_grid">
                    {rides.map((ride) => (
                        ride.title.toLowerCase().startsWith(searchQuery) && (
                            <Rides ride={ride} key={ride.id} />
                        )
                    ))}
            </div>
        </div>
    );
}
export default Home;