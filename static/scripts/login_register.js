const labels = document.querySelectorAll('.form-control label');

labels.forEach(label =>{
    label.innerHTML = label.innerText.split('').map((Element,idx) => `<span style="transition-delay:${idx * 30}ms">${Element}</span>`).join('');
})