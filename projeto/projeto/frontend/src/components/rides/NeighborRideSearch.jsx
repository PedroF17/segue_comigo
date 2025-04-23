import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../../css/NeighborRideSearch.css'; // Import CSS for styling

function NeighborRideSearch() {
    const [origin, setOrigin] = useState('');
    const [destination, setDestination] = useState('');
    const [date, setDate] = useState('');
    const navigate = useNavigate();

    const handleOriginChange = (event) => {
        setOrigin(event.target.value);
    };

    const handleDestinationChange = (event) => {
        setDestination(event.target.value);
    };

    const handleDateChange = (event) => {
        setDate(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const queryParams = new URLSearchParams();
        if (origin) queryParams.append('origin', origin);
        if (destination) queryParams.append('destination', destination);
        if (date) queryParams.append('date', date);

        navigate(`/resultados?${queryParams.toString()}`);
    };

    return (
        <div className="neighbor-ride-search">
            <h2>Encontre ou ofereça uma boleia na vizinhança</h2>
            <form onSubmit={handleSubmit} className="ride-search-form">
                <div className="form-group">
                    <label htmlFor="origin">Origem:</label>
                    <input
                        type="text"
                        id="origin"
                        placeholder="Partida"
                        value={origin}
                        onChange={handleOriginChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="destination">Destino:</label>
                    <input
                        type="text"
                        id="destination"
                        placeholder="Chegada"
                        value={destination}
                        onChange={handleDestinationChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="date">Data:</label>
                    <input
                        type="date"
                        id="date"
                        value={date}
                        onChange={handleDateChange}
                    />
                </div>
                <button type="submit" className="search-button">
                    Pesquisar Boleias
                </button>
            </form>
            <p className="offer-ride-link">
                Quer oferecer uma boleia? <a href="#">Clique aqui</a>
            </p>
        </div>
    );
}

export default NeighborRideSearch;