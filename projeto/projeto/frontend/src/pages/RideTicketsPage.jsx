import React, { useState, useEffect } from 'react';
import '../css/RideTicketsPage.css';
import RideTicket from '../components/rides/RideTicket.jsx';
import { useNavigate } from 'react-router-dom';
import { checkPassageiro } from '../services/auth';
import Select from 'react-select';

function RideTicketsPage() {
  const [activeTab, setActiveTab] = useState('Reservas');
  const [tickets, setTickets] = useState([]);
  const [reservas, setReservas] = useState([]);
  const [viagens, setViagens] = useState([]);
  const [viagemSelecionada, setViagemSelecionada] = useState(null);
  const navigate = useNavigate();

  const [filtroStatus, setFiltroStatus] = useState('Todas');
  const [filtroOrdenacao, setFiltroOrdenacao] = useState('id');
  const [filtroStatusViagem, setFiltroStatusViagem] = useState('Todas');
  const [filtroOrdenacaoViagem, setFiltroOrdenacaoViagem] = useState('id');


  const [utilizadores, setUtilizadores] = useState([]);
  const [utilizadorSelecionado, setUtilizadorSelecionado] = useState(null);
  const [isLoadingUtilizadores, setIsLoadingUtilizadores] = useState(false);
  const tabs = ['Reservas', 'Desvios', 'Viagens'];

  const [pontos, setPontos] = useState([]);
  const [pontoSelecionado, setPontoSelecionado] = useState(null);
  const [loading, setLoading] = useState(false);
  const [pontoInicial, setPontoInicial] = useState(null);
  const [pontoFinal, setPontoFinal] = useState(null);


  useEffect(() => {
    const verifyAccess = async () => {
      const token = localStorage.getItem('accessToken');
      if (!token) {
        navigate('/login');
        return;
      }

      const isPassageiro = await checkPassageiro();

      if (!isPassageiro) {
        navigate('/');
        return;
      }

      //fetchRideTickets();
      fetchReservas(token);
      fetchViagens(token);
      buscarPontos(setPontos, setLoading);
    };

    /*
    const fetchRideTickets = async () => {
      try {
        const response = await fetch('/api/user/tickets');
        if (!response.ok) throw new Error('Erro ao buscar bilhetes');
        const data = await response.json();
        setTickets(data);
      } catch (err) {
        console.error('Erro ao buscar bilhetes:', err);
        setTickets([]);
      }
    };
    */

    const fetchReservas = async (token) => {
      try {
        const response = await fetch('http://127.0.0.1:8000/viagem/reserva/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (!response.ok) throw new Error('Erro ao buscar reservas');
        const data = await response.json();
        setReservas(data);
      } catch (err) {
        console.error('Erro ao buscar reservas:', err);
        setReservas([]);
      }
    };

    const fetchViagens = async (token) => {
      try {
        const response = await fetch('http://127.0.0.1:8000/viagem/viagem/list/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) throw new Error('Erro ao buscar viagens');
        const data = await response.json();
        setViagens(data);
      } catch (err) {
        console.error('Erro ao buscar viagens:', err);
        setViagens([]);
      }
    };

    verifyAccess();
  }, [navigate]);

  const handleDeleteReserva = async (idReserva) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    const confirmDelete = window.confirm("Tem certeza que deseja remover esta reserva?");
    if (!confirmDelete) return;

    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/reserva/${idReserva}/`, {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (response.status === 204) {
        alert("Reserva removida com sucesso!");
        setReservas(prev => prev.filter(r => r.id_reserva !== idReserva));
      } else {
        const data = await response.json();
        alert(data.erro || "Erro ao remover reserva.");
      }
    } catch (err) {
      console.error('Erro ao remover reserva:', err);
    }
  };

  const handleAcceptReserva = async (idReserva) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/reserva/confirm2/${idReserva}/`, {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        alert("Reserva aceite com sucesso!");
        setReservas(prev => prev.map(r =>
          r.id_reserva === idReserva
            ? {
                ...r,
                status_reservaid_status_reserva: {
                  ...r.status_reservaid_status_reserva,
                  id_status_reserva: 3,
                  descricao: 'Finalizada',
                }
              }
            : r
        ));
      } else {
        const data = await response.json();
        alert(data.erro || "Erro ao aceitar reserva.");
      }
    } catch (err) {
      console.error('Erro ao aceitar reserva:', err);
    }
  };

  const buscarUtilizadoresDoGrupo = async () => {
    const token = localStorage.getItem('accessToken');
    setIsLoadingUtilizadores(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/utilizador/grupo/view/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const data = await response.json();
      const options = data.map((u) => ({
        value: u.id_utilizador,
        label: `${u.nome_primeiro} ${u.nome_ultimo}`,
      }));
      setUtilizadores(options);
    } catch (err) {
      console.error('Erro ao buscar utilizadores:', err);
    } finally {
      setIsLoadingUtilizadores(false);
    }
  };

  const associarUtilizadorAViagem = async () => {
    const token = localStorage.getItem('accessToken');
    if (!utilizadorSelecionado || !viagemSelecionada) return;

    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/viagem/associate/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          id_viagem: viagemSelecionada.id_viagem,
          id_utilizador: utilizadorSelecionado.value,
        }),
      });

      const data = await response.json();
      if (response.ok) {
        alert('Passageiro associado com sucesso. Atualize a página para ver as mudanças.');
        setUtilizadorSelecionado(null);
      } else {
        alert(data.error || 'Erro ao associar passageiro.');
      }
    } catch (err) {
      console.error('Erro ao associar passageiro:', err);
    }
  };

  const removerPassageiro = async (idUtilizador) => {
    const token = localStorage.getItem('accessToken');
    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/viagem/associate/', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          id_viagem: viagemSelecionada.id_viagem,
          id_utilizador: idUtilizador,
        }),
      });

      const data = await response.json();
      if (response.ok) {
        alert('Passageiro removido com sucesso. Atualize a página para ver as mudanças.');
      } else {
        alert(data.error || 'Erro ao remover passageiro.');
      }
    } catch (err) {
      console.error('Erro ao remover passageiro:', err);
    }
  };

  const autoRemoverPassageiro = async () => {
    const token = localStorage.getItem('accessToken');
    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/viagem/desassociate/', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          id_viagem: viagemSelecionada.id_viagem
        }),
      });

      const data = await response.json();
      if (response.ok) {
        alert('Passageiro removido com sucesso. Atualize a página para ver as mudanças.');
      } else {
        alert(data.error || 'Erro ao remover passageiro.');
      }
    } catch (err) {
      console.error('Erro ao remover passageiro:', err);
    }
  };


  const solicitarDesvio = async (viagemId, pontoInicialId, pontoFinalId, limparSelecao) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/desvio/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          id_viagem: viagemId,
          ponto_inicial_id: pontoInicialId,
          ponto_final_id: pontoFinalId,
        }),
      });

      const data = await response.json();
      if (response.ok) {
        alert('Desvio solicitado com sucesso. Atualize a página para ver as mudanças.');
        limparSelecao(); // limpar seleção dos pontos
      } else {
        alert(data.error || 'Erro ao solicitar desvio.');
      }
    } catch (err) {
      console.error('Erro ao solicitar desvio:', err);
    }
  };


  const cancelarDesvio = async (idDesvio) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/desvio/${idDesvio}/`, {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        alert("Desvio cancelado com sucesso!");
      }
    } catch (err) {
      console.error('Erro ao cancelar desvio:', err);
    }
  };

  const buscarPontos = async (setPontos, setLoading) => {
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


  const reservasFiltradas = reservas.filter((reserva) => {
    const status = reserva.status_reservaid_status_reserva?.descricao;
    if (filtroStatus === 'Todas') return true;
    return status === filtroStatus;
  });

  const reservasOrdenadas = [...reservasFiltradas].sort((a, b) => {
    if (filtroOrdenacao === 'data_emissao_desc') {
      return new Date(b.data_emissao) - new Date(a.data_emissao);
    }
    return a.id_reserva - b.id_reserva;
  });

  const viagensFiltradas = viagens.filter((viagem) => {
    const status = viagem.status_viagemid_status_viagem?.descricao;
    if (filtroStatusViagem === 'Todas') return true;
    return status === filtroStatusViagem;
  });

  const viagensOrdenadas = [...viagensFiltradas].sort((a, b) => {
    if (filtroOrdenacaoViagem === 'data_viagem_desc') {
      return new Date(b.data_viagem) - new Date(a.data_viagem);
    }
    return a.id_viagem - b.id_viagem;
  });


  return (
    <div className="ride-tickets-page">
      <h1>Painel do Passageiro</h1>

      <div className="tab-buttons">
        {tabs.map((tab) => (
          <button
            key={tab}
            className={activeTab === tab ? 'active' : ''}
            onClick={() => setActiveTab(tab)}
          >
            {tab}
          </button>
        ))}
      </div>

      <div className="tab-content">
        {activeTab === 'Reservas' && (
          <>
            <h2>Minhas Reservas</h2>

            <div style={{ display: 'flex', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label htmlFor="filtroStatus">Filtrar por status:</label><br />
                <select id="filtroStatus" value={filtroStatus} onChange={(e) => setFiltroStatus(e.target.value)}>
                  <option value="Todas">Todas</option>
                  <option value="Pendente">Pendente</option>
                  <option value="Aceite">Aceite</option>
                  <option value="Finalizada">Finalizada</option>
                </select>
              </div>
              <div>
                <label htmlFor="filtroOrdenacao">Ordenar por:</label><br />
                <select id="filtroOrdenacao" value={filtroOrdenacao} onChange={(e) => setFiltroOrdenacao(e.target.value)}>
                  <option value="ID">ID</option>
                  <option value="data_emissao_desc">Data de Emissão</option>
                </select>
              </div>
            </div>

            {reservasOrdenadas.length === 0 ? (
              <p>Nenhuma reserva disponível.</p>
            ) : (
              <table className="admin-table">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Data de Emissão</th>
                    <th>Data da Viagem</th>
                    <th>Valor</th>
                    <th>Condutor</th>
                    <th>Origem</th>
                    <th>Destino</th>
                    <th>Status</th>
                    <th>Ações</th>
                  </tr>
                </thead>
                <tbody>
                  {reservasOrdenadas.map((reserva) => {
                    const origem = reserva.pontos_reserva.find(p => p.destino === 0)?.pontoid_ponto.descricao || '-';
                    const destino = reserva.pontos_reserva.find(p => p.destino === 1)?.pontoid_ponto.descricao || '-';
                    const status = reserva.status_reservaid_status_reserva?.descricao || '-';
                    const statusId = reserva.status_reservaid_status_reserva?.id_status_reserva;

                    return (
                      <tr key={reserva.id_reserva}>
                        <td>{reserva.id_reserva}</td>
                        <td>{reserva.data_emissao}</td>
                        <td>{new Date(reserva.data_viagem).toLocaleDateString()}</td>
                        <td>{reserva.valor}€</td>
                        <td>{reserva.condutorid_condutor?.id_condutor || '-'}</td>
                        <td>{origem}</td>
                        <td>{destino}</td>
                        <td>{status}</td>
                        <td>
                          <div style={{ display: 'flex', gap: '8px' }}>
                            {(statusId === 1 || statusId === 2) && (
                              <button onClick={() => handleDeleteReserva(reserva.id_reserva)}>Remover</button>
                            )}
                            {statusId === 2 && (
                              <button onClick={() => handleAcceptReserva(reserva.id_reserva)}>Aceitar</button>
                            )}
                          </div>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            )}
          </>
        )}


        {activeTab === 'Desvios' && (
          <div>
            <h2>Meus Desvios</h2>

            <div style={{ display: 'flex', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label htmlFor="filtroStatusViagem">Filtrar por status:</label><br />
                <select
                  id="filtroStatusViagem"
                  value={filtroStatusViagem}
                  onChange={(e) => setFiltroStatusViagem(e.target.value)}
                >
                  <option value="Todas">Todas</option>
                  <option value="Pendente">Pendente</option>
                  <option value="Em Andamento">Em Andamento</option>
                  <option value="Finalizada">Finalizada</option>
                </select>
              </div>
              <div>
                <label htmlFor="filtroOrdenacaoViagem">Ordenar por:</label><br />
                <select
                  id="filtroOrdenacaoViagem"
                  value={filtroOrdenacaoViagem}
                  onChange={(e) => setFiltroOrdenacaoViagem(e.target.value)}
                >
                  <option value="id">ID</option>
                  <option value="data_viagem_desc">Data da Viagem</option>
                </select>
              </div>
            </div>

            {viagensOrdenadas.length === 0 ? (
                  <p>Nenhuma viagem encontrada.</p>
                ) : (
                  <table className="admin-table">
                    <thead>
                      <tr>
                        <th>ID</th>
                        <th>Data da Viagem</th>
                        <th>Distância Percorrida (km)</th>
                        <th>Condutor</th>
                        <th>Origem</th>
                        <th>Destino</th>
                        <th>Status</th>
                        <th>Ações</th>
                      </tr>
                    </thead>
                    <tbody>
                      {viagensOrdenadas.map((viagem) => (

                        <React.Fragment key={viagem.id_viagem}>
                          <tr>
                            <td>{viagem.id_viagem}</td>
                            <td>{new Date(viagem.data_viagem).toLocaleDateString()}</td>
                            <td>{viagem.distancia_percorrida}</td>
                            <td>{viagem.condutorid_condutor}</td>
                            <td>{viagem.pontos_viagem.find(p => p.destino === 0)?.pontoid_ponto.descricao}</td>
                            <td>{viagem.pontos_viagem.find(p => p.destino === 1)?.pontoid_ponto.descricao}</td>
                            <td>{viagem.status_viagemid_status_viagem?.descricao}</td>
                            <td>
                                <button onClick={() => {
                                setViagemSelecionada(prev => prev?.id_viagem === viagem.id_viagem ? null : viagem);
                              }}>
                                Desvios
                              </button>
                            </td>
                          </tr>
                          {viagemSelecionada?.id_viagem === viagem.id_viagem && (
                          <tr>
                            <td colSpan="8">
                              <div style={{ marginBottom: '1rem' }}>
                                <button
                                  onClick={() => {
                                    if (pontos.length > 0) {
                                      setPontos([]);
                                    } else {
                                      setLoading(true);
                                      buscarPontos(setPontos, setLoading);
                                    }
                                  }}
                                  disabled={loading}
                                >
                                  {loading ? 'Carregando pontos...' : 'Solicitar Desvio'}
                                </button>
                                {pontos.length > 0 && (
                                <div style={{ marginTop: '10px' }}>
                                  
                                <div style={{ marginTop: '10px', display: 'flex', flexDirection: 'column', gap: '0.5rem'  }}>
                                  <Select
                                    options={pontos}
                                    value={pontoInicial}
                                    onChange={setPontoInicial}
                                    placeholder="Selecione o ponto de origem"
                                  />
                                  <Select
                                    options={pontos}
                                    value={pontoFinal}
                                    onChange={setPontoFinal}
                                    placeholder="Selecione o ponto de destino"
                                  />
                                </div>
                                <button
                                    onClick={() => solicitarDesvio(
                                      viagemSelecionada.id_viagem,
                                      pontoInicial?.value,
                                      pontoFinal?.value,
                                      () => {
                                        setPontoInicial(null);
                                        setPontoFinal(null);
                                      }
                                    )}
                                    disabled={!pontoInicial || !pontoFinal}
                                  >
                                    Solicitar
                                  </button>

                                </div>
                              )}
                              </div>

                              <label>Desvios da Viagem</label>
                              {viagem.desvios && viagem.desvios.length > 0 ? (
                                <table className="admin-table">
                                  <thead>
                                    <tr>
                                      <th>ID Desvio</th>
                                      <th>Data de Emissão</th>
                                      <th>Origem</th>
                                      <th>Destino</th>
                                      <th>Nova Origem</th>
                                      <th>Novo Destino</th>
                                      <th>Status</th>
                                      <th>Ações</th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {viagem.desvios
                                      .slice()
                                      .sort((a, b) => {
                                        const prioridade = (status) => {
                                          if (status === "Pendente") return 0;
                                          if (status === "Ativo") return 1;
                                          return 2;
                                        };
                                        return prioridade(a.status_desvio) - prioridade(b.status_desvio);
                                      })
                                      .map((desvio, idx) => {
                                        const origem = desvio.pontos_desvio.find(p => p.original === "1" && p.destino === "0");
                                        const destino = desvio.pontos_desvio.find(p => p.original === "1" && p.destino === "1");
                                        const novaOrigem = desvio.pontos_desvio.find(p => p.original === "0" && p.destino === "0");
                                        const novoDestino = desvio.pontos_desvio.find(p => p.original === "0" && p.destino === "1");

                                        return (
                                          <tr key={idx}>
                                            <td>{desvio.id_desvio}</td>
                                            <td>{new Date(desvio.data_emissao).toLocaleDateString()}</td>
                                            <td>{origem?.descricao_ponto || '—'}</td>
                                            <td>{destino?.descricao_ponto || '—'}</td>
                                            <td>{novaOrigem?.descricao_ponto || '—'}</td>
                                            <td>{novoDestino?.descricao_ponto || '—'}</td>
                                            <td>{desvio.status_desvio}</td>
                                            <td>
                                              {desvio.status_desvio === "Pendente" && (
                                                <button onClick={() => cancelarDesvio(viagem.id_viagem)}>
                                                  Cancelar
                                                </button>
                                              )}
                                            </td>
                                          </tr>
                                        );
                                      })}
                                  </tbody>
                                </table>
                              ) : (
                                <p>Nenhum desvio registrado para esta viagem.</p>
                              )}
                            </td>
                          </tr>
                        )}
                        </React.Fragment>
                      ))}
                    </tbody>
                  </table>
                )}
            </div>
        )}


        {activeTab === 'Viagens' && (
          <div>
            <h2>Minhas Viagens</h2>

            <div style={{ display: 'flex', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label htmlFor="filtroStatusViagem">Filtrar por status:</label><br />
                <select
                  id="filtroStatusViagem"
                  value={filtroStatusViagem}
                  onChange={(e) => setFiltroStatusViagem(e.target.value)}
                >
                  <option value="Todas">Todas</option>
                  <option value="Pendente">Pendente</option>
                  <option value="Em Andamento">Em Andamento</option>
                  <option value="Finalizada">Finalizada</option>
                </select>
              </div>
              <div>
                <label htmlFor="filtroOrdenacaoViagem">Ordenar por:</label><br />
                <select
                  id="filtroOrdenacaoViagem"
                  value={filtroOrdenacaoViagem}
                  onChange={(e) => setFiltroOrdenacaoViagem(e.target.value)}
                >
                  <option value="id">ID</option>
                  <option value="data_viagem_desc">Data da Viagem</option>
                </select>
              </div>
            </div>

            {viagensOrdenadas.length === 0 ? (
                  <p>Nenhuma viagem encontrada.</p>
                ) : (
                  <table className="admin-table">
                    <thead>
                      <tr>
                        <th>ID</th>
                        <th>Data da Viagem</th>
                        <th>Distância Percorrida (km)</th>
                        <th>Condutor</th>
                        <th>Origem</th>
                        <th>Destino</th>
                        <th>Status</th>
                        <th>Ações</th>
                      </tr>
                    </thead>
                    <tbody>
                      {viagensOrdenadas.map((viagem) => (

                        <React.Fragment key={viagem.id_viagem}>
                          <tr>
                            <td>{viagem.id_viagem}</td>
                            <td>{new Date(viagem.data_viagem).toLocaleDateString()}</td>
                            <td>{viagem.distancia_percorrida}</td>
                            <td>{viagem.condutorid_condutor}</td>
                            <td>{viagem.pontos_viagem.find(p => p.destino === 0)?.pontoid_ponto.descricao}</td>
                            <td>{viagem.pontos_viagem.find(p => p.destino === 1)?.pontoid_ponto.descricao}</td>
                            <td>{viagem.status_viagemid_status_viagem?.descricao}</td>
                            <td>
                              <button onClick={() => {
                                setViagemSelecionada(prev => prev?.id_viagem === viagem.id_viagem ? null : viagem);
                              }}>
                                Passageiros
                              </button>
                            </td>
                          </tr>
                          {viagemSelecionada?.id_viagem === viagem.id_viagem && (
                          <tr>
                            <td colSpan="8">
                              <div style={{ marginBottom: '1rem' }}>
                                <button
                                  onClick={() => {
                                    if (utilizadores.length > 0) {
                                      setUtilizadores([]);
                                    } else {
                                      buscarUtilizadoresDoGrupo();
                                    }
                                  }}
                                  disabled={isLoadingUtilizadores}
                                >
                                  {isLoadingUtilizadores ? 'Carregando utilizadores...' : 'Adicionar Passageiro'}
                                </button>
                                <button onClick={() => autoRemoverPassageiro()}>
                                  Sair
                                </button>
                                {utilizadores.length > 0 && (
                                  <div style={{ marginTop: '10px' }}>
                                    <Select
                                      options={utilizadores}
                                      value={utilizadorSelecionado}
                                      onChange={setUtilizadorSelecionado}
                                      placeholder="Selecione um utilizador"
                                    />
                                    <button onClick={associarUtilizadorAViagem} disabled={!utilizadorSelecionado}>
                                      Associar
                                    </button>
                                  </div>
                                )}
                              </div>

                              <label>Passageiros da Viagem</label>
                              <table className="admin-table">
                                <thead>
                                  <tr>
                                    <th>ID Utilizador</th>
                                    <th>Nome</th>
                                    <th>Sobrenome</th>
                                    <th>Ações</th>
                                  </tr>
                                </thead>
                                <tbody>
                                  {viagem.passageiros.map((p, i) => (
                                    <tr key={i}>
                                      <td>{p.utilizadorid_utilizador?.id_utilizador}</td>
                                      <td>{p.utilizadorid_utilizador?.nome_primeiro}</td>
                                      <td>{p.utilizadorid_utilizador?.nome_ultimo}</td>
                                      <td>
                                        <button
                                          onClick={() => removerPassageiro(p.utilizadorid_utilizador?.id_utilizador)}
                                        >
                                          Remover
                                        </button>
                                        
                                      </td>
                                    </tr>
                                  ))}
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        )}
                        </React.Fragment>
                      ))}
                    </tbody>
                  </table>
                )}
            </div>
          )}

        </div>

      <div className="terms-and-conditions">
        <h2>Termos e Condições</h2>
        <p>Pagamentos:</p>
        <ul>
          <li>Está a comprar o seu bilhete usando um cartão de débito ou crédito...</li>
          <li>Se não fornecer o endereço de faturação corretamente...</li>
          <li>Alguns bancos podem exigir verificação adicional...</li>
        </ul>
      </div>
    </div>
  );
}

export default RideTicketsPage;
