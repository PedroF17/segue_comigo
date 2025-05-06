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
        const response = await fetch('/api/user/tickets'); // 'http://127.0.0.1:8000/viagem/viagem/list/'
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setTickets(data);
      } catch (err) {
        setError('Failed to load ride tickets.');
        console.error('Error fetching tickets:', err);
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
      <h1>Bilhete Digital</h1>
      <p className="important-note">Não é necessário imprimir o seu bilhete</p>

      {tickets.map((ticket) => (
        <RideTicket key={ticket.id} ticket={ticket} />
      ))}

      <div className="terms-and-conditions">
        <h2>Termos e Condições</h2>
        <p>Pagamentos:</p>
        <ul>
          <li>Está a Comprar o Seu Bilhete Usando Um Cartão de Débito ou Crédito Através do Website, Processaremos Estes Pagamentos Através do Gateway de Pagamento Comum Seguro Autorizado Que Estará Sujeito a Fins de Verificação de Fraude.</li>
          <li>Se Não Fornecer o Endereço de Faturação do Cartão Correto e/ou Informações do Titular do Cartão, a Sua Reserva Não Será Confirmada e a Transação Geral Poderá Ser Recusada. Se Não Fornecer o Endereço de Faturação do Cartão Correto e/ou Informações do Titular do Cartão, Isso Poderá Resultar no Cancelamento do Seu Bilhete e Poderá Ser Tratado Como Um Não Comparecimento. Se Fornecer Informações de Cartão de Crédito/Débito Incorretas, Se Tornar Evidente Ou For Notificada Qualquer Atividade Fraudulenta Ou Ilegal Associada ao Pagamento da Reserva, a Empresa Emissora de Bilhetes Reserva-se o Direito de Cancelar a Sua Reserva Sem Mais Notificação. A Empresa Emissora de Bilhetes Reserva-se o Direito de Iniciar Qualquer Ação Que Possa Ser Tomada Contra Si.</li>
          <li>Alguns Bancos Podem Exigir Que o Titular do Cartão Forneça Verificação de Pagamento Adicional Mediante Solicitação da Companhia Aérea Ou da Nossa Empresa Emissora de Bilhetes. Isso Poderá Ocorrer no Aeroporto no Momento do Check-In. A Companhia Aérea Reserva-se o Direito de Recusar o Embarque Ou de Cobrar Uma Garantia (Pagamento em Dinheiro Ou de Outro Cartão de Crédito) Se o Cartão Originalmente Usado Para a Compra Não Puder Ser Apresentado Pelo Titular do Cartão. O Cartão de Crédito Fornecido no Momento da Reserva Deve Ser Portado Pelo Passageiro Nomeado e Apresentado Para Verificação no Momento do Check-In. O Não Cumprimento Poderá Resultar na Recusa de Embarque ao Titular do Bilhete. Os Detalhes do Cartão de Crédito São Mantidos Num Ambiente Seguro e Transferidos Através de Um Sistema Aceito Internacionalmente.</li>
        </ul>
      </div>
    </div>
  );
}

export default RideTicketsPage;