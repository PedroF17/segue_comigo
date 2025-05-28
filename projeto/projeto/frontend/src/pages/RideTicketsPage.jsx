// RideTicketsPage.jsx
import React, { useState, useEffect } from 'react';
import '../css/RideTicketsPage.css';
import RateRideTicket from '../components/rides/RateRideTicket.jsx';
//import PassengerManagementSection from '../components/rides/PassengerManagementSection.jsx';
//import DeviationManagementSection from '../components/rides/DeviationManagementSection.jsx';
import { useNavigate } from 'react-router-dom';
import { checkPassageiro } from '../services/auth';
import Select from 'react-select';

function RideTicketsPage() {
  const [activeTab, setActiveTab] = useState('Reservas');
  const [reservas, setReservas] = useState([]);
  const [viagens, setViagens] = useState([]);
  const [viagemSelecionada, setViagemSelecionada] = useState(null);
  const navigate = useNavigate();

  const [filtroStatusReserva, setFiltroStatusReserva] = useState('Todas');
  const [filtroOrdenacaoReserva, setFiltroOrdenacaoReserva] = useState('id');

  const [filtroStatusViagemDesvio, setFiltroStatusViagemDesvio] = useState('Todas');
  const [filtroOrdenacaoViagemDesvio, setFiltroOrdenacaoViagemDesvio] = useState('id');

  const [filtroStatusViagemAvaliar, setFiltroStatusViagemAvaliar] = useState('Finalizada');
  const [filtroOrdenacaoViagemAvaliar, setFiltroOrdenacaoViagemAvaliar] = useState('data_viagem_desc');

  const [utilizadores, setUtilizadores] = useState([]);
  const [utilizadorSelecionado, setUtilizadorSelecionado] = useState(null);
  const [isLoadingUtilizadores, setIsLoadingUtilizadores] = useState(false);
  const tabs = ['Reservas', 'Desvios', 'Viagens'];

  const [pontos, setPontos] = useState([]);
  const [pontoInicial, setPontoInicial] = useState(null);
  const [pontoFinal, setPontoFinal] = useState(null);
  const [loadingPontos, setLoadingPontos] = useState(false);


  const fetchAllData = async (token) => {
    fetchReservas(token);
    fetchViagens(token);
    buscarPontos(setPontos, setLoadingPontos);
  };

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

      fetchAllData(token);
    };
    verifyAccess();
  }, [navigate]);

  const fetchReservas = async (token) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/reserva/', {
        headers: { Authorization: `Bearer ${token}` },
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
        headers: { Authorization: `Bearer ${token}` },
      });
      if (!response.ok) throw new Error('Erro ao buscar viagens');
      const data = await response.json();
      setViagens(data);
    } catch (err) {
      console.error('Erro ao buscar viagens:', err);
      setViagens([]);
    }
  };

  const handleDeleteReserva = async (idReserva) => {
    const token = localStorage.getItem('accessToken');
    if (!token || !window.confirm("Tem certeza que deseja remover esta reserva?")) return;
    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/reserva/${idReserva}/`, {
        method: 'DELETE', headers: { Authorization: `Bearer ${token}` },
      });
      if (response.status === 204) {
        alert("Reserva removida com sucesso!");
        fetchReservas(token);
      } else {
        const data = await response.json();
        alert(data.erro || "Erro ao remover reserva.");
      }
    } catch (err) { console.error('Erro ao remover reserva:', err); }
  };

  const handleAcceptReserva = async (idReserva) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;
    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/reserva/confirm2/${idReserva}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
      });
      if (response.ok) {
        alert("Reserva aceite com sucesso!");
        fetchReservas(token);
      } else {
        const data = await response.json();
        alert(data.erro || "Erro ao aceitar reserva.");
      }
    } catch (err) { console.error('Erro ao aceitar reserva:', err); }
  };

  const buscarUtilizadoresDoGrupo = async () => {
    const token = localStorage.getItem('accessToken');
    setIsLoadingUtilizadores(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/utilizador/grupo/view/', {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await response.json();
      const options = data.map((u) => ({
        value: u.id_utilizador, label: `${u.nome_primeiro} ${u.nome_ultimo}`,
      }));
      setUtilizadores(options);
    } catch (err) { console.error('Erro ao buscar utilizadores:', err); }
    finally { setIsLoadingUtilizadores(false); }
  };

  const associarUtilizadorAViagem = async () => {
    const token = localStorage.getItem('accessToken');
    if (!utilizadorSelecionado || !viagemSelecionada) return;
    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/viagem/associate/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ id_viagem: viagemSelecionada.id_viagem, id_utilizador: utilizadorSelecionado.value }),
      });
      const data = await response.json();
      if (response.ok) {
        alert('Passageiro associado com sucesso.');
        setUtilizadorSelecionado(null);
        fetchViagens(token);
      } else {
        alert(data.error || 'Erro ao associar passageiro.');
      }
    } catch (err) { console.error('Erro ao associar passageiro:', err); }
  };

  const removerPassageiro = async (idUtilizador) => {
    const token = localStorage.getItem('accessToken');
    if (!viagemSelecionada) return;
    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/viagem/associate/', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ id_viagem: viagemSelecionada.id_viagem, id_utilizador: idUtilizador }),
      });
      const data = await response.json();
      if (response.ok) {
        alert('Passageiro removido com sucesso.');
        fetchViagens(token);
      } else {
        alert(data.error || 'Erro ao remover passageiro.');
      }
    } catch (err) { console.error('Erro ao remover passageiro:', err); }
  };

  const autoRemoverPassageiro = async () => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      alert("Não autenticado.");
      return;
    }
    if (!viagemSelecionada) {
      alert("Nenhuma viagem selecionada.");
      return;
    }
    if (!window.confirm("Tem certeza que deseja sair desta viagem?")) {
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/viagem/desassociate/', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ id_viagem: viagemSelecionada.id_viagem }),
      });
      const data = await response.json();
      if (response.ok) {
        alert('Você foi removido da viagem com sucesso.');
        fetchViagens(token); // Refresh the list of travels
        setViagemSelecionada(null); // Close the management section
      } else {
        alert(data.error || 'Erro ao tentar sair da viagem.');
      }
    } catch (err) {
      console.error('Erro ao remover passageiro:', err);
      alert('Ocorreu um erro ao tentar sair da viagem.');
    }
  };


  const solicitarDesvio = async (viagemId, pontoInicialId, pontoFinalId, limparSelecao) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;
    try {
      const response = await fetch('http://127.0.0.1:8000/viagem/desvio/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ id_viagem: viagemId, ponto_inicial_id: pontoInicialId, ponto_final_id: pontoFinalId }),
      });
      const data = await response.json();
      if (response.ok) {
        alert('Desvio solicitado com sucesso.');
        limparSelecao();
        fetchViagens(token);
      } else {
        alert(data.error || 'Erro ao solicitar desvio.');
      }
    } catch (err) { console.error('Erro ao solicitar desvio:', err); }
  };

  const cancelarDesvio = async (idDesvio) => {
    const token = localStorage.getItem('accessToken');
    if (!token) return;
    try {
      const response = await fetch(`http://127.0.0.1:8000/viagem/desvio/${idDesvio}/`, {
        method: 'DELETE',
        headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
      });
      if (response.ok) {
        alert("Desvio cancelado com sucesso!");
        fetchViagens(token);
      } else {
        const data = await response.json();
        alert(data.erro || "Erro ao cancelar desvio.");
      }
    } catch (err) { console.error('Erro ao cancelar desvio:', err); }
  };

  const buscarPontos = async (setPontos, setLoading) => {
    try {
      const res = await fetch('http://127.0.0.1:8000/viagem/ponto/');
      if (!res.ok) throw new Error('Erro ao buscar pontos');
      const data = await res.json();
      const formatted = data.map((p) => ({ value: p.id_ponto, label: p.descricao }));
      setPontos(formatted);
    } catch (error) { console.error(error); }
    finally { setLoading(false); }
  };

  const reservasOrdenadas = [...reservas]
    .filter(reserva => filtroStatusReserva === 'Todas' || reserva.status_reservaid_status_reserva?.descricao === filtroStatusReserva)
    .sort((a, b) => {
      if (filtroOrdenacaoReserva === 'data_emissao_desc') {
        return new Date(b.data_emissao) - new Date(a.data_emissao);
      }
      return a.id_reserva - b.id_reserva;
    });

  const viagensParaDesviosOrdenadas = [...viagens]
    .filter(viagem => filtroStatusViagemDesvio === 'Todas' || viagem.status_viagemid_status_viagem?.descricao === filtroStatusViagemDesvio)
    .sort((a, b) => {
      if (filtroOrdenacaoViagemDesvio === 'data_viagem_desc') {
        return new Date(b.data_viagem) - new Date(a.data_viagem);
      }
      return a.id_viagem - b.id_viagem;
    });

  const viagensConcluidasParaAvaliar = [...viagens]
  .filter(viagem =>
    viagem &&
    viagem.status_viagemid_status_viagem &&
    viagem.status_viagemid_status_viagem.descricao === filtroStatusViagemAvaliar
  )
  .sort((a, b) => {
    if (filtroOrdenacaoViagemAvaliar === 'data_viagem_desc') {
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
            onClick={() => {
              setActiveTab(tab);
              setViagemSelecionada(null); // Reset selected trip when changing tabs
            }}
          >
            {tab}
          </button>
        ))}
      </div>

      <div className="tab-content">
        {activeTab === 'Reservas' && (
          <>
            <h2>Minhas Reservas</h2>

            <div className="filters-container">
              <div>
                <label htmlFor="filtroStatusReserva">Filtrar por status:</label>
                <select id="filtroStatusReserva" value={filtroStatusReserva} onChange={(e) => setFiltroStatusReserva(e.target.value)}>
                  <option value="Todas">Todas</option>
                  <option value="Pendente">Pendente</option>
                  <option value="Aceite">Aceite</option>
                  <option value="Finalizada">Finalizada</option>
                  {/* Adicione outros status de reserva se necessário */}
                </select>
              </div>
              <div>
                <label htmlFor="filtroOrdenacaoReserva">Ordenar por:</label>
                <select id="filtroOrdenacaoReserva" value={filtroOrdenacaoReserva} onChange={(e) => setFiltroOrdenacaoReserva(e.target.value)}>
                  <option value="ID">ID</option>
                  <option value="data_emissao_desc">Data de Emissão (Mais Recente)</option>
                  {/* Adicione outras opções de ordenação se necessário */}
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
                        <td>{new Date(reserva.data_emissao).toLocaleDateString()}</td>
                        <td>{new Date(reserva.data_viagem).toLocaleDateString()}</td>
                        <td>{reserva.valor}€</td>
                        {/* Renderiza o ID do condutor ou "N/A" se for null/undefined.
                            Se 'condutorid_condutor' for um objeto completo,
                            adicione '?.nome_primeiro' ou '?.nome_completo'
                        */}
                        <td>{reserva.condutorid_condutor || '-'}</td>
                        <td>{origem}</td>
                        <td>{destino}</td>
                        <td>{status}</td>
                        <td>
                          <div style={{ display: 'flex', gap: '8px' }}>
                            {/* Ajuste as condições para os botões com base nos status ID do seu backend */}
                            {(statusId === 1 || statusId === 2) && ( // Exemplo: 1=Pendente, 2=Aceite
                              <button onClick={() => handleDeleteReserva(reserva.id_reserva)}>Remover</button>
                            )}
                            {statusId === 2 && ( // Exemplo: 2=Aceite
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
            <h2>Minhas Viagens com Desvios</h2>

            <div className="filters-container">
              <div>
                <label htmlFor="filtroStatusViagemDesvio">Filtrar por status:</label>
                <select
                  id="filtroStatusViagemDesvio"
                  value={filtroStatusViagemDesvio}
                  onChange={(e) => setFiltroStatusViagemDesvio(e.target.value)}
                >
                  <option value="Todas">Todas</option>
                  <option value="Pendente">Pendente</option>
                  <option value="Em Andamento">Em Andamento</option>
                  <option value="Finalizada">Finalizada</option>
                  {/* Adicione outros status de viagem se necessário */}
                </select>
              </div>
              <div>
                <label htmlFor="filtroOrdenacaoViagemDesvio">Ordenar por:</label>
                <select
                  id="filtroOrdenacaoViagemDesvio"
                  value={filtroOrdenacaoViagemDesvio}
                  onChange={(e) => setFiltroOrdenacaoViagemDesvio(e.target.value)}
                >
                  <option value="id">ID</option>
                  <option value="data_viagem_desc">Data da Viagem (Mais Recente)</option>
                  {/* Adicione outras opções de ordenação se necessário */}
                </select>
              </div>
            </div>

            {viagensParaDesviosOrdenadas.length === 0 ? (
              <p>Nenhuma viagem encontrada para gerenciar desvios.</p>
            ) : (
              <table className="admin-table">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Data da Viagem</th>
                    <th>Condutor</th>
                    <th>Origem</th>
                    <th>Destino</th>
                    <th>Status</th>
                    <th>Ações</th>
                  </tr>
                </thead>
                <tbody>
                  {viagensParaDesviosOrdenadas.map((viagem) => (
                    <React.Fragment key={viagem.id_viagem}>
                      <tr onClick={() => {
                        setViagemSelecionada(prev => prev?.id_viagem === viagem.id_viagem ? null : viagem);
                      }} className={viagemSelecionada?.id_viagem === viagem.id_viagem ? 'selected-row' : ''}>
                        <td>{viagem.id_viagem}</td>
                        <td>{new Date(viagem.data_viagem).toLocaleDateString()}</td>
                        {/* Ajuste para exibir o nome do condutor se 'condutorid_condutor' for um objeto */}
                        <td>{viagem.condutorid_condutor?.nome_primeiro ? `${viagem.condutorid_condutor.nome_primeiro} ${viagem.condutorid_condutor.nome_ultimo}` : 'N/A'}</td>
                        <td>{viagem.pontos_viagem?.find(p => p.destino === 0)?.pontoid_ponto.descricao || '-'}</td>
                        <td>{viagem.pontos_viagem?.find(p => p.destino === 1)?.pontoid_ponto.descricao || '-'}</td>
                        <td>{viagem.status_viagemid_status_viagem?.descricao || '-'}</td>
                        <td>
                          <button onClick={(e) => {
                            e.stopPropagation(); // Prevents row click from firing
                            setViagemSelecionada(prev => prev?.id_viagem === viagem.id_viagem ? null : viagem);
                          }}>
                            Gerenciar
                          </button>
                        </td>
                      </tr>
                      {viagemSelecionada?.id_viagem === viagem.id_viagem && (
                        <tr>
                          <td colSpan="7">
                            <DeviationManagementSection
                              viagem={viagem}
                              pontos={pontos}
                              pontoInicial={pontoInicial}
                              setPontoInicial={setPontoInicial}
                              pontoFinal={pontoFinal}
                              setPontoFinal={setPontoFinal}
                              loadingPontos={loadingPontos}
                              solicitarDesvio={solicitarDesvio}
                              cancelarDesvio={cancelarDesvio}
                              onClose={() => setViagemSelecionada(null)}
                            />
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
            <h2>Avalie As Suas Viagens Concluídas</h2>

            <div className="filters-container">
              <div>
                <label htmlFor="filtroStatusViagemAvaliar">Filtrar por status:</label>
                <select
                  id="filtroStatusViagemAvaliar"
                  value={filtroStatusViagemAvaliar}
                  onChange={(e) => setFiltroStatusViagemAvaliar(e.target.value)}
                  disabled // Mantido desabilitado pois a aba é apenas para viagens "Finalizadas"
                >
                  <option value="Finalizada">Finalizada</option>
                  {/* Pode adicionar outras opções para testes, mas para a UI final, 'Finalizada' é a única relevante aqui */}
                </select>
              </div>
              <div>
                <label htmlFor="filtroOrdenacaoViagemAvaliar">Ordenar por:</label>
                <select
                  id="filtroOrdenacaoViagemAvaliar"
                  value={filtroOrdenacaoViagemAvaliar}
                  onChange={(e) => setFiltroOrdenacaoViagemAvaliar(e.target.value)}
                >
                  <option value="data_viagem_desc">Data da Viagem (Mais Recente)</option>
                  <option value="id">ID</option>
                </select>
              </div>
            </div>

            {viagensConcluidasParaAvaliar.length === 0 ? (
              <p>Nenhuma viagem concluída para avaliar.</p>
            ) : (
              <div className="ride-tickets-grid">
                {viagensConcluidasParaAvaliar.map((viagem) => (
                  <div key={viagem.id_viagem} className="ride-ticket-item-wrapper">
                    <RateRideTicket
                      viagem={viagem}
                      onFeedbackSubmitted={() => fetchViagens(localStorage.getItem('accessToken'))}
                      onAnomalySubmitted={() => fetchViagens(localStorage.getItem('accessToken'))}
                    />
                    <button
                      className="manage-passengers-button"
                      onClick={() => setViagemSelecionada(prev => prev?.id_viagem === viagem.id_viagem ? null : viagem)}
                    >
                      {viagemSelecionada?.id_viagem === viagem.id_viagem ? 'Fechar Passageiros' : 'Gerenciar Passageiros'}
                    </button>

                    {viagemSelecionada?.id_viagem === viagem.id_viagem && (
                      <PassengerManagementSection
                        viagem={viagem}
                        utilizadores={utilizadores}
                        utilizadorSelecionado={utilizadorSelecionado}
                        setUtilizadorSelecionado={setUtilizadorSelecionado}
                        isLoadingUtilizadores={isLoadingUtilizadores}
                        buscarUtilizadoresDoGrupo={() => buscarUtilizadoresDoGrupo()}
                        associarUtilizadorAViagem={() => associarUtilizadorAViagem()}
                        removerPassageiro={removerPassageiro}
                        autoRemoverPassageiro={autoRemoverPassageiro}
                        onClose={() => setViagemSelecionada(null)}
                      />
                    )}
                  </div>
                ))}
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
        </ul>
      </div>
    </div>
  );
}

export default RideTicketsPage;