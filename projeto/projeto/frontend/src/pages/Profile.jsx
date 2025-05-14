import '../css/NavBar.css';
import '../css/Admin.css';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function Profile() {
  const [utilizador, setUtilizador] = useState(null);
  const [formData, setFormData] = useState({});
  const [loading, setLoading] = useState(true);
  const [mensagem, setMensagem] = useState('');
  const [estadosCivis, setEstadosCivis] = useState([]);
  const [nacionalidades, setNacionalidades] = useState([]);
  const navigate = useNavigate();
  const [isPassageiro, setIsPassageiro] = useState(false);
  const [isCondutor, setIsCondutor] = useState(false);
  const [grupoUtilizadores, setGrupoUtilizadores] = useState([]);
  const [codigoGrupo, setCodigoGrupo] = useState('');
  const [novoNomeGrupo, setNovoNomeGrupo] = useState('');

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      navigate('/login');
      return;
    }

    const verificarTiposUsuario = async () => {
      const token = localStorage.getItem('accessToken');

      try {
        const resPassageiro = await fetch('http://127.0.0.1:8000/utilizador/check_passageiro/', {
          headers: { Authorization: `Bearer ${token}` }
        });
        if (resPassageiro.ok) {
          const data = await resPassageiro.json();
          setIsPassageiro(data.is_passageiro === true);
        }

        const resCondutor = await fetch('http://127.0.0.1:8000/utilizador/check_condutor/', {
          headers: { Authorization: `Bearer ${token}` }
        });
        if (resCondutor.ok) {
          const data = await resCondutor.json();
          setIsCondutor(data.is_condutor === true);
        }
      } catch (error) {
        console.error("Erro ao verificar tipo de utilizador:", error);
      }
    };

    fetchUserData();
    fetchEstadosCivis();
    fetchNacionalidades();
    verificarTiposUsuario();
  }, [navigate]);

  const fetchUserData = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/utilizador/view/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (!response.ok) throw new Error('Erro ao carregar dados do utilizador.');

      const data = await response.json();
      setUtilizador(data.utilizador);
      setFormData(data.utilizador);
      fetchGrupoUtilizadores(data.utilizador.grupoid_grupo);
      fetchCodigoGrupo();
      setLoading(false);
    } catch (error) {
      console.error(error);
      setMensagem('Erro ao carregar perfil.');
    }
  };

  const fetchEstadosCivis = async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/utilizador/estado_civil/');
      const data = await res.json();
      setEstadosCivis(data);
    } catch (error) {
      console.error('Erro ao carregar estados civis:', error);
    }
  };

  const fetchNacionalidades = async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/utilizador/nacionalidade/');
      const data = await res.json();
      setNacionalidades(data);
    } catch (error) {
      console.error('Erro ao carregar nacionalidades:', error);
    }
  };

  const fetchGrupoUtilizadores = async (grupoId) => {
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch('http://127.0.0.1:8000/utilizador/grupo/view/', {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (!res.ok) throw new Error('Erro ao carregar utilizadores do grupo.');
      const data = await res.json();

      // Filtra os utilizadores com o mesmo grupoid
      const filtrados = data.filter(u => u.grupoid_grupo === grupoId);
      setGrupoUtilizadores(filtrados);
    } catch (error) {
      console.error('Erro ao buscar utilizadores do grupo:', error);
    }
  };

  const fetchCodigoGrupo = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch('http://127.0.0.1:8000/utilizador/grupo/view/code/', {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (!res.ok) throw new Error('Erro ao buscar código do grupo.');
      const data = await res.json();
      setCodigoGrupo(data);
    } catch (error) {
      console.error('Erro ao buscar código do grupo:', error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMensagem('');
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/utilizador/view/', {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error('Erro ao atualizar dados.');
      const data = await response.json();
      setMensagem('Perfil atualizado com sucesso.');
      setUtilizador(data.utilizador);
    } catch (error) {
      console.error(error);
      setMensagem('Erro ao atualizar perfil.');
    }
  };

  const tornarPassageiro = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/viagem/passageiro/create/', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();
      if (response.ok) {
        alert('Você agora é um passageiro!');
        setIsPassageiro(true);
        window.location.reload(); // ⬅️ Recarrega a página
      } else {
        alert('Erro ao tornar-se passageiro: ' + JSON.stringify(data));
      }
    } catch (error) {
      console.error('Erro ao tornar-se passageiro:', error);
    }
  };

  const tornarCondutor = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/condutor/create/', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();
      if (response.ok) {
        alert('Você agora é um condutor!');
        setIsCondutor(true);
        window.location.reload(); // ⬅️ Recarrega a página
      } else {
        alert('Erro ao tornar-se condutor: ' + JSON.stringify(data));
      }
    } catch (error) {
      console.error('Erro ao tornar-se condutor:', error);
    }
  };

  const gerarNovoCodigoGrupo = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch('http://127.0.0.1:8000/utilizador/grupo/view/', {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`
        }
      });
      if (!res.ok) throw new Error('Erro ao gerar novo código.');
      const data = await res.json();
      setCodigoGrupo(data.novo_nome_grupo);
      alert('Novo código de grupo gerado com sucesso!');
    } catch (error) {
      console.error('Erro ao gerar novo código:', error);
      alert('Erro ao gerar novo código.');
    }
  };

  const entrarNoGrupoExistente = async () => {
    if (!novoNomeGrupo.trim()) {
      alert('Por favor, insira um nome de grupo válido.');
      return;
    }

    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/utilizador/grupo/view/code/', {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ grupo_nome: novoNomeGrupo })
      });

      const data = await response.json();
      if (response.ok) {
        alert('Grupo atualizado com sucesso!');
        fetchUserData(); // Atualiza o perfil
      } else {
        alert(data.erro || 'Erro ao entrar no grupo.');
      }
    } catch (error) {
      console.error('Erro ao entrar no grupo existente:', error);
      alert('Erro ao entrar no grupo.');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    navigate('/login');
    window.location.reload();
  };


  if (loading) return <p>Carregando perfil...</p>;

  return (
    <div className="admin-page">
      <h1>Meu Perfil</h1>

      <button onClick={handleLogout} className="btn" style={{ marginBottom: '20px' }}>
        Logout
      </button>

      {mensagem && <p>{mensagem}</p>}

      <form onSubmit={handleSubmit} className="form-container">
        <label>
          Primeiro Nome:
          <input
            type="text"
            name="nome_primeiro"
            value={formData.nome_primeiro || ''}
            onChange={handleChange}
          />
        </label>

        <label>
          Último Nome:
          <input
            type="text"
            name="nome_ultimo"
            value={formData.nome_ultimo || ''}
            onChange={handleChange}
          />
        </label>

        <label>
          Email:
          <input
            type="email"
            name="email"
            value={formData.email || ''}
            onChange={handleChange}
          />
        </label>

        <label>
          Data de Nascimento:
          <input
            type="date"
            name="data_nasc"
            value={formData.data_nasc || ''}
            onChange={handleChange}
          />
        </label>

        <label>
          Gênero:
          <select name="genero" value={formData.genero || ''} onChange={handleChange}>
            <option value="">Selecione</option>
            <option value="M">Masculino</option>
            <option value="F">Feminino</option>
            <option value="O">Outro</option>
          </select>
        </label>

        <label>
          Nº Cartão de Cidadão:
          <input
            type="text"
            name="numero_cc"
            value={formData.numero_cc || ''}
            onChange={handleChange}
          />
        </label>

        <label>
          ID Grupo:
          <input
            type="number"
            name="grupoid_grupo"
            value={formData.grupoid_grupo || ''}
            onChange={handleChange}
          />
        </label>

        <label>
          Estado Civil:
          <select
            name="estado_civilid_estado_civil"
            value={formData.estado_civilid_estado_civil || ''}
            onChange={handleChange}
          >
            <option value="">Selecione</option>
            {estadosCivis.map((estado) => (
              <option key={estado.id_estado_civil} value={estado.id_estado_civil}>
                {estado.descricao}
              </option>
            ))}
          </select>
        </label>

        <label>
          Nacionalidade:
          <select
            name="nacionalidadeid_nacionalidade"
            value={formData.nacionalidadeid_nacionalidade || ''}
            onChange={handleChange}
          >
            <option value="">Selecione</option>
            {nacionalidades.map((nacionalidade) => (
              <option key={nacionalidade.id_nacionalidade} value={nacionalidade.id_nacionalidade}>
                {nacionalidade.paisid_pais.nome}
              </option>
            ))}
          </select>
        </label>

        <label>
          Nova Senha:
          <input
            type="password"
            name="password"
            value={formData.password || ''}
            onChange={handleChange}
          />
        </label>

        <button type="submit">Atualizar Perfil</button>
      </form>

      <div style={{ marginTop: '30px' }}>
        {!isPassageiro && (
          <button onClick={tornarPassageiro} className="btn">
            Tornar-se Passageiro
          </button>
        )}

        {!isCondutor && (
          <button onClick={tornarCondutor} className="btn" style={{ marginLeft: '10px' }}>
            Tornar-se Condutor
          </button>
        )}
      </div>

      <div style={{ marginTop: '40px' }}>
        <h2>Membros do Grupo</h2>
        {grupoUtilizadores.length === 0 ? (
          <p>Nenhum outro utilizador no grupo.</p>
        ) : (
          <div className="table-container">
            <table className="admin-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Primeiro Nome</th>
                  <th>Último Nome</th>
                </tr>
              </thead>
              <tbody>
                {grupoUtilizadores.map((u) => (
                  <tr key={u.id_utilizador}>
                    <td>{u.id_utilizador}</td>
                    <td>{u.nome_primeiro}</td>
                    <td>{u.nome_ultimo}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
      <div style={{ marginTop: '30px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <input
            type="text"
            value={codigoGrupo}
            readOnly
            style={{ padding: '8px', fontSize: '16px', flex: '1', backgroundColor: '#f5f5f5' }}
          />
          <button onClick={gerarNovoCodigoGrupo} className="btn">
            Gerar Novo Código
          </button>
        </div>
      </div>
      <div style={{ marginTop: '20px' }}>
      <h3>Entrar em Grupo Existente</h3>
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <input
            type="text"
            value={novoNomeGrupo}
            onChange={(e) => setNovoNomeGrupo(e.target.value)}
            placeholder="Nome do grupo"
            style={{ padding: '8px', fontSize: '16px', flex: '1' }}
          />
          <button onClick={entrarNoGrupoExistente} className="btn">
            Entrar no Grupo
          </button>
        </div>
      </div>


    </div>
  );
}

export default Profile;
