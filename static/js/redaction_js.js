var editBtn = document.getElementById('editBtn');
var editables = document.querySelectorAll('#title, #content');

console.log(window.location.href) 

if (typeof(Storage) !== "undefined") {
  if (localStorage.getItem('title') !== null) {
    editables[0].innerHTML = localStorage.getItem('title');
    console.log(localStorage.getItem('title'))
  }
  if (localStorage.getItem('content') !== null) {
    editables[1].innerHTML = localStorage.getItem('content');
    console.log(localStorage.getItem('content'))
  }
}

editBtn.addEventListener('click', function(e) {
  if (!editables[0].isContentEditable) {
    editables[0].contentEditable = 'true';;
    editables[1].contentEditable = 'true';
    editBtn.innerHTML = 'Save Changes';
    editBtn.style.backgroundColor = 'green';
  } else {
    editBtn.innerHTML = 'Enable Editing';
    editBtn.style.backgroundColor = 'red';
    // Сохраните данные 
    for (var i = 0; i < editables.length; i++) {
      localStorage.setItem(editables[i].getAttribute('id'), editables[i].innerHTML);
      console.log(i)
      console.log($('input[name="csrfmiddlewaretoken"]').attr('value'))
    function save(){
        console.log(window.location.href)
        $.ajax({
        url: window.location.href,         /* Куда пойдет запрос */
        method: 'post',             /* Метод передачи (post или get) */
        dataType: 'html',          /* Тип данных в ответе (xml, json, script, html). */
        data: {csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value'), title: localStorage.getItem('title'), text: localStorage.getItem('content')},     /* Параметры передаваемые в запросе. */
        success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
          alert(data);            /* В переменной data содержится ответ от index.php. */

  }

});
    }
    }
    save()
  }
});

setInterval(function() {
  for (var i = 0; i < editables.length; i++) {
    localStorage.setItem(editables[i].getAttribute('id'), editables[i].innerHTML);
  }
}, 5000);

