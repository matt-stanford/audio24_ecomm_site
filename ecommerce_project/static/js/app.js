let addBtns = Array.from(document.querySelectorAll('#add'));
let subtractBtns = Array.from(document.querySelectorAll('#subtract'));
let deleteBtns = Array.from(document.querySelectorAll('#delete'));

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
        if (parseInt(quantity.value) > 0) {
            quantity.value--;
        }
    });
});

deleteBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        var product = this.dataset.product;
        let quantity = document.getElementById('quantity'+product);
        quantity.value = 0;
    });
});