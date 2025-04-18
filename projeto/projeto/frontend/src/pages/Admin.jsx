import '../css/NavBar.css';
import '../css/Admin.css';
import { useState } from 'react';

function Admin() {
  const [activeTab, setActiveTab] = useState('Users');

  const categories = ['Utilizadores', 'Viagens', 'Denuncias'];

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
        <input type="text" placeholder={`Procurar ${activeTab.toLowerCase()}`} className="search-input" />

        <table className="admin-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nome</th>
              <th>Estado</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {/* Example rows (static for now) */}
            <tr>
              <td>1</td>
              <td>Exemplo 1</td>
              <td>Ativo</td>
              <td>
                <button>Editar</button>
                <button>Apagar</button>
              </td>
            </tr>
            <tr>
              <td>2</td>
              <td>Exemplo 2</td>
              <td>Pendente</td>
              <td>
                <button>Editar</button>
                <button>Apagar</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Admin;
