import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import Rides from '../components/rides/Rides'; // Component to display individual ride results
import '../css/RideResultsPage.css'; // CSS for the results page
import FilterSidebar from '../components/FilterSidebar'; // Component for filters (optional)

function RideResultsPage() {
    const [searchParams] = useSearchParams();
    const [searchResults, setSearchResults] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // State for filters (example)
    const [sortBy, setSortBy] = useState('relevance');
    const [maxPrice, setMaxPrice] = useState('');

    useEffect(() => {
        const origin = searchParams.get('origin');
        const destination = searchParams.get('destination');
        const date = searchParams.get('date');

        setLoading(true);
        setError(null);

        // Simulate fetching ride results based on search parameters
        const fetchRides = async () => {
            try {
                // Replace this with your actual API call using origin, destination, etc.
                const allRides = [
                    { id: 1, driver: 'Ana', origin: 'Lisboa', destination: 'Porto', date: '2025-04-20', time: '10:00', price: 25, seatsAvailable: 2, rating: 4.5, agency: null, imageUrl: 'https://via.placeholder.com/150/FF0000' },
                    { id: 2, driver: 'Carlos', origin: 'Braga', destination: 'Lisboa', date: '2025-04-21', time: '15:30', price: 30, seatsAvailable: 1, rating: 3.8, agency: 'RideShare', imageUrl: 'https://via.placeholder.com/150/00FF00' },
                    { id: 3, driver: 'Sofia', origin: 'Lisboa', destination: 'Faro', date: '2025-04-22', time: '09:00', price: 20, seatsAvailable: 3, rating: 4.9, agency: null, imageUrl: 'https://via.placeholder.com/150/0000FF' },
                    // ... more ride objects
                ];

                // Basic filtering based on search parameters
                const filteredResults = allRides.filter(ride => {
                    const originMatch = !origin || ride.origin.toLowerCase().includes(origin.toLowerCase());
                    const destinationMatch = !destination || ride.destination.toLowerCase().includes(destination.toLowerCase());
                    const dateMatch = !date || ride.date === date;
                    return originMatch && destinationMatch && dateMatch;
                });

                setSearchResults(filteredResults);
                setLoading(false);
            } catch (err) {
                setError('Erro ao buscar as boleias.');
                setLoading(false);
            }
        };

        fetchRides();
    }, [searchParams]);

    const handleSortChange = (event) => {
        setSortBy(event.target.value);
        // Implement sorting logic here based on sortBy
    };

    const handleMaxPriceChange = (event) => {
        setMaxPrice(event.target.value);
        // Implement filtering by price logic here
    };

    if (loading) {
        return <p>A procurar boleias...</p>;
    }

    if (error) {
        return <p>Erro: {error}</p>;
    }

    return (
        <div className="ride-results-page">
            <aside className="filter-sidebar">
                {/* Render FilterSidebar component here */}
                <h3>Filtrar por:</h3>
                <div>
                    <label htmlFor="sort">Ordenar por:</label>
                    <select id="sort" value={sortBy} onChange={handleSortChange}>
                        <option value="relevance">Relevância</option>
                        <option value="price_asc">Preço (Mais Baixo)</option>
                        <option value="price_desc">Preço (Mais Alto)</option>
                        <option value="rating">Avaliação</option>
                    </select>
                </div>
                <div>
                    <label htmlFor="maxPrice">Preço Máximo:</label>
                    <input
                        type="number"
                        id="maxPrice"
                        value={maxPrice}
                        onChange={handleMaxPriceChange}
                        placeholder="Ex: 30"
                    />
                </div>
                {/* Add more filter options */}
            </aside>
            <main className="results-list">
                <h2>Resultados da Procura</h2>
                {searchResults.length > 0 ? (
                    searchResults.map(ride => (
                        <Rides key={ride.id} ride={ride} />
                    ))
                ) : (
                    <p>Nenhuma boleia encontrada com os seus critérios.</p>
                )}
                {/* Add "Ver Mais Resultados" button if needed */}
            </main>
        </div>
    );
}

export default RideResultsPage;