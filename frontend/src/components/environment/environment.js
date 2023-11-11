import Character from "../character/character"
import Sleepbar from "../sleepbar/sleepbar"
import Stepsbar from "../stepsbar/stepsbar"
import "./environment.css"

export default function Environment() {
    return (
        <div className="environment">
            <Character />
            <Sleepbar />
            <Stepsbar />
        </div>
    )
}