const dataController = (function () {

})();

const UIcontroller = (function () {
    const DOMstrings = {
        selectMonth: '.select-months',
        selectItemType: '.select-type',
        inputItemName: '#name',
        inputItemValue: '#value',
        inputItemDate: '#date',
        btnAdd: '.btn-add',
        btnSmallMenu: '#ico-small-menu',
        smallMenuContent: '#small-menu',
        btnSmallMenuClose: '#btn-small-menu-close',
        btnEditItem: '.btn-edit-item',
        btnCloseEdit: '.btn-close-edit',
        modalEdit: '#modal-edit',
        expensesBox: '#box-expenses',
        incomeBox: '#box-income'
    };

    return {
        setInitialDate: function() {
            document.querySelector(DOMstrings.inputItemDate).valueAsDate = new Date();
        },


        getDOMstrings: function() {
            return DOMstrings;
        }
    };
})();




const controller = (function (dataCtrl, UICtrl) {
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

        // open editing box
        document.querySelector(DOM.expensesBox).addEventListener('click', event => {
            if(event.target.className === 'btn btn-edit')
                document.querySelector(DOM.modalEdit).style.display = 'block';
        });

        document.querySelector(DOM.incomeBox).addEventListener('click', event => {
            if(event.target.className === 'btn btn-edit')
                document.querySelector(DOM.modalEdit).style.display = 'block';
        });

        // close the editing box
        document.querySelector(DOM.btnEditItem).addEventListener('click', () => {
            document.querySelector(DOM.modalEdit).style.display = 'none';
        });

        document.querySelector(DOM.btnCloseEdit).addEventListener('click', () => {
            document.querySelector(DOM.modalEdit).style.display = 'none';
        });
    }

    return {
        initialize: function() {
            setUpDOM();
            UICtrl.setInitialDate();
        },
    };
})(dataController, UIcontroller);

controller.initialize();
