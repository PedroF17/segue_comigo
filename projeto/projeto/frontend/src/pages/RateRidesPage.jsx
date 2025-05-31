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

            // Verifica se o token existe
            if (!accessToken) {
                throw new Error('Token de acesso não encontrado. Faça login novamente.');
            }

            const response = await fetch('http://127.0.0.1:8000/viagem/viagem/list/', {
                headers: {
                    'Authorization': `Bearer ${accessToken}`,
                    'Content-Type': 'application/json',
                    'Accept': 'application/json', // Garante que o servidor saiba que você quer JSON
                },
            });

            // Verifica se a resposta é JSON válido
            const responseText = await response.text();
            if (!response.ok) {
                // Se a resposta for HTML (ex.: página de erro), mostra o conteúdo para debug
                console.error('Resposta do servidor (HTML/erro):', responseText);
                throw new Error(`Erro HTTP: ${response.status} - ${response.statusText}`);
            }

            // Tenta parsear o JSON só se a resposta for válida
            const data = JSON.parse(responseText);
            setViagens(Array.isArray(data) ? data : []);
        } catch (err) {
            console.error('Erro na requisição:', err);
            setError(err.message || 'Erro ao carregar viagens.');
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