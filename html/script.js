function btn_enviar(){

	//Constrói os dados que serão enviados para o servidor
	var escrever_text = document.getElementById('escrever_text');
  var serializedData = {
		mensagem: escrever_text.value,
		op: 'chat_response'
	}

	//Faz o envio das informações para o servidor
	request = $.ajax({
    url: "http://31.220.51.204:5000",
    type: "POST",
    data: serializedData
  });

  //Se o request funcionar, executar esta função
  request.done(function (response, textStatus, jqXHR){
    //Para fins de depuração
    console.log(response);

		//Atualiza o container de mensagens
		var container_mensagens = document.getElementById('msg_conteudo');

		container_mensagens.innerHTML+= "<span class=\"msg_information\">Usuario1 - "+new Date()+"</span></br>";
		container_mensagens.innerHTML+= escrever_text.value+"<br/>";

		container_mensagens.innerHTML+= "<span class=\"msg_information\">Estrela Bot - "+new Date()+"</span></br>";
		container_mensagens.innerHTML+= response+"<br/>";

		escrever_text.value = "";
		escrever_text.focus();
		container_mensagens.scrolltop = container_mensagens.scrollHeight;

  });

  //Se o request falhar, executar esta função
  request.fail(function (jqXHR, textStatus, errorThrown){
		//Se ocorrer um erro, mostrar aviso de erro.


    // Log the error to the console
    console.error(
      "O seguinte erro ocorreu: "+
      textStatus, errorThrown
    );
  });

}

function btn_recarregar(){
	location.reload();
}

document.getElementById('escrever_text').addEventListener('keydown', function onEvent(event) {
		if (event.key === "Enter") {
			btn_enviar();
		}
});

/*
// Get the input field
var input = document.getElementById("myInput");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
 // Number 13 is the "Enter" key on the keyboard
 if (event.keyCode === 13) {
	 // Cancel the default action, if needed
	 event.preventDefault();
	 // Trigger the button element with a click
	 document.getElementById("myBtn").click();
 }
});
*/
