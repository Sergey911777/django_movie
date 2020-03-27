// Add star rating
const rating = document.querySelector('form[name=rating]');

rating.addEventListener("change", function (e) {
    // Получаем данные из формы
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
        .then(response => alert("Рейтинг установлен"))
        .catch(error => alert("Ошибка"))
});

function initBootstrapForms() {
    $("form.bootstrap-form").find("input,textarea").addClass("form-control");
    $("form.bootstrap-form").find("input[type='submit']").removeClass("form-control");
}

$(document).ready(function(){
    initBootstrapForms();
});

