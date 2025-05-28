import React, { useEffect, useState } from 'react';
import RateRideTicket from '../components/rides/RateRideTicket';
import '../css/RateRidesPage.css';

function RateRidesPage() {
    const [viagens, setViagens] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchViagens = async () => {
            try {
                const accessToken = localStorage.getItem('accessToken');
                const response = await fetch('http://127.0.0.1:8000/viagem/viagem/list/', {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'Content-Type': 'application/json',
                    },
                });

                if (!response.ok) {
                    throw new Error('Erro ao buscar as viagens');
                }

                const data = await response.json();
                setViagens(Array.isArray(data) ? data : []);
            } catch (err) {
                console.error(err);
                setError('Erro ao carregar viagens.');
            } finally {
                setLoading(false);
            }
        };

        fetchViagens();
    }, []);

    const handleFeedbackSubmitted = (viagemId) => {
        console.log(`Feedback enviado para a viagem ${viagemId}`);
    };

    const handleAnomalySubmitted = (viagemId) => {
        console.log(`Anomalia enviada para a viagem ${viagemId}`);
    };

    if (loading) return <p>Carregando...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div className="rate-rides-page">
            <h1>Minhas Viagens</h1>
            {viagens.length === 0 ? (
                <p>Você não tem viagens para avaliar.</p>
            ) : (
                viagens
                    .filter((viagem) => viagem !== undefined && viagem !== null)
                    .map((viagem) => (
                        <RateRideTicket
                            key={viagem.id_viagem}
                            viagem={viagem}
                            onFeedbackSubmitted={() => handleFeedbackSubmitted(viagem.id_viagem)}
                            onAnomalySubmitted={() => handleAnomalySubmitted(viagem.id_viagem)}
                        />
                    ))
            )}
        </div>
    );
}

export default RateRidesPage;