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

// price match modal

const priceMatchOpen = document.querySelector('.price-match-modal-trigger');
const priceMatchClose = document.querySelector('.price-match-modal-close-btn');
const priceMatchModal = document.querySelector('.price-match-modal');

const priceMatchCheckbox = document.querySelector('#price-match-checkbox');
const priceMatchSubmit = document.querySelector('#price-match-submit');

const priceMatchWrapper = document.querySelector('.price-match-form-wrapper');
const priceMatchSubmitted = document.querySelector('.price-match-submitted');

priceMatchOpen.addEventListener('click', function() {
    priceMatchModal.style.display = 'block';
});

priceMatchClose.addEventListener('click', function() {
    priceMatchModal.style.display = 'none';
});

window.addEventListener('click', function(e) {
    if (e.target == priceMatchModal) {
        priceMatchModal.style.display = 'none'
    }
});

priceMatchCheckbox.addEventListener('click', function() {
    if (priceMatchCheckbox.checked == true) {
        priceMatchSubmit.disabled = false;
        priceMatchSubmit.setAttribute('title', '')
    } else {
        priceMatchSubmit.disabled = true;
        priceMatchSubmit.setAttribute('title', 'Please agree to privacy policy');
    }
});

priceMatchSubmit.addEventListener('click', function() {
    priceMatchWrapper.style.display = 'none';
    priceMatchSubmitted.style.display = 'flex';
})

// wishlist button change

let addToWishlist = document.querySelector('#addwishlist');
let goToWishlist = document.querySelector('#go-to-wishlist');

addToWishlist.addEventListener('click', function() {
    addToWishlist.style.display = 'none';
    goToWishlist.style.display = 'flex';
    console.log('clicked')
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
        } else {
            star.classList.replace('fas', 'far');
        }
    });
}

// average rating

const rating = document.querySelector('.review-average').getAttribute('data-rating')
const starPercentage = `${Math.round(rating / 5 * 100) / 10 * 10}%`

document.querySelector('.stars-inner').style.width = starPercentage;

// message block

const msgClose = document.querySelector('.message-close-btn');
const msgBlock = document.querySelector('.message-block');

msgClose.addEventListener('click', function() {
    msgBlock.style.display = 'none';
    console.log('clicked')
});