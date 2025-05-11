import React from 'react';
import '../../css/ReservaCard.css';

function formatDate(dateString) {
  const options = { day: '2-digit', month: '2-digit', year: 'numeric' };
  return new Date(dateString).toLocaleDateString('pt-PT', options);
}

function ReservaCard({ reserva }) {
  const { data_emissao, data_viagem, valor, condutorid_condutor } = reserva;

  return (
    <div className="reserva-card">
      <h3>Reserva #{reserva.id_reserva}</h3>
      <p><strong>Data de Emissão:</strong> {formatDate(data_emissao)}</p>
      <p><strong>Data da Viagem:</strong> {formatDate(data_viagem)}</p>
      <p><strong>Valor:</strong> €{valor}</p>
      <p><strong>ID do Condutor:</strong> {condutorid_condutor?.id_condutor}</p>
    </div>
  );
}

export default ReservaCard;
