import React, { useState, useEffect } from 'react';
import '../css/RideTicketsPage.css';
import RideTicket from '../components/rides/RideTicket.jsx';

function RideTicketsPage() {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRideTickets = async () => {
      setLoading(true);
      setError(null);
      try {
        const accessToken = localStorage.getItem('refreshToken'); // Obtenha o access token

        if (!accessToken) {
          setError('Não está autenticado.');
          setLoading(false);
          return;
        }

        const response = await fetch('http://127.0.0.1:8000/viagem/viagem/list/', { // Use o endpoint correto para buscar os tickets do utilizador
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`, // Adicione o cabeçalho de autorização com o Bearer token
          },
        });

        if (!response.ok) {
          if (response.status === 401) {
            setError('Não autorizado a aceder aos bilhetes.');
          } else {
            const errorData = await response.json();
            setError(errorData.detail || `Erro ao carregar os seus bilhetes: Status ${response.status}`);
          }
        } else {
          const data = await response.json();
          setTickets(data);
        }
      } catch (err) {
        setError('Falha ao carregar os seus bilhetes.');
        console.error('Erro ao buscar bilhetes:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchRideTickets();
  }, []);

  if (loading) {
    return <p>A carregar os seus bilhetes...</p>;
  }

  if (error) {
    return <p>Erro ao carregar os bilhetes: {error}</p>;
  }

  return (
    <div className="ride-tickets-page">
      <h1>Os Seus Bilhetes</h1>
      {tickets.map((ticket) => (
        <RideTicket key={ticket.id} ticket={ticket} />
      ))}
    </div>
  );
}

export default RideTicketsPage;