// var toastElList = [].slice.call(document.querySelectorAll('.toast'))
// var toastList = toastElList.map(function (toastEl) {
//   return new bootstrap.Toast(toastEl, animation)
// })
// btn-close
log = console.log
var bell_notification = document.getElementById('bell-notification');
var toast = document.querySelector('.toast')
var close_button = document.querySelector('.toast')
log(bell_notification)
bell_notification.addEventListener("click",(event)=>{
    log(toast)

    toast.classList.toggle('show')
})

close_button.addEventListener("click",(event)=>{
    

    toast.classList.toggle('show')
})