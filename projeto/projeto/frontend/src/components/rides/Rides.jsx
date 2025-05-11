import React, { useState } from 'react';
import '../../css/Rides.css';
import RideConfirmationModal from './RideConfirmationModal.jsx';

function Rides({ ride }) {
        const [showConfirmationModal, setShowConfirmationModal] = useState(false);

        const handleBuyClick = () => {
         setShowConfirmationModal(true);
        };

        const handleCloseModal = () => {
         setShowConfirmationModal(false);
         };

        const handleConfirmPurchase = (selectedRide) => {
         // Implement your purchase logic here (e.g., send data to backend)
        console.log('Compra confirmada para:', selectedRide);
        setShowConfirmationModal(false);
        };


    return (
        <div className="ride-card">
            <div className="ride-image">
                <img src={ride.imageUrl} alt={`Boleia de ${ride.driver}`} />
            </div>
            <div className="ride-details">
                <h3>{ride.driver} {ride.agency && `(${ride.agency})`}</h3>
                <p>De: {ride.origin} para: {ride.destination}</p>
                <p>Data: {ride.date}, Hora: {ride.time}</p>
                <p>Lugares Disponíveis: {ride.seatsAvailable}</p>
            </div>
            <div className="ride-pricing">
                <span className="price">${ride.price}</span>
                <button className="buy-button" onClick={handleBuyClick} >Comprar</button>
                <button className="view-details-button">Ver Detalhes</button>
            </div>
            {ride.rating && (
                <div className="ride-rating">
                    Avaliação: {ride.rating} <span className="star">★</span>
                </div>
            )}
            {showConfirmationModal && (
                <RideConfirmationModal
                  ride={ride}
                  onClose={handleCloseModal}
                  onConfirm={handleConfirmPurchase}
                />
            )}
        </div>
    );
}

export default Rides;