import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Select from 'react-select';
import '../../css/NeighborRideSearch.css';

function NeighborRideSearch() {
  const [pontos, setPontos] = useState([]);
  const [origin, setOrigin] = useState(null);
  const [destination, setDestination] = useState(null);
  const [date, setDate] = useState('');
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Verificação de autenticação e tipo
  const checkUserAuth = async () => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      navigate('/login');
      return false;
    }

    const response = await fetch('http://127.0.0.1:8000/check_passageiro/', {
      headers: { Authorization: `Bearer ${token}` },
    });

    if (!response.ok) {
      navigate('/login');
      return false;
    }

    const result = await response.json();
    if (!result.is_passageiro) {
      navigate('/login');
      return false;
    }

    return true;
  };

  // Buscar pontos
  useEffect(() => {
    const fetchPontos = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/viagem/ponto/');
        if (!res.ok) throw new Error('Erro ao buscar pontos');
        const data = await res.json();
        const formatted = data.map((p) => ({
          value: p.id_ponto,
          label: p.descricao,
        }));
        setPontos(formatted);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    fetchPontos();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const isValidUser = await checkUserAuth();
    if (!isValidUser) return;

    if (!origin || !destination || !date) {
      alert('Todos os campos são obrigatórios.');
      return;
    }

    const reservaPayload = {
      ponto_inicial_id: origin.value,
      ponto_final_id: destination.value,
      data_viagem: date,
      valor: 10, // ← valor fixo (pode ajustar conforme necessário)
    };

    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/viagem/reserva/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(reservaPayload),
      });

      const result = await response.json();
      if (response.ok) {
        alert('Reserva criada com sucesso!');
        navigate('/os-meus-tickets'); // redireciona após sucesso (ajuste o path se necessário)
      } else {
        alert(result.detail || result.erro || 'Erro ao criar reserva.');
      }
    } catch (error) {
      console.error('Erro ao enviar reserva:', error);
      alert('Erro técnico ao criar reserva.');
    }
  };

  if (loading) return <p>A carregar pontos...</p>;

  return (
    <div className="neighbor-ride-search">
      <h2>Reserve uma boleia na vizinhança</h2>
      <form onSubmit={handleSubmit} className="ride-search-form">
        <div className="form-group">
          <label>Origem:</label>
          <Select
            options={pontos}
            value={origin}
            onChange={setOrigin}
            placeholder="Escolha o ponto de origem"
            isSearchable
            required
          />
        </div>

        <div className="form-group">
          <label>Destino:</label>
          <Select
            options={pontos}
            value={destination}
            onChange={setDestination}
            placeholder="Escolha o ponto de destino"
            isSearchable
            required
          />
        </div>

        <div className="form-group">
          <label>Data da Viagem:</label>
          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          />
        </div>

        <button type="submit" className="search-button">
          Criar Reserva
        </button>
      </form>
    </div>
  );
}

export default NeighborRideSearch;
