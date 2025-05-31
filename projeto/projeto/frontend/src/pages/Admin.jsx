import '../css/NavBar.css';
import '../css/Admin.css';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { checkAdmin } from '../services/auth';

function Admin() {
  const [activeTab, setActiveTab] = useState('Ocorrências');
  const [loading, setLoading] = useState(true);
  const [ocorrencias, setOcorrencias] = useState([]);
  const [condutores, setCondutores] = useState([]);
  const [sortBy, setSortBy] = useState('id_ocorrencia');
  const [sortOrder, setSortOrder] = useState('desc');
  const navigate = useNavigate();

  const categories = ['Condutores', 'Ocorrências'];

  useEffect(() => {
    const verifyAccess = async () => {
      const token = localStorage.getItem('accessToken');
      if (!token) {
        navigate('/login');
        return;
      }

      const isAdmin = await checkAdmin();
      if (!isAdmin) {
        navigate('/');
        return;
      }

      setLoading(false);
    };

    verifyAccess();
  }, [navigate]);

  useEffect(() => {
    if (activeTab === 'Ocorrências') {
      fetchOcorrencias();
    } else if (activeTab === 'Condutores') {
      fetchCondutores();
    }
  }, [activeTab]);

  const fetchOcorrencias = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/comunicacao/ocorrencia/read/', {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (!response.ok) throw new Error('Erro ao buscar ocorrências.');
      const data = await response.json();
      setOcorrencias(data);
    } catch (error) {
      console.error('Erro ao buscar ocorrências:', error);
      setOcorrencias([]);
    }
  };

  const fetchCondutores = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/condutor/list/', {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (!response.ok) throw new Error('Erro ao buscar condutores.');
      const data = await response.json();
      setCondutores(data);
    } catch (error) {
      console.error('Erro ao buscar condutores:', error);
      setCondutores([]);
    }
  };

  const handleAtualizarCondutor = async (idUtilizador) => {
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/condutor/list/', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ id_utilizador: idUtilizador }),
      });

      if (!response.ok) throw new Error('Erro ao atualizar condutor.');
      alert('Condutor atualizado com sucesso!');
      fetchCondutores(); // Atualiza lista após alteração
    } catch (error) {
      console.error('Erro ao atualizar condutor:', error);
      alert('Erro ao atualizar condutor.');
    }
  };

  const sortOcorrencias = (list) => {
    const sorted = [...list].sort((a, b) => {
      const aVal = sortBy === 'id_ocorrencia'
        ? a.id_ocorrencia
        : new Date(a.viagemid_viagem?.data_viagem || 0);
      const bVal = sortBy === 'id_ocorrencia'
        ? b.id_ocorrencia
        : new Date(b.viagemid_viagem?.data_viagem || 0);

      return sortOrder === 'asc' ? aVal - bVal : bVal - aVal;
    });
    return sorted;
  };

  if (loading) return <p>Verificando permissões...</p>;

  return (
    <div className="admin-page">
      <h1>Painel Admin</h1>

      <div className="tab-buttons">
        {categories.map((cat) => (
          <button
            key={cat}
            className={activeTab === cat ? 'active' : ''}
            onClick={() => setActiveTab(cat)}
          >
            {cat}
          </button>
        ))}
      </div>

      <div className="table-container">
        <h2>{activeTab}</h2>

        {activeTab === 'Condutores' && (
  <div className="admin-card-list">
    {condutores.map((c) => (
      <div className="admin-card" key={c.id_condutor}>
        <div className="admin-card-row">
          <span className="label">ID Utilizador: </span>
          <span className="value">{c.utilizadorid_utilizador?.id_utilizador}</span>
        </div>
        <div className="admin-card-row">
          <span className="label">ID Condutor: </span>
          <span className="value">{c.id_condutor}</span>
        </div>
        <div className="admin-card-row">
          <span className="label">Nome: </span>
          <span className="value">{c.utilizadorid_utilizador?.nome_primeiro} {c.utilizadorid_utilizador?.nome_ultimo}</span>
        </div>
        <div className="admin-card-row">
          <span className="label">Conta Condutor: </span>
          <span className="value">{c.reputacao === 1 ? 'Validado' : 'Invalidado'}</span>
        </div>
        <div className="admin-card-actions">
          <button
            onClick={() => handleAtualizarCondutor(c.utilizadorid_utilizador?.id_utilizador)}
          >
            Atualizar
          </button>
        </div>
      </div>
    ))}
  </div>
)}

        {activeTab === 'Ocorrências' && (
          <>
            <div className="filters">
              <label>
                Ordenar por:{' '}
                <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
                  <option value="id_ocorrencia">ID</option>
                  <option value="data_viagem">Data da Viagem</option>
                </select>
              </label>
              <label>
                Ordem:{' '}
                <select value={sortOrder} onChange={(e) => setSortOrder(e.target.value)}>
                  <option value="asc">Crescente</option>
                  <option value="desc">Decrescente</option>
                </select>
              </label>
            </div>

            <div className="admin-card-list">
      {sortOcorrencias(ocorrencias).map((o) => (
        <div className="admin-card" key={o.id_ocorrencia}>
          <div className="admin-card-row">
            <span className="label">ID:</span>
            <span className="value">{o.id_ocorrencia}</span>
          </div>
          <div className="admin-card-row">
            <span className="label">Data de Envio:</span>
            <span className="value">{new Date(o.data_envio).toLocaleDateString()}</span>
          </div>
          <div className="admin-card-row">
            <span className="label">Descrição:</span>
            <span className="value">{o.descricao}</span>
          </div>
          <div className="admin-card-row">
            <span className="label">Viagem:</span>
            <span className="value">
              #{o.viagemid_viagem?.id_viagem}
              {o.viagemid_viagem?.data_viagem
                ? ` - ${new Date(o.viagemid_viagem.data_viagem).toLocaleDateString()}`
                : ''}
            </span>
          </div>
          <div className="admin-card-row">
            <span className="label">Utilizador:</span>
            <span className="value">
              #{o.utilizadorid_utilizador?.id_utilizador} -{' '}
              {o.utilizadorid_utilizador?.nome_primeiro}{' '}
              {o.utilizadorid_utilizador?.nome_ultimo}
            </span>
          </div>
        </div>
      ))}
    </div>
          </>
        )}
      </div>
    </div>
  );
}

export default Admin;
