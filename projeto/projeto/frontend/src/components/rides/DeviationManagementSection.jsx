// components/rides/DeviationManagementSection.jsx
import React from 'react';
import Select from 'react-select';
import '../../css/DeviationManagementSection.css';

function DeviationManagementSection({
  viagem,
  pontos,
  pontoInicial,
  setPontoInicial,
  pontoFinal,
  setPontoFinal,
  loadingPontos,
  solicitarDesvio,
  cancelarDesvio,
  onClose
}) {

  const limparSelecaoPontos = () => {
    setPontoInicial(null);
    setPontoFinal(null);
  };

  return (
    <div className="deviation-management-section">
      <h4>Gerenciar Desvios da Viagem {viagem.id_viagem}</h4>

      <div className="new-deviation-controls">
        <h5>Solicitar Novo Desvio</h5>
        <div className="deviation-select-group">
          <div className="select-item">
            <label>Ponto de Origem do Desvio:</label>
            <Select
              options={pontos}
              value={pontoInicial}
              onChange={setPontoInicial}
              placeholder="Selecione o ponto de origem"
              isLoading={loadingPontos}
            />
          </div>
          <div className="select-item">
            <label>Ponto de Destino do Desvio:</label>
            <Select
              options={pontos}
              value={pontoFinal}
              onChange={setPontoFinal}
              placeholder="Selecione o ponto de destino"
              isLoading={loadingPontos}
            />
          </div>
          <button
            onClick={e => {
              e.stopPropagation();
              solicitarDesvio(
                viagem.id_viagem,
                pontoInicial?.value,
                pontoFinal?.value,
                limparSelecaoPontos
            );
          }}
            disabled={!pontoInicial || !pontoFinal}
          >
            Solicitar Desvio
          </button>
        </div>
      </div>

      <hr className="divider" />

      <h5>Desvios Existentes</h5>
      {viagem.desvios && viagem.desvios.length > 0 ? (
        <table className="admin-table deviation-table">
          <thead>
            <tr>
              <th>ID Desvio</th>
              <th>Data Emissão</th>
              <th>Origem (Viagem)</th>
              <th>Destino (Viagem)</th>
              <th>Nova Origem (Desvio)</th>
              <th>Novo Destino (Desvio)</th>
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
                const origemViagem = desvio.pontos_desvio?.find(p => p.original === true && p.destino === 0)?.descricao_ponto || '—';
                const destinoViagem = desvio.pontos_desvio?.find(p => p.original === true && p.destino === 1)?.descricao_ponto || '—';
                const novaOrigemDesvio = desvio.pontos_desvio?.find(p => p.original === false && p.destino === 0)?.descricao_ponto || '—';
                const novoDestinoDesvio = desvio.pontos_desvio?.find(p => p.original === false && p.destino === 1)?.descricao_ponto || '—';

                return (
                  <tr key={desvio.id_desvio || idx}>
                    <td>{desvio.id_desvio}</td>
                    <td>{new Date(desvio.data_emissao).toLocaleDateString()}</td>
                    <td>{origemViagem}</td>
                    <td>{destinoViagem}</td>
                    <td>{novaOrigemDesvio}</td>
                    <td>{novoDestinoDesvio}</td>
                    <td>{desvio.status_desvio}</td>
                    <td>
                      {desvio.status_desvio === "Pendente" && (
                        <button onClick={() => cancelarDesvio(desvio.id_desvio)}>
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
    </div>
  );
}

export default DeviationManagementSection;