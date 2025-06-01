import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { checkCondutor } from '../services/auth';

function CondutorTicketsPage() {
  const [activeTab, setActiveTab] = useState('Reservas');
  const [reservas, setReservas] = useState([]);
  const [viagens, setViagens] = useState([]);
  const [viagemSelecionada, setViagemSelecionada] = useState(null);

  const [filtroStatus, setFiltroStatus] = useState('Todas');
  const [ordenacao, setOrdenacao] = useState('ID');
  const [filtroStatusViagem, setFiltroStatusViagem] = useState('Todas');
  const [filtroOrdenacaoViagem, setFiltroOrdenacaoViagem] = useState('id');
  
  const navigate = useNavigate();

  const tabs = ['Reservas', 'Desvios', 'Viagens'];

  useEffect(() => {
    const verifyAccess = async () => {
      const token = localStorage.getItem('accessToken');
      if (!token) {
        navigate('/login');
        return;
      }

      const isCondutor = await checkCondutor();

      if (!isCondutor) {
        navigate('/');
        return;
      }

      //fetchRideTickets();
      fetchReservas(token);
      fetchViagensCondutor(token);
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
        const response = await fetch('http://127.0.0.1:8000/viagem/reserva_condutor/', {
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

    const fetchViagensCondutor = async (token) => {
      try {
        const response = await fetch('http://127.0.0.1:8000/viagem/viagem/list_condutor/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (!response.ok) throw new Error('Erro ao buscar viagens do condutor');
        const data = await response.json();
        setViagens(data);
      } catch (err) {
        console.error('Erro ao buscar viagens do condutor:', err);
        setViagens([]);
      }
    };

    verifyAccess();
  }, [navigate]);

  const handleAcceptReserva = async (idReserva) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/reserva_condutor/${idReserva}/`, {
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
                  id_status_reserva: 2,
                  descricao: 'Aceite',
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

  const handleCancelReserva = async (idReserva) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/reserva_condutor/cancel/${idReserva}/`, {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        alert("Reserva cancelada com sucesso!");
        setReservas(prev => prev.map(r =>
          r.id_reserva === idReserva
            ? {
                ...r,
                status_reservaid_status_reserva: {
                  ...r.status_reservaid_status_reserva,
                  id_status_reserva: 1,
                  descricao: 'Pendente',
                }
              }
            : r
        ));
      } else {
        const data = await response.json();
        alert(data.erro || "Erro ao cancelar reserva.");
      }
    } catch (err) {
      console.error('Erro ao cancelar reserva:', err);
    }
  };

  const iniciarViagem = async (idViagem) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/viagem/start/${idViagem}/`, {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (response.ok) {
        alert('Viagem iniciada com sucesso!');
        // Atualiza o status localmente
        setViagens(prev =>
          prev.map(v => v.id_viagem === idViagem
            ? { ...v, status_viagemid_status_viagem: { ...v.status_viagemid_status_viagem, id_status_viagem: 2, descricao: 'Em Andamento' } }
            : v
          )
        );
      } else {
        const data = await response.json();
        alert(data.error || 'Erro ao iniciar viagem.');
      }
    } catch (err) {
      console.error('Erro ao iniciar viagem:', err);
    }
  };

  const finalizarViagem = async (idViagem) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    const distancia = prompt('Digite a distância percorrida (em km):');
    if (!distancia) return;

    const distanciaInt = parseInt(distancia);
    if (isNaN(distanciaInt)) {
      alert('Por favor, insira um número inteiro válido para a distância.');
      return;
    }

    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/viagem/finish/${idViagem}/`, {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ distancia_percorrida: distanciaInt }),
      });

      if (response.ok) {
        alert('Viagem finalizada com sucesso!');
        setViagens(prev =>
          prev.map(v => v.id_viagem === idViagem
            ? { ...v, status_viagemid_status_viagem: { ...v.status_viagemid_status_viagem, id_status_viagem: 3, descricao: 'Finalizada' }, distancia_percorrida: distanciaInt }
            : v
          )
        );
      } else {
        const data = await response.json();
        alert(data.error || 'Erro ao finalizar viagem.');
      }
    } catch (err) {
      console.error('Erro ao finalizar viagem:', err);
    }
  };

  const aceitarDesvio = async (idViagem) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/desvio_condutor/${idViagem}/`, {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        alert("Desvio aceite com sucesso!");
      }
    } catch (err) {
      console.error('Erro ao aceitar desvio:', err);
    }
  };

  const recusarDesvio = async (idViagem) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;

    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/desvio_condutor/${idViagem}/`, {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        alert("Desvio recusado com sucesso!");
      }
    } catch (err) {
      console.error('Erro ao recusar desvio:', err);
    }
  };

  const reservasFiltradas = reservas
    .filter((reserva) => {
      const status = reserva.status_reservaid_status_reserva?.descricao;
      if (filtroStatus === 'Todas') return true;
      return status === filtroStatus;
    })
    .sort((a, b) => {
      if (ordenacao === 'DataEmissao') {
        return new Date(b.data_emissao) - new Date(a.data_emissao);
      }
      return a.id_reserva - b.id_reserva; // ordenacao por ID (default)
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
      <h1>Painel do Condutor</h1>

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
                <label htmlFor="ordenacao">Ordenar por:</label><br />
                <select id="ordenacao" value={ordenacao} onChange={(e) => setOrdenacao(e.target.value)}>
                  <option value="ID">ID</option>
                  <option value="DataEmissao">Data de Emissão</option>
                </select>
              </div>
            </div>

            {reservasFiltradas.length === 0 ? (
              <p>Nenhuma reserva disponível.</p>
            ) : (
              <div className="ride-tickets-grid">
        {reservasFiltradas.map((reserva) => {
          const origem = reserva.pontos_reserva.find(p => p.destino === 0)?.pontoid_ponto.descricao || '-';
          const destino = reserva.pontos_reserva.find(p => p.destino === 1)?.pontoid_ponto.descricao || '-';
          const status = reserva.status_reservaid_status_reserva?.descricao || '-';
          const statusId = reserva.status_reservaid_status_reserva?.id_status_reserva;

          return (
            <div key={reserva.id_reserva} className="rate-ride-ticket">
              <div className="ticket-status-header">
                <span className={`status-pill ${status.toLowerCase().replace(/\s/g, '-')}`}>{status}</span>
                <span className="ticket-id">Reserva #{reserva.id_reserva}</span>
              </div>
              <div className="ticket-details-grid">
                <div className="detail-item">
                  <div className="label">Data de Emissão</div>
                  <div className="value">{new Date(reserva.data_emissao).toLocaleDateString()}</div>
                </div>
                <div className="detail-item">
                  <div className="label">Data da Viagem</div>
                  <div className="value">{new Date(reserva.data_viagem).toLocaleDateString()}</div>
                </div>
                <div className="detail-item">
                  <div className="label">Valor</div>
                  <div className="value">{reserva.valor}€</div>
                </div>
                <div className="detail-item">
                  <div className="label">Passageiro</div>
                  <div className="value">
                    {typeof reserva.utilizadorid_utilizador === 'object'
                      ? `${reserva.utilizadorid_utilizador.nome_primeiro} ${reserva.utilizadorid_utilizador.nome_ultimo}`
                      : reserva.utilizadorid_utilizador || '-'}
                  </div>
                </div>
                <div className="detail-item">
                  <div className="label">Origem</div>
                  <div className="value">{origem}</div>
                </div>
                <div className="detail-item">
                  <div className="label">Destino</div>
                  <div className="value">{destino}</div>
                </div>
              </div>
              <div className="ticket-actions">
                {statusId === 1 && (
                  <button className="aceitar" onClick={() => handleAcceptReserva(reserva.id_reserva)}>Aceitar</button>
                )}
                {statusId === 2 && (
                  <button className="cancelar" onClick={() => handleCancelReserva(reserva.id_reserva)}>Cancelar</button>
                )}
              </div>
            </div>
          );
        })}
      </div>
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
                  <div className="ride-tickets-grid">
        {viagensOrdenadas.map((viagem) => (
          <div key={viagem.id_viagem} className="rate-ride-ticket">
            <div className="ticket-status-header">
              <span className={`status-pill ${viagem.status_viagemid_status_viagem?.descricao?.toLowerCase().replace(/\s/g, '-')}`}>
                {viagem.status_viagemid_status_viagem?.descricao}
              </span>
              <span className="ticket-id">Viagem #{viagem.id_viagem}</span>
            </div>
            <div className="ticket-details-grid">
              <div className="detail-item">
                <div className="label">Data da Viagem</div>
                <div className="value">{new Date(viagem.data_viagem).toLocaleDateString()}</div>
              </div>
              <div className="detail-item">
                <div className="label">Distância Percorrida (km)</div>
                <div className="value">{viagem.distancia_percorrida}</div>
              </div>
              <div className="detail-item">
                <div className="label">Condutor</div>
                <div className="value">{viagem.condutorid_condutor}</div>
              </div>
              <div className="detail-item">
                <div className="label">Origem</div>
                <div className="value">{viagem.pontos_viagem.find(p => p.destino === 0)?.pontoid_ponto?.descricao || '-'}</div>
              </div>
              <div className="detail-item">
                <div className="label">Destino</div>
                <div className="value">{viagem.pontos_viagem.find(p => p.destino === 1)?.pontoid_ponto?.descricao || '-'}</div>
              </div>
            </div>
            <div className="ticket-actions">
              <button onClick={() => setViagemSelecionada(viagemSelecionada?.id_viagem === viagem.id_viagem ? null : viagem)}>
                Desvios
              </button>
            </div>
            {viagemSelecionada?.id_viagem === viagem.id_viagem && (
              <div style={{ marginTop: '1rem' }}>
                <label>Desvios da Viagem</label>
                {viagem.desvios && viagem.desvios.length > 0 ? (
                  <div>
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
                          <div key={idx} className="rate-ride-ticket" style={{ margin: '1rem 0', background: '#f9f9f9' }}>
                            <div className="ticket-status-header">
                              <span className={`status-pill ${desvio.status_desvio?.toLowerCase().replace(/\s/g, '-')}`}>
                                {desvio.status_desvio}
                              </span>
                              <span className="ticket-id">Desvio #{desvio.id_desvio}</span>
                            </div>
                            <div className="ticket-details-grid">
                              <div className="detail-item">
                                <div className="label">Data de Emissão</div>
                                <div className="value">{new Date(desvio.data_emissao).toLocaleDateString()}</div>
                              </div>
                              <div className="detail-item">
                                <div className="label">Origem</div>
                                <div className="value">{origem?.descricao_ponto || '—'}</div>
                              </div>
                              <div className="detail-item">
                                <div className="label">Destino</div>
                                <div className="value">{destino?.descricao_ponto || '—'}</div>
                              </div>
                              <div className="detail-item">
                                <div className="label">Nova Origem</div>
                                <div className="value">{novaOrigem?.descricao_ponto || '—'}</div>
                              </div>
                              <div className="detail-item">
                                <div className="label">Novo Destino</div>
                                <div className="value">{novoDestino?.descricao_ponto || '—'}</div>
                              </div>
                            </div>
                            <div className="ticket-actions">
                              {desvio.status_desvio === "Pendente" && (
                                <>
                                  <button onClick={() => aceitarDesvio(viagem.id_viagem)}>Aceitar</button>
                                  <button onClick={() => recusarDesvio(viagem.id_viagem)}>Rejeitar</button>
                                </>
                              )}
                            </div>
                          </div>
                        );
                      })}
                  </div>
                ) : (
                  <p>Nenhum desvio registrado para esta viagem.</p>
                )}
              </div>
            )}
          </div>
        ))}
      </div>
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

            {viagens.length === 0 ? (
              <p>Nenhuma viagem encontrada.</p>
            ) : (
              <div className="ride-tickets-grid">
        {viagensOrdenadas.map((viagem) => {
          const origem = viagem.pontos_viagem.find(p => p.destino === 0)?.pontoid_ponto?.descricao || '-';
          const destino = viagem.pontos_viagem.find(p => p.destino === 1)?.pontoid_ponto?.descricao || '-';
          return (
            <div key={viagem.id_viagem} className="rate-ride-ticket">
              <div className="ticket-status-header">
                <span className={`status-pill ${viagem.status_viagemid_status_viagem?.descricao?.toLowerCase().replace(/\s/g, '-')}`}>
                  {viagem.status_viagemid_status_viagem?.descricao}
                </span>
                <span className="ticket-id">Viagem #{viagem.id_viagem}</span>
              </div>
              <div className="ticket-details-grid">
                <div className="detail-item">
                  <div className="label">Data da Viagem</div>
                  <div className="value">{new Date(viagem.data_viagem).toLocaleDateString()}</div>
                </div>
                <div className="detail-item">
                  <div className="label">Distância Percorrida (km)</div>
                  <div className="value">{viagem.distancia_percorrida}</div>
                </div>
                <div className="detail-item">
                  <div className="label">Condutor</div>
                  <div className="value">{viagem.condutorid_condutor}</div>
                </div>
                <div className="detail-item">
                  <div className="label">Origem</div>
                  <div className="value">{origem}</div>
                </div>
                <div className="detail-item">
                  <div className="label">Destino</div>
                  <div className="value">{destino}</div>
                </div>
              </div>
              <div className="ticket-actions" style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <button onClick={() => setViagemSelecionada(viagemSelecionada?.id_viagem === viagem.id_viagem ? null : viagem)}>
                  Passageiros
                </button>
                {viagem.status_viagemid_status_viagem?.id_status_viagem === 1 && (
                  <button onClick={() => iniciarViagem(viagem.id_viagem)}>Iniciar</button>
                )}
                {viagem.status_viagemid_status_viagem?.id_status_viagem === 2 && (
                  <button onClick={() => finalizarViagem(viagem.id_viagem)}>Finalizar</button>
                )}
              </div>
              {viagemSelecionada?.id_viagem === viagem.id_viagem && (
                <div style={{ marginTop: '1rem' }}>
                  <label>Passageiros da Viagem</label>
                  {viagem.passageiros?.length > 0 ? (
                    <div>
                      {viagem.passageiros.map((p, i) => (
                        <div key={i} className="detail-item">
                          <span>{p.utilizadorid_utilizador?.id_utilizador} - {p.utilizadorid_utilizador?.nome_primeiro} {p.utilizadorid_utilizador?.nome_ultimo}</span>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <p>Nenhum passageiro associado.</p>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>
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

export default CondutorTicketsPage;
