CLS_CUBE_TURNED = "cube_turned"

let cube = document.querySelector(".cube_click")

function slideCube() {
    cube.classList.toggle(CLS_CUBE_TURNED)
}

sides_click = document.querySelectorAll(".side_click")
sides_click.forEach(side => {
    side.addEventListener("click", slideCube)
})
