import "./stepsbar.css"

export default function Stepsbar() {
        var steps_data;
        var storedId;
        var xhr = new XMLHttpRequest();

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
    
        console.log( "ID: "+ storedId)

        // Fetch data
        xhr.open("GET", `http://localhost:8081/steps/${storedId}`, true);
        xhr.onload = function (e) {
            if ((xhr.readyState === 4 ) && (xhr.status === 200)) {
                steps_data = xhr.responseText;
                draw_data( JSON.parse(steps_data) )
            }
        };
        xhr.send();

        function draw_data( steps_data ) {
            var steps = steps_data['steps']

            var bar = document.getElementsByClassName("stepsbar_bottom")[0]

            var percentile = parseInt(parseInt(steps) / 15000 * 100) 
            var width = parseInt((280 / 100) * percentile)

            bar.style.width = width
        }
    return (
        <>
            <div className="stepsbar_top"></div>
            <div className="stepsbar_bottom"></div>
        </>
    )
}