$.ajax({
  type: "POST",
  url: "localhost:5000",
  data: JSON.stringify({mensagem:document.getElementById('escrever_text').value}),
  contentType: "text/json; charset=utf-8",
  dataType: "text",
  success: function (msg) {
    console.log(msg);
  }
});

//
$.ajax({
  url: "http://localhost:5000/?msg=chuamba",
  type: 'GET',
  success: function(res) {
    console.log(res);
    alert(res);
  }
});

function enviarPost() {

  //Pega a mensagem digitada pelo usuário
  var serializedData = {mensagem: document.getElementById('escrever_text').value }
  request = $.ajax({
    url: "http://localhost:5000/",
    type: "POST",
    data: serializedData
  });

  // Callback handler that will be called on success
  request.done(function (response, textStatus, jqXHR){
    // Log a message to the console
    console.log("Hooray, it worked!");
  });

  // Callback handler that will be called on failure
  request.fail(function (jqXHR, textStatus, errorThrown){
    // Log the error to the console
    console.error(
      "The following error occurred: "+
      textStatus, errorThrown
    );
  });

  // Callback handler that will be called regardless
  // if the request failed or succeeded
  request.always(function () {
    // Reenable the inputs
    $inputs.prop("disabled", false);
  });
}


//Teste com post
