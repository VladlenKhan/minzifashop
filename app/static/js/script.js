const slider = document.querySelector('.slider');
const sliderContainer = document.querySelector('.slider-container');
const slides = document.querySelectorAll('.slide');
const slideWidth = slides[0].offsetWidth;
let currentIndex = 0;

function goToSlide(index) {
    if (index < 0 || index >= slides.length) return;

    currentIndex = index;
    const translateX = -slideWidth * currentIndex;
    sliderContainer.style.transform = `translateX(${translateX}px)`;
}

function nextSlide() {
    goToSlide(currentIndex + 1);
}

function previousSlide() {
    goToSlide(currentIndex - 1);
}

slider.addEventListener('mouseenter', () => {
    slider.classList.add('hover');
});

slider.addEventListener('mouseleave', () => {
    slider.classList.remove('hover');
});

setInterval(() => {
    if (!slider.classList.contains('hover')) {
        nextSlide();
    }
}, 6000);

document.querySelector('.burger').addEventListener('click', function() {
    this.classList.toggle('active');
    document.querySelector('.nav').classList.toggle('open');
})

const priceRange = document.getElementById('priceRange');
const priceOutput = document.getElementById('priceOutput');

priceRange.addEventListener('input', updatePrice);

function updatePrice() {
  const price = priceRange.value;
  priceOutput.textContent = `$${price}`;
}
