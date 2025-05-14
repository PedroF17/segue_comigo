import '../css/NavBar.css';
import '../css/Admin.css';
import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

function Alerts() {
  const [loading, setLoading] = useState(true);
  const [alertas, setAlertas] = useState([]);
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      navigate('/login');
      return;
    }

    // Verifica se já foi recarregado nesta entrada
    const jaRecarregado = new URLSearchParams(location.search).get('reloaded');

    if (!jaRecarregado) {
      const novaUrl = `${location.pathname}?reloaded=true`;
      window.location.replace(novaUrl); // recarrega com flag
      return;
    }

    const carregarAlertas = async () => {
      await atualizarStatusAlertas();
      await buscarAlertas();
      setLoading(false);
    };

    carregarAlertas();
  }, [navigate, location]);

  const buscarAlertas = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/comunicacao/utilizador_alerta/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (!response.ok) throw new Error('Erro ao buscar alertas.');
      const data = await response.json();
      const ordenado = data.sort((a, b) => b.id_alerta - a.id_alerta);
      setAlertas(ordenado);
    } catch (error) {
      console.error('Erro ao buscar alertas:', error);
      setAlertas([]);
    }
  };

  const atualizarStatusAlertas = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      await fetch('http://127.0.0.1:8000/comunicacao/utilizador_alerta/', {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tipo_alerta_origem: 1, tipo_alerta_destino: 2 }),
      });
    } catch (error) {
      console.error('Erro ao atualizar status dos alertas:', error);
    }
  };

  if (loading) return <p>Carregando alertas...</p>;

  return (
    <div className="admin-page">
      <h1>Meus Alertas</h1>

      <div className="table-container">
        <table className="admin-table">
          <thead>
            <tr>
              <th>ID Alerta</th>
              <th>Descrição</th>
            </tr>
          </thead>
          <tbody>
            {alertas.map((alerta) => (
              <tr key={alerta.id_alerta}>
                <td>{alerta.id_alerta}</td>
                <td>{alerta.descricao}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Alerts;
