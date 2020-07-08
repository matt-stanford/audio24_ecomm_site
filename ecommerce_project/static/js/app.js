const subtractBtn = document.getElementById('subtract')
const addBtn = document.getElementById('add')
const quantity = document.getElementById('quantity')

subtractBtn.addEventListener('click', () => {
    if (parseInt(quantity.value) > 0) {
        quantity.value--;
    }
})

addBtn.addEventListener('click', () => {
    quantity.value++;
})