import React from 'react';
import '../../css/RideList.css';

function RideList({ rides }) {
  if (!rides || rides.length === 0) {
    return <p>Nenhuma boleia encontrada com os critérios de pesquisa.</p>;
  }

  return (
    <div className="ride-list">
      <h3>Boleias Encontradas:</h3>
      <ul>
        {rides.map(ride => (
          <li key={ride.id}>
            De: {ride.origin} para {ride.destination}))
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RideList;