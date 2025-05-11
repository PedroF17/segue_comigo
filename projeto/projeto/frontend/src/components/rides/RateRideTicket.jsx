import React, { useState } from 'react';
import '../../css/RateRideTicket.css';

function RateRideTicket({ ride }) {
  const [feedbackText, setFeedbackText] = useState('');
  const [anomalyDescription, setAnomalyDescription] = useState('');

  const handleFeedbackChange = (event) => {
    setFeedbackText(event.target.value);
  };

  const handleAnomalyChange = (event) => {
    setAnomalyDescription(event.target.value);
  };

  const handleSubmitFeedback = () => {
    // Lógica para enviar o feedback para o backend
    console.log(`Enviar feedback: "${feedbackText}" para a viagem com ID: ${ride.id}`);
    // TODO: Implementar chamada de API
  };

  const handleSubmitAnomaly = () => {
    // Lógica para enviar a declaração de anomalia para o backend
    console.log(`Declarar anomalia: "${anomalyDescription}" para a viagem com ID: ${ride.id}`);
    // TODO: Implementar chamada de API
  };

  return (
    <div className="rate-ride-ticket">
      <div className="ticket-header">
        <span className="ride-icon">Ride</span>
        <span className="airline">{ride.airline || 'N/A'}</span>
        {ride.remainingPlaces && <span className="remaining-places">Lugares Restantes: {ride.remainingPlaces}</span>}
      </div>
      <div className="ticket-details">
        <div className="from-section">
          <p className="label">De</p>
          <p className="location">{ride.departureLocation}</p>
          <p className="airport">{ride.departureAirport}</p>
          <p className="date-time">{ride.departureDateTime}</p>
        </div>
        <div className="to-section">
          <p className="label">Para</p>
          <p className="location">{ride.arrivalLocation}</p>
          <p className="airport">{ride.arrivalAirport}</p>
          <p className="date-time">{ride.arrivalDateTime}</p>
        </div>
        <div className="duration-section">
          <p className="label">Duração</p>
          <p className="duration">{ride.duration || 'N/A'}</p>
        </div>
        <div className="status-section">
          <p className="label">Estado da Reserva</p>
          <p className="status">{ride.status}</p>
        </div>
      </div>

      <div className="feedback-section">
        <h3>Avaliação e Anomalias</h3>
        <div className="feedback-input">
          <label htmlFor={`feedback-${ride.id}`}>Seu Feedback:</label>
          <textarea
            id={`feedback-${ride.id}`}
            value={feedbackText}
            onChange={handleFeedbackChange}
            placeholder="Compartilhe sua experiência..."
          />
          <button onClick={handleSubmitFeedback}>Devolver Feedback</button>
        </div>
        <div className="anomaly-input">
          <label htmlFor={`anomaly-${ride.id}`}>Declarar Anomalia:</label>
          <textarea
            id={`anomaly-${ride.id}`}
            value={anomalyDescription}
            onChange={handleAnomalyChange}
            placeholder="Descreva qualquer problema ocorrido..."
          />
          <button onClick={handleSubmitAnomaly}>Declarar Anomalia</button>
        </div>
      </div>
    </div>
  );
}

export default RateRideTicket;