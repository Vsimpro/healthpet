import "./sleepbar.css"

export default function Sleepbar(){
    var sleep_data = 0;
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
    xhr.open("GET", `http://localhost:8081/sleep/${storedId}`, true);
    xhr.onload = function (e) {
        if ((xhr.readyState === 4 ) && (xhr.status === 200)) {
            sleep_data = xhr.response
            draw_data( sleep_data )
        }
    };
    xhr.send();

    function draw_data( sleep_data ) {
        var time = JSON.parse(sleep_data).time
        var hour = parseInt(time / 60)
        
        var sleepBar = document.getElementById( "sleepbar" )
        var sleep_text = sleepBar.innerText

        var _span_beg = `<span class=colouredBar>`
        var _span_end = ``
        var escaped = false
        for (let i = 0; i < sleep_text.length; i++) {
            if (i > (hour - 1) ) {
                if (!escaped) {
                    escaped = true
                    _span_beg = _span_beg + "</span>"
                }
            }
            _span_beg = _span_beg + "Z" 
        }

        sleepBar.innerHTML = _span_beg + _span_end
    }

    return (
        <div className="sleepbar">
            <p id="sleepbar">ZZZZZZZZZZ</p>
        </div>
    )
}