const layerCount = 5
const starCount = 400
const maxTime = 30

let starfield = document.querySelector(".starfield")
let width = starfield.clientWidth
let heigth = starfield.clientHeight

for (let i = 0; i < starCount; i++) {
    let yPos = Math.round(Math.random() * heigth)
    let star = document.createElement("div")
    let speed = 1000 * (Math.random() * maxTime + 1)
    star.classList.add("star", "star" + (3 - Math.floor(speed / 1000 / 8)))

    starfield.appendChild(star)

    let keyframes = [
        {
            transform: `translate(${width}px, ${yPos}px)`
        },
        {
            transform: `translate(-${Math.random() * 256}px, ${yPos}px)`
        }
    ]
    let settingsAnimation = {
        delay: Math.random() * -speed,
        duration: speed,
        iterations: 1000
    }

    star.animate(keyframes, settingsAnimation)
}
