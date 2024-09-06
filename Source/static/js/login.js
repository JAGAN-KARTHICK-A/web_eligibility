function login(){
    var email = document.getElementById("emailInput").value;
    var password = document.getElementById("passwordInput").value;
    if (email.length > 0 && password.length > 8){
        $.post("/login",
            {
              email: email,
              password: password,
            },
            function(data, status){
                if (data.status === "success"){
                    window.location = "/student/dashboard";
                }
                else{
                    alert("Please enter correct details");
                }
            });
    }
    else{
        alert("Please enter correct details");
    }
}