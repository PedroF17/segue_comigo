import React from 'react';
import '../../css/RideTicket.css'; // Crie este ficheiro CSS

function RideTicket({ ticket }) {
  const getStatusColor = (status) => {
    switch (status) {
      case 'Aceite':
        return 'green';
      case 'Pendente':
        return 'orange';
      case 'cancelamento pendente':
        return 'yellow';
      case 'cancelado com sucesso':
        return 'gray';
      case 'rejeitada':
        return 'red';
      default:
        return 'black';
    }
  };

  return (
    <div className="ride-ticket">
      <div className="ticket-header">
        <span className="ride-icon">Ride</span> {/* Pode usar um ícone real aqui */}
        <span className="airline">{ticket.airline || 'N/A'}</span>
        {ticket.remainingPlaces && <span className="remaining-places">Remaining Places: {ticket.remainingPlaces}</span>}
      </div>
      <div className="ticket-details">
          <p className="label">From</p>
          <p className="location">{ticket.departureLocation}</p>
          <p className="airport">{ticket.departureAirport}</p>
          <p className="date-time">{ticket.departureDateTime}</p>
        </div>
        <div className="to-section">
          <p className="label">To</p>
          <p className="location">{ticket.arrivalLocation}</p>
          <p className="airport">{ticket.arrivalAirport}</p>
          <p className="date-time">{ticket.arrivalDateTime}</p>
        </div>
        <div className="duration-section">
          <p className="label">Duration</p>
          <p className="duration">{ticket.duration || 'N/A'}</p>
        </div>
        <div className="status-section">
          <p className="label">State of Registration/Request</p>
          <p className="status" style={{ backgroundColor: getStatusColor(ticket.status) }}>
            {ticket.status}
          </p>
        </div>
      </div>
      );
}

export default RideTicket;