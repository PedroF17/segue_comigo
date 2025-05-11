import React, { useState, useEffect } from 'react';
import Select from 'react-select';
import { useNavigate } from 'react-router-dom';

function OcorrenciasPage() {
  const [descricao, setDescricao] = useState('');
  const [viagens, setViagens] = useState([]);
  const [tiposOcorrencia, setTiposOcorrencia] = useState([]);
  const [viagemSelecionada, setViagemSelecionada] = useState(null);
  const [tipoOcorrenciaSelecionado, setTipoOcorrenciaSelecionado] = useState(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      navigate('/login');
      return;
    }

    fetchViagens(token);
    fetchTiposOcorrencia(token);
  }, [navigate]);

  const fetchViagens = async (token) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/viagem/list/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (!response.ok) throw new Error('Erro ao buscar viagens');
      const data = await response.json();

      const formatted = data.map((viagem) => ({
        value: viagem.id_viagem,
        label: `Viagem #${viagem.id_viagem} - ${new Date(viagem.data_viagem).toLocaleString()}`,
      }));

      setViagens(formatted);
    } catch (err) {
      console.error('Erro ao buscar viagens:', err);
      setViagens([]);
    }
  };

  const fetchTiposOcorrencia = async (token) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/comunicacao/tipo_ocorrencia/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (!response.ok) throw new Error('Erro ao buscar tipos de ocorrência');
      const data = await response.json();

      const formatted = data.map((tipo) => ({
        value: tipo.id_tipo_ocorrencia,
        label: tipo.descricao,
      }));

      setTiposOcorrencia(formatted);
    } catch (err) {
      console.error('Erro ao buscar tipos de ocorrência:', err);
      setTiposOcorrencia([]);
    }
  };

  const handleSubmit = async () => {
    const token = localStorage.getItem('accessToken');

    if (!descricao || !viagemSelecionada || !tipoOcorrenciaSelecionado) {
      alert('Por favor, preencha todos os campos.');
      return;
    }

    setLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:8000/comunicacao/ocorrencia/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          descricao: descricao,
          viagemid_viagem: viagemSelecionada.value,
          tipo_ocorrenciaid_tipo_ocorrencia: tipoOcorrenciaSelecionado.value,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Erro ao enviar ocorrência.');
      }

      alert('Ocorrência enviada com sucesso!');
      setDescricao('');
      setViagemSelecionada(null);
      setTipoOcorrenciaSelecionado(null);
    } catch (err) {
      console.error('Erro ao enviar ocorrência:', err);
      alert(err.message || 'Erro ao enviar ocorrência.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="ride-tickets-page" style={{ display: 'flex', justifyContent: 'center' }}>
      <div style={{ width: '80%', maxWidth: '800px' }}>
        <h1>Feedback</h1>

        <div className="tab-content">

          <div style={{ marginBottom: '1rem' }}>
            <label>Descrição da Ocorrência:</label>
            <textarea
              value={descricao}
              onChange={(e) => setDescricao(e.target.value)}
              rows={6}
              style={{ width: '100%', resize: 'vertical', padding: '0.5rem' }}
              placeholder="Descreva o que aconteceu..."
            />
          </div>

          <div style={{ marginBottom: '1rem' }}>
            <label>Selecione a Viagem:</label>
            <Select
              options={viagens}
              value={viagemSelecionada}
              onChange={setViagemSelecionada}
              placeholder="Escolha uma viagem..."
            />
          </div>

          <div style={{ marginBottom: '1rem' }}>
            <label>Tipo de Ocorrência:</label>
            <Select
              options={tiposOcorrencia}
              value={tipoOcorrenciaSelecionado}
              onChange={setTipoOcorrenciaSelecionado}
              placeholder="Escolha um tipo..."
            />
          </div>

          <button onClick={handleSubmit} disabled={loading} style={{ padding: '0.5rem 1rem' }}>
            {loading ? 'Enviando...' : 'Enviar Ocorrência'}
          </button>
        </div>
      </div>
    </div>
  );
}

export default OcorrenciasPage;
