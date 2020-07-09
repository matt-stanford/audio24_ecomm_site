let addBtns = Array.from(document.querySelectorAll('#add'));
let subtractBtns = Array.from(document.querySelectorAll('#subtract'));
let deleteBtns = Array.from(document.querySelectorAll('#delete'));

const affirmOpen = document.querySelector('.affirm-modal-trigger');
const affirmClose = document.querySelector('.affirm-modal-close-btn');
const affirmModal = document.querySelector('.affirm-modal');

addBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        var product = this.dataset.product;
        let quantity = document.getElementById('quantity'+product);
        quantity.value++;
    });
});

subtractBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        var product = this.dataset.product;
        let quantity = document.getElementById('quantity'+product);
        if (parseInt(quantity.value) > 1) {
            quantity.value--;
        }
    });
});

affirmOpen.addEventListener('click', function() {
    affirmModal.style.display = 'block'
});

affirmClose.addEventListener('click', function() {
    affirmModal.style.display = 'none'
});