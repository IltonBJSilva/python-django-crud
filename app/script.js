    function checkForm() {
        // Fetching values from all input fields and storing them in variables.
        var nome = document.getElementById("nome").value;

        //Check input Fields Should not be blanks.
        if (nome == '') {
            alert("Por favor preencha todos os campos.");
            return false;
        } else {
            //Notifying error fields
            var name = document.getElementById("nome");
            //Check All Values/Informations Filled by User are Valid Or Not.If All Fields Are invalid Then Generate alert.
            if (name.innerHTML == 'Nome') {
                alert("Por favor, preencha o formul&aacute;rio com informa&ccedil;&otilde;es v&aacute;lidas");
                return false;
            } else {
                //Submit Form When All values are valid.
                document.getElementById("myForm").submit();
                return true;
            }

        }
    }