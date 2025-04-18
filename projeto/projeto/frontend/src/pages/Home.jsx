import NeighborRideSearch from '../components/rides/NeighborRideSearch.jsx';
import '../css/NavBar.css';
import '../css/Home.css'

function Home() {

    const handleSearchRide = (searchParams) => {
        console.log('Parâmetros de busca de boleia:', searchParams);
        // Aqui você implementaria a lógica para buscar as boleias com base nos parâmetros
    };

    return (
        <div className="home">
            <section className="hero">
                <div className="hero-content">
                    <h1>Onde é que precisa de ir?</h1>
                    <NeighborRideSearch onSearch={handleSearchRide} />
                    <p className="subtitle">Consiga boleias onde quer que a sua viagem o leve.</p>
                </div>
            </section>
        </div>
    );
    // tentar colocar uma grid com algumas boleias
}
export default Home;