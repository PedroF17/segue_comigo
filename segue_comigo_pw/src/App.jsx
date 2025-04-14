import './css/App.css'
import Rides from './components/rides/boleias';

function App() {
  return (
    <>
        <Rides ride={{title: "Mario",origin: "Barcelos", destiny: "Braga", departure: '12:00', arrive: "13:00",description:"Por Martim"}}/>
    </>
  );
}

export default App;
