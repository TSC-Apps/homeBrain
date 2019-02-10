//================================================
// Assigning DOM elements to variables

var btnAddExpenses = document.getElementById('btn-add-expenses');
var btnAddIncome = document.getElementById('btn-add-income');

var btnAddExpensesFinal = document.getElementById('btn-add-expenses-final');
var btnAddIncomeFinal = document.getElementById('btn-add-income-final');

var modalExpenses = document.getElementById('modal-expenses');
var modalIncome = document.getElementById('modal-income');

var btnExpensesClose = document.getElementById('btn-expenses-close');
var btnIncomeClose = document.getElementById('btn-income-close');


//================================================
// Event Listeners

// "Add expense" button in expenses modal
btnAddExpenses.addEventListener('click', function() {
    modalExpenses.style.display = 'block';
});

// "Add income" button in expenses modal
btnAddIncome.addEventListener('click', function() {
    modalIncome.style.display = 'block';
});


//================================================
// Close modals

// Close "add expense" modal button
btnExpensesClose.addEventListener('click', function() {
    modalExpenses.style.display = 'none';
});

// Close "add income" modal button
btnIncomeClose.addEventListener('click', function() {
    modalIncome.style.display = 'none';
});


