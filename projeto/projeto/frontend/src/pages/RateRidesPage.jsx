import React, { useState, useEffect, useCallback } from 'react';
import '../css/RateRidesPage.css';
import RateRideTicket from '../components/rides/RateRideTicket';

function RateRidesPage() {
    const [ridesToRate, setRidesToRate] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

     const fetchRidesToRate = useCallback(async () => {
        setLoading(true);
        setError(null);
        try {
            const accessToken = localStorage.getItem('accessToken');
            if (!accessToken) {
                setError('Não está autenticado.');
                setLoading(false);
                return;
            }
            const response = await fetch('http://127.0.0.1:8000/viagem/viagem/list', { // Endpoint
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${accessToken}`,
                },
            });

            if (!response.ok) {
                if (response.status === 401) {
                    setError('Não autorizado a aceder ao histórico de viagens.');
                } else {
                    const errorData = await response.json();
                    setError(errorData.detail || `Erro ao carregar o histórico de viagens: Status ${response.status}`);
                }
            } else {
                const data = await response.json();
                // Filter only completed rides.  You might need to adjust the 'status' check
                const completedRides = data.filter(ride => ride.status === 'completed' || ride.status === 'finished');
                setRidesToRate(completedRides);
            }
        } catch (err) {
            setError('Falha ao carregar o histórico de viagens.');
            console.error('Erro ao buscar histórico de viagens:', err);
        } finally {
            setLoading(false);
        }
    }, []);


    useEffect(() => {
        fetchRidesToRate();
    }, [fetchRidesToRate]);

    const handleFeedbackSubmitted = useCallback((rideId) => {
        // Remove a viagem da lista após o envio do feedback
        setRidesToRate(prevRides => prevRides.filter(ride => ride.id !== rideId));
    }, []);

    const handleAnomalySubmitted = useCallback((rideId) => {
        // Remove a viagem da lista após o envio da anomalia
        setRidesToRate(prevRides => prevRides.filter(ride => ride.id !== rideId));
    }, []);

    if (loading) {
        return <p>A carregar as viagens para avaliação...</p>;
    }

    if (error) {
        return <p>Erro ao carregar as viagens para avaliação: {error}</p>;
    }

    return (
        <div className="rate-rides-page">
            <h1>Avalie As Seguintes Viagens</h1>
            {ridesToRate.map((ride) => (
                <RateRideTicket
                    key={ride.id}
                    ride={ride}
                    onFeedbackSubmitted={handleFeedbackSubmitted}
                    onAnomalySubmitted={handleAnomalySubmitted}
                />
            ))}
            <div className="terms-and-conditions">
                {/* ... termos e condições ... */}
            </div>
        </div>
    );
}

export default RateRidesPage;