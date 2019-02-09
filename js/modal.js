var btnAddExpenses = document.getElementById('btn-add-expenses');
var btnAddIncome = document.getElementById('btn-add-income');

var btnAddExpensesFinal = document.getElementById('btn-add-expenses-final');
var btnAddIncomeFinal = document.getElementById('btn-add-income-final');

var modalExpenses = document.getElementById('modal-expenses');
var modalIncome = document.getElementById('modal-income');

var btnExpensesClose = document.getElementById('btn-expenses-close');
var btnIncomeClose = document.getElementById('btn-income-close');


btnAddExpenses.addEventListener('click', function() {
    modalExpenses.style.display = 'block';
});

btnExpensesClose.addEventListener('click', function() {
    modalExpenses.style.display = 'none';
});

btnAddIncome.addEventListener('click', function() {
    modalIncome.style.display = 'block';
});

btnIncomeClose.addEventListener('click', function() {
    modalIncome.style.display = 'none';
});


