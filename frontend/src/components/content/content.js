import "./content.css"
import Container from "../container/container"
import Demos from "../demos/demos"
import Instructions from "../instructions/instructions"

export default function Content() {
    return (
        <div className="content">
            <Instructions />
            <Container />
            <Demos />
        </div>
    )
}