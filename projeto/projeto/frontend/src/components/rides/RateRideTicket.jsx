import React, { useState } from 'react';
import '../../css/RateRideTicket.css';

function RateRideTicket({ ride, onFeedbackSubmitted, onAnomalySubmitted }) {
    const [feedbackText, setFeedbackText] = useState('');
    const [anomalyDescription, setAnomalyDescription] = useState('');
    const [feedbackSent, setFeedbackSent] = useState(false);
    const [anomalySent, setAnomalySent] = useState(false);

    const handleFeedbackChange = (event) => {
        setFeedbackText(event.target.value);
    };

    const handleAnomalyChange = (event) => {
        setAnomalyDescription(event.target.value);
    };

    /*const handleSubmitFeedback = async () => {
        // Lógica para enviar o feedback para o backend
        console.log(`Enviar feedback: "${feedbackText}" para a viagem com ID: ${ride.id}`);
        // Substitua esta simulação pela sua chamada de API real
        // Exemplo de chamada de API usando fetch:
        try {
            const response = await fetch(`/api/feedback/${ride.id}`, { // Certifique-se de ter o endpoint correto
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // Inclua o token de autenticação se necessário
                    'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                },
                body: JSON.stringify({ feedback: feedbackText }),
            });
            if (response.ok) {
                setFeedbackSent(true);
                if (onFeedbackSubmitted) {
                    onFeedbackSubmitted(ride.id);
                }
            } else {
                const errorData = await response.json();
                console.error("Failed to send feedback:", errorData);
                alert("Failed to send feedback. Please try again."); // Informar o usuário
            }

        } catch (error) {
            console.error("Error sending feedback:", error);
            alert("Error sending feedback. Please check your network connection.");
        }

    };*/

    const handleSubmitAnomaly = async () => {
        // Lógica para enviar a declaração de anomalia para o backend
        console.log(`Declarar anomalia: "${anomalyDescription}" para a viagem com ID: ${ride.id}`);
        // Substitua esta simulação pela sua chamada de API real
        try {
            const response = await fetch(`http://127.0.0.1:8000/comunicacao/ocorrencia/${ride.id}`, {  // Endpoint correto
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                     'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                },
                body: JSON.stringify({ anomalia: anomalyDescription }),
            });
             if (response.ok) {
                setAnomalySent(true);
                 if (onAnomalySubmitted) {
                    onAnomalySubmitted(ride.id);
                }
            } else {
                const errorData = await response.json();
                console.error("Failed to send anomaly:", errorData);
                 alert("Failed to send anomaly. Please try again.");
            }
        } catch (error) {
             console.error("Error sending anomaly:", error);
             alert("Error sending anomaly. Please check your network connection.");
        }

    };

    return (
        <div className={`rate-ride-ticket ${feedbackSent || anomalySent ? 'submitted' : ''}`}>
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
                {!(feedbackSent || anomalySent) ? (
                    <>
                        <div className="feedback-input">
                            <label htmlFor={`feedback-${ride.id}`}>Seu Feedback:</label>
                            <textarea
                                id={`feedback-${ride.id}`}
                                value={feedbackText}
                                onChange={handleFeedbackChange}
                                placeholder="Compartilhe sua experiência..."
                            />
                            <button onClick={handleSubmitFeedback} disabled={feedbackSent}>Devolver Feedback</button>
                        </div>
                        <div className="anomaly-input">
                            <label htmlFor={`anomaly-${ride.id}`}>Declarar Anomalia:</label>
                            <textarea
                                id={`anomaly-${ride.id}`}
                                value={anomalyDescription}
                                onChange={handleAnomalyChange}
                                placeholder="Descreva qualquer problema ocorrido..."
                            />
                            <button onClick={handleSubmitAnomaly} disabled={anomalySent}>Declarar Anomalia</button>
                        </div>
                     </>
                ) : (
                    <p className="submission-message">Obrigado pelo seu feedback!</p>
                )}
            </div>
        </div>
    );
}

export default RateRideTicket;