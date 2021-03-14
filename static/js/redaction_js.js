var editBtn = document.getElementById('editBtn');
var editables = document.querySelectorAll('#title, #content');

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
    editBtn.style.backgroundColor = '#6F9';
  } else {
    // Отключить Редактирование
    editables[0].contentEditable = 'false';
    editables[1].contentEditable = 'false';;
    // Изменить текст и цвет кнопки
    editBtn.innerHTML = 'Enable Editing';
    editBtn.style.backgroundColor = '#F96';
    // Сохраните данные в localStorage 
    for (var i = 0; i < editables.length; i++) {
      localStorage.setItem(editables[i].getAttribute('id'), editables[i].innerHTML);
    }
  }
});

setInterval(function() {
  for (var i = 0; i < editables.length; i++) {
    localStorage.setItem(editables[i].getAttribute('id'), editables[i].innerHTML);
  }
}, 5000);

