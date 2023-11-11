import "./character.css"

export default function Character() {
    var storedId;

    // Get ID
    try { 
        storedId = localStorage.getItem('target_id');
        if ((storedId == undefined) || (storedId == null)) {
            storedId = 0
        }
    } catch(e) {
        storedId = 0;
        console.log(e)
    }

    console.log( "Char ID: "+ storedId)
    switch (parseInt(storedId)) {
        case 0:
            return (
                <div className="character">
                    <img id="character" src="/images/tyytyväinen.png" alt=""></img>
                </div>
            )

        case 1:
            return (
                <div className="character">
                    <img id="character" src="/images/epäilevä.png" alt=""></img>
                </div>
            )

        case 2:
            return (
                <div className="character">
                    <img id="character" src="/images/surullinen.png" alt=""></img>
                </div>
            )
        
        case 3:
            return (
                <div className="character">
                    <img id="character" src="/images/onnellinen.png" alt=""></img>
                </div>
            )
    
        default:
            break;
    }

    return (
        <div className="character">
            <img id="character" src="/images/tyytyväinen.png" alt=""></img>
        </div>
    )
}