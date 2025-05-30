// components/rides/PassengerManagementSection.jsx
import React from 'react';
import Select from 'react-select';
import '../../css/PassengerManagementSection.css';

function PassengerManagementSection({
  viagem,
  utilizadores,
  utilizadorSelecionado,
  setUtilizadorSelecionado,
  isLoadingUtilizadores,
  buscarUtilizadoresDoGrupo,
  associarUtilizadorAViagem,
  removerPassageiro,
  autoRemoverPassageiro,
  onClose
}) {
  return (
    <div className="passenger-management-section">
      <h4>Gerenciar Passageiros da Viagem {viagem.id_viagem}</h4>
      <div className="add-passenger-controls">
        <button
          onClick={() => {
            if (utilizadores.length > 0) {
              setUtilizadores([]); // Clear users if already loaded to allow re-fetch
            } else {
              buscarUtilizadoresDoGrupo();
            }
          }}
          disabled={isLoadingUtilizadores}
        >
          {isLoadingUtilizadores ? 'Carregando utilizadores...' : 'Adicionar Passageiro'}
        </button>
        {/* Adicionei um botão para a funcionalidade de "Sair da Viagem" */}
        <button onClick={autoRemoverPassageiro}>
          Sair da Viagem
        </button>
        {utilizadores.length > 0 && (
          <div className="add-passenger-select">
            <Select
              options={utilizadores}
              value={utilizadorSelecionado}
              onChange={setUtilizadorSelecionado}
              placeholder="Selecione um utilizador"
              isLoading={isLoadingUtilizadores}
            />
            <button onClick={associarUtilizadorAViagem} disabled={!utilizadorSelecionado}>
              Associar
            </button>
          </div>
        )}
      </div>

      <h5>Passageiros Atuais</h5>
      {viagem.passageiros && viagem.passageiros.length > 0 ? (
        <table className="admin-table passenger-table">
          <thead>
            <tr>
              <th>ID Utilizador</th>
              <th>Nome</th>
              <th>Sobrenome</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {viagem.passageiros.map((p) => (
              <tr key={p.utilizadorid_utilizador?.id_utilizador}>
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
      ) : (
        <p>Nenhum passageiro associado a esta viagem ainda.</p>
      )}
    </div>
  );
}

export default PassengerManagementSection;