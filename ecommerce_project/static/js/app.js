// cart buttons

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
        if (parseInt(quantity.value) > 1) {
            quantity.value--;
        }
    });
});

// affirm modal

const affirmOpen = document.querySelector('.affirm-modal-trigger');
const affirmClose = document.querySelector('.affirm-modal-close-btn');
const affirmModal = document.querySelector('.affirm-modal');

affirmOpen.addEventListener('click', function() {
    affirmModal.style.display = 'block'
});

affirmClose.addEventListener('click', function() {
    affirmModal.style.display = 'none'
});

window.addEventListener('click', function(e) {
    if (e.target == affirmModal) {
        affirmModal.style.display = 'none'
    }
});

// star rating

let stars = Array.from(document.querySelectorAll('.star-rating'));

stars.forEach((star, index) => {
    star.addEventListener('click', (function(idx) {
        document.querySelector('.stars').setAttribute('value', idx + 1);
        setRating();
    }).bind(window, index));
});

function setRating() {
    let stars = Array.from(document.querySelectorAll('.star-rating'));
    let rating = parseInt(document.querySelector('.stars').getAttribute('value'));
    stars.forEach((star, index) => {
        if (rating > index) {
            star.classList.replace('far', 'fas');
            console.log('added rated on', index );
        } else {
            star.classList.replace('fas', 'far')
            console.log('removed rated on', index );
        }
    });
}

// average rating

const rating = document.querySelector('.review-average').getAttribute('data-rating')
const starPercentage = `${Math.round(rating / 5 * 100) / 10 * 10}%`

document.querySelector('.stars-inner').style.width = starPercentage;

// wishlist button change

let addToWishlist = document.querySelector('#add-to-wishlist');
let goToWishlist = document.querySelector('#go-to-wishlist');

addToWishlist.addEventListener('click', function() {
    addToWishlist.style.display = 'none';
    goToWishlist.style.display = 'flex';
});