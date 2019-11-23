var listElement = document.querySelector('#app ul')
var inputElement = document.querySelector('#app input')
var buttonElement = document.querySelector('#app button')

var todos = JSON.parse(localStorage.getItem('list_todos'))
if (todos === '') {
  todos = []
}

function renderTodos() {
  //removendo conteudo do listelement
  listElement.innerHTML = ''

  for (item of todos) {
    var todoElement = document.createElement('p')
    var todotext = document.createTextNode(item)

    var linkElement = document.createElement('img')
    linkElement.setAttribute('src', './delete.png')

    var pos = todos.indexOf(item)
    linkElement.setAttribute('onclick', 'deleteTodo(' + pos + ')')

    todoElement.appendChild(todotext)
    todoElement.appendChild(linkElement)
    listElement.appendChild(todoElement)
  }
}
renderTodos()

function addTodo() {
  var add = inputElement.value
  if (add === '') return;
  todos.push(add)
  inputElement.value = ''
  renderTodos()
  saveToStorange()
}
buttonElement.onclick = addTodo;

function deleteTodo(pos) {
  todos.splice(pos, 1)
  renderTodos()
  saveToStorange()
}

function saveToStorange() {
  localStorage.setItem('list_todos', JSON.stringify(todos))
}