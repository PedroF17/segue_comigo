import React, { useState, useEffect } from 'react';
import '../../css/RateRideTicket.css';

function RateRideTicket({ viagem, onFeedbackSubmitted, onAnomalySubmitted }) {
    if (
        !viagem ||
        typeof viagem !== 'object' ||
        !('id_viagem' in viagem)
    ) {
        console.warn("RateRideTicket received invalid viagem prop:", viagem);
        return <div>Erro: Nenhuma viagem fornecida ou viagem inválida.</div>;
    }

    const [feedbackText, setFeedbackText] = useState('');
    const [anomalyDescription, setAnomalyDescription] = useState('');
    const [isSubmittingFeedback, setIsSubmittingFeedback] = useState(false);
    const [isSubmittingAnomaly, setIsSubmittingAnomaly] = useState(false);
    const [feedbackError, setFeedbackError] = useState(null);
    const [anomalyError, setAnomalyError] = useState(null);
    const [feedbackSuccess, setFeedbackSuccess] = useState(false);
    const [anomalySuccess, setAnomalySuccess] = useState(false);

    useEffect(() => {
        setFeedbackSuccess(false);
        setAnomalySuccess(false);
        setFeedbackError(null);
        setAnomalyError(null);
        setFeedbackText('');
        setAnomalyDescription('');
    }, [viagem]);

    const pontoPartida = viagem?.pontos_viagem?.find(p => p.destino === 0);
    const pontoChegada = viagem?.pontos_viagem?.find(p => p.destino === 1);

    const formattedDate = viagem?.data_viagem
        ? new Date(viagem.data_viagem).toLocaleDateString('pt-PT', { year: 'numeric', month: '2-digit', day: '2-digit' })
        : 'Data Inválida';

    const formattedTime = viagem?.data_viagem
        ? new Date(viagem.data_viagem).toLocaleTimeString('pt-PT', { hour: '2-digit', minute: '2-digit' })
        : 'Hora Inválida';

    const statusViagem = viagem?.status_viagemid_status_viagem?.descricao || 'N/A';
    const condutorNome = viagem?.condutorid_condutor?.nome_primeiro && viagem?.condutorid_condutor?.nome_ultimo
        ? `${viagem.condutorid_condutor.nome_primeiro} ${viagem.condutorid_condutor.nome_ultimo}`
        : (viagem?.condutorid_condutor?.id_condutor || 'N/A');

    const handleFeedbackChange = (event) => {
        setFeedbackText(event.target.value);
        if (feedbackError) setFeedbackError(null);
    };

    const handleAnomalyChange = (event) => {
        setAnomalyDescription(event.target.value);
        if (anomalyError) setAnomalyError(null);
    };

    const handleSubmitFeedback = async () => {
        if (!feedbackText.trim()) {
            setFeedbackError('Por favor, digite seu feedback.');
            return;
        }

        setIsSubmittingFeedback(true);
        try {
            const accessToken = localStorage.getItem('accessToken');
            if (!accessToken) throw new Error('Usuário não autenticado.');

            //const response = await fetch(`http://127.0.0.1:8000/viagem/${viagem.id_viagem}/feedback/`, {
            const response = await fetch(`http://127.0.0.1:8000/comunicacao/ocorrencia/${viagem.id_viagem}/`, {    
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${accessToken}`,
                },
                body: JSON.stringify({ feedback_text: feedbackText }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Erro ao enviar feedback.');
            }

            setFeedbackSuccess(true);
            setFeedbackText('');
            onFeedbackSubmitted?.(viagem.id_viagem);
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
        try {
            const accessToken = localStorage.getItem('accessToken');
            if (!accessToken) throw new Error('Usuário não autenticado.');

            const response = await fetch(`http://127.0.0.1:8000/comunicacao/alerta/${viagem.id_viagem}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${accessToken}`,
                },
                body: JSON.stringify({ description: anomalyDescription }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Erro ao declarar anomalia.');
            }

            setAnomalySuccess(true);
            setAnomalyDescription('');
            onAnomalySubmitted?.(viagem.id_viagem);
        } catch (error) {
            console.error('Erro ao declarar anomalia:', error);
            setAnomalyError(error.message);
        } finally {
            setIsSubmittingAnomaly(false);
        }
    };

    return (
        <div className="rate-ride-ticket">
            <div className="ticket-status-header">
                <span className={`status-pill ${statusViagem.toLowerCase().replace(/\s/g, '-')}`}>{statusViagem}</span>
                <span className="ticket-id">ID: {viagem.id_viagem || 'N/A'}</span>
            </div>
            <div className="ticket-details-grid">
                <div className="detail-item from">
                    <p className="label">De</p>
                    <p className="value location">{pontoPartida?.pontoid_ponto?.descricao || 'Local de Partida Indefinido'}</p>
                </div>
                <div className="detail-item to">
                    <p className="label">Para</p>
                    <p className="value location">{pontoChegada?.pontoid_ponto?.descricao || 'Local de Chegada Indefinido'}</p>
                </div>
                <div className="detail-item date">
                    <p className="label">Data</p>
                    <p className="value">{formattedDate}</p>
                </div>
                <div className="detail-item time">
                    <p className="label">Hora</p>
                    <p className="value">{formattedTime}</p>
                </div>
                <div className="detail-item driver">
                    <p className="label">Condutor</p>
                    <p className="value">{condutorNome}</p>
                </div>
                <div className="detail-item duration">
                    <p className="label">Distância</p>
                    <p className="value">{viagem.distancia_percorrida ? `${viagem.distancia_percorrida} km` : 'N/A'}</p>
                </div>
            </div>

            <div className="feedback-section">
                <h3>O que achou da sua viagem?</h3>
                {!feedbackSuccess ? (
                    <div className="feedback-input-group">
                        <textarea
                            value={feedbackText}
                            onChange={handleFeedbackChange}
                            placeholder="Compartilhe a sua experiência..."
                            disabled={isSubmittingFeedback}
                        />
                        {feedbackError && <p className="error-message">{feedbackError}</p>}
                        <button onClick={handleSubmitFeedback} disabled={isSubmittingFeedback}>
                            {isSubmittingFeedback ? 'Enviando...' : 'Enviar Feedback'}
                        </button>
                    </div>
                ) : (
                    <p className="success-message">Feedback enviado com sucesso!</p>
                )}
            </div>

            <div className="anomaly-section">
                <h3>Declarar Anomalia</h3>
                {!anomalySuccess ? (
                    <div className="anomaly-input-group">
                        <textarea
                            value={anomalyDescription}
                            onChange={handleAnomalyChange}
                            placeholder="Descreva o problema ocorrido..."
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
            </div>
        </div>
    );
}

export default RateRideTicket;
