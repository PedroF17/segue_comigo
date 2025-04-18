import Rides from "../components/rides/Rides.jsx";
import React from "react";

<form onSubmit={handleSearch} className="search_form">
    <label htmlFor="origem">Origem</label>
    <input type="text"
           placeholder = "Origem"
           className="search_input"
           value = {searchQuery}
           onChange={(e) => setSearchQuery(e.target.value)}
    />

    <button type="submit" className="search_button"> Pesquisar </button>
</form>
<div className="ride-grid">
    {rides.map((ride) => (
        ride.title.toLowerCase().startsWith(searchQuery) && (
            <Rides ride={ride} key={ride.id} />)
    ))}