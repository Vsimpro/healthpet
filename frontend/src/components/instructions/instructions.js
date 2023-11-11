import "./instructions.css"

export default function Instructions() {
    return (
        <div className="instructions">
            <h2>Instructions:</h2>
            <p>The middle box of this page cointains the visualization of our project. It is a simple Demo of a "Health pet" expansion for Huawei Health -app.</p> 
            <p>The idea behind it was to "guilt trip" young people to take better care of themselves. Who would not be sad to see their "pet" not feel good?</p>
            <p>The state of the Cat depends on your personal health data like sleeping, steps and stress level. Depending on the data, the Cat can appear sad, glad, stressed or absolutely joyful.</p>
            <p>On the right side there is buttons with which you can change the dataset and see how the cat and status bars change.</p>
            <p>PS. the container is the size it would be on a phone. SO feel free to zoom a bit to see better. :D</p>
        </div>
    )
}