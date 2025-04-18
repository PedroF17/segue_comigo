//Não foi implementado

import {useState} from 'react'

function SearchBar({ onSearch }) {
    const [searchTerm, setSearchTerm] = useState('');

    const handleChange = (event) => {
        setSearchTerm(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (onSearch) {
            onSearch(searchTerm);
        }
    };

    return (
        <form className="search-bar" onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Pesquisar em todo o site..."
                value={searchTerm}
                onChange={handleChange}
            />
            <button type="submit">Pesquisar</button>
        </form>
    );
}

export default SearchBar;