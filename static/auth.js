async function login(){

let email=document.getElementById("email").value
let password=document.getElementById("password").value

let res=await fetch("/login",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({email,password})

})

let data=await res.json()

if(data.status=="success"){
window.location="/dashboard"
}
else{
alert("Login failed")
}

}


async function register(){

let email=document.getElementById("email").value
let password=document.getElementById("password").value

await fetch("/register",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({email,password})

})

alert("Registered successfully")

window.location="/"

}