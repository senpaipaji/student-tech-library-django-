let listitems = document.querySelectorAll('.listitem')
       
listitems.forEach((element,index) => {
    element.addEventListener('click',()=>{
        document.querySelector('.listitem.active').classList.remove('active')
        element.classList.add('active')
    })
});
        