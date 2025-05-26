import React, { useState } from 'react';
import '../../css/RateRideTicket.css';


function RateRideTicket({ ride, onFeedbackSubmitted, onAnomalySubmitted }) {
  const [feedbackText, setFeedbackText] = useState('');
  const [anomalyDescription, setAnomalyDescription] = useState('');
  const [isSubmittingFeedback, setIsSubmittingFeedback] = useState(false);
  const [isSubmittingAnomaly, setIsSubmittingAnomaly] = useState(false);
  const [feedbackError, setFeedbackError] = useState(null);
  const [anomalyError, setAnomalyError] = useState(null);
  const [feedbackSuccess, setFeedbackSuccess] = useState(false);
  const [anomalySuccess, setAnomalySuccess] = useState(false);

  const handleFeedbackChange = (event) => {
    setFeedbackText(event.target.value);
    if (feedbackError) setFeedbackError(null); // Clear error on change
  };

  const handleAnomalyChange = (event) => {
    setAnomalyDescription(event.target.value);
    if (anomalyError) setAnomalyError(null); // Clear error on change
  };

  const handleSubmitFeedback = async () => {
    if (!feedbackText.trim()) {
      setFeedbackError('Por favor, digite seu feedback.');
      return;
    }

    setIsSubmittingFeedback(true);
    setFeedbackError(null);
    try {
      const accessToken = localStorage.getItem('accessToken'); // Or use your getAccessToken() function
      if (!accessToken) {
        throw new Error('Usuário não autenticado.');
      }

      const response = await fetch(`http://127.0.0.1:8000/api/viagem/${ride.id}/feedback/`, { // Example endpoint
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`,
        },
        body: JSON.stringify({ feedback_text: feedbackText }), // Adjust field name to your backend
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Erro ao enviar feedback.');
      }

      setFeedbackSuccess(true);
      setFeedbackText(''); // Clear textarea
      // Inform the parent component that feedback was submitted for this ride
      if (onFeedbackSubmitted) {
        onFeedbackSubmitted(ride.id);
      }
    } catch (error) {
      console.error('Erro ao enviar feedback:', error);
      setFeedbackError(error.message);
    } finally {
      setIsSubmittingFeedback(false);
    }
  };

  const handleSubmitAnomaly = async () => {
    if (!anomalyDescription.trim()) {
      setAnomalyError('Por favor, descreva a anomalia.');
      return;
    }

    setIsSubmittingAnomaly(true);
    setAnomalyError(null);
    try {
      const accessToken = localStorage.getItem('accessToken'); // Or use your getAccessToken() function
      if (!accessToken) {
        throw new Error('Usuário não autenticado.');
      }

      const response = await fetch(`http://127.0.0.1:8000/api/viagem/${ride.id}/anomalia/`, { // Example endpoint
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`,
        },
        body: JSON.stringify({ description: anomalyDescription }), // Adjust field name to your backend
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Erro ao declarar anomalia.');
      }

      setAnomalySuccess(true);
      setAnomalyDescription(''); // Clear textarea
      // Inform the parent component that an anomaly was submitted for this ride
      if (onAnomalySubmitted) {
        onAnomalySubmitted(ride.id);
      }
    } catch (error) {
      console.error('Erro ao declarar anomalia:', error);
      setAnomalyError(error.message);
    } finally {
      setIsSubmittingAnomaly(false);
    }
  };

  // Helper to determine if both feedback and anomaly have been submitted
  const isFullyProcessed = feedbackSuccess && anomalySuccess;

  return (
    <div className={`rate-ride-ticket ${feedbackSuccess || anomalySuccess ? 'submitted-partially' : ''} ${isFullyProcessed ? 'submitted-fully' : ''}`}>
      <div className="ticket-header">
        <span className="ride-icon">Ride</span>
      </div>
      <div className="ticket-details">
        <div className="from-section">
          <p className="label">De</p>
          <p className="location">{ride.departureLocation}</p>
          <p className="date-time">{ride.departureDateTime}</p>
        </div>
        <div className="to-section">
          <p className="label">Para</p>
          <p className="location">{ride.arrivalLocation}</p>
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
        {!feedbackSuccess ? (
          <div className="feedback-input">
            <label htmlFor={`feedback-${ride.id}`}>Seu Feedback:</label>
            <textarea
              id={`feedback-${ride.id}`}
              value={feedbackText}
              onChange={handleFeedbackChange}
              placeholder="Compartilhe sua experiência..."
              disabled={isSubmittingFeedback}
            />
            {feedbackError && <p className="error-message">{feedbackError}</p>}
            <button onClick={handleSubmitFeedback} disabled={isSubmittingFeedback}>
              {isSubmittingFeedback ? 'Enviando...' : 'Devolver Feedback'}
            </button>
          </div>
        ) : (
          <p className="success-message">Feedback enviado com sucesso!</p>
        )}

        {!anomalySuccess ? (
          <div className="anomaly-input">
            <label htmlFor={`anomaly-${ride.id}`}>Declarar Anomalia:</label>
            <textarea
              id={`anomaly-${ride.id}`}
              value={anomalyDescription}
              onChange={handleAnomalyChange}
              placeholder="Descreva qualquer problema ocorrido..."
              disabled={isSubmittingAnomaly}
            />
            {anomalyError && <p className="error-message">{anomalyError}</p>}
            <button onClick={handleSubmitAnomaly} disabled={isSubmittingAnomaly}>
              {isSubmittingAnomaly ? 'Enviando...' : 'Declarar Anomalia'}
            </button>
          </div>
        ) : (
          <p className="success-message">Anomalia declarada com sucesso!</p>
        )}

        {/* You could add a combined message if both are submitted and you want to remove the card */}
        {/* {feedbackSuccess && anomalySuccess && <p className="final-message">Viagem avaliada completamente!</p>} */}
      </div>
    </div>
  );
}

export default RateRideTicket;