import React from 'react';
import '../../css/Rides.css';

function Rides({ ride }) {
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
                <button className="buy-button">Comprar</button>
                <button className="view-details-button">Ver Detalhes</button>
            </div>
            {ride.rating && (
                <div className="ride-rating">
                    Avaliação: {ride.rating} <span className="star">★</span>
                </div>
            )}
        </div>
    );
}

export default Rides;