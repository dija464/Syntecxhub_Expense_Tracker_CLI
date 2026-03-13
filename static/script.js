async function loadData(){

let res=await fetch("/transactions")

let data=await res.json()

let income=0
let expense=0

data.forEach(t=>{

if(t.type=="income")
income+=t.amount
else
expense+=t.amount

})

document.getElementById("income").innerText=income
document.getElementById("expense").innerText=expense
document.getElementById("balance").innerText=income-expense

drawChart(income,expense)

}


async function addTransaction(){

let date=document.getElementById("date").value
let type=document.getElementById("type").value
let category=document.getElementById("category").value
let amount=document.getElementById("amount").value

await fetch("/add",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({date,type,category,amount})

})

loadData()

}


function drawChart(income,expense){

new Chart(document.getElementById("chart"),{

type:"pie",

data:{
labels:["Income","Expense"],
datasets:[{
data:[income,expense]
}]
}

})

}


async function exportExcel(){

await fetch("/export")

alert("Excel file exported")

}

loadData()