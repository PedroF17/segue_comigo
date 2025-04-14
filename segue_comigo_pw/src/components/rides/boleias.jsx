
function Rides({ride}) {

    function onFavoriteClick() {
        alert("Favorite clicked!")
    }

    return  <div className = "ride">
                <div className = "ride_img">
                    <img src = {ride.url} alt = {ride.title}/>
                    <div className = "ride_overlay">
                        <button className = "favorite_btn" onClick={onFavoriteClick}> ♥ </button>
                    </div>
                </div>
                <div className = "ride_info">
                    <h3>{ride.title}</h3>
                    <p><b>{ride.origin}</b><t><b>{ride.destiny}</b></t></p>
                    <p>{ride.departure}<t>{ride.arrive}</t></p>
                    <p>{ride.description}</p>
                </div>
            </div>
}
export default Rides