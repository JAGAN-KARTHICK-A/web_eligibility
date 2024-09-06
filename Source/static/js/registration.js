function register(){
    var name = document.getElementById("nameInput").value;
    var email = document.getElementById("emailInput").value;
    var password = document.getElementById("passwordInput").value;
    var number = document.getElementById("phoneInput").value;
    var address = document.getElementById("addressInput").value;
    if (name.length > 0 && email.length > 0 && password.length > 0 && number.length > 0 && address.length > 0){
        if (password.length > 8){
            $.post("/register",
                {
                  name: name,
                  email: email,
                  password: password,
                  number: number,
                  address: address
                },
                function(data, status){
                    if (data.status === "success"){
                        window.location = "/login";
                    }
                    else{
                        alert("Unable to register you (Maybe there might be another account with the same email)")
                    }
                });
        }
        else{
            alert("password must have minimum 8 charecters.")
        }
    }
    else{
        alert("Please fill all details to proceed.");
    }
}