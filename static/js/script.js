function reconhecerFala() {
  fetch('/reconhecer_fala', {
      method: 'POST'
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('area-texto').value = data.texto;
  })
  .catch(error => console.error('Erro:', error));
}

function falarTexto() {
  const texto = document.getElementById('entrada-texto').value;
  if (texto.trim() === "") {
      alert("Por favor, insira um texto para ser falado.");
      return;
  }

  fetch('/falar_texto', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ texto: texto })
  })
  .then(response => response.json())
  .then(data => console.log(data.status))
  .catch(error => console.error('Erro:', error));
}

function limparTexto() {
  document.getElementById('area-texto').value = "";
  document.getElementById('entrada-texto').value = "";
}
