 alert("js loaded");
 let expenses = JSON.parse(localStorage.getItem("expenses")) || [];

function save(){
    localStorage.setItem("expenses", JSON.stringify(expenses));
}

function addExpense(){
    let title = document.getElementById("title").value;
    let amount = document.getElementById("amount").value;
    let category = document.getElementById("category").value;
    let date = document.getElementById("date").value;

    if(!title || amount <= 0){
        alert("Enter valid details");
        return;
    }

    expenses.push({title, amount:Number(amount), category, date});
    save();
    display();
}

function deleteExpense(i){
    expenses.splice(i,1);
    save();
    display();
}

function display(){
    let list = document.getElementById("list");
    let analytics = document.getElementById("analytics");
    let total = 0;
    let cat = {};

    list.innerHTML = "";
    analytics.innerHTML = "";

    expenses.forEach((e,i)=>{
        total += e.amount;
        cat[e.category] = (cat[e.category] || 0) + e.amount;

        list.innerHTML += `
            <div class="expense">
                ${e.title} | ₹${e.amount} | ${e.category} | ${e.date}
                <button onclick="deleteExpense(${i})">❌</button>
            </div>`;
    });

    document.getElementById("total").innerText = total;

    for(let c in cat){
        analytics.innerHTML += `<p>${c} → ₹${cat[c]}</p>`;
    }
}

display();