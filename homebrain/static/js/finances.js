const UIcontroller = (function () {
    const DOMstrings = {
        selectMonth: '.select-months',
        selectItemType: '.select-type',
        selectMonths: '.select-months',
        selectYears: '.select-years',
        selectAcceptDate: '.select-accept-date',

        inputItemName: '#name',
        inputItemValue: '#value',
        inputItemDate: '#date',

        btnAdd: '.btn-add',
        btnSmallMenu: '#ico-small-menu',
        smallMenuContent: '#small-menu',
        btnSmallMenuClose: '#btn-small-menu-close',
        btnEditItem: '.btn-edit-item',
        btnDeleteItem: '.btn-delete-item',
        btnCloseEdit: '.btn-close-edit',
        btnCloseDelete: '.btn-close-delete',

        modalContainer: '.modal-container',
        modalEdit: '#modal-edit',
        modalDelete: '#modal-delete',
        expensesBox: '#box-expenses',
        incomeBox: '#box-income',

        inputItemEditID: '.input-edit-id',
        inputItemEditName: '.input-edit-name',
        inputItemEditValue: '.input-edit-value',
        inputItemEditDate: '.input-edit-date',
        inputItemDeleteID: '.input-delete-id'
    };

    return {
        setInitialDate: function() {
            let now, month, year, months, years, selectMonths, selectYears, optionMonths, optionYears;

            now = new Date();
            month = now.getMonth();
            year = now.getFullYear();
            months = ['STY', 'LUT', 'MAR', 'KWI', 'MAJ', 'CZE', 'LIP', 'SIE', 'WRZ', 'PAZ', 'LIS', 'GRU'];
            years = [];

            // set input date to today
            document.querySelector(DOMstrings.inputItemDate).valueAsDate = now;

            for(let i = 2018; i <= year; i++) {
                years.push(i);
            }

            // fill in months select
            selectMonths = document.querySelector(DOMstrings.selectMonths);
            optionMonths = [];

            for(let i = 0; i < months.length; i++) {
                optionMonths[i] = document.createElement("option");
                optionMonths[i].text = months[i];
                optionMonths[i].value = i + 1;
                selectMonths.add(optionMonths[i]);
            }

            // fill in years select
            selectYears = document.querySelector(DOMstrings.selectYears);
            optionYears = [];

            for(let i = 0; i < years.length; i++) {
                optionYears[i] = document.createElement("option");
                optionYears[i].text = years[i];
                optionYears[i].value = years[i];
                selectYears.add(optionYears[i]);
            }

            // set initial select values
            selectMonths.selectedIndex = month;
            selectYears.selectedIndex = year - 2018;
        },


        setModalBoxValues: function(event) {
            let item, itemID, itemName, itemValue, itemDate;

            item = event.target.parentNode.parentNode;

            itemID = item.id.split('-')[1];
            itemName = item.firstChild.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling;
            itemValue = itemName.nextSibling.nextSibling;
            itemDate = itemValue.nextSibling.nextSibling.nextSibling.nextSibling;
            itemName = itemName.textContent;
            itenValue = itemValue.textContent.substr(0, 1) == '-' ? itemValue = itemValue.textContent.split('-')[1] : itemValue = itemValue.textContent.split('+')[1];
            itemDate = itemDate.textContent;

            if(event.target.className === "btn btn-edit") {
                document.querySelector(DOMstrings.inputItemEditID).value = itemID;
                document.querySelector(DOMstrings.inputItemEditName).value = itemName;
                document.querySelector(DOMstrings.inputItemEditValue).value = itemValue;
                document.querySelector(DOMstrings.inputItemEditDate).value = itemDate;
            }

            if(event.target.className === "btn btn-remove") {
                document.querySelector(DOMstrings.inputItemDeleteID).value = itemID;
            }
        },


        getDOMstrings: function() {
            return DOMstrings;
        }
    };
})();




const controller = (function (UICtrl) {
    let DOM;

    function toggleSmallMenu() {
        document.querySelector(DOM.smallMenuContent).classList.toggle('visible');
    }


    function setUpDOM() {
        DOM = UICtrl.getDOMstrings();

        // enter and close hamburger menu
        document.querySelector(DOM.btnSmallMenu).addEventListener('click', toggleSmallMenu);
        document.querySelector(DOM.btnSmallMenuClose).addEventListener('click', toggleSmallMenu);

        // change input border-color depending on item type - income/expense
        document.querySelector(DOM.selectItemType).addEventListener('change', () => {
            const inputs = document.querySelectorAll('.input');
            const arrInputs = Array.from(inputs);

            arrInputs.forEach(current => {
                current.classList.toggle('input-income');
            })
        });

        setUpModalButtons();
    }


    function setUpModalButtons() {
        // open editing box
        document.querySelector(DOM.expensesBox).addEventListener('click', event => {
            if(event.target.className === 'btn btn-edit') {
                document.querySelector(DOM.modalEdit).style.display = 'block';
                document.querySelector(DOM.modalContainer).style.display = 'block'
            }

            UICtrl.setModalBoxValues(event);
        });

        document.querySelector(DOM.incomeBox).addEventListener('click', event => {
            if(event.target.className === 'btn btn-edit') {
                document.querySelector(DOM.modalEdit).style.display = 'block';
                document.querySelector(DOM.modalContainer).style.display = 'block'
            }

            UICtrl.setModalBoxValues(event);
        });

        // open deleting box
        document.querySelector(DOM.expensesBox).addEventListener('click', event => {
            if(event.target.className === 'btn btn-remove') {
                document.querySelector(DOM.modalDelete).style.display = 'block';
                document.querySelector(DOM.modalContainer).style.display = 'block'
            }

            UICtrl.setModalBoxValues(event);
        });

        document.querySelector(DOM.incomeBox).addEventListener('click', event => {
            if(event.target.className === 'btn btn-remove') {
                document.querySelector(DOM.modalDelete).style.display = 'block';
                document.querySelector(DOM.modalContainer).style.display = 'block'
            }

            UICtrl.setModalBoxValues(event);
        });

        // close the editing box
        document.querySelector(DOM.btnEditItem).addEventListener('click', () => {
            if(document.querySelector('.form-edit').valid) {
                document.querySelector(DOM.modalEdit).style.display = 'none';
                document.querySelector(DOM.modalContainer).style.display = 'none'
            }
        });

        document.querySelector(DOM.btnCloseEdit).addEventListener('click', () => {
            document.querySelector(DOM.modalEdit).style.display = 'none';
            document.querySelector(DOM.modalContainer).style.display = 'none'
        });

        // close the deleting box
        document.querySelector(DOM.btnDeleteItem).addEventListener('click', () => {
            document.querySelector(DOM.modalDelete).style.display = 'none';
            document.querySelector(DOM.modalContainer).style.display = 'none'
        });

        document.querySelector(DOM.btnCloseDelete).addEventListener('click', () => {
            document.querySelector(DOM.modalDelete).style.display = 'none';
            document.querySelector(DOM.modalContainer).style.display = 'none'
        });
    }


    function setUpDate() {
        UICtrl.setInitialDate();
    }

    return {
        initialize: function() {
            setUpDOM();
            setUpDate();
        },
    };
})(UIcontroller);

controller.initialize();
