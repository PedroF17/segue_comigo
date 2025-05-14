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
          <>
            <table className="admin-table">
              <thead>
                <tr>
                  <th>ID Utilizador</th>
                  <th>ID Condutor</th>
                  <th>Nome</th>
                  <th>Apelido</th>
                  <th>Reputação</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {condutores.map((c) => (
                  <tr key={c.id_condutor}>
                    <td>{c.utilizadorid_utilizador?.id_utilizador}</td>
                    <td>{c.id_condutor}</td>
                    <td>{c.utilizadorid_utilizador?.nome_primeiro}</td>
                    <td>{c.utilizadorid_utilizador?.nome_ultimo}</td>
                    <td>{c.reputacao === 1 ? 'Validado' : 'Invalidado'}</td>
                    <td>
                      <button
                        onClick={() => handleAtualizarCondutor(c.utilizadorid_utilizador?.id_utilizador)}
                      >
                        Atualizar
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </>
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

            <table className="admin-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Data de Envio</th>
                  <th>Descrição</th>
                  <th>Viagem</th>
                  <th>Utilizador</th>
                </tr>
              </thead>
              <tbody>
                {sortOcorrencias(ocorrencias).map((o) => (
                  <tr key={o.id_ocorrencia}>
                    <td>{o.id_ocorrencia}</td>
                    <td>{new Date(o.data_envio).toLocaleDateString()}</td>
                    <td>{o.descricao}</td>
                    <td>
                      #{o.viagemid_viagem?.id_viagem}{' '}
                      {o.viagemid_viagem?.data_viagem
                        ? `- ${new Date(o.viagemid_viagem.data_viagem).toLocaleDateString()}`
                        : ''}
                    </td>
                    <td>
                      #{o.utilizadorid_utilizador?.id_utilizador} -{' '}
                      {o.utilizadorid_utilizador?.nome_primeiro}{' '}
                      {o.utilizadorid_utilizador?.nome_ultimo}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </>
        )}
      </div>
    </div>
  );
}

export default Admin;
