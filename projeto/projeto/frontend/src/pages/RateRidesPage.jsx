import React, { useState, useEffect, useCallback } from 'react';
import '../css/RateRidesPage.css';
import RateRideTicket from '../components/rides/RateRideTicket.jsx'; // Corrected import path

function RateRidesPage() {
  const [ridesToRate, setRidesToRate] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);


  const fetchRidesToRate = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const accessToken = localStorage.getItem('accessToken'); // Get the access token
      if (!accessToken) {
        setError('Não está autenticado. Por favor, faça login.');
        setLoading(false);
        return;
      }


      const response = await fetch('http://127.0.0.1:8000/viagem/viagem/list/', { // Adjust this endpoint to your actual API for completed trips
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`,
        },
      });

      if (!response.ok) {
        if (response.status === 401) {
          setError('Sessão expirada ou não autorizado. Por favor, faça login novamente.');
        } else {
          const errorData = await response.json();
          setError(errorData.detail || `Erro ao carregar as viagens: Status ${response.status}`);
        }
      } else {
        const data = await response.json();

        const formatted = data.map((viagem) => ({
            value: viagem.id_viagem,
            label: `Viagem #${viagem.id_viagem} - ${new Date(viagem.data_viagem).toLocaleString()}`,
            }));

        setRidesToRate(formatted);
      }
    } catch (err) {
      setError('Falha ao carregar as viagens para avaliação. Verifique sua conexão.');
      console.error('Erro ao buscar viagens para avaliar:', err);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchRidesToRate();
  }, [fetchRidesToRate]);
  const handleRideActionCompleted = useCallback((rideId) => {

    setRidesToRate(currentRides => currentRides.filter(ride => ride.id !== rideId));

  }, []);


  if (loading) {
    return <p className="loading-message">A carregar as viagens para avaliação...</p>;
  }

  if (error) {
    return <p className="error-message">Erro ao carregar as viagens: {error}</p>;
  }

  if (ridesToRate.length === 0) {
    return <p className="no-rides-message">Não há viagens para avaliar no momento.</p>;
  }

  return (
    <div className="rate-rides-page">
      <h1>Avalie As Suas Viagens Concluídas</h1>
      {ridesToRate.map((ride) => (
        <RateRideTicket
          key={ride.id}
          ride={ride}
          onFeedbackSubmitted={handleRideActionCompleted} // Pass this handler to remove the ride
          onAnomalySubmitted={handleRideActionCompleted}   // Pass this handler to remove the ride
        />
      ))}

      <div className="terms-and-conditions">
        <h2>Termos e Condições</h2>
        <p>Pagamentos:</p>
        <ul>
          <li>Ao Adquirir o Seu Bilhete Utilizando um Cartão de Débito ou Crédito Através do Website, Processaremos Estes Pagamentos Através do Gateway de Pagamento Comum Seguro Autorizado Que Estará Sujeito a Fins de Verificação de Fraude.</li>
          <li>Se Não Fornecer o Endereço de Faturação do Cartão Correto e/ou Informações do Titular do Cartão, a Sua Reserva Não Será Confirmada e a Transação Geral Poderá Ser Recusada. Se Não Fornecer o Endereço de Faturação do Cartão Correto e/ou Informações do Titular do Cartão, Isso Poderá Resultar no Cancelamento do Seu Bilhete e Poderá Ser Tratado Como Um Não Comparecimento. Se Fornecer Informações de Cartão de Crédito/Débito Incorretas, Se Tornar Evidente Ou For Notificada Qualquer Atividade Fraudulenta Ou Ilegal Associada ao Pagamento da Reserva, a Empresa Emissora de Bilhetes Reserva-se o Direito de Cancelar a Sua Reserva Sem Mais Notificação. A Empresa Emissora de Bilhetes Reserva-se o Direito de Iniciar Qualquer Ação Que Possa Ser Tomada Contra Si.</li>
          <li>Alguns Bancos Podem Exigir Que o Titular do Cartão Forneça Verificação de Pagamento Adicional Mediante Solicitação da Companhia Aérea Ou da Nossa Empresa Emissora de Bilhetes. Isso Poderá Ocorrer no Aeroporto no Momento do Check-In. A Companhia Aérea Reserva-se o Direito de Recusar o Embarque Ou de Cobrar Uma Garantia (Pagamento em Dinheiro Ou de Outro Cartão de Crédito) Se o Cartão Originalmente Usado Para a Compra Não Puder Ser Apresentado Pelo Titular do Cartão. O Cartão de Crédito Fornecido no Momento da Reserva Deve Ser Portado Pelo Passageiro Nomeado e Apresentado Para Verificação no Momento do Check-In. O Não Cumprimento Poderá Resultar na Recusa de Embarque ao Titular do Bilhete. Os Detalhes do Cartão de Crédito São Mantidos Num Ambiente Seguro e Transferidos Através de Um Sistema Aceito Internacionalmente.</li>
        </ul>
      </div>
    </div>
  );
}

export default RateRidesPage;