import "./demos.css"
import React from 'react';

class Demos extends React.Component {
    toggleId = (event) => {
        let _id = event.target.id;
        localStorage.setItem("target_id", _id);
        window.location.reload();
    }

    render() {
        return (
            <div className="demos">
                <p>Change demodata:</p>
                <button id="0" onClick={ this.toggleId }>Dataset1</button>
                <button id="1" onClick={ this.toggleId }>Dataset2</button>
                <button id="2" onClick={ this.toggleId }>Dataset3</button>
                <button id="3" onClick={ this.toggleId }>Dataset4</button>
            </div>
        )
    }
}
export default Demos;