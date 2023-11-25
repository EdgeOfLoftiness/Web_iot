const iconoMenu = document.querySelector("#nav__responsive")

iconoMenu.addEventListener("click", (e) =>{

    const menu = document.querySelector(".nav__content")

    menu.classList.toggle("disabled")
})