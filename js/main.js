const iconoMenu = document.querySelector("#nav__responsive")
const menu = document.querySelector(".nav__content")


iconoMenu.addEventListener("click", () =>{
    menu.classList.toggle("disabled")
})

window.addEventListener("resize", () =>{

    menu.classList.add("disabled")

    const width = window.innerWidth

    if (width > 914 && menu.classList.contains("disabled"))
    {
        menu.classList.remove("disabled")
    }

})

