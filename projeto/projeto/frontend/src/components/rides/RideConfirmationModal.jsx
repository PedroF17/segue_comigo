import React from 'react';
import '../../css/RideConfirmationModal.css';

function RideConfirmationModal({ ride, onClose, onConfirm }) {
  if (!ride) {
    return null;
  }

  return (
    <div className="ride-confirmation-modal-overlay">
      <div className="ride-confirmation-modal">
        <div className="modal-header">
          <h3>Confirmar Boleia</h3>
          <button onClick={onClose} className="close-button">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div className="modal-body">
          <div className="ride-details-confirmation">
            <div className="airline-info">
              {ride.agency && <p>{ride.agency}</p>}
              {ride.imageUrl && <img src={ride.imageUrl} alt={`${ride.driver || 'Boleia'} Logo`} />}
            </div>
            <div className="departure-arrival">
              <div className="departure">
                <h4>{ride.origin.substring(0, 3).toUpperCase()}</h4> {/* Example: First 3 letters */}
                <p>{ride.origin}</p>
                <p>{ride.time}</p>
              </div>
              <div className="arrow-icon">→</div>
              <div className="arrival">
                <h4>{ride.destination.substring(0, 3).toUpperCase()}</h4> {/* Example: First 3 letters */}
                <p>{ride.destination}</p>
                <p>{ride.time}</p> {/* Assuming same time for simplicity */}
              </div>
            </div>
            <p className="price-confirmation">Preço Total: <span className="price">${ride.price}</span></p>
          </div>
          <div className="payment-options">
            <p>Opções de Pagamento:</p>
            <div className="payment-icons">
              <span className="visa">Visa</span>
              <span className="mastercard">Mastercard</span>
              <span className="paypal">PayPal</span>
              {/* Add more payment icons/options as needed */}
            </div>
            <p className="encryption-info">Transações Encriptadas pela Segue Comigo (Placeholder)</p>
          </div>
        </div>
        <div className="modal-footer">
          <button onClick={onClose} className="cancel-button">Cancelar</button>
          <button onClick={() => onConfirm(ride)} className="confirm-button">Comprar Agora</button>
        </div>
      </div>
    </div>
  );
}

export default RideConfirmationModal;